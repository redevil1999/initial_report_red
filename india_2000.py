import json

with open('india_200.json', encoding= 'utf-16') as file:
    data = json.load(file)

#first select for the country India
india_list = []
for observation in data:
    if observation['country'] ==  'India':
        india_list.append(observation)
        if observation['year'] != int(2000):
            india_list.remove(observation)



with open('india_fatalities.csv', 'w', encoding= 'utf8') as file:
    for entry in india_list:
        fatalities = {
            'deaths': entry['best']
        }
        file.write(f"{fatalities['deaths']}\n")