#!/usr/bin/env python3
"""
Hospital Classification Workflow

Config-driven hospital classification for TAM analysis.
All weights, thresholds, and parameters are defined in YAML configs.

Usage:
    python classify_hospitals.py [--config CONFIG_DIR] [--input INPUT_CSV] [--output OUTPUT_DIR]

Configs:
    - configs/classification.yaml: Tier, pricing, scoring parameters
    - configs/health_systems.yaml: Health system pattern matching

Outputs:
    - hospitals_classified.csv: Enriched hospital data with all classifications
    - classification_summary.json: Aggregate statistics and TAM calculations
"""

import argparse
import csv
import json
import re
from pathlib import Path
from datetime import datetime

import yaml


class HospitalClassifier:
    """Config-driven hospital classifier."""

    def __init__(self, config_dir: Path):
        """Load configuration files."""
        self.config_dir = config_dir
        self.classification_config = self._load_yaml('classification.yaml')
        self.health_systems_config = self._load_yaml('health_systems.yaml')

        # Extract commonly used config sections
        self.config = self.classification_config['classification']
        self.systems = self.health_systems_config['health_systems']['systems']

        # Build lookup tables
        self._build_tier_lookup()
        self._build_size_multiplier_lookup()
        self._build_system_discount_lookup()

    def _load_yaml(self, filename: str) -> dict:
        """Load a YAML config file."""
        path = self.config_dir / filename
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def _build_tier_lookup(self):
        """Build tier lookup from config."""
        self.tiers = []
        for tier_id, tier_config in self.config['tier_thresholds'].items():
            self.tiers.append({
                'id': tier_id,
                'name': tier_config['name'],
                'min_beds': tier_config.get('min_beds', 0),
                'max_beds': tier_config.get('max_beds'),
            })
        # Sort by min_beds descending for matching
        self.tiers.sort(key=lambda x: x['min_beds'], reverse=True)

    def _build_size_multiplier_lookup(self):
        """Build size multiplier lookup from config."""
        self.size_multipliers = self.config['system_pricing']['size_multipliers']
        # Sort by max_beds descending for matching
        self.size_multipliers.sort(
            key=lambda x: x['max_beds'] if x['max_beds'] else float('inf'),
            reverse=True
        )

    def _build_system_discount_lookup(self):
        """Build system discount lookup from config."""
        self.system_discounts = self.config['system_pricing']['system_discounts']
        # Sort by min_hospitals descending for matching
        self.system_discounts.sort(key=lambda x: x['min_hospitals'], reverse=True)

    # ═══════════════════════════════════════════════════════════════════════
    # CLASSIFICATION METHODS
    # ═══════════════════════════════════════════════════════════════════════

    def classify_tier(self, beds: int) -> dict:
        """Assign pricing tier based on bed count."""
        for tier in self.tiers:
            min_beds = tier['min_beds']
            max_beds = tier['max_beds']

            if beds >= min_beds:
                if max_beds is None or beds <= max_beds:
                    return tier

        # Default to first tier (smallest)
        return self.tiers[-1]

    def calculate_individual_price(self, beds: int, tier_id: str) -> float:
        """Calculate individual hospital price based on config."""
        pricing = self.config['individual_pricing']

        base_price = pricing['base_prices'].get(tier_id, 5000)
        per_bed_rate = pricing['per_bed_rates'].get(tier_id, 0)
        price_cap = pricing['price_caps'].get(tier_id, 200000)

        # Calculate price
        price = base_price + (beds * per_bed_rate)

        # Apply cap
        return min(price, price_cap)

    def calculate_system_price(self, beds: int) -> float:
        """Calculate per-hospital system deal price based on config."""
        pricing = self.config['system_pricing']
        base_price = pricing['base_price']

        # Find size multiplier - check thresholds in ascending order
        multiplier = 1.0
        size_multipliers = sorted(
            pricing['size_multipliers'],
            key=lambda x: x['max_beds'] if x['max_beds'] else float('inf')
        )

        for sm in size_multipliers:
            max_beds = sm['max_beds']
            if max_beds is None:
                # This is the unbounded tier (1000+)
                multiplier = sm['multiplier']
                break
            elif beds <= max_beds:
                multiplier = sm['multiplier']
                break

        return base_price * multiplier

    def get_system_discount(self, hospital_count: int) -> float:
        """Get discount rate for system based on hospital count."""
        for sd in self.system_discounts:
            min_h = sd['min_hospitals']
            max_h = sd.get('max_hospitals')

            if hospital_count >= min_h:
                if max_h is None or hospital_count <= max_h:
                    return sd['discount']

        return 0.0

    def match_to_system(self, hospital_name: str, city: str, state: str) -> tuple:
        """
        Match hospital to health system using patterns.

        Returns: (system_id, system_name) or (None, None)
        """
        hospital_lower = hospital_name.lower()

        for system in self.systems:
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

            # Check state-specific patterns (more precise)
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

    def classify_segment(self, hospital_name: str, beds: int, rural_urban: str) -> str:
        """Classify hospital segment based on config rules."""
        segments = self.config['segment_classification']['segments']

        for segment in segments:
            # Check bed count constraints
            min_beds = segment.get('min_beds', 0)
            max_beds = segment.get('max_beds')

            if beds < min_beds:
                continue
            if max_beds and beds > max_beds:
                continue

            # Check rural constraint
            if segment.get('rural_only') and rural_urban != 'Rural':
                continue

            # Check name patterns
            patterns = segment.get('patterns', [])
            if patterns:
                for pattern in patterns:
                    if re.search(pattern, hospital_name, re.IGNORECASE):
                        return segment['id']
            elif not segment.get('rural_only'):
                # No patterns means this is a fallback segment
                return segment['id']

        return 'community'  # Default segment

    def calculate_priority_score(self, hospital: dict) -> int:
        """Calculate deal priority score (0-100) based on config weights."""
        if not self.config['priority_scoring']['enabled']:
            return 0

        weights = self.config['priority_scoring']['weights']
        scoring = self.config['priority_scoring']

        score = 0

        # Revenue potential scoring
        price = hospital.get('effective_price', 0)
        for rs in scoring['revenue_scoring']:
            max_price = rs['max_price']
            if max_price is None or price <= max_price:
                score += rs['score'] * weights['revenue_potential']
                break

        # Strategic value scoring
        strategic = scoring['strategic_scoring']
        if hospital.get('entity_type') == 'system_member':
            score += strategic['system_member'] * weights['strategic_value']
        if hospital.get('segment') == 'academic':
            score += strategic['academic_center'] * weights['strategic_value']
        elif hospital.get('segment') == 'regional':
            score += strategic['regional_anchor'] * weights['strategic_value']

        # Accessibility scoring (estimate greenfield probability)
        greenfield_rate = scoring['accessibility_scoring']['greenfield_estimate']
        # Simple heuristic: smaller hospitals more likely greenfield
        beds = hospital.get('beds', 0)
        if beds < 200:
            score += scoring['accessibility_scoring']['greenfield_score'] * weights['accessibility']
        else:
            # Blend based on size
            blend = max(0, 1 - (beds / 1000))
            score += (
                blend * scoring['accessibility_scoring']['greenfield_score'] +
                (1 - blend) * scoring['accessibility_scoring']['displacement_score']
            ) * weights['accessibility']

        # Size factor scoring
        for ss in scoring['size_scoring']:
            max_beds = ss['max_beds']
            if max_beds is None or beds <= max_beds:
                score += ss['score'] * weights['size_factor']
                break

        return min(100, max(0, int(score)))

    def get_region(self, state: str) -> str:
        """Get region name for state."""
        regions = self.config['geographic_adjustments']['regions']
        for region_id, region_data in regions.items():
            if state in region_data['states']:
                return region_data['name']
        return 'Other'

    # ═══════════════════════════════════════════════════════════════════════
    # MAIN WORKFLOW
    # ═══════════════════════════════════════════════════════════════════════

    def classify_hospitals(self, input_csv: Path, output_dir: Path):
        """Main classification workflow."""
        print("=" * 70)
        print("HOSPITAL CLASSIFICATION WORKFLOW")
        print(f"Config version: {self.config['version']}")
        print("=" * 70)

        # Load hospitals
        hospitals = []
        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = list(reader.fieldnames)
            for row in reader:
                hospitals.append(row)

        print(f"\nLoaded {len(hospitals)} hospitals from {input_csv.name}")

        # First pass: Match all hospitals to systems and count per system
        system_hospital_counts = {}
        for hospital in hospitals:
            name = hospital.get('name', '')
            city = hospital.get('city', '')
            state = hospital.get('state', '')

            system_id, system_name = self.match_to_system(name, city, state)
            hospital['_system_id'] = system_id
            hospital['_system_name'] = system_name

            if system_id:
                system_hospital_counts[system_id] = system_hospital_counts.get(system_id, 0) + 1

        # Second pass: Apply all classifications
        stats = {
            'total': len(hospitals),
            'by_tier': {},
            'by_entity_type': {'system_member': 0, 'independent': 0},
            'by_segment': {},
            'by_system': {},
            'tam': {
                'individual': 0,
                'system_level': 0,
                'independent': 0,
                'realistic': 0,
            }
        }

        for hospital in hospitals:
            # Extract base fields
            name = hospital.get('name', '')
            beds = self._get_beds(hospital)
            state = hospital.get('state', '')
            rural_urban = hospital.get('rural_urban', '')

            # 1. Tier classification
            tier = self.classify_tier(beds)
            hospital['tier'] = tier['name']

            # 2. Individual pricing
            individual_price = self.calculate_individual_price(beds, tier['id'])
            hospital['individual_price'] = individual_price

            # 3. Entity type and system pricing
            system_id = hospital.get('_system_id')
            system_name = hospital.get('_system_name')

            if system_id:
                hospital['entity_type'] = 'system_member'
                hospital['parent_system'] = system_name
                hospital['parent_system_id'] = system_id

                # Calculate system price with discount
                base_system_price = self.calculate_system_price(beds)
                hospital_count = system_hospital_counts.get(system_id, 1)
                discount = self.get_system_discount(hospital_count)
                system_price = base_system_price * (1 - discount)
                hospital['system_price'] = system_price
                hospital['effective_price'] = system_price

                stats['by_entity_type']['system_member'] += 1
                stats['by_system'][system_name] = stats['by_system'].get(system_name, 0) + 1
                stats['tam']['system_level'] += system_price
            else:
                hospital['entity_type'] = 'independent'
                hospital['parent_system'] = ''
                hospital['parent_system_id'] = ''
                hospital['system_price'] = ''
                hospital['effective_price'] = individual_price

                stats['by_entity_type']['independent'] += 1
                stats['tam']['independent'] += individual_price

            # 4. Segment classification
            segment = self.classify_segment(name, beds, rural_urban)
            hospital['segment'] = segment

            # 5. Geographic region
            hospital['region'] = self.get_region(state)

            # 6. Priority score
            hospital['priority_score'] = self.calculate_priority_score(hospital)

            # Update stats
            stats['by_tier'][tier['name']] = stats['by_tier'].get(tier['name'], 0) + 1
            stats['by_segment'][segment] = stats['by_segment'].get(segment, 0) + 1
            stats['tam']['individual'] += individual_price

            # Clean up temp fields
            del hospital['_system_id']
            del hospital['_system_name']

        # Calculate realistic TAM
        stats['tam']['realistic'] = stats['tam']['system_level'] + stats['tam']['independent']

        # Define output columns
        new_columns = [
            'entity_type', 'parent_system', 'parent_system_id', 'tier', 'segment',
            'individual_price', 'system_price', 'effective_price', 'priority_score', 'region'
        ]
        output_fieldnames = fieldnames + new_columns

        # Write classified CSV
        output_csv = output_dir / 'hospitals_classified.csv'
        with open(output_csv, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=output_fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(hospitals)

        print(f"\nClassified CSV saved to: {output_csv}")

        # Write summary JSON
        summary = self._build_summary(hospitals, stats)
        output_json = output_dir / 'classification_summary.json'
        with open(output_json, 'w') as f:
            json.dump(summary, f, indent=2)

        print(f"Summary JSON saved to: {output_json}")

        # Print summary
        self._print_summary(stats)

        return hospitals, stats

    def _get_beds(self, row: dict) -> int:
        """Extract bed count from hospital row."""
        for field in ['total_beds', 'beds', 'Beds', 'Total_Beds']:
            value = row.get(field)
            if value:
                try:
                    return int(float(value))
                except (ValueError, TypeError):
                    continue
        return 0

    def _build_summary(self, hospitals: list, stats: dict) -> dict:
        """Build summary JSON structure."""
        return {
            'generated': datetime.now().isoformat(),
            'config_version': self.config['version'],
            'methodology': 'Config-driven classification with pattern matching',
            'totals': {
                'total_hospitals': stats['total'],
                'system_members': stats['by_entity_type']['system_member'],
                'independent': stats['by_entity_type']['independent'],
                'systems_identified': len(stats['by_system']),
            },
            'tam': {
                'individual_tam': stats['tam']['individual'],
                'system_level_tam': stats['tam']['system_level'],
                'independent_tam': stats['tam']['independent'],
                'realistic_tam': stats['tam']['realistic'],
            },
            'by_tier': stats['by_tier'],
            'by_segment': stats['by_segment'],
            'by_system': dict(sorted(stats['by_system'].items(), key=lambda x: -x[1])),
        }

    def _print_summary(self, stats: dict):
        """Print classification summary."""
        print("\n" + "=" * 70)
        print("CLASSIFICATION SUMMARY")
        print("=" * 70)

        print(f"\nTotal hospitals: {stats['total']:,}")
        print(f"System members: {stats['by_entity_type']['system_member']:,} "
              f"({stats['by_entity_type']['system_member']/stats['total']*100:.1f}%)")
        print(f"Independent: {stats['by_entity_type']['independent']:,} "
              f"({stats['by_entity_type']['independent']/stats['total']*100:.1f}%)")
        print(f"Systems identified: {len(stats['by_system'])}")

        print("\nBy Tier:")
        for tier, count in sorted(stats['by_tier'].items()):
            print(f"  {tier}: {count:,}")

        print("\nBy Segment:")
        for segment, count in sorted(stats['by_segment'].items(), key=lambda x: -x[1]):
            print(f"  {segment}: {count:,}")

        print("\n" + "=" * 70)
        print("TAM SUMMARY")
        print("=" * 70)
        print(f"\nIndividual TAM: ${stats['tam']['individual']:,.0f}")
        print(f"System-Level TAM: ${stats['tam']['system_level']:,.0f}")
        print(f"Independent TAM: ${stats['tam']['independent']:,.0f}")
        print(f"Realistic TAM: ${stats['tam']['realistic']:,.0f}")


def main():
    parser = argparse.ArgumentParser(description='Hospital Classification Workflow')
    parser.add_argument('--config', type=Path, default=None,
                        help='Config directory (default: ../configs)')
    parser.add_argument('--input', type=Path, default=None,
                        help='Input CSV file (default: ../hospitals_pricing.csv)')
    parser.add_argument('--output', type=Path, default=None,
                        help='Output directory (default: ..)')

    args = parser.parse_args()

    # Set defaults relative to script location
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent

    config_dir = args.config or base_dir / 'configs'
    input_csv = args.input or base_dir / 'hospitals_pricing.csv'
    output_dir = args.output or base_dir

    # Validate paths
    if not config_dir.exists():
        print(f"Error: Config directory not found: {config_dir}")
        return 1
    if not input_csv.exists():
        print(f"Error: Input CSV not found: {input_csv}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    # Run classification
    classifier = HospitalClassifier(config_dir)
    classifier.classify_hospitals(input_csv, output_dir)

    return 0


if __name__ == '__main__':
    exit(main())
