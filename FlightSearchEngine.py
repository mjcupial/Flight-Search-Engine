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

def return_data_to_file(input, file_name):
    with open(f"{file_name}", "w") as file:
        file.write(str(input))
        file.close()

def read_data(input):
    with open(f"jsons/{input}", "r") as file:
        data = json.load(file)
        file.close()
        return data

def delete_duplicates_city_and_airports(data):
    """Delete duplicates and format data for city_and_airport"""
    unique_data = {}
    for elem in data:
        key = (elem['nameCountry'], elem['nameCity'])
        if key not in unique_data:
            unique_data[key] = {
                'nameCountry': elem['nameCountry'],
                'codeIso2Country': elem['codeIso2Country'],
                'nameCity': elem['nameCity'],
                'codeIataCity': elem['codeIataCity'],
                'nameAirport': [elem['nameAirport']],
                'codeIataAirport': [elem['codeIataAirport']],
                'codeIcaoAirport': [elem['codeIcaoAirport']]
            }
        else:
            unique_data[key]['nameAirport'].append(elem['nameAirport'])
            unique_data[key]['codeIataAirport'].append(elem['codeIataAirport'])
            unique_data[key]['codeIcaoAirport'].append(elem['codeIcaoAirport'])
    unique_list = list(unique_data.values())
    return unique_list

def find_city_and_airport(city):
    """Type your city and find departure airport"""
    # city = input("Please type departure city: ")
    city = city[0].upper() + city[1:].lower()
    print("Please wait for proccessing data...")
    cities = read_data("Cities.json")           # <-- from file
    airports = read_data("Airports.json")       # <-- from file
    # cities = generate_request('cities')       # <-- origin
    # airports = generate_request('airports')   # <-- origin
    city_and_airport = []
    for elem_cities in cities:
        if elem_cities['nameCity'] == city:
            codeIataCity = elem_cities['codeIataCity']
            for elem_airports in airports:
                if elem_airports['codeIataCity'] == codeIataCity:
                    tpl_city_and_airport = {
                        'nameCountry':elem_airports['nameCountry'],
                        'codeIso2Country':elem_cities['codeIso2Country'],
                        'nameCity':elem_cities['nameCity'],
                        'codeIataCity':elem_cities['codeIataCity'],
                        'nameAirport':elem_airports['nameAirport'],
                        'codeIataAirport':elem_airports['codeIataAirport'],
                        'codeIcaoAirport':elem_airports['codeIcaoAirport']
                    }
                    city_and_airport.append(tpl_city_and_airport)
    city_and_airport = delete_duplicates_city_and_airports(city_and_airport)
    return_data_to_file(city_and_airport, "cities_and_airports.json")
    if bool(city_and_airport) == False:
        print(f"Sorry, but {city} city doesn't exists on the list")
    else:
        return city_and_airport

def format_cities_list(cities_list):
    """
    PARIS (France):
    Charles De Gaulle [CDG] ...
    """
    for elem in cities_list:
        print(f"{elem['nameCity'].upper()} ({elem['nameCountry']}):")
        for e in elem['nameAirport']:
            print(f"\t{e} ({elem['codeIataAirport'][elem['nameAirport'].index(e)]})")


def choose_airport_from_codeIataAirport(iata_generated):
    iata_list = [airport for iata in iata_generated for airport in iata['codeIataAirport']]
    iata_from = input("Type the IATA code from generated list: ").upper()
    while iata_from not in iata_list:
        iata_from = input(f"Your IATA code ({iata_from}) is not on the list. Please type again: ").upper()
    for elem in iata_generated:
        if iata_from in elem['codeIataAirport']:
            airport_index = elem['codeIataAirport'].index(iata_from)
            airport_name = elem['nameAirport'][airport_index]
            print(f"\nAirport: {iata_from} ({airport_name})")
            print(f"City: {elem['nameCity']}")
            print(f"Country: {elem['nameCountry']}")

    # For IATA generate new data structure and store it under iata_from / generate link with IATA
    # create file iata_from

def check_connections_for_iata_from():
    # using other json check connections for iata_from
    # print ot for user
    # call choose_airport_to_codeIAtaAirport() to choose by user airport
    # check if iata exists. If not, try again until exists
    # For IATA generate new data structure and store it under iata_to
    # create file iata_to.json
    pass


def check_connection():
    """Check connection from your 'start airport'"""
    pass

cities_list = find_city_and_airport("PAris")
# print(cities_list)
format_cities_list(cities_list)
choose_airport_from_codeIataAirport(cities_list)