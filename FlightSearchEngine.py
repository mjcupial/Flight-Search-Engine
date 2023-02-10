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

def find_and_select_city(city, data):
    """Find your city as a 'start airport'"""
    cities_list = [f"{elem['nameCity']} | {elem['codeIso2Country']}" for elem in data if elem['nameCity'] == city]
    if bool(cities_list) == False:
        print("Sorry")
    return cities_list

def find_airport():
    """Show the list of available airports for choosen city"""
    pass

def check_connection(start_airport):
    """Check connection from your 'start airport'"""
    pass

start_airport = find_and_select_city(city, data)
# print(start_airport)