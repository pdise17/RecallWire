#!/usr/bin/env python3
"""
State-by-state analysis to identify missed health system affiliations.
Focuses on large independents and common naming patterns within each state.
"""

import csv
import re
from collections import defaultdict
from pathlib import Path


def load_hospitals():
    """Load classified hospitals."""
    base_path = Path(__file__).parent.parent
    hospitals = []
    with open(base_path / 'hospitals_classified.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hospitals.append(row)
    return hospitals


def analyze_by_state(hospitals):
    """Analyze independent hospitals by state."""
    by_state = defaultdict(list)

    for h in hospitals:
        if h.get('entity_type') == 'independent':
            state = h.get('state', 'Unknown')
            by_state[state].append(h)

    return by_state


def find_large_independents(hospitals, min_beds=200):
    """Find large independent hospitals that are likely system members."""
    large = []
    for h in hospitals:
        if h.get('entity_type') == 'independent':
            try:
                beds = int(float(h.get('total_beds', 0) or 0))
                if beds >= min_beds:
                    large.append({
                        'name': h['name'],
                        'state': h['state'],
                        'city': h.get('city', ''),
                        'beds': beds,
                        'revenue': h.get('estimated_revenue', '')
                    })
            except:
                pass

    return sorted(large, key=lambda x: x['beds'], reverse=True)


def find_state_patterns(independents):
    """Find common naming patterns within a state's independents."""
    # Extract potential system prefixes
    prefix_groups = defaultdict(list)

    for h in independents:
        name = h['name']
        words = name.split()

        # Try 2-word and 3-word prefixes
        if len(words) >= 2:
            prefix2 = ' '.join(words[:2])
            # Skip generic prefixes
            if not any(g in prefix2.lower() for g in ['regional medical', 'community hospital', 'memorial hospital', 'county hospital', 'general hospital', 'medical center']):
                prefix_groups[prefix2].append(h)

        if len(words) >= 3:
            prefix3 = ' '.join(words[:3])
            if not any(g in prefix3.lower() for g in ['regional medical center', 'community hospital', 'memorial hospital']):
                prefix_groups[prefix3].append(h)

    # Return groups with 2+ hospitals
    return {k: v for k, v in prefix_groups.items() if len(v) >= 2}


def main():
    print("Loading hospitals...")
    hospitals = load_hospitals()

    total = len(hospitals)
    independents = [h for h in hospitals if h.get('entity_type') == 'independent']
    system_members = total - len(independents)

    print(f"\nDataset: {total} hospitals")
    print(f"  System members: {system_members} ({system_members/total*100:.1f}%)")
    print(f"  Independents: {len(independents)} ({len(independents)/total*100:.1f}%)")

    # State-by-state analysis
    by_state = analyze_by_state(hospitals)

    print("\n" + "="*80)
    print("STATE-BY-STATE INDEPENDENT ANALYSIS")
    print("="*80)

    # Sort by number of independents
    state_counts = [(state, len(hosps)) for state, hosps in by_state.items()]
    state_counts.sort(key=lambda x: x[1], reverse=True)

    print("\nStates with most independents:")
    print("-" * 50)
    for state, count in state_counts[:20]:
        pct = count / len(independents) * 100
        print(f"  {state}: {count} independents ({pct:.1f}%)")

    # Detailed analysis for top states
    print("\n" + "="*80)
    print("DETAILED STATE ANALYSIS (Top 15 states)")
    print("="*80)

    for state, _ in state_counts[:15]:
        state_independents = by_state[state]
        patterns = find_state_patterns(state_independents)

        # Find large hospitals
        large = [h for h in state_independents if int(float(h.get('total_beds', 0) or 0)) >= 200]

        if patterns or large:
            print(f"\n{'='*60}")
            print(f"STATE: {state} ({len(state_independents)} independents)")
            print(f"{'='*60}")

            if large:
                print(f"\n  Large independents (200+ beds) - likely system members:")
                for h in sorted(large, key=lambda x: int(float(x.get('total_beds', 0) or 0)), reverse=True)[:10]:
                    beds = int(float(h.get('total_beds', 0) or 0))
                    print(f"    {beds:4d} beds | {h['name'][:50]:<50} | {h.get('city', '')}")

            if patterns:
                # Sort patterns by group size
                sorted_patterns = sorted(patterns.items(), key=lambda x: len(x[1]), reverse=True)
                print(f"\n  Common naming patterns (potential systems):")
                for prefix, group in sorted_patterns[:8]:
                    if len(prefix) > 6:  # Skip short prefixes
                        print(f"    '{prefix}' ({len(group)} hospitals):")
                        for h in group[:3]:
                            print(f"      - {h['name'][:55]}")
                        if len(group) > 3:
                            print(f"      ... and {len(group) - 3} more")

    # Large independents across all states
    print("\n" + "="*80)
    print("LARGEST INDEPENDENT HOSPITALS (likely system members)")
    print("="*80)

    large_all = find_large_independents(hospitals, min_beds=300)
    print(f"\nFound {len(large_all)} independents with 300+ beds")
    print("\nTop 50 largest independents:")
    print("-" * 90)

    for h in large_all[:50]:
        print(f"  {h['beds']:4d} beds | {h['state']} | {h['name'][:55]:<55} | {h['city']}")

    # Identify likely missed systems from patterns
    print("\n" + "="*80)
    print("LIKELY MISSED HEALTH SYSTEMS")
    print("="*80)

    # Collect all prefix patterns across states
    all_patterns = defaultdict(list)
    for state, state_hosps in by_state.items():
        patterns = find_state_patterns(state_hosps)
        for prefix, group in patterns.items():
            for h in group:
                h['state'] = state  # Ensure state is set
                all_patterns[prefix].append(h)

    # Filter to significant patterns
    significant = {k: v for k, v in all_patterns.items()
                   if len(v) >= 3 and len(k) > 8}

    print(f"\nFound {len(significant)} potential systems (3+ hospitals, prefix > 8 chars)")
    print("\nTop candidates:")

    for prefix, group in sorted(significant.items(), key=lambda x: len(x[1]), reverse=True)[:25]:
        states = set(h['state'] for h in group)
        if len(states) <= 3:  # Regional systems typically span 1-3 states
            print(f"\n  '{prefix}' - {len(group)} hospitals in {', '.join(sorted(states))}")
            for h in group[:4]:
                beds = int(float(h.get('total_beds', 0) or 0))
                print(f"    {beds:4d} beds | {h['name'][:50]} ({h.get('city', '')}, {h['state']})")
            if len(group) > 4:
                print(f"    ... and {len(group) - 4} more")


if __name__ == '__main__':
    main()
