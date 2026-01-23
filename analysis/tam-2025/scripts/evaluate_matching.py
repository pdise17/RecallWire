#!/usr/bin/env python3
"""
Evaluate alternative matching approaches for health system identification.
Tests: fuzzy matching, geographic clustering, multi-signal scoring.
"""

import csv
import re
import yaml
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path


def load_data():
    """Load hospitals and health systems config."""
    base_path = Path(__file__).parent.parent

    # Load hospitals
    hospitals = []
    with open(base_path / 'hospitals_classified.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hospitals.append(row)

    # Load health systems config
    with open(base_path / 'configs' / 'health_systems.yaml', 'r') as f:
        systems_config = yaml.safe_load(f)

    return hospitals, systems_config


def get_independent_hospitals(hospitals):
    """Get only independent hospitals."""
    return [h for h in hospitals if h.get('entity_type') == 'independent']


def tokenize_name(name):
    """Extract meaningful tokens from hospital name."""
    # Normalize
    name = name.lower()

    # Remove common suffixes/prefixes
    remove_words = {
        'hospital', 'hospitals', 'medical', 'center', 'centers', 'health',
        'healthcare', 'system', 'systems', 'regional', 'community', 'memorial',
        'general', 'inc', 'llc', 'corp', 'the', 'of', 'and', 'at', 'campus',
        'facility', 'authority', 'district', 'county', 'clinic', 'clinics'
    }

    # Split on spaces and special chars
    tokens = re.split(r'[\s\-\.\,\&\(\)\/]+', name)

    # Filter tokens
    meaningful = []
    for token in tokens:
        if token and len(token) > 2 and token not in remove_words:
            meaningful.append(token)

    return meaningful


def fuzzy_match_score(name1, name2):
    """Calculate fuzzy match score between two names."""
    return SequenceMatcher(None, name1.lower(), name2.lower()).ratio()


def evaluate_fuzzy_matching(hospitals, systems_config):
    """Evaluate fuzzy string matching approach."""
    print("\n" + "="*80)
    print("APPROACH 1: FUZZY STRING MATCHING")
    print("="*80)

    independents = get_independent_hospitals(hospitals)
    systems = systems_config['health_systems']['systems']

    # Build system name variants
    system_names = {}
    for sys in systems:
        sys_id = sys['id']
        sys_name = sys['name']
        system_names[sys_id] = {
            'name': sys_name,
            'tokens': tokenize_name(sys_name),
            'patterns': sys.get('patterns', [])
        }

    # Find fuzzy matches
    matches = []
    for hospital in independents:
        hosp_name = hospital['name']
        best_match = None
        best_score = 0

        for sys_id, sys_info in system_names.items():
            # Direct name comparison
            score = fuzzy_match_score(hosp_name, sys_info['name'])

            # Also check if hospital contains system name
            if sys_info['name'].lower().split()[0] in hosp_name.lower():
                score = max(score, 0.6)  # Boost if contains first word

            if score > best_score:
                best_score = score
                best_match = (sys_id, sys_info['name'])

        if best_score >= 0.5:  # Threshold
            matches.append({
                'hospital': hosp_name,
                'state': hospital['state'],
                'system': best_match[1],
                'system_id': best_match[0],
                'score': best_score
            })

    # Sort by score
    matches.sort(key=lambda x: x['score'], reverse=True)

    print(f"\nFound {len(matches)} potential matches (score >= 0.5)")
    print("\nTop 30 fuzzy matches:")
    print("-" * 100)
    for m in matches[:30]:
        print(f"  {m['score']:.2f} | {m['hospital'][:45]:<45} | {m['state']} → {m['system']}")

    # Score distribution
    score_bands = defaultdict(int)
    for m in matches:
        if m['score'] >= 0.8:
            score_bands['0.80+'] += 1
        elif m['score'] >= 0.7:
            score_bands['0.70-0.79'] += 1
        elif m['score'] >= 0.6:
            score_bands['0.60-0.69'] += 1
        else:
            score_bands['0.50-0.59'] += 1

    print(f"\nScore distribution:")
    for band, count in sorted(score_bands.items(), reverse=True):
        print(f"  {band}: {count} matches")

    return matches


def evaluate_geographic_clustering(hospitals, systems_config):
    """Evaluate geographic clustering approach."""
    print("\n" + "="*80)
    print("APPROACH 2: GEOGRAPHIC CLUSTERING")
    print("="*80)

    independents = get_independent_hospitals(hospitals)
    systems = systems_config['health_systems']['systems']

    # Build system HQ locations and member locations
    system_locations = {}
    for sys in systems:
        sys_id = sys['id']
        hq = sys.get('headquarters', '')
        if hq:
            # Parse "City, ST" format
            parts = hq.split(',')
            if len(parts) >= 2:
                city = parts[0].strip().lower()
                state = parts[1].strip().upper()[:2]
                system_locations[sys_id] = {
                    'name': sys['name'],
                    'hq_city': city,
                    'hq_state': state,
                    'member_cities': set(),
                    'member_states': set()
                }

    # Find system members and their locations
    system_members = get_system_hospitals(hospitals)
    for sys_id, members in system_members.items():
        if sys_id in system_locations:
            for member in members:
                city = member.get('city', '').lower()
                state = member.get('state', '').upper()
                if city:
                    system_locations[sys_id]['member_cities'].add(city)
                if state:
                    system_locations[sys_id]['member_states'].add(state)

    # Find independents in same city/state as system hospitals
    city_matches = []
    state_matches = []

    for hospital in independents:
        hosp_city = hospital.get('city', '').lower()
        hosp_state = hospital.get('state', '').upper()

        for sys_id, loc_info in system_locations.items():
            # Same city match (strong signal)
            if hosp_city and hosp_city in loc_info['member_cities']:
                city_matches.append({
                    'hospital': hospital['name'],
                    'city': hospital['city'],
                    'state': hosp_state,
                    'system': loc_info['name'],
                    'system_id': sys_id,
                    'match_type': 'city'
                })
            # Same state match (weak signal)
            elif hosp_state and hosp_state in loc_info['member_states']:
                state_matches.append({
                    'hospital': hospital['name'],
                    'city': hospital['city'],
                    'state': hosp_state,
                    'system': loc_info['name'],
                    'system_id': sys_id,
                    'match_type': 'state'
                })

    print(f"\nCity-level matches: {len(city_matches)}")
    print(f"State-level matches: {len(state_matches)}")

    # Sample city matches
    print("\nSample city-level matches (same city as system members):")
    print("-" * 100)
    seen_cities = set()
    for m in city_matches[:50]:
        key = (m['city'], m['system'])
        if key not in seen_cities:
            print(f"  {m['hospital'][:40]:<40} | {m['city']}, {m['state']} | near {m['system']}")
            seen_cities.add(key)
        if len(seen_cities) >= 20:
            break

    return city_matches, state_matches


def get_system_hospitals(hospitals):
    """Group hospitals by their parent system."""
    system_members = defaultdict(list)
    for h in hospitals:
        if h.get('entity_type') == 'system_member' and h.get('parent_system_id'):
            system_members[h['parent_system_id']].append(h)
    return system_members


def evaluate_name_token_matching(hospitals, systems_config):
    """Evaluate name tokenization and token overlap matching."""
    print("\n" + "="*80)
    print("APPROACH 3: NAME TOKEN MATCHING")
    print("="*80)

    independents = get_independent_hospitals(hospitals)
    systems = systems_config['health_systems']['systems']

    # Build system token sets from system names
    system_tokens = {}
    for sys in systems:
        sys_id = sys['id']
        sys_name = sys['name']
        tokens = set(tokenize_name(sys_name))
        # Add key identifying tokens
        for pattern in sys.get('patterns', []):
            pattern_tokens = set(tokenize_name(pattern))
            tokens.update(pattern_tokens)
        system_tokens[sys_id] = {
            'name': sys_name,
            'tokens': tokens
        }

    # Find token overlaps
    matches = []
    for hospital in independents:
        hosp_tokens = set(tokenize_name(hospital['name']))

        best_overlap = 0
        best_match = None

        for sys_id, sys_info in system_tokens.items():
            overlap = hosp_tokens & sys_info['tokens']
            overlap_score = len(overlap)

            if overlap_score > best_overlap:
                best_overlap = overlap_score
                best_match = {
                    'hospital': hospital['name'],
                    'state': hospital['state'],
                    'system': sys_info['name'],
                    'system_id': sys_id,
                    'overlap_count': overlap_score,
                    'overlap_tokens': overlap
                }

        if best_match and best_overlap >= 2:  # At least 2 token overlap
            matches.append(best_match)

    # Sort by overlap count
    matches.sort(key=lambda x: x['overlap_count'], reverse=True)

    print(f"\nFound {len(matches)} matches with 2+ token overlap")
    print("\nTop 30 token overlap matches:")
    print("-" * 100)
    for m in matches[:30]:
        tokens_str = ', '.join(m['overlap_tokens'])
        print(f"  {m['overlap_count']} tokens | {m['hospital'][:40]:<40} → {m['system'][:25]} ({tokens_str})")

    # Overlap distribution
    overlap_counts = defaultdict(int)
    for m in matches:
        overlap_counts[m['overlap_count']] += 1

    print(f"\nOverlap distribution:")
    for count in sorted(overlap_counts.keys(), reverse=True):
        print(f"  {count} tokens: {overlap_counts[count]} matches")

    return matches


def evaluate_keyword_matching(hospitals, systems_config):
    """Evaluate keyword-based matching (brand names, distinctive terms)."""
    print("\n" + "="*80)
    print("APPROACH 4: KEYWORD/BRAND MATCHING")
    print("="*80)

    independents = get_independent_hospitals(hospitals)

    # Extract distinctive brand keywords from known systems
    brand_keywords = {
        'advent': ('AdventHealth', 'adventhealth'),
        'adventist': ('Adventist Health (West)', 'adventist_health'),
        'ascension': ('Ascension', 'ascension'),
        'aurora': ('Advocate Health', 'advocate_health'),
        'advocate': ('Advocate Health', 'advocate_health'),
        'atrium': ('Advocate Health', 'advocate_health'),
        'banner': ('Banner Health', 'banner_health'),
        'baptist': ('Baptist Health (Multi-state)', 'baptist_health_system'),  # Requires state validation
        'baylor': ('Baylor Scott & White Health', 'baylor_scott_white'),
        'baycare': ('BayCare Health System', 'baycare'),
        'bjc': ('BJC HealthCare', 'bjc'),
        'bon secours': ('Bon Secours Mercy Health', 'bon_secours_mercy'),
        'cedars': ('Cedars-Sinai', 'cedars_sinai'),  # Different from Mount Sinai
        'christus': ('CHRISTUS Health', 'christus'),
        'cleveland clinic': ('Cleveland Clinic', 'cleveland_clinic'),
        'commonspirit': ('CommonSpirit Health', 'commonspirit'),
        'dignity': ('CommonSpirit Health', 'commonspirit'),
        'chi ': ('CommonSpirit Health', 'commonspirit'),
        'corewell': ('Corewell Health', 'corewell'),
        'spectrum': ('Corewell Health', 'corewell'),
        'duke': ('Duke Health', 'duke_health'),
        'emory': ('Emory Healthcare', 'emory'),
        'essentia': ('Essentia Health', 'essentia'),
        'fairview': ('M Health Fairview', 'm_health_fairview'),
        'franciscan': ('Franciscan Health', 'franciscan_health'),
        'geisinger': ('Geisinger', 'geisinger'),
        'hca': ('HCA Healthcare', 'hca'),
        'henry ford': ('Henry Ford Health', 'henry_ford'),
        'houston methodist': ('Houston Methodist', 'houston_methodist'),
        'inova': ('Inova Health System', 'inova'),
        'intermountain': ('Intermountain Health', 'intermountain'),
        'jefferson': ('Jefferson Health', 'jefferson_health'),
        'johns hopkins': ('Johns Hopkins Medicine', 'johns_hopkins'),
        'kaiser': ('Kaiser Permanente', 'kaiser_permanente'),
        'kettering': ('Kettering Health', 'kettering'),
        'lehigh valley': ('Lehigh Valley Health Network', 'lehigh_valley'),
        'lifepoint': ('LifePoint Health', 'lifepoint'),
        'marshfield': ('Marshfield Clinic Health System', 'marshfield'),
        'mayo': ('Mayo Clinic', 'mayo_clinic'),
        'memorial hermann': ('Memorial Hermann Health System', 'memorial_hermann'),
        'mercy': ('Mercy (Midwest)', 'mercy_midwest'),  # Midwest specific
        'methodist': ('Methodist Healthcare (Multi-state)', 'methodist_healthcare'),
        'montefiore': ('Montefiore Health System', 'montefiore'),
        'mount sinai': ('Mount Sinai Health System', 'mount_sinai'),  # NY only
        'musc': ('MUSC Health', 'musc'),
        'northwell': ('Northwell Health', 'northwell'),
        'northwestern': ('Northwestern Medicine', 'northwestern'),
        'novant': ('Novant Health', 'novant'),
        'ochsner': ('Ochsner Health', 'ochsner'),
        'ohiohealth': ('OhioHealth', 'ohiohealth'),
        'orlando health': ('Orlando Health', 'orlando_health'),
        'osf': ('OSF HealthCare', 'osf'),
        'penn medicine': ('Penn Medicine', 'penn_medicine'),
        'piedmont': ('Piedmont Healthcare', 'piedmont'),
        'prisma': ('Prisma Health', 'prisma'),
        'providence': ('Providence', 'providence'),
        'sanford': ('Sanford Health', 'sanford'),
        'scripps': ('Scripps Health', 'scripps'),
        'sentara': ('Sentara Healthcare', 'sentara'),
        'sharp': ('Sharp HealthCare', 'sharp'),
        'ssm': ('SSM Health', 'ssm'),
        'stanford': ('Stanford Health Care', 'stanford'),
        'st. joseph': ('CommonSpirit Health', 'commonspirit'),
        'sutter': ('Sutter Health', 'sutter'),
        'tenet': ('Tenet Healthcare', 'tenet'),
        'thedacare': ('ThedaCare', 'thedacare'),
        'trinity': ('Trinity Health', 'trinity_health'),
        'uab': ('UAB Medicine', 'uab_medicine'),
        'uc health': ('UCHealth', 'uchealth'),
        'uci health': ('UCI Health', 'uci_health'),
        'ucla': ('UCLA Health', 'ucla_health'),
        'ucsf': ('UCSF Health', 'ucsf_health'),
        'uf health': ('UF Health', 'uf_health'),
        'universal health': ('Universal Health Services', 'uhs'),
        'university hospital': (None, None),  # Too generic
        'upmc': ('UPMC', 'upmc'),
        'ut health': ('UT Health', 'ut_health'),
        'utmb': ('UTMB Health', 'utmb'),
        'vanderbilt': ('Vanderbilt University Medical Center', 'vanderbilt'),
        'wellspan': ('WellSpan Health', 'wellspan'),
        'wellstar': ('Wellstar Health System', 'wellstar'),
    }

    matches = []
    for hospital in independents:
        hosp_name = hospital['name'].lower()

        for keyword, (system_name, system_id) in brand_keywords.items():
            if system_name is None:
                continue
            if keyword in hosp_name:
                matches.append({
                    'hospital': hospital['name'],
                    'state': hospital['state'],
                    'city': hospital.get('city', ''),
                    'system': system_name,
                    'system_id': system_id,
                    'keyword': keyword
                })
                break  # Only first match

    print(f"\nFound {len(matches)} keyword matches")
    print("\nKeyword matches by system:")

    by_system = defaultdict(list)
    for m in matches:
        by_system[m['system']].append(m)

    for system, system_matches in sorted(by_system.items(), key=lambda x: len(x[1]), reverse=True)[:20]:
        print(f"\n  {system} ({len(system_matches)} matches):")
        for sm in system_matches[:3]:
            print(f"    - {sm['hospital'][:50]} ({sm['state']})")
        if len(system_matches) > 3:
            print(f"    ... and {len(system_matches) - 3} more")

    return matches


def evaluate_area_code_clustering(hospitals, systems_config):
    """Evaluate phone area code clustering."""
    print("\n" + "="*80)
    print("APPROACH 5: PHONE AREA CODE CLUSTERING")
    print("="*80)

    # Get area codes for system members
    system_area_codes = defaultdict(set)
    for hospital in hospitals:
        if hospital.get('entity_type') == 'system_member' and hospital.get('parent_system_id'):
            phone = hospital.get('phone', '')
            if phone:
                # Extract area code
                match = re.search(r'\((\d{3})\)', phone)
                if match:
                    area_code = match.group(1)
                    system_area_codes[hospital['parent_system_id']].add(area_code)

    print(f"\nExtracted area codes for {len(system_area_codes)} systems")

    # Find independents sharing area codes with systems
    independents = get_independent_hospitals(hospitals)
    matches = []

    for hospital in independents:
        phone = hospital.get('phone', '')
        if phone:
            match = re.search(r'\((\d{3})\)', phone)
            if match:
                area_code = match.group(1)

                for sys_id, codes in system_area_codes.items():
                    if area_code in codes:
                        matches.append({
                            'hospital': hospital['name'],
                            'state': hospital['state'],
                            'area_code': area_code,
                            'system_id': sys_id
                        })

    print(f"Found {len(matches)} area code matches")

    # This is a weak signal - many hospitals in same area share codes
    # Better used as confirming signal with other approaches

    return matches


def evaluate_combined_scoring(hospitals, systems_config):
    """Evaluate combined multi-signal scoring approach."""
    print("\n" + "="*80)
    print("COMBINED MULTI-SIGNAL SCORING")
    print("="*80)

    independents = get_independent_hospitals(hospitals)
    systems = systems_config['health_systems']['systems']

    # Weights for different signals
    WEIGHTS = {
        'fuzzy_name': 30,      # Direct name similarity
        'token_overlap': 25,   # Meaningful token overlap
        'keyword_match': 40,   # Brand/keyword match
        'city_match': 15,      # Same city as system member
        'state_match': 5,      # Same state as system member
        'area_code': 5         # Same area code
    }

    # Build system reference data
    system_data = {}
    for sys in systems:
        sys_id = sys['id']
        system_data[sys_id] = {
            'name': sys['name'],
            'tokens': set(tokenize_name(sys['name'])),
            'states': set(),
            'cities': set(),
            'area_codes': set()
        }
        # Add state patterns
        for state in sys.get('state_patterns', {}).keys():
            system_data[sys_id]['states'].add(state)

    # Add member location data
    for hospital in hospitals:
        if hospital.get('entity_type') == 'system_member' and hospital.get('parent_system_id'):
            sys_id = hospital['parent_system_id']
            if sys_id in system_data:
                system_data[sys_id]['states'].add(hospital.get('state', ''))
                system_data[sys_id]['cities'].add(hospital.get('city', '').lower())
                phone = hospital.get('phone', '')
                if phone:
                    match = re.search(r'\((\d{3})\)', phone)
                    if match:
                        system_data[sys_id]['area_codes'].add(match.group(1))

    # Score each independent against each system
    results = []
    for hospital in independents:
        hosp_name = hospital['name']
        hosp_state = hospital.get('state', '')
        hosp_city = hospital.get('city', '').lower()
        hosp_phone = hospital.get('phone', '')
        hosp_area_code = ''
        if hosp_phone:
            match = re.search(r'\((\d{3})\)', hosp_phone)
            if match:
                hosp_area_code = match.group(1)

        hosp_tokens = set(tokenize_name(hosp_name))

        best_match = None
        best_score = 0
        best_signals = {}

        for sys_id, sys_info in system_data.items():
            score = 0
            signals = {}

            # Fuzzy name match
            fuzzy_score = fuzzy_match_score(hosp_name, sys_info['name'])
            if fuzzy_score >= 0.5:
                signals['fuzzy_name'] = fuzzy_score
                score += WEIGHTS['fuzzy_name'] * fuzzy_score

            # Token overlap
            overlap = hosp_tokens & sys_info['tokens']
            if len(overlap) >= 2:
                token_score = min(len(overlap) / 3, 1.0)  # Normalize
                signals['token_overlap'] = len(overlap)
                score += WEIGHTS['token_overlap'] * token_score

            # City match
            if hosp_city and hosp_city in sys_info['cities']:
                signals['city_match'] = True
                score += WEIGHTS['city_match']

            # State match
            if hosp_state and hosp_state in sys_info['states']:
                signals['state_match'] = True
                score += WEIGHTS['state_match']

            # Area code match
            if hosp_area_code and hosp_area_code in sys_info['area_codes']:
                signals['area_code'] = True
                score += WEIGHTS['area_code']

            if score > best_score:
                best_score = score
                best_match = sys_info['name']
                best_signals = signals

        if best_score >= 25:  # Minimum threshold
            results.append({
                'hospital': hosp_name,
                'state': hosp_state,
                'city': hosp_city,
                'best_match': best_match,
                'score': best_score,
                'signals': best_signals
            })

    # Sort by score
    results.sort(key=lambda x: x['score'], reverse=True)

    print(f"\nFound {len(results)} matches with combined score >= 25")
    print("\nTop 40 multi-signal matches:")
    print("-" * 120)

    for r in results[:40]:
        signals_str = ', '.join([f"{k}={v}" for k, v in r['signals'].items()])
        print(f"  {r['score']:5.1f} | {r['hospital'][:40]:<40} | {r['state']} → {r['best_match'][:25]} | {signals_str}")

    # Score distribution
    score_bands = defaultdict(int)
    for r in results:
        if r['score'] >= 50:
            score_bands['50+'] += 1
        elif r['score'] >= 40:
            score_bands['40-49'] += 1
        elif r['score'] >= 30:
            score_bands['30-39'] += 1
        else:
            score_bands['25-29'] += 1

    print(f"\nScore distribution:")
    for band in ['50+', '40-49', '30-39', '25-29']:
        print(f"  {band}: {score_bands[band]} matches")

    return results


def identify_likely_missed_affiliations(hospitals):
    """Identify patterns in independent hospitals that suggest missed affiliations."""
    print("\n" + "="*80)
    print("ANALYSIS: LIKELY MISSED AFFILIATIONS")
    print("="*80)

    independents = get_independent_hospitals(hospitals)

    # Look for common prefixes in independent names
    prefixes = defaultdict(list)
    for hospital in independents:
        name = hospital['name']
        # Get first 2-3 words
        words = name.split()
        if len(words) >= 2:
            prefix2 = ' '.join(words[:2])
            prefixes[prefix2].append(hospital)
        if len(words) >= 3:
            prefix3 = ' '.join(words[:3])
            prefixes[prefix3].append(hospital)

    # Find prefixes with multiple hospitals (potential missed systems)
    print("\nIndependent hospitals sharing prefixes (potential systems):")
    print("-" * 80)

    potential_systems = []
    for prefix, hosp_list in sorted(prefixes.items(), key=lambda x: len(x[1]), reverse=True):
        if len(hosp_list) >= 3 and len(prefix) > 8:  # 3+ hospitals, prefix > 8 chars
            # Filter out generic prefixes
            if not any(generic in prefix.lower() for generic in ['regional medical', 'community hospital', 'memorial hospital', 'county hospital', 'general hospital']):
                potential_systems.append((prefix, hosp_list))

    for prefix, hosp_list in potential_systems[:20]:
        states = set(h['state'] for h in hosp_list)
        print(f"\n  '{prefix}' ({len(hosp_list)} hospitals across {len(states)} states: {', '.join(sorted(states))})")
        for h in hosp_list[:3]:
            print(f"    - {h['name'][:60]} ({h['city']}, {h['state']})")
        if len(hosp_list) > 3:
            print(f"    ... and {len(hosp_list) - 3} more")

    return potential_systems


def main():
    """Run all matching evaluations."""
    print("Loading data...")
    hospitals, systems_config = load_data()

    total = len(hospitals)
    independents = len(get_independent_hospitals(hospitals))
    system_members = total - independents

    print(f"\nDataset: {total} hospitals")
    print(f"  - System members: {system_members} ({system_members/total*100:.1f}%)")
    print(f"  - Independents: {independents} ({independents/total*100:.1f}%)")

    # Run evaluations
    fuzzy_matches = evaluate_fuzzy_matching(hospitals, systems_config)
    token_matches = evaluate_name_token_matching(hospitals, systems_config)
    keyword_matches = evaluate_keyword_matching(hospitals, systems_config)
    city_matches, state_matches = evaluate_geographic_clustering(hospitals, systems_config)
    combined_results = evaluate_combined_scoring(hospitals, systems_config)
    potential_systems = identify_likely_missed_affiliations(hospitals)

    # Summary
    print("\n" + "="*80)
    print("SUMMARY & RECOMMENDATIONS")
    print("="*80)

    print(f"""
Evaluation Results:
  - Fuzzy matching: {len(fuzzy_matches)} candidates (score >= 0.5)
  - Token overlap: {len(token_matches)} candidates (2+ tokens)
  - Keyword/brand: {len(keyword_matches)} candidates
  - Geographic (city): {len(city_matches)} candidates
  - Combined scoring: {len(combined_results)} candidates (score >= 25)
  - Potential new systems: {len(potential_systems)} prefixes with 3+ hospitals

Key Insights:
  1. Keyword/brand matching is most reliable for known systems
  2. Token overlap catches variations (St. vs Saint, abbreviations)
  3. Geographic clustering is weak alone but good confirming signal
  4. Combined scoring with multiple signals reduces false positives

Recommended Approach:
  - Use keyword matching as primary method (high confidence)
  - Add token overlap for name variations
  - Require state validation to avoid geographic false positives
  - Consider adding potential new systems identified by prefix analysis

High-Confidence Candidates (combined score 40+):
  {len([r for r in combined_results if r['score'] >= 40])} hospitals
""")


if __name__ == '__main__':
    main()
