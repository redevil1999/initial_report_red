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
            india_list_2001_2015.append(observation)



#as the best estimate seems the most reliable estimate for the fatalities, it makes most sense to have those in the csv file
#As the goal of this report is to calculate the number of fatalities in India in 2000, there is no reason to include any other variables
#(especially because the file is already selected for India and the year 2000)
# with open('india_fatalities.csv', 'w', encoding= 'utf8') as file:
#     file.write('fatalities, type of violence\n')
#     for entry in india_list:
#         fatalities = {
#             'deaths': entry['best'],
#             'Type of violence': entry['type_of_violence']
#         }
#         file.write(f"{fatalities['deaths']}, {fatalities['Type of violence']}\n")