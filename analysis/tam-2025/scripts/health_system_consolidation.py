#!/usr/bin/env python3
"""
Health System Consolidation Script
Data-driven approach to consolidate hospitals under verified parent health systems
and calculate system-level pricing.

Key insight: Mount Sinai (7 hospitals) rejected $50K, target is $25-45K
This means system pricing should be ~$3,500-$6,000 per hospital for large systems.
"""

import csv
import json
from collections import defaultdict
from pathlib import Path

# Verified health system affiliations from authoritative sources
# Source: Wikipedia, official health system websites, CMS data
HEALTH_SYSTEMS = {
    "Mount Sinai Health System": {
        "patterns": [],  # Don't rely on patterns
        "verified_hospitals": [
            "Mount Sinai Hospital",
            "Mount Sinai West",
            "Mount Sinai Beth Israel",  # Closed April 2025, may still be in data
            "Mount Sinai South Nassau",
            "N Y Eye and Ear Infirmary",
            "Brooklyn Hospital Center",  # Affiliated
        ],
        "headquarters": "New York, NY",
        "notes": "Beth Israel closed April 2025. Missing: Morningside, Queens, Brooklyn proper"
    },
    "New York-Presbyterian": {
        "patterns": ["New York-Presbyterian"],
        "verified_hospitals": [
            "New York-Presbyterian Hospital",
            "New York-Presbyterian/queens",
        ],
        "headquarters": "New York, NY"
    },
    "Northwell Health": {
        "patterns": ["Northwell"],
        "verified_hospitals": [
            "North Shore University Hospital",
            "Long Island Jewish Medical Center",
            "Staten Island University Hospital",
            "Lenox Hill Hospital",
            "Glen Cove Hospital",
            "Plainview Hospital",
            "South Shore University Hospital",
        ],
        "headquarters": "New Hyde Park, NY"
    },
    "NYC Health + Hospitals": {
        "patterns": [],
        "verified_hospitals": [
            "Bellevue Hospital Center",
            "Kings County Hospital Center",
            "Queens Hospital Center",
            "Elmhurst Hospital Center",
            "Jacobi Medical Center",
            "Lincoln Medical & Mental Health Center",
            "Harlem Hospital Center",
            "Metropolitan Hospital Center",
            "Woodhull Medical & Mental Health Center",
        ],
        "headquarters": "New York, NY",
        "notes": "Public hospital system - may have different procurement"
    },
    "Montefiore Health System": {
        "patterns": ["Montefiore"],
        "verified_hospitals": [
            "Montefiore Medical Center",
            "Montefiore New Rochelle Hospital",
        ],
        "headquarters": "Bronx, NY"
    },
    "NYU Langone Health": {
        "patterns": ["NYU Langone"],
        "verified_hospitals": [
            "NYU Langone Hospitals",
        ],
        "headquarters": "New York, NY"
    },
    "HCA Healthcare": {
        "patterns": ["HCA", "Medical City", "HealthONE"],
        "verified_hospitals": [],  # Nationwide - need to verify by state
        "headquarters": "Nashville, TN",
        "notes": "77+ hospitals nationwide"
    },
    "Ascension": {
        "patterns": ["Ascension", "St. Vincent"],
        "verified_hospitals": [],
        "headquarters": "St. Louis, MO",
        "notes": "85+ hospitals nationwide"
    },
    "CommonSpirit Health": {
        "patterns": ["CommonSpirit", "CHI", "Dignity Health"],
        "verified_hospitals": [],
        "headquarters": "Chicago, IL"
    },
    "Providence": {
        "patterns": ["Providence"],
        "verified_hospitals": [],
        "headquarters": "Renton, WA"
    },
    "Kaiser Permanente": {
        "patterns": ["Kaiser"],
        "verified_hospitals": [],
        "headquarters": "Oakland, CA"
    },
    "St. Luke's Health System (Pennsylvania)": {
        "patterns": [],
        "verified_hospitals": [
            "St. Luke's Hospital Bethlehem",
            "St. Luke's Hospital - Easton Campus",
            "St. Luke's Hospital - Anderson Campus",
            "St. Luke's Hospital - Monroe Campus",
            "St. Luke's Hospital - Upper Bucks Campus",
            "St. Luke's Hospital - Carbon Campus",
            "St. Luke's Miners Memorial Hospital",
            "Geisinger St. Luke's Hospital",
            "St. Luke's Warren Hospital",
        ],
        "headquarters": "Bethlehem, PA",
        "notes": "Not to be confused with St. Luke's in other states"
    },
    "St. Luke's Health System (Idaho)": {
        "patterns": [],
        "verified_hospitals": [
            "St. Luke's Regional Medical Center",  # Boise
            "St. Luke's Magic Valley Rmc",
            "St. Luke's Nampa Medical Center",
            "St. Luke's Jerome",
            "St. Luke's Elmore Medical Center",
            "St. Luke's Mccall",
            "St. Luke's Wood River Medical Center",
        ],
        "headquarters": "Boise, ID"
    },
    "CHI St. Luke's Health (Texas)": {
        "patterns": ["Chi St. Luke", "Chi St. Lukes"],
        "verified_hospitals": [
            "Chi St. Luke's Health Baylor College of Medicine Me",
            "Chi St. Luke's Health Brazosport",
            "Chi St. Lukes Health Memorial Lufkin",
            "Chi St. Lukes Health Memorial Livingston",
            "Chi St. Lukes Health Memorial San Augustine",
            "St. Luke's the Woodlands Hospital",
            "St. Lukes Lakeside Hospital",
            "St. Luke's Patients Medical Center",
            "St. Luke's Sugar Land Hospital",
            "St. Luke's Hospital at the Vintage",
        ],
        "headquarters": "Houston, TX"
    },
    "University of Rochester Medical Center": {
        "patterns": [],
        "verified_hospitals": [
            "Strong Memorial Hospital",
            "Highland Hospital",
        ],
        "headquarters": "Rochester, NY"
    },
    "Rochester Regional Health": {
        "patterns": [],
        "verified_hospitals": [
            "Rochester General Hospital",
            "Unity Hospital of Rochester",
            "Unity Specialty Hospital",
            "Newark-Wayne Community Hospital",
            "Clifton Springs Hospital and Clinic",
        ],
        "headquarters": "Rochester, NY"
    },
}


def load_hospitals(csv_path):
    """Load hospital data from CSV."""
    hospitals = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hospitals.append(row)
    return hospitals


def match_hospital_to_system(hospital_name, city, state, systems):
    """Match a hospital to its parent health system using verified lists."""
    # First try exact match from verified lists
    for system_name, system_data in systems.items():
        for verified in system_data.get('verified_hospitals', []):
            # Case-insensitive partial match
            if verified.lower() in hospital_name.lower() or hospital_name.lower() in verified.lower():
                return system_name

    # Then try pattern matching (less reliable)
    for system_name, system_data in systems.items():
        for pattern in system_data.get('patterns', []):
            if pattern.lower() in hospital_name.lower():
                return system_name

    return None


def get_beds(hospital):
    """Extract bed count from hospital dict, trying multiple field names."""
    for field in ['total_beds', 'beds', 'Beds', 'Total_Beds']:
        value = hospital.get(field)
        if value:
            try:
                return int(float(value))
            except (ValueError, TypeError):
                continue
    return 0


def get_hospital_size_multiplier(beds):
    """Get pricing multiplier based on hospital bed count."""
    try:
        beds = int(beds) if beds else 0
    except (ValueError, TypeError):
        beds = 0

    if beds >= 1000:
        return 1.75  # Enterprise hospitals
    elif beds >= 500:
        return 1.5   # Large hospitals
    elif beds >= 200:
        return 1.25  # Medium hospitals
    else:
        return 1.0   # Small hospitals


def calculate_system_pricing_v2(hospitals_list):
    """
    Calculate system-level pricing using per-hospital complexity-based pricing.

    Key insight from Mount Sinai feedback:
    - 7 hospitals rejected $50K for entire system
    - Target is $25-45K for the system
    - That's ~$3,500-$6,500 per hospital

    New formula: Per-hospital pricing based on complexity
    - Base: $4,000 per hospital
    - Multiplier by size: 1.0x (small) to 1.75x (enterprise)
    - System size discount: 10-20% for larger systems
    """
    BASE_PRICE_PER_HOSPITAL = 4000

    # Calculate per-hospital prices based on complexity
    total_price = 0
    hospital_prices = []

    for h in hospitals_list:
        beds = get_beds(h)
        multiplier = get_hospital_size_multiplier(beds)
        price = BASE_PRICE_PER_HOSPITAL * multiplier
        total_price += price
        hospital_prices.append({
            'name': h.get('name', h.get('Name', '')),
            'beds': beds,
            'multiplier': multiplier,
            'price': price
        })

    # Apply system size discount
    hospital_count = len(hospitals_list)
    if hospital_count >= 51:
        discount = 0.20
        tier = "Enterprise Premier"
    elif hospital_count >= 16:
        discount = 0.15
        tier = "Enterprise Plus"
    elif hospital_count >= 6:
        discount = 0.10
        tier = "Enterprise"
    elif hospital_count >= 2:
        discount = 0.05
        tier = "Standard (Multi-site)"
    else:
        discount = 0
        tier = "Standard"

    system_price = total_price * (1 - discount)

    # Round to nearest $100
    system_price = round(system_price / 100) * 100

    return {
        'tier': tier,
        'system_price': system_price,
        'discount_pct': discount * 100,
        'per_hospital_avg': round(system_price / hospital_count, 2) if hospital_count > 0 else 0,
        'hospital_breakdown': hospital_prices
    }


def calculate_system_pricing(hospital_count, total_individual_tam):
    """
    Legacy function - calculate system-level pricing based on total individual TAM.
    Used for summary calculations when we don't have hospital-level details.
    """
    # Use same discount tiers as v2
    if hospital_count >= 51:
        discount = 0.20
        tier = "Enterprise Premier"
    elif hospital_count >= 16:
        discount = 0.15
        tier = "Enterprise Plus"
    elif hospital_count >= 6:
        discount = 0.10
        tier = "Enterprise"
    elif hospital_count >= 2:
        discount = 0.05
        tier = "Standard (Multi-site)"
    else:
        discount = 0
        tier = "Standard"

    # For legacy, estimate based on per-hospital average of $5K
    estimated_price = hospital_count * 5000 * (1 - discount)
    system_price = round(estimated_price / 100) * 100

    return {
        'tier': tier,
        'system_price': system_price,
        'discount_pct': discount * 100,
        'per_hospital_avg': round(system_price / hospital_count, 2) if hospital_count > 0 else 0
    }


def consolidate_hospitals(hospitals, systems):
    """Consolidate hospitals under their parent health systems."""
    # Track which hospitals belong to which system
    system_hospitals = defaultdict(list)
    independent_hospitals = []

    for hospital in hospitals:
        name = hospital.get('name', hospital.get('Name', ''))
        city = hospital.get('city', hospital.get('City', ''))
        state = hospital.get('state', hospital.get('State', ''))

        system = match_hospital_to_system(name, city, state, systems)

        if system:
            system_hospitals[system].append(hospital)
        else:
            independent_hospitals.append(hospital)

    return dict(system_hospitals), independent_hospitals


def analyze_mount_sinai_specifically(hospitals):
    """Special analysis for Mount Sinai to validate pricing."""
    ms_hospitals = []
    for h in hospitals:
        name = h.get('name', h.get('Name', ''))
        state = h.get('state', h.get('State', ''))
        if state == 'NY' and any(x in name for x in ['Mount Sinai', 'Sinai', 'Eye and Ear', 'Brooklyn Hospital Center']):
            # Exclude non-NYC Sinai hospitals
            city = h.get('city', h.get('City', ''))
            if 'Mount Sinai' in name or 'Eye and Ear' in name or 'Brooklyn Hospital Center' in name:
                # Exclude Beth Israel (closed April 2025)
                if 'Beth Israel' not in name:
                    ms_hospitals.append(h)

    print("\n" + "="*60)
    print("MOUNT SINAI HEALTH SYSTEM ANALYSIS (V2 Pricing)")
    print("="*60)

    total_individual = 0
    for h in ms_hospitals:
        name = h.get('name', h.get('Name', ''))
        price = float(h.get('recallwire_price', 0))
        beds = get_beds(h)
        total_individual += price
        print(f"  {name}: ${price:,.0f} individual ({beds} beds)")

    print(f"\n  Total Individual TAM: ${total_individual:,.0f}")
    print(f"  Hospital Count: {len(ms_hospitals)}")
    print(f"  Note: Excluding Beth Israel (closed April 2025)")
    print(f"  Note: Missing from data: Morningside, Queens, Brooklyn")

    # Calculate system price using V2 formula
    pricing = calculate_system_pricing_v2(ms_hospitals)
    print(f"\n  SYSTEM PRICING (V2 - per-hospital complexity):")
    print(f"    Tier: {pricing['tier']}")
    print(f"    System Price: ${pricing['system_price']:,.0f}")
    print(f"    System Discount: {pricing['discount_pct']:.0f}%")
    print(f"    Per Hospital Avg: ${pricing['per_hospital_avg']:,.0f}")

    print(f"\n  Hospital Breakdown:")
    for hp in pricing['hospital_breakdown']:
        print(f"    {hp['name'][:40]}: ${hp['price']:,.0f} ({hp['multiplier']}x, {hp['beds']} beds)")

    # Check against target
    target_min, target_max = 25000, 45000
    print(f"\n  Target Range: ${target_min:,} - ${target_max:,}")
    if target_min <= pricing['system_price'] <= target_max:
        print(f"  ✓ WITHIN TARGET RANGE!")
    elif pricing['system_price'] < target_min:
        print(f"  Note: Below target (conservative pricing)")
    else:
        print(f"  ✗ Above target - need adjustment")

    # Estimate with missing hospitals
    print(f"\n  ESTIMATE WITH MISSING HOSPITALS:")
    # Add estimates for Morningside, Queens, Brooklyn
    estimated_missing = 3  # Morningside, Queens, Brooklyn
    estimated_additional = estimated_missing * 5000  # Assume medium-sized
    estimated_total = pricing['system_price'] + estimated_additional
    print(f"    Adding ~{estimated_missing} missing hospitals @ ~$5K each")
    print(f"    Estimated Total: ${estimated_total:,.0f}")
    if target_min <= estimated_total <= target_max:
        print(f"    ✓ Still within target range")

    return ms_hospitals, pricing


def main():
    # Paths
    base_dir = Path(__file__).parent.parent
    csv_path = base_dir / 'hospitals_pricing.csv'
    output_path = base_dir / 'health_systems_consolidated.json'

    print("Loading hospital data...")
    hospitals = load_hospitals(csv_path)
    print(f"Loaded {len(hospitals)} hospitals")

    # Special Mount Sinai analysis first
    ms_hospitals, ms_pricing = analyze_mount_sinai_specifically(hospitals)

    # Consolidate all hospitals
    print("\n" + "="*60)
    print("CONSOLIDATING ALL HEALTH SYSTEMS")
    print("="*60)

    system_hospitals, independent = consolidate_hospitals(hospitals, HEALTH_SYSTEMS)

    # Calculate system-level metrics
    results = {
        'summary': {
            'total_hospitals': len(hospitals),
            'hospitals_in_systems': sum(len(h) for h in system_hospitals.values()),
            'independent_hospitals': len(independent),
            'health_systems_identified': len(system_hospitals),
        },
        'health_systems': {},
        'mount_sinai_validation': {
            'hospitals_found': len(ms_hospitals),
            'individual_tam': sum(float(h.get('recallwire_price', 0)) for h in ms_hospitals),
            'system_price': ms_pricing['system_price'],
            'target_range': [25000, 45000],
            'within_target': 25000 <= ms_pricing['system_price'] <= 45000,
        }
    }

    total_system_tam = 0
    total_individual_tam_in_systems = 0

    for system_name, hospitals_list in sorted(system_hospitals.items(), key=lambda x: -len(x[1])):
        individual_tam = sum(float(h.get('recallwire_price', 0)) for h in hospitals_list)
        # Use V2 pricing for accurate per-hospital pricing
        pricing = calculate_system_pricing_v2(hospitals_list)

        total_system_tam += pricing['system_price']
        total_individual_tam_in_systems += individual_tam

        # Calculate discount vs individual TAM
        discount_vs_individual = (1 - pricing['system_price'] / individual_tam) * 100 if individual_tam > 0 else 0

        results['health_systems'][system_name] = {
            'hospital_count': len(hospitals_list),
            'individual_tam': individual_tam,
            'system_price': pricing['system_price'],
            'discount_pct': pricing['discount_pct'],
            'discount_vs_individual': round(discount_vs_individual, 1),
            'per_hospital': pricing['per_hospital_avg'],
            'tier': pricing['tier'],
            'hospitals': [
                {
                    'name': h.get('name', h.get('Name', '')),
                    'city': h.get('city', h.get('City', '')),
                    'state': h.get('state', h.get('State', '')),
                    'beds': get_beds(h),
                    'individual_price': float(h.get('recallwire_price', 0)),
                    'system_price': hp['price']
                }
                for h, hp in zip(hospitals_list, pricing['hospital_breakdown'])
            ]
        }

        print(f"\n{system_name}:")
        print(f"  Hospitals: {len(hospitals_list)}")
        print(f"  Individual TAM: ${individual_tam:,.0f}")
        print(f"  System Price: ${pricing['system_price']:,.0f} ({discount_vs_individual:.0f}% off individual)")

    # Calculate independent hospital TAM
    independent_tam = sum(float(h.get('recallwire_price', 0)) for h in independent)

    results['summary']['system_level_tam'] = total_system_tam
    results['summary']['individual_tam_in_systems'] = total_individual_tam_in_systems
    results['summary']['independent_tam'] = independent_tam
    results['summary']['total_realistic_tam'] = total_system_tam + independent_tam
    results['summary']['tam_reduction_from_systems'] = total_individual_tam_in_systems - total_system_tam

    print("\n" + "="*60)
    print("TAM SUMMARY")
    print("="*60)
    print(f"Hospitals in identified systems: {results['summary']['hospitals_in_systems']}")
    print(f"Independent hospitals: {results['summary']['independent_hospitals']}")
    print(f"\nIndividual TAM (system hospitals): ${total_individual_tam_in_systems:,.0f}")
    print(f"System-Level TAM: ${total_system_tam:,.0f}")
    print(f"TAM Reduction: ${total_individual_tam_in_systems - total_system_tam:,.0f}")
    print(f"\nIndependent Hospital TAM: ${independent_tam:,.0f}")
    print(f"\nTOTAL REALISTIC TAM: ${total_system_tam + independent_tam:,.0f}")

    # Save results
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_path}")


if __name__ == '__main__':
    main()
