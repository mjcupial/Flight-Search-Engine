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
    unique_data = {}
    for item in data:
        if item["nameCountry"] in unique_data:
            unique_data[item["nameCountry"]]["nameAirport"].append(item["nameAirport"])
        else:
            unique_data[item["nameCountry"]] = {
                "nameCountry": item["nameCountry"],
                "codeIso2Country": item["codeIso2Country"],
                "nameCity": item["nameCity"],
                "codeIataCity": item["codeIataCity"],
                "nameAirport": [item["nameAirport"]],
                "codeIataAirport": item["codeIataAirport"],
                "codeIcaoAirport": item["codeIcaoAirport"]
            }
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

def check_connection():
    """Check connection from your 'start airport'"""
    pass

cities_list = find_city_and_airport("PAris")
print(cities_list)