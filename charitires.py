import requests as r
import time
import json

categories = ['animals']
dictionary = {}
url = "https://www.canadahelps.org/en/search/charities/?category={category}&offset={number}"

for category in categories:
	base = r.get(url.format(category=category, number=str(0))).json()
	print(url.format(category=category, number=str(0)))
	print(base)
	n = base['count']
	i=0
	j=1

	while i<n:
		print(i)
		print(url.format(category=category, number=str(0)))
		dictionary[category] = dict({str(j):r.get(url=url.format(category=str(category), number=str(i))).json()})
		print(dictionary)
		time.sleep(2)
		if i == 40:
			break
		i += 20
		j += 1

with open('data.txt', 'w') as outfile:
	dictionary = json.dumps(dictionary, sort_keys=True, indent=4)
	json.dump(dictionary, outfile)