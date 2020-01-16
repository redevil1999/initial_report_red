import json

with open('india_200.json', encoding= 'utf-16') as file:
    data = json.load(file)

#first select for the country India
india_incidents = []
for observation in data:
    if observation['country'] ==  'India':
        india_incidents.append(observation)
        if observation['year'] != int(2000):
            india_incidents.remove(observation)


for india in india_incidents:
    if india['year'] != 2000:
        print('there is a not 2000 in there!')


