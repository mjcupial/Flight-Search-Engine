import os
import requests
import json

fl_key = os.getenv('FLK')
fl_request = {
    'real time flights': 'flights',
    'flight schedules': 'advanced-flights-schedules',
    'airports': 'airports',
    'airlines': 'airlines',
    'countries': 'countries',
    'cities': 'cities'
}
city = input("the city of departure: ")
print("Please wait for proccessing data...")

response = requests.get(
    f"https://app.goflightlabs.com/{fl_request['cities']}?access_key="+fl_key
)
data = response.json()['data']

def findCity(city, data):
    cities_list = [f"{elem['nameCity']} | {elem['codeIso2Country']}" for elem in data if elem['nameCity'] == city]
    print(cities_list)
    # for elem in cities_list:
    #     print(f"{elem['nameCity']} | {elem['codeIso2Country']}")

findCity(city, data)