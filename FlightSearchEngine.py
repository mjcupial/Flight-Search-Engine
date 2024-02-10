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
    if type(fl_key) != str:
        raise Exception("Check your fl_key value")
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

def delete_duplicates_city_and_airportss(data):
    """Delete duplicates and format data for city_and_airports"""
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

def find_city_and_airports(direction):
    """Type your city and find departure airport"""
    city = input(f"Please type {direction} city: ")
    city = city[0].upper() + city[1:].lower()
    print("Please wait for proccessing data...")
    cities = read_data("Cities.json")           # <-- from file
    airports = read_data("Airports.json")       # <-- from file
    # cities = generate_request('cities')       # <-- origin
    # airports = generate_request('airports')   # <-- origin
    city_and_airports = []
    for elem_city in cities:
        if elem_city['nameCity'] == city:
            codeIataCity = elem_city['codeIataCity']
            for elem_airport in airports:
                if elem_airport['codeIataCity'] == codeIataCity:
                    tpl_city_and_airports = {
                        'nameCountry':elem_airport['nameCountry'],
                        'codeIso2Country':elem_city['codeIso2Country'],
                        'nameCity':elem_city['nameCity'],
                        'codeIataCity':elem_city['codeIataCity'],
                        'nameAirport':elem_airport['nameAirport'],
                        'codeIataAirport':elem_airport['codeIataAirport'],
                        'codeIcaoAirport':elem_airport['codeIcaoAirport']
                    }
                    city_and_airports.append(tpl_city_and_airports)
    city_and_airports = delete_duplicates_city_and_airportss(city_and_airports)
    return_data_to_file(city_and_airports, "cities_and_airports.json")
    if bool(city_and_airports) == False:
        print(f"Sorry, but {city} city doesn't exists on the list")
    else:
        return city_and_airports

def format_cities_list(cities_list):
    """
    PARIS (France):
    Charles De Gaulle [CDG] ...
    """
    for elem in cities_list:
        print(f"{elem['nameCity'].upper()} ({elem['nameCountry']}):")
        for e in elem['nameAirport']:
            print(f"\t{e} | IATA: {elem['codeIataAirport'][elem['nameAirport'].index(e)]}")


def return_specific_airport(iata_generated):
    iata_list = [airport for iata in iata_generated for airport in iata['codeIataAirport']]
    print(iata_list)
    iata = input("\nType the IATA code from generated list: ").upper()
    while iata not in iata_list:
        iata = input(f"Your IATA code ({iata}) is not on the list. Please type again: ").upper()
    for elem in iata_generated:
        if iata in elem['codeIataAirport']:
            airport_index = elem['codeIataAirport'].index(iata)
            airport_name = elem['nameAirport'][airport_index]
            print(f"\nAirport: {iata} ({airport_name})")
            print(f"City: {elem['nameCity']}")
            print(f"Country: {elem['nameCountry']}")

def check_connections_for_iata():
    # using other json check connections for iata
    # print ot for user
    # call choose_airport_to_codeIAtaAirport() to choose by user airport
    # check if iata exists. If not, try again until exists
    # For IATA generate new data structure and store it under iata_to
    # create file iata_to.json
    pass


def check_connection():
    """Check connection from your 'start airport'"""
    pass

cities_list = find_city_and_airports("departure")
format_cities_list(cities_list)
return_specific_airport(cities_list)
print("\n")
cities_list = find_city_and_airports("arriaval")
format_cities_list(cities_list)
return_specific_airport(cities_list)
