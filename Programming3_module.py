# Alyosha Perez, Mizuki Hashimoto

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
} # Dictionary with abbreviation as key and state name as value


state_capitals = {
    "WA": "Olympia",
    "OR": "Salem",
    "CA": "Sacramento",
    "OH": "Columbus",
    "NE": "Lincoln",
    "CO": "Denver",
    "MI": "Lansing",
    "MA": "Boston",
    "FL": "Tallahassee",
    "TX": "Austin",
    "OK": "Oklahoma City",
    "HI": "Honolulu",
    "AK": "Juneau",
    "UT": "Salt Lake City",
    "NM": "Santa Fe",
    "ND": "Bismarck",
    "SD": "Pierre",
    "WV": "Charleston",
    "VA": "Richmond",
    "NJ": "Trenton",
    "MN": "Saint Paul",
    "IL": "Springfield",
    "IN": "Indianapolis",
    "KY": "Frankfort",
    "TN": "Nashville",
    "GA": "Atlanta",
    "AL": "Montgomery",
    "MS": "Jackson",
    "NC": "Raleigh",
    "SC": "Columbia",
    "ME": "Augusta",
    "VT": "Montpelier",
    "NH": "Concord",
    "CT": "Hartford",
    "RI": "Providence",
    "WY": "Cheyenne",
    "MT": "Helena",
    "KS": "Topeka",
    "IA": "Des Moines",
    "PA": "Harrisburg",
    "MD": "Annapolis",
    "MO": "Jefferson City",
    "AZ": "Phoenix",
    "NV": "Carson City",
    "NY": "Albany",
    "WI": "Madison",
    "DE": "Dover",
    "ID": "Boise",
    "AR": "Little Rock",
    "LA": "Baton Rouge"
} # Dictionary with abbreviation as key and capital as value

name = input()  # Get the state name
abb = input()  # Get the abbreviation

def state_abb(name, states):
    # Return the abbreviation when given the state name
    for key in states:
        if name == states[key]:
            return key

def abb_state(abb, states):
    # Return the state name when given the abbreviation
    for key in states:
        if abb == key:
            return states[key]

def abb_capital(abb, state_capitals):
    # Return the capital when given the abbreviation
    for key in state_capitals:
        if abb == key:
            return state_capitals[key]

print(state_abb(name, states))
print(abb_state(abb, states))
print(abb_capital(abb, state_capitals))