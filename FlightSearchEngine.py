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

def generate_request(fl_request_key):
    """function for generate requests based on fl_request dictionary"""
    response = requests.get(
        f"https://app.goflightlabs.com/{fl_request[fl_request_key]}?access_key=" + fl_key
    )
    data = response.json()['data']
    return data

def create_data(input, file_name):
    with open(f"{file_name}", "w") as file:
        file.write(str(input))
        file.close()

def find_city_and_airport(city):
    """Type your city and find departure airport"""
    # city = input("Please type departure city: ")
    city = city[0].upper() + city[1:].lower()
    print("Please wait for proccessing data...")
    cities = generate_request('cities')
    airports = generate_request('airports')
    airports_lst = []
    for elem_cities in cities:
        if elem_cities['nameCity'] == city:
            codeIataCity = elem_cities['codeIataCity']
            for elem_airports in airports:
                if elem_airports['codeIataCity'] == codeIataCity:
                    tpl = {
                        'nameCountry':elem_airports['nameCountry'],
                        'codeIso2Country':elem_cities['codeIso2Country'],
                        'nameCity':elem_cities['nameCity'],
                        'codeIataCity':elem_cities['codeIataCity'],
                        'nameAirport':elem_airports['nameAirport'],
                        'codeIataAirport':elem_airports['codeIataAirport'],
                        'codeIcaoAirport':elem_airports['codeIcaoAirport']
                    }
                    airports_lst.append(tpl)
                    create_data(airports_lst, "airports_lst.json")
    if bool(airports_lst) == False:
        print(f"Sorry, but {city} city doesn't exists on the list")
    else:
        return airports_lst

def check_connection():
    """Check connection from your 'start airport'"""
    pass

cities_list = find_city_and_airport('Paris')
print(cities_list)