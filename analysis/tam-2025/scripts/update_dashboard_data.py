#!/usr/bin/env python3
"""
Update dashboard_data.json with consolidated system-level pricing.
"""

import json
from pathlib import Path

base_dir = Path(__file__).parent.parent

# Load existing dashboard data
with open(base_dir / 'dashboard_data.json') as f:
    dashboard_data = json.load(f)

# Load consolidated health system data
with open(base_dir / 'health_systems_consolidated.json') as f:
    consolidated = json.load(f)

# Update summary with realistic TAM
old_tam = dashboard_data['summary']['total_tam']
new_tam = consolidated['summary']['total_realistic_tam']

dashboard_data['summary']['individual_tam'] = old_tam
dashboard_data['summary']['total_tam'] = new_tam
dashboard_data['summary']['tam_reduction'] = old_tam - new_tam
dashboard_data['summary']['system_level_tam'] = consolidated['summary']['system_level_tam']
dashboard_data['summary']['independent_tam'] = consolidated['summary']['independent_tam']
dashboard_data['summary']['hospitals_in_systems'] = consolidated['summary']['hospitals_in_systems']
dashboard_data['summary']['independent_hospitals'] = consolidated['summary']['independent_hospitals']
dashboard_data['summary']['health_systems_count'] = consolidated['summary']['health_systems_identified']

# Add consolidated health systems
dashboard_data['health_systems_consolidated'] = []
for name, info in sorted(consolidated['health_systems'].items(), key=lambda x: -x[1]['system_price']):
    dashboard_data['health_systems_consolidated'].append({
        'name': name,
        'hospital_count': info['hospital_count'],
        'individual_tam': info['individual_tam'],
        'system_price': info['system_price'],
        'discount_vs_individual': info['discount_vs_individual'],
        'per_hospital': info['per_hospital'],
        'tier': info['tier']
    })

# Add Mount Sinai validation data
dashboard_data['mount_sinai_validation'] = consolidated['mount_sinai_validation']

# Save updated dashboard data
with open(base_dir / 'dashboard_data.json', 'w') as f:
    json.dump(dashboard_data, f, indent=2)

print(f"Dashboard data updated successfully!")
print(f"  Original TAM: ${old_tam:,.0f}")
print(f"  Realistic TAM: ${new_tam:,.0f}")
print(f"  TAM Reduction: ${old_tam - new_tam:,.0f} ({(old_tam - new_tam)/old_tam*100:.1f}%)")
