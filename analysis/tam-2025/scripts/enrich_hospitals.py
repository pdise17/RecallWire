#!/usr/bin/env python3
"""
Enrich hospitals CSV with health system affiliations.

Adds columns:
- entity_type: "independent" or "system_member"
- parent_system: Name of parent health system (or null)
- parent_system_id: ID for rollup
- system_deal_price: Price when sold as part of system
"""

import csv
import re
import json
from pathlib import Path
from health_systems_master import HEALTH_SYSTEMS_MASTER

def get_beds(row):
    """Extract bed count from hospital row."""
    for field in ['total_beds', 'beds', 'Beds', 'Total_Beds']:
        value = row.get(field)
        if value:
            try:
                return int(float(value))
            except (ValueError, TypeError):
                continue
    return 0


def calculate_system_price(beds):
    """Calculate per-hospital price for system deals."""
    BASE_PRICE = 4000
    if beds >= 1000:
        multiplier = 1.75
    elif beds >= 500:
        multiplier = 1.5
    elif beds >= 200:
        multiplier = 1.25
    else:
        multiplier = 1.0
    return int(BASE_PRICE * multiplier)


def match_hospital_to_system(hospital_name, city, state, systems):
    """
    Match a hospital to a health system using patterns.

    Returns (system_id, system_name) or (None, None) if no match.
    """
    hospital_name_lower = hospital_name.lower()

    for system in systems:
        system_id = system['id']
        system_name = system['name']

        # Check exclude patterns first
        exclude_patterns = system.get('exclude_patterns', [])
        excluded = False
        for pattern in exclude_patterns:
            if re.search(pattern, hospital_name, re.IGNORECASE):
                excluded = True
                break
        if excluded:
            continue

        # Check state-specific patterns first (more precise)
        state_patterns = system.get('state_patterns', {})
        if state in state_patterns:
            for pattern in state_patterns[state]:
                if re.search(pattern, hospital_name, re.IGNORECASE):
                    return system_id, system_name

        # Check general patterns
        for pattern in system.get('patterns', []):
            if re.search(pattern, hospital_name, re.IGNORECASE):
                return system_id, system_name

    return None, None


def enrich_hospitals(input_csv, output_csv):
    """Enrich hospital CSV with system affiliations."""

    # Load hospitals
    hospitals = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            hospitals.append(row)

    print(f"Loaded {len(hospitals)} hospitals")

    # Track statistics
    stats = {
        'total': len(hospitals),
        'matched': 0,
        'independent': 0,
        'by_system': {}
    }

    # Enrich each hospital
    for hospital in hospitals:
        name = hospital.get('name', '')
        city = hospital.get('city', '')
        state = hospital.get('state', '')
        beds = get_beds(hospital)

        system_id, system_name = match_hospital_to_system(name, city, state, HEALTH_SYSTEMS_MASTER)

        if system_id:
            hospital['entity_type'] = 'system_member'
            hospital['parent_system'] = system_name
            hospital['parent_system_id'] = system_id
            hospital['system_deal_price'] = calculate_system_price(beds)
            stats['matched'] += 1
            stats['by_system'][system_name] = stats['by_system'].get(system_name, 0) + 1
        else:
            hospital['entity_type'] = 'independent'
            hospital['parent_system'] = ''
            hospital['parent_system_id'] = ''
            hospital['system_deal_price'] = ''
            stats['independent'] += 1

    # Add new columns to fieldnames
    new_fieldnames = list(fieldnames) + ['entity_type', 'parent_system', 'parent_system_id', 'system_deal_price']

    # Write enriched CSV
    with open(output_csv, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(hospitals)

    print(f"\nEnriched CSV saved to: {output_csv}")

    return hospitals, stats


def generate_summary(hospitals, stats, output_json):
    """Generate summary JSON with system rollups."""

    # Calculate system-level metrics
    systems_summary = {}

    for hospital in hospitals:
        if hospital['entity_type'] == 'system_member':
            system_name = hospital['parent_system']
            system_id = hospital['parent_system_id']

            if system_name not in systems_summary:
                systems_summary[system_name] = {
                    'id': system_id,
                    'name': system_name,
                    'hospital_count': 0,
                    'total_beds': 0,
                    'individual_tam': 0,
                    'system_tam': 0,
                    'hospitals': []
                }

            beds = get_beds(hospital)
            individual_price = float(hospital.get('recallwire_price', 0))
            system_price = int(hospital.get('system_deal_price', 0))

            systems_summary[system_name]['hospital_count'] += 1
            systems_summary[system_name]['total_beds'] += beds
            systems_summary[system_name]['individual_tam'] += individual_price
            systems_summary[system_name]['system_tam'] += system_price
            systems_summary[system_name]['hospitals'].append({
                'name': hospital.get('name', ''),
                'city': hospital.get('city', ''),
                'state': hospital.get('state', ''),
                'beds': beds,
                'individual_price': individual_price,
                'system_price': system_price
            })

    # Apply system-level discounts
    for system_name, data in systems_summary.items():
        count = data['hospital_count']
        base_tam = data['system_tam']

        # System discount based on size
        if count >= 100:
            discount = 0.20
        elif count >= 50:
            discount = 0.15
        elif count >= 20:
            discount = 0.10
        elif count >= 6:
            discount = 0.05
        else:
            discount = 0

        data['system_discount'] = discount
        data['final_system_price'] = int(base_tam * (1 - discount))
        data['per_hospital_avg'] = int(data['final_system_price'] / count) if count > 0 else 0
        data['discount_vs_individual'] = round((1 - data['final_system_price'] / data['individual_tam']) * 100, 1) if data['individual_tam'] > 0 else 0

    # Calculate independent hospital metrics
    independent_hospitals = [h for h in hospitals if h['entity_type'] == 'independent']
    independent_tam = sum(float(h.get('recallwire_price', 0)) for h in independent_hospitals)

    # Build final summary
    summary = {
        'generated': '2025-01',
        'methodology': 'Pattern matching against top 50 US health systems',
        'totals': {
            'total_hospitals': len(hospitals),
            'system_members': stats['matched'],
            'independent': stats['independent'],
            'systems_identified': len(systems_summary),
            'individual_tam': sum(float(h.get('recallwire_price', 0)) for h in hospitals),
            'system_level_tam': sum(s['final_system_price'] for s in systems_summary.values()),
            'independent_tam': independent_tam,
        },
        'health_systems': dict(sorted(systems_summary.items(), key=lambda x: -x[1]['hospital_count'])),
    }

    # Calculate realistic TAM
    summary['totals']['realistic_tam'] = summary['totals']['system_level_tam'] + summary['totals']['independent_tam']

    # Save JSON
    with open(output_json, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"Summary JSON saved to: {output_json}")

    return summary


def main():
    base_dir = Path(__file__).parent.parent

    input_csv = base_dir / 'hospitals_pricing.csv'
    output_csv = base_dir / 'hospitals_enriched.csv'
    output_json = base_dir / 'health_systems_enriched.json'

    print("="*70)
    print("HOSPITAL ENRICHMENT - HEALTH SYSTEM AFFILIATIONS")
    print("="*70)

    # Enrich hospitals
    hospitals, stats = enrich_hospitals(input_csv, output_csv)

    # Print statistics
    print("\n" + "="*70)
    print("ENRICHMENT STATISTICS")
    print("="*70)
    print(f"\nTotal hospitals: {stats['total']}")
    print(f"Matched to systems: {stats['matched']} ({stats['matched']/stats['total']*100:.1f}%)")
    print(f"Independent: {stats['independent']} ({stats['independent']/stats['total']*100:.1f}%)")
    print(f"\nSystems identified: {len(stats['by_system'])}")

    print("\nTop 20 systems by hospital count:")
    print("-"*50)
    for system, count in sorted(stats['by_system'].items(), key=lambda x: -x[1])[:20]:
        print(f"  {system:<40} {count:>5}")

    # Generate summary
    print("\n" + "="*70)
    print("GENERATING SUMMARY")
    print("="*70)
    summary = generate_summary(hospitals, stats, output_json)

    print("\n" + "="*70)
    print("TAM SUMMARY")
    print("="*70)
    print(f"\nIndividual TAM: ${summary['totals']['individual_tam']:,.0f}")
    print(f"System-Level TAM: ${summary['totals']['system_level_tam']:,.0f}")
    print(f"Independent TAM: ${summary['totals']['independent_tam']:,.0f}")
    print(f"Realistic TAM: ${summary['totals']['realistic_tam']:,.0f}")

    # Validate Mount Sinai
    if 'Mount Sinai Health System' in summary['health_systems']:
        ms = summary['health_systems']['Mount Sinai Health System']
        print("\n" + "="*70)
        print("MOUNT SINAI VALIDATION")
        print("="*70)
        print(f"Hospitals: {ms['hospital_count']}")
        print(f"Individual TAM: ${ms['individual_tam']:,.0f}")
        print(f"System Price: ${ms['final_system_price']:,.0f}")
        print(f"Per Hospital: ${ms['per_hospital_avg']:,.0f}")
        if 25000 <= ms['final_system_price'] <= 45000:
            print("✓ Within target range ($25K-$45K)")
        else:
            print(f"Note: Outside target range ($25K-$45K)")


if __name__ == '__main__':
    main()
