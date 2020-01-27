import requests as r
import time
import json

def get_page_json(category=str, offset=0) -> json:
    url = "https://www.canadahelps.org/en/search/charities/?category=%s&offset=%d" % (category, offset)
    print(f"Getting: {url}")
    response = r.get(url)
    return response.json()

categories = ['animals']
dictionary = {}

for category in categories:
    base_count = get_page_json(category)['count']
    print(f"Base Count:\n{base_count}")
    dictionary[category] = list()
    offset = 0

    while offset < base_count:
        results = get_page_json(category, offset)['results']
        for item in results:
            dictionary[category].append(item)
        offset += 20

    print(len(dictionary[category]))

with open('datag.txt', 'w') as outfile:
    json.dump(dictionary, outfile, indent=4, sort_keys=True)
