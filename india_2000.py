import json

with open('india_200.json', encoding= 'utf-16') as file:
    data = json.load(file)

#first select for the country India
india_incidents = []
for observation in data:
    india_incidents.append(observation['country_id'])
    if observation['country'] ==  'India':
        india_incidents.append(observation['country_id'])

print(set(india_incidents))

#select countries with a different country id
#700, 100, 438, 770, 145
