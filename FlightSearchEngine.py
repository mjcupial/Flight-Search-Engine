import os
import requests
import json

# fl_key = os.getenv('FLK')
# fl_request = {
#     'real time flights': 'flights',
#     'flight schedules': 'advanced-flights-schedules',
#     'airports': 'airports',
#     'airlines': 'airlines',
#     'countries': 'countries',
#     'cities': 'cities'
# }
# city = input("the city of departure: ")
#
# response = requests.get(
#     f"https://app.goflightlabs.com/{fl_request['cities']}?access_key="+fl_key)
# data = response.json()
# print(data)






# Opening JSON file
f = open('Cities.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['data']:
    # print(i)
    if i['nameCity'] == "Berlin":
        print(i)

# Closing file
f.close()

