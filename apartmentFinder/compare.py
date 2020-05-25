from apartmentFinderWeb import find_data as find1
from apartmentsWeb import find_data as find2
from apartmentFinderLinks import city_search as city_search1
from apartmentFinderLinks import links as links1
from apartmentsLinks import city_search as city_search2
from apartmentsLinks import links as links2

city = input('Please enter a city name: ')
state = input('Please enter the state: ')
beds = input('Please enter a number of beds: ')

state_dict = {'alabama': 'al', 'alaska': 'ak', 'arizona': 'az', "arkansas": 'ar', 'california': 'ca', 'colorado': 'co',
              'connecticut': 'ct', 'delaware': 'de', 'florida': 'fl', 'georgia': 'ga', 'hawaii': 'hi', 'idaho': 'id',
              'illinois': 'il', 'indiana': 'id', 'iowa': 'ia', 'kansas': 'ks', 'kentucky': 'ky', 'louisiana': 'la',
              'maine': 'me', 'maryland': 'md', 'massachusetts': 'ma', 'michigan': 'mi', 'minnesota': 'mn',
              'mississippi': 'ms', 'missouri': 'mo', 'montana': 'mt', 'nebraska': 'ne', 'nevada': 'nv',
              'new hampshire': 'nh', 'new jersey': 'nj', 'new mexico': 'nm', 'new york': 'ny', 'north carolina': 'nc',
              'north dakota': 'nd', 'ohio': 'oh', 'oklahoma': 'ok', 'oregon': 'or', 'pennsylvania': 'pa',
              'rhode island': 'ri', 'south carolina': 'sc', 'south dakota': 'sd', 'tennessee': 'tn', 'texas': 'tx',
              'utah': 'ut', 'vermont': 'vt', 'virginia': 'va', 'washington': 'wa', 'west virgina': 'wv',
              'wisconsin': 'wi', 'wyoming': 'wy'}

abbrev = state_dict[state]

city_search1(city, state)
city_search2(city, abbrev)

first_web = []

for link in links1:
    first_web.append(find1(beds, link))

second_web = []

for link in links2:
    second_web.append(find2(beds, link))

print(first_web)
print(second_web)