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


#as the best estimate seems the most reliable estimate for the fatalities, it makes most sense to have those in the csv file
#As the goal of this report is to calculate the number of fatalities in India in 2000, there is no reason to include any other variables
#(especially because the file is already selected for India and the year 2000)
with open('india_fatalities.csv', 'w', encoding= 'utf8') as file:
    file.write('fatalities\n')
    for entry in india_list:
        fatalities = {
            'deaths': entry['best']
        }
        file.write(f"{fatalities['deaths']}\n")