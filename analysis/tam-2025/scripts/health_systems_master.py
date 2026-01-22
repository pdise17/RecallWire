#!/usr/bin/env python3
"""
Health Systems Master Data
Top 50 US Health Systems with identification patterns

Sources:
- Becker's Hospital Review (2024)
- Definitive Healthcare
- Individual health system websites
"""

# Master list of top 50 health systems with identification patterns
# Each system has:
#   - name: Official name
#   - aliases: Alternative names/patterns to match
#   - headquarters: HQ location
#   - hospital_count: Approximate number of hospitals
#   - states: States where they operate
#   - patterns: Regex patterns for matching hospital names

HEALTH_SYSTEMS_MASTER = [
    # === MEGA SYSTEMS (100+ hospitals) ===
    {
        "id": "hca",
        "name": "HCA Healthcare",
        "aliases": ["HCA", "Hospital Corporation of America"],
        "headquarters": "Nashville, TN",
        "hospital_count": 187,
        "type": "for-profit",
        "patterns": [
            r"HCA\b",
            r"Medical City",
            r"HealthONE",
            r"Tristar",
            r"MountainStar",
            r"Mission Hospital.*Asheville",
            r"Parallon",
        ],
        "state_patterns": {
            "TX": ["Medical City", "Las Palmas", "Del Sol", "Rio Grande"],
            "FL": ["Brandon Regional", "Blake Medical", "Citrus Memorial", "Doctors Hospital.*FL", "Fawcett", "JFK Medical", "Kendall Regional", "Lawnwood", "Largo Medical", "Memorial Hospital.*Jacksonville", "NCH", "Northwest Medical Center", "Northside Hospital.*FL", "Ocala Regional", "Orange Park", "Osceola Regional", "Palms West", "Plantation General", "Poinciana", "Regional Medical Center Bayonet", "St. Lucie", "Twin Cities.*FL", "University Hospital.*FL", "West Florida", "Westside Regional"],
            "CO": ["HealthONE", "Swedish Medical", "Sky Ridge", "Rose Medical", "North Suburban", "Presbyterian/St Luke's.*Denver", "Medical Center of Aurora", "Spalding Rehab"],
            "TN": ["TriStar", "Centennial", "Hendersonville", "Horizon", "Parkridge", "Southern Hills", "Skyline", "Summit"],
            "CA": ["Good Samaritan.*San Jose", "Los Robles", "Regional Medical Center.*San Jose", "Riverside Community"],
            "NV": ["MountainView", "Southern Hills.*NV", "Sunrise", "Valley Health System"],
            "VA": ["Chippenham", "Henrico Doctors", "John Randolph", "Johnston-Willis", "Parham Doctors", "Retreat Doctors", "Spotsylvania Regional"],
            "GA": ["Cartersville Medical", "Coliseum Medical", "Eastside Medical", "Fairview Park", "Redmond Regional"],
        }
    },
    {
        "id": "commonspirit",
        "name": "CommonSpirit Health",
        "aliases": ["CommonSpirit", "CHI", "Catholic Health Initiatives", "Dignity Health"],
        "headquarters": "Chicago, IL",
        "hospital_count": 137,
        "type": "nonprofit",
        "patterns": [
            r"CommonSpirit",
            r"\bCHI\b",
            r"Dignity Health",
            r"Catholic Health Initiatives",
            r"St\.? Joseph.*Health",  # Many CHI facilities
            r"Mercy.*CHI",
        ],
        "state_patterns": {
            "CA": ["Dignity Health", "Marian Regional", "Mercy.*CA", "Dominican", "Sequoia", "St. Mary.*CA", "Woodland Memorial"],
            "TX": ["CHI St. Luke", "Baylor St. Luke", "St. Joseph.*TX"],
            "NE": ["CHI Health", "Immanuel", "Lakeside", "Midlands", "Nebraska Heart"],
            "AZ": ["Dignity Health.*AZ", "Chandler Regional", "Mercy Gilbert", "St. Joseph.*Phoenix"],
            "KY": ["CHI Saint Joseph"],
            "OH": ["Mercy Health.*OH"],
            "CO": ["CommonSpirit.*CO", "Penrose", "St. Francis.*CO"],
        }
    },
    {
        "id": "ascension",
        "name": "Ascension",
        "aliases": ["Ascension Health"],
        "headquarters": "St. Louis, MO",
        "hospital_count": 136,
        "type": "nonprofit",
        "patterns": [
            r"Ascension",
            r"St\.? Vincent.*Ascension",
            r"Providence.*Ascension",
        ],
        "state_patterns": {
            "MI": ["Ascension.*MI", "St. John.*MI", "Borgess", "Genesys", "Providence.*MI", "St. Mary.*MI"],
            "WI": ["Ascension.*WI", "Columbia St. Mary", "Ministry"],
            "IN": ["Ascension St. Vincent", "St. Vincent.*IN", "Peyton Manning"],
            "TX": ["Ascension Seton", "Dell Seton", "Seton.*TX"],
            "TN": ["Ascension Saint Thomas", "Saint Thomas.*TN"],
            "FL": ["Ascension Sacred Heart", "Sacred Heart.*FL", "St. Vincent.*FL"],
            "NY": ["Our Lady of Lourdes.*NY"],
            "MD": ["Ascension Saint Agnes"],
            "OK": ["Ascension St. John.*OK", "Jane Phillips"],
            "KS": ["Ascension Via Christi"],
        }
    },
    {
        "id": "lifepoint",
        "name": "LifePoint Health",
        "aliases": ["LifePoint", "RCCH HealthCare"],
        "headquarters": "Brentwood, TN",
        "hospital_count": 65,
        "type": "for-profit",
        "patterns": [
            r"LifePoint",
        ],
        "state_patterns": {
            # LifePoint hospitals often retain local names
            "VA": ["LewisGale", "Clinch Valley", "Danville Regional", "Sovah Health"],
            "WV": ["Raleigh General", "Williamson"],
            "KY": ["Clark Regional", "Georgetown Community", "Lake Cumberland", "Logan Memorial", "Bourbon Community"],
            "TN": ["NorthCrest", "Sumner Regional", "Livingston Regional"],
        }
    },

    # === LARGE SYSTEMS (50-100 hospitals) ===
    {
        "id": "trinity",
        "name": "Trinity Health",
        "aliases": ["Trinity"],
        "headquarters": "Livonia, MI",
        "hospital_count": 93,
        "type": "nonprofit",
        "patterns": [
            r"Trinity Health",
            r"Mercy Health.*Trinity",
            r"St\.? Joseph Mercy",
            r"St\.? Mary Mercy",
        ],
        "state_patterns": {
            "MI": ["Trinity Health.*MI", "St. Joseph Mercy", "St. Mary Mercy", "Mercy Health.*MI"],
            "OH": ["Trinity.*OH", "Mount Carmel"],
            "IN": ["Saint Joseph Health System"],
            "IA": ["MercyOne", "Mercy Medical Center.*IA"],
            "ID": ["Saint Alphonsus"],
            "NJ": ["St. Francis.*NJ"],
            "NY": ["St. Peter's Health Partners"],
            "MA": ["Mercy Medical Center.*MA"],
        }
    },
    {
        "id": "chs",
        "name": "Community Health Systems",
        "aliases": ["CHS"],
        "headquarters": "Franklin, TN",
        "hospital_count": 69,
        "type": "for-profit",
        "patterns": [
            r"Community Health Systems",
        ],
        "state_patterns": {
            # CHS hospitals typically retain local names
            "AL": ["Grandview Medical", "Crestwood Medical"],
            "AZ": ["Northwest Medical Center.*AZ", "Oro Valley"],
            "FL": ["Bayfront Health", "Northwest.*FL"],
            "IN": ["Bluffton Regional", "Dukes Memorial"],
            "PA": ["Berwick Hospital", "Brandywine", "Easton Hospital", "Jennersville", "Pottstown Memorial"],
            "TN": ["Tennova", "Dyersburg Regional", "Lakeway Regional"],
        }
    },
    {
        "id": "advocate",
        "name": "Advocate Health",
        "aliases": ["Advocate Aurora", "Atrium Health"],
        "headquarters": "Charlotte, NC",
        "hospital_count": 69,
        "type": "nonprofit",
        "patterns": [
            r"Advocate",
            r"Aurora Health",
            r"Atrium Health",
        ],
        "state_patterns": {
            "IL": ["Advocate.*IL", "Christ Medical", "Good Samaritan.*IL", "Lutheran General", "South Suburban", "Trinity.*IL"],
            "WI": ["Aurora.*WI", "Aurora Medical Center", "Aurora St. Luke's", "Aurora Sinai"],
            "NC": ["Atrium Health", "Carolinas Medical", "Levine Children's", "Mercy.*Charlotte"],
            "GA": ["Atrium Health.*GA", "Floyd Medical"],
        }
    },
    {
        "id": "tenet",
        "name": "Tenet Healthcare",
        "aliases": ["Tenet"],
        "headquarters": "Dallas, TX",
        "hospital_count": 60,
        "type": "for-profit",
        "patterns": [
            r"Tenet",
            r"USPI",  # United Surgical Partners
        ],
        "state_patterns": {
            "TX": ["Baptist.*San Antonio", "Nacogdoches Medical", "Resolute Health"],
            "CA": ["Desert Regional", "Emanuel Medical", "Doctors Hospital.*CA", "Doctors Medical Center.*CA", "Fountain Valley Regional", "Placentia-Linda", "San Ramon Regional", "Sierra Vista Regional"],
            "FL": ["Coral Gables", "Delray Medical", "Good Samaritan.*FL", "Hialeah", "North Shore.*FL", "Palm Beach Gardens", "Palmetto General", "St. Mary's.*FL", "West Boca"],
            "AZ": ["Abrazo", "Carondelet", "Maryvale"],
            "AL": ["Brookwood Baptist"],
        }
    },
    {
        "id": "providence",
        "name": "Providence",
        "aliases": ["Providence St. Joseph", "Providence Health"],
        "headquarters": "Renton, WA",
        "hospital_count": 52,
        "type": "nonprofit",
        "patterns": [
            r"Providence(?! .*Ascension)",  # Exclude Ascension's Providence
            r"Swedish.*Seattle",
            r"Kadlec",
        ],
        "state_patterns": {
            "WA": ["Providence.*WA", "Swedish", "Kadlec", "St. Peter.*WA"],
            "OR": ["Providence.*OR", "St. Vincent.*OR", "Milwaukie", "Medford", "Hood River"],
            "CA": ["Providence.*CA", "St. Joseph.*CA", "St. Jude.*CA", "Little Company of Mary", "Mission Hospital.*CA", "Torrance Memorial"],
            "AK": ["Providence Alaska"],
            "MT": ["Providence.*MT", "St. Patrick.*MT"],
        }
    },
    {
        "id": "uhs",
        "name": "Universal Health Services",
        "aliases": ["UHS"],
        "headquarters": "King of Prussia, PA",
        "hospital_count": 28,
        "type": "for-profit",
        "patterns": [
            r"Universal Health Services",
        ],
        "state_patterns": {
            "NV": ["Valley Health System.*NV", "Valley Hospital.*NV", "Summerlin", "Centennial Hills", "Henderson", "Desert Springs"],
            "DC": ["George Washington University Hospital"],
            "TX": ["Texoma Medical", "Doctors Hospital.*Laredo"],
            "CA": ["Corona Regional", "Inland Valley"],
        }
    },

    # === MAJOR REGIONAL SYSTEMS (20-50 hospitals) ===
    {
        "id": "kaiser",
        "name": "Kaiser Permanente",
        "aliases": ["Kaiser"],
        "headquarters": "Oakland, CA",
        "hospital_count": 40,
        "type": "nonprofit",
        "patterns": [
            r"Kaiser",
        ],
        "state_patterns": {
            "CA": ["Kaiser.*CA"],
            "OR": ["Kaiser.*OR"],
            "WA": ["Kaiser.*WA"],
            "CO": ["Kaiser.*CO"],
            "GA": ["Kaiser.*GA"],
            "HI": ["Kaiser.*HI"],
            "VA": ["Kaiser.*VA"],
            "MD": ["Kaiser.*MD"],
            "DC": ["Kaiser.*DC"],
        }
    },
    {
        "id": "bswh",
        "name": "Baylor Scott & White Health",
        "aliases": ["BSWH", "Baylor Scott White"],
        "headquarters": "Dallas, TX",
        "hospital_count": 52,
        "type": "nonprofit",
        "patterns": [
            r"Baylor Scott.*White",
            r"Baylor.*Medical Center",
            r"Scott.*White",
        ],
        "state_patterns": {
            "TX": ["Baylor", "Scott & White", "Hillcrest.*Waco"],
        }
    },
    {
        "id": "upmc",
        "name": "UPMC",
        "aliases": ["University of Pittsburgh Medical Center"],
        "headquarters": "Pittsburgh, PA",
        "hospital_count": 40,
        "type": "nonprofit",
        "patterns": [
            r"\bUPMC\b",
            r"University of Pittsburgh Medical",
        ],
        "state_patterns": {
            "PA": ["UPMC", "Magee-Womens", "Western Psychiatric"],
            "NY": ["UPMC.*NY"],
            "MD": ["UPMC.*MD"],
        }
    },
    {
        "id": "northwell",
        "name": "Northwell Health",
        "aliases": ["North Shore-LIJ"],
        "headquarters": "New Hyde Park, NY",
        "hospital_count": 22,
        "type": "nonprofit",
        "patterns": [
            r"Northwell",
            r"North Shore.*University",
            r"Long Island Jewish",
            r"LIJ\b",
            r"Lenox Hill",
            r"Staten Island University",
        ],
        "state_patterns": {
            "NY": ["North Shore University", "Long Island Jewish", "Lenox Hill", "Staten Island University", "Glen Cove", "Plainview", "Syosset", "Huntington", "Southside", "Peconic Bay", "Mather", "South Shore University"],
        }
    },
    {
        "id": "christus",
        "name": "CHRISTUS Health",
        "aliases": ["CHRISTUS"],
        "headquarters": "Irving, TX",
        "hospital_count": 50,
        "type": "nonprofit",
        "patterns": [
            r"CHRISTUS",
            r"Christus",
        ],
        "state_patterns": {
            "TX": ["CHRISTUS.*TX", "Spohn", "Santa Rosa", "St. Michael.*TX", "St. Elizabeth.*TX"],
            "LA": ["CHRISTUS.*LA", "St. Frances Cabrini", "St. Patrick.*LA"],
            "AR": ["CHRISTUS.*AR", "St. Michael.*AR"],
            "NM": ["CHRISTUS St. Vincent"],
        }
    },
    {
        "id": "adventhealth",
        "name": "AdventHealth",
        "aliases": ["Adventist Health System", "Florida Hospital"],
        "headquarters": "Altamonte Springs, FL",
        "hospital_count": 50,
        "type": "nonprofit",
        "patterns": [
            r"AdventHealth",
            r"Advent Health",
            r"Florida Hospital",
        ],
        "state_patterns": {
            "FL": ["AdventHealth.*FL", "Florida Hospital"],
            "CO": ["AdventHealth.*CO", "Porter", "Littleton", "Castle Rock", "Parker"],
            "GA": ["AdventHealth.*GA", "Gordon", "Murray", "Redmond"],
            "NC": ["AdventHealth.*NC", "Park Ridge"],
            "TX": ["AdventHealth.*TX", "Texas Health.*AdventHealth"],
            "WI": ["AdventHealth.*WI"],
            "KS": ["AdventHealth.*KS", "Shawnee Mission"],
        }
    },
    {
        "id": "sutter",
        "name": "Sutter Health",
        "aliases": ["Sutter"],
        "headquarters": "Sacramento, CA",
        "hospital_count": 22,
        "type": "nonprofit",
        "patterns": [
            r"Sutter",
            r"Alta Bates",
            r"California Pacific Medical",
            r"CPMC",
            r"Eden Medical",
            r"Mills-Peninsula",
            r"Palo Alto Medical Foundation",
        ],
        "state_patterns": {
            "CA": ["Sutter", "Alta Bates", "CPMC", "California Pacific", "Eden Medical", "Mills-Peninsula", "Memorial Medical.*Modesto", "Novato Community", "St. Luke's.*SF"],
        }
    },
    {
        "id": "ochsner",
        "name": "Ochsner Health",
        "aliases": ["Ochsner"],
        "headquarters": "New Orleans, LA",
        "hospital_count": 46,
        "type": "nonprofit",
        "patterns": [
            r"Ochsner",
        ],
        "state_patterns": {
            "LA": ["Ochsner"],
            "MS": ["Ochsner.*MS"],
        }
    },
    {
        "id": "intermountain",
        "name": "Intermountain Health",
        "aliases": ["Intermountain Healthcare", "SCL Health"],
        "headquarters": "Salt Lake City, UT",
        "hospital_count": 33,
        "type": "nonprofit",
        "patterns": [
            r"Intermountain",
            r"SCL Health",
        ],
        "state_patterns": {
            "UT": ["Intermountain.*UT", "LDS Hospital", "Primary Children's", "McKay-Dee", "Utah Valley"],
            "ID": ["Intermountain.*ID", "Cassia Regional"],
            "CO": ["SCL Health", "Lutheran.*CO", "Good Samaritan.*CO", "St. Joseph.*CO"],
            "MT": ["SCL Health.*MT"],
            "NV": ["Intermountain.*NV"],
        }
    },
    {
        "id": "spectrum",
        "name": "Corewell Health",
        "aliases": ["Spectrum Health", "Beaumont Health"],
        "headquarters": "Grand Rapids, MI",
        "hospital_count": 22,
        "type": "nonprofit",
        "patterns": [
            r"Corewell",
            r"Spectrum Health",
            r"Beaumont",
        ],
        "state_patterns": {
            "MI": ["Spectrum", "Beaumont", "Corewell", "Butterworth", "Blodgett", "Helen DeVos"],
        }
    },
    {
        "id": "piedmont",
        "name": "Piedmont Healthcare",
        "aliases": ["Piedmont"],
        "headquarters": "Atlanta, GA",
        "hospital_count": 18,
        "type": "nonprofit",
        "patterns": [
            r"Piedmont(?! Medical)",  # Exclude generic "Piedmont Medical Center"
        ],
        "state_patterns": {
            "GA": ["Piedmont Atlanta", "Piedmont Fayette", "Piedmont Henry", "Piedmont Newton", "Piedmont Mountainside", "Piedmont Newnan", "Piedmont Columbus", "Piedmont Athens", "Piedmont Walton", "Piedmont Eastside"],
        }
    },
    {
        "id": "penn_medicine",
        "name": "Penn Medicine",
        "aliases": ["University of Pennsylvania Health System"],
        "headquarters": "Philadelphia, PA",
        "hospital_count": 9,
        "type": "nonprofit",
        "patterns": [
            r"Penn Medicine",
            r"Hospital of the University of Pennsylvania",
            r"Penn Presbyterian",
            r"Pennsylvania Hospital",
            r"Chester County Hospital",
            r"Lancaster General",
        ],
        "state_patterns": {
            "PA": ["Penn Medicine", "HUP", "Pennsylvania Hospital", "Chester County", "Lancaster General", "Princeton"],
            "NJ": ["Penn Medicine.*NJ", "Princeton"],
        }
    },
    {
        "id": "nyp",
        "name": "NewYork-Presbyterian",
        "aliases": ["NY-Presbyterian", "NYP"],
        "headquarters": "New York, NY",
        "hospital_count": 10,
        "type": "nonprofit",
        "patterns": [
            r"New York.?Presbyterian",
            r"NY.?Presbyterian",
            r"NYP\b",
        ],
        "state_patterns": {
            "NY": ["NewYork-Presbyterian", "NY-Presbyterian", "Weill Cornell", "Columbia University Medical", "Allen Hospital", "Lawrence Hospital", "Hudson Valley", "Queens.*Presbyterian"],
        }
    },
    {
        "id": "mount_sinai",
        "name": "Mount Sinai Health System",
        "aliases": ["Mount Sinai"],
        "headquarters": "New York, NY",
        "hospital_count": 8,
        "type": "nonprofit",
        "patterns": [
            # No general patterns - Mount Sinai name is used by unaffiliated systems
            # Only match via state_patterns for NY
        ],
        "state_patterns": {
            # NYC Mount Sinai only - other "Sinai" hospitals are separate systems
            "NY": ["Mount Sinai", "Mt\\.? Sinai", "N\\.?Y\\.?\\s?Eye and Ear", "NYEE", "Eye and Ear Infirmary"],
        },
        "exclude_patterns": [],
        "notes": "Validated: $25-45K system deal target"
    },
    {
        "id": "nyu_langone",
        "name": "NYU Langone Health",
        "aliases": ["NYU Langone", "NYU Medical Center"],
        "headquarters": "New York, NY",
        "hospital_count": 6,
        "type": "nonprofit",
        "patterns": [
            r"NYU Langone",
            r"NYU.*Medical",
            r"Tisch Hospital",
            r"Rusk Rehabilitation",
        ],
        "state_patterns": {
            "NY": ["NYU Langone", "Tisch Hospital", "Rusk", "Hospital for Joint Diseases"],
            "FL": ["NYU Langone.*FL"],
        }
    },
    {
        "id": "montefiore",
        "name": "Montefiore Health System",
        "aliases": ["Montefiore"],
        "headquarters": "Bronx, NY",
        "hospital_count": 11,
        "type": "nonprofit",
        "patterns": [
            r"Montefiore",
            r"Einstein.*Bronx",
        ],
        "state_patterns": {
            "NY": ["Montefiore", "Moses", "Weiler", "Wakefield", "Nyack", "White Plains.*Montefiore", "New Rochelle.*Montefiore", "St. Luke's Cornwall"],
        }
    },
    {
        "id": "mass_general_brigham",
        "name": "Mass General Brigham",
        "aliases": ["Partners HealthCare", "MGB"],
        "headquarters": "Somerville, MA",
        "hospital_count": 12,
        "type": "nonprofit",
        "patterns": [
            r"Mass General Brigham",
            r"Massachusetts General",
            r"Brigham and Women",
            r"Partners HealthCare",
        ],
        "state_patterns": {
            "MA": ["Massachusetts General", "Brigham and Women", "McLean", "Spaulding Rehabilitation", "Newton-Wellesley", "North Shore Medical", "Faulkner", "Martha's Vineyard", "Nantucket Cottage"],
        }
    },
    {
        "id": "cleveland_clinic",
        "name": "Cleveland Clinic",
        "aliases": ["CCF"],
        "headquarters": "Cleveland, OH",
        "hospital_count": 23,
        "type": "nonprofit",
        "patterns": [
            r"Cleveland Clinic",
        ],
        "state_patterns": {
            "OH": ["Cleveland Clinic", "Fairview", "Hillcrest.*Cleveland", "Marymount.*Cleveland", "South Pointe", "Lutheran.*Cleveland", "Medina", "Akron General"],
            "FL": ["Cleveland Clinic.*FL", "Weston", "Indian River"],
            "NV": ["Cleveland Clinic.*NV", "Lou Ruvo"],
            "AB": ["Cleveland Clinic.*Canada"],
        }
    },
    {
        "id": "mayo",
        "name": "Mayo Clinic",
        "aliases": ["Mayo"],
        "headquarters": "Rochester, MN",
        "hospital_count": 22,
        "type": "nonprofit",
        "patterns": [
            r"Mayo Clinic",
            r"Mayo\b",
        ],
        "state_patterns": {
            "MN": ["Mayo Clinic.*MN", "Rochester Methodist", "Saint Marys.*Rochester"],
            "AZ": ["Mayo Clinic.*AZ", "Mayo.*Phoenix", "Mayo.*Scottsdale"],
            "FL": ["Mayo Clinic.*FL", "Mayo.*Jacksonville"],
            "WI": ["Mayo Clinic Health System.*WI", "Franciscan.*La Crosse", "Eau Claire"],
            "IA": ["Mayo Clinic Health System.*IA"],
        }
    },
    {
        "id": "johns_hopkins",
        "name": "Johns Hopkins Medicine",
        "aliases": ["Johns Hopkins", "JHM"],
        "headquarters": "Baltimore, MD",
        "hospital_count": 6,
        "type": "nonprofit",
        "patterns": [
            r"Johns Hopkins",
            r"JHH\b",
        ],
        "state_patterns": {
            "MD": ["Johns Hopkins", "Howard County General", "Suburban Hospital", "Sibley"],
            "DC": ["Sibley Memorial"],
            "FL": ["Johns Hopkins All Children's"],
        }
    },
    {
        "id": "emory",
        "name": "Emory Healthcare",
        "aliases": ["Emory"],
        "headquarters": "Atlanta, GA",
        "hospital_count": 11,
        "type": "nonprofit",
        "patterns": [
            r"Emory(?! .*University Hospital.*AL)",  # Exclude Emory University Hospital in AL (different)
        ],
        "state_patterns": {
            "GA": ["Emory University Hospital", "Emory Midtown", "Emory Saint Joseph", "Emory Johns Creek", "Emory Decatur", "Emory Hillandale"],
        }
    },
    {
        "id": "duke",
        "name": "Duke Health",
        "aliases": ["Duke University Health System"],
        "headquarters": "Durham, NC",
        "hospital_count": 3,
        "type": "nonprofit",
        "patterns": [
            r"Duke University",
            r"Duke Health",
            r"Duke Regional",
        ],
        "state_patterns": {
            "NC": ["Duke University", "Duke Regional", "Duke Raleigh"],
        }
    },
    {
        "id": "memorial_hermann",
        "name": "Memorial Hermann Health System",
        "aliases": ["Memorial Hermann"],
        "headquarters": "Houston, TX",
        "hospital_count": 17,
        "type": "nonprofit",
        "patterns": [
            r"Memorial Hermann",
        ],
        "state_patterns": {
            "TX": ["Memorial Hermann"],
        }
    },
    {
        "id": "houston_methodist",
        "name": "Houston Methodist",
        "aliases": ["Methodist Hospital Houston"],
        "headquarters": "Houston, TX",
        "hospital_count": 8,
        "type": "nonprofit",
        "patterns": [
            r"Houston Methodist",
            r"Methodist Hospital.*Houston",
        ],
        "state_patterns": {
            "TX": ["Houston Methodist", "Methodist.*Houston"],
        }
    },
    {
        "id": "texas_health",
        "name": "Texas Health Resources",
        "aliases": ["Texas Health", "THR"],
        "headquarters": "Arlington, TX",
        "hospital_count": 29,
        "type": "nonprofit",
        "patterns": [
            r"Texas Health",
        ],
        "state_patterns": {
            "TX": ["Texas Health"],
        }
    },
    {
        "id": "orlando_health",
        "name": "Orlando Health",
        "aliases": ["Orlando Regional"],
        "headquarters": "Orlando, FL",
        "hospital_count": 17,
        "type": "nonprofit",
        "patterns": [
            r"Orlando Health",
            r"Orlando Regional",
            r"Arnold Palmer",
            r"Winnie Palmer",
        ],
        "state_patterns": {
            "FL": ["Orlando Health", "Orlando Regional", "Arnold Palmer", "Winnie Palmer", "Dr. P. Phillips", "South Seminole", "Health Central"],
        }
    },
    {
        "id": "baptist_health_fl",
        "name": "Baptist Health South Florida",
        "aliases": ["Baptist Health FL"],
        "headquarters": "Coral Gables, FL",
        "hospital_count": 12,
        "type": "nonprofit",
        "patterns": [
            r"Baptist Health.*South Florida",
            r"Baptist Hospital.*Miami",
            r"South Miami Hospital",
            r"Doctors Hospital.*Miami",
            r"Homestead Hospital",
            r"Mariners Hospital",
            r"Fishermen's.*Community",
        ],
        "state_patterns": {
            "FL": ["Baptist Health South Florida", "Baptist Hospital.*FL", "South Miami", "Homestead", "Mariners", "Fishermen", "West Kendall"],
        }
    },
    {
        "id": "baptist_health_ky",
        "name": "Baptist Health (Kentucky)",
        "aliases": ["Baptist Health KY"],
        "headquarters": "Louisville, KY",
        "hospital_count": 9,
        "type": "nonprofit",
        "patterns": [
            r"Baptist Health.*Kentucky",
            r"Baptist Health.*KY",
        ],
        "state_patterns": {
            "KY": ["Baptist Health.*KY", "Baptist Health Louisville", "Baptist Health Lexington", "Baptist Health La Grange", "Baptist Health Richmond", "Baptist Health Corbin", "Baptist Health Paducah", "Baptist Health Madisonville", "Baptist Health Hardin"],
        }
    },
    {
        "id": "baptist_health_ar",
        "name": "Baptist Health (Arkansas)",
        "aliases": ["Baptist Health AR"],
        "headquarters": "Little Rock, AR",
        "hospital_count": 11,
        "type": "nonprofit",
        "patterns": [
            r"Baptist Health.*Arkansas",
            r"Baptist Health.*AR",
        ],
        "state_patterns": {
            "AR": ["Baptist Health.*AR", "Baptist Health Medical Center"],
        }
    },
    {
        "id": "wellstar",
        "name": "Wellstar Health System",
        "aliases": ["WellStar"],
        "headquarters": "Marietta, GA",
        "hospital_count": 11,
        "type": "nonprofit",
        "patterns": [
            r"WellStar",
            r"Wellstar",
        ],
        "state_patterns": {
            "GA": ["Wellstar", "WellStar", "Kennestone", "Cobb", "Douglas", "Paulding", "Spalding Regional", "Sylvan Grove", "North Fulton"],
        }
    },
    {
        "id": "bon_secours_mercy",
        "name": "Bon Secours Mercy Health",
        "aliases": ["Bon Secours", "Mercy Health"],
        "headquarters": "Cincinnati, OH",
        "hospital_count": 50,
        "type": "nonprofit",
        "patterns": [
            r"Bon Secours",
            r"Mercy Health(?!.*Trinity)",  # Exclude Trinity's Mercy
        ],
        "state_patterns": {
            "OH": ["Mercy Health.*OH", "Mercy.*Cincinnati", "Mercy.*Toledo", "Mercy.*Youngstown", "Mercy.*Springfield"],
            "KY": ["Mercy Health.*KY", "Bon Secours.*KY"],
            "VA": ["Bon Secours.*VA", "St. Francis.*VA", "St. Mary's.*VA", "Memorial Regional.*VA", "Southampton Memorial"],
            "SC": ["Bon Secours St. Francis"],
        }
    },
    {
        "id": "geisinger",
        "name": "Geisinger",
        "aliases": ["Geisinger Health"],
        "headquarters": "Danville, PA",
        "hospital_count": 10,
        "type": "nonprofit",
        "patterns": [
            r"Geisinger",
        ],
        "state_patterns": {
            "PA": ["Geisinger"],
            "NJ": ["Geisinger.*NJ"],
        }
    },
    {
        "id": "sanford",
        "name": "Sanford Health",
        "aliases": ["Sanford"],
        "headquarters": "Sioux Falls, SD",
        "hospital_count": 47,
        "type": "nonprofit",
        "patterns": [
            r"Sanford(?! .*USD)",  # Exclude USD Medical Center
        ],
        "state_patterns": {
            "SD": ["Sanford.*SD", "Sanford USD"],
            "ND": ["Sanford.*ND"],
            "MN": ["Sanford.*MN"],
        }
    },
    {
        "id": "banner",
        "name": "Banner Health",
        "aliases": ["Banner"],
        "headquarters": "Phoenix, AZ",
        "hospital_count": 33,
        "type": "nonprofit",
        "patterns": [
            r"Banner(?! .*Boswell)",  # Careful with Sun Health acquisition
        ],
        "state_patterns": {
            "AZ": ["Banner.*AZ", "Banner University", "Banner Estrella", "Banner Gateway", "Banner Thunderbird", "Banner Del E. Webb", "Banner Boswell", "Banner Baywood", "Banner Desert", "Banner Goldfield", "Banner Ironwood", "Banner Payson", "Banner Casa Grande"],
            "CO": ["Banner.*CO", "Banner Fort Collins", "Banner Health Center.*CO", "North Colorado", "McKee Medical"],
            "WY": ["Banner.*WY"],
            "NE": ["Banner.*NE"],
        }
    },
    {
        "id": "inova",
        "name": "Inova Health System",
        "aliases": ["Inova"],
        "headquarters": "Falls Church, VA",
        "hospital_count": 6,
        "type": "nonprofit",
        "patterns": [
            r"Inova",
        ],
        "state_patterns": {
            "VA": ["Inova"],
        }
    },
    {
        "id": "sentara",
        "name": "Sentara Healthcare",
        "aliases": ["Sentara"],
        "headquarters": "Norfolk, VA",
        "hospital_count": 12,
        "type": "nonprofit",
        "patterns": [
            r"Sentara",
        ],
        "state_patterns": {
            "VA": ["Sentara"],
            "NC": ["Sentara.*NC", "Sentara Albemarle"],
        }
    },
    {
        "id": "nyc_hhc",
        "name": "NYC Health + Hospitals",
        "aliases": ["HHC", "Health and Hospitals Corporation"],
        "headquarters": "New York, NY",
        "hospital_count": 11,
        "type": "public",
        "patterns": [
            r"NYC Health.*Hospital",
            r"Health.*Hospitals Corporation",
        ],
        "state_patterns": {
            "NY": ["Bellevue", "Elmhurst Hospital Center", "Jacobi", "Kings County Hospital", "Lincoln Medical", "Metropolitan Hospital.*NY", "Queens Hospital Center", "Woodhull", "Harlem Hospital", "Coney Island Hospital", "North Central Bronx"],
        }
    },
    {
        "id": "uchealth",
        "name": "UCHealth",
        "aliases": ["University of Colorado Health"],
        "headquarters": "Aurora, CO",
        "hospital_count": 13,
        "type": "nonprofit",
        "patterns": [
            r"UCHealth",
            r"University of Colorado Hospital",
        ],
        "state_patterns": {
            "CO": ["UCHealth", "University of Colorado Hospital", "Poudre Valley", "Medical Center of the Rockies", "Memorial Hospital.*CO Springs", "Highlands Ranch"],
            "WY": ["UCHealth.*WY"],
        }
    },
    {
        "id": "scripps",
        "name": "Scripps Health",
        "aliases": ["Scripps"],
        "headquarters": "San Diego, CA",
        "hospital_count": 5,
        "type": "nonprofit",
        "patterns": [
            r"Scripps(?! Research)",  # Exclude Scripps Research Institute
        ],
        "state_patterns": {
            "CA": ["Scripps"],
        }
    },
    {
        "id": "sharp",
        "name": "Sharp HealthCare",
        "aliases": ["Sharp"],
        "headquarters": "San Diego, CA",
        "hospital_count": 7,
        "type": "nonprofit",
        "patterns": [
            r"Sharp(?! .*Memorial.*OK)",  # Exclude Sharp Memorial in OK
        ],
        "state_patterns": {
            "CA": ["Sharp"],
        }
    },
    {
        "id": "adventist_west",
        "name": "Adventist Health (West)",
        "aliases": ["Adventist Health"],
        "headquarters": "Roseville, CA",
        "hospital_count": 28,
        "type": "nonprofit",
        "patterns": [
            r"Adventist Health(?!.*System)",  # Different from AdventHealth (FL-based)
        ],
        "state_patterns": {
            "CA": ["Adventist Health.*CA", "Adventist.*Bakersfield", "Adventist.*Glendale", "Adventist.*Hanford", "Adventist.*Lodi", "Adventist.*Reedley", "Adventist.*Selma", "Adventist.*Sonora", "Adventist.*Tulare", "Adventist.*Ukiah", "Adventist.*Willits", "Feather River", "Frank R. Howard", "St. Helena", "Simi Valley"],
            "OR": ["Adventist Health.*OR", "Adventist.*Portland", "Adventist.*Tillamook"],
            "HI": ["Adventist Health Castle"],
        }
    },
]

# Count hospitals
total_hospitals = sum(s.get('hospital_count', 0) for s in HEALTH_SYSTEMS_MASTER)
print(f"Total health systems: {len(HEALTH_SYSTEMS_MASTER)}")
print(f"Total estimated hospitals: {total_hospitals}")
