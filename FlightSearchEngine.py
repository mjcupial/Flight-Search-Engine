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

TEMP_VAR = ['Paris | FR', 'Paris | US', 'Paris | US']


def generate_request(fl_request_key):
    """function for generate requests based on fl_request dictionary"""
    response = requests.get(
        f"https://app.goflightlabs.com/{fl_request[fl_request_key]}?access_key=" + fl_key
    )
    data = response.json()['data']
    return data

def find_and_select_city():
    """Find your city as a 'start airport'"""
    city = input("the city of departure: ")
    city = city[0].upper() + city[1:].lower()
    print("Please wait for proccessing data...")
    cities = generate_request('cities')
    airports = generate_request('airports')
    cities_list = []
    for elem_cities in cities:
        if elem_cities['nameCity'] == city:
    #         cities_list.append(f"{elem['nameCity']} | {elem['codeIso2Country']}")
    #         print(f"{elem['nameCity']} | {elem['codeIso2Country']}")
    #         codeIataCity = elem['codeIataCity']
    #         for elem in airports:
    #             if elem['codeIataCity'] == codeIataCity:
    #                 print(f"{elem['nameCountry']} --- {elem['nameAirport']}")
    # # cities_list = [f"{elem['nameCity']} | {elem['codeIso2Country']}" for elem in cities if elem['nameCity'] == city]
    # if bool(cities_list) == False:
    #     print(f"Sorry, but {city} city doesn't exists on the list")
    # else:
    #     print(cities_list)
    #     return cities_list
            codeIataCity = elem_cities['codeIataCity']
            for elem_airports in airports:
                if elem_airports['codeIataCity'] == codeIataCity:
                    print(f"country: {elem_airports['nameCountry']} | city: {elem_cities['nameCity']} | airport: {elem_airports['nameAirport']}")


def find_airport(cities_list):
    """Show the list of available airports for choosen city"""
    print(cities_list)
    print([(i, city) for i, city in enumerate(cities_list, start = 1)])
    print([f"{i}: {city}" for i, city in enumerate(cities_list, start = 1)])
    for i, city in enumerate(cities_list, start = 1):
        print(f"{i}: {city}")


def check_connection():
    """Check connection from your 'start airport'"""
    pass

cities_list = find_and_select_city()
# find_airport(cities_list)
# find_airport(TEMP_VAR)