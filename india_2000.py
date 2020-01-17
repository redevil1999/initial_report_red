import json

with open('india_200.json', encoding= 'utf-16') as file:
    data = json.load(file)

#first select for the country India
india_list_1989_2001 = []
india_list_2001_2015 = []
for observation in data:
    if observation['country'] ==  'India':
        if observation['year'] <= int(2001):
            india_list_1989_2001.append(observation)
        else:
            india_list_2002_2015.append(observation)



#as the best estimate seems the most reliable estimate for the fatalities, it makes most sense to have those in the csv file
#The aim is to compare the fatalities per type of violence of the first half of the dataset to the second half of the dataset,
#Therefore, 2 datasets will be made that include both fatalities and types of violence.
with open('india_1989_2001.csv', 'w', encoding= 'utf8') as file:
    file.write('fatalities, type of violence\n')
    for entry1 in india_list_1989_2001:
        fatalities1 = {
            'deaths': entry1['best'],
            'Type of violence': entry1['type_of_violence']
        }
        file.write(f"{fatalities1['deaths']}, {fatalities1['Type of violence']}\n")

with open('india_2002_2015.csv', 'w', encoding= 'utf8') as file:
    file.write('fatalities, type of violence\n')
    for entry2 in india_list_2002_2015:
        fatalities2 = {
            'deaths': entry2['best'],
            'Type of violence': entry2['type_of_violence']
        }
        file.write(f"{fatalities2['deaths']}, {fatalities2['Type of violence']}\n")