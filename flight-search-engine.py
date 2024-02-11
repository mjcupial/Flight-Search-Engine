import os
import requests
from datetime import datetime, timedelta
from helper import *
import json

FL_KEY = os.getenv('FLK')

def generate_request():
    response = requests.get(
        f"https://app.goflightlabs.com/flights?access_key=" + FL_KEY
    )
    data = response.json()['data']
    return data

def generate_future_flights_request(type, iata, date):
    response = requests.get(
        f"https://app.goflightlabs.com/advanced-future-flights?access_key={FL_KEY}&type={type}&iataCode={iata}&date={date}"
    )
    try:
        data = response.json()['data']
        return data
    except:
        expected_day = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
        raise KeyError(f"Date must be above 7 days to current date: {expected_day}")

def return_links(data, arrival):
    for link in data:
        if link['arrival']['iataCode'] == arrival.lower():
            return link

def format_return_links(link):
    dep_iata = link['departure']['iataCode'].upper()
    dep_icao = link['departure']['icaoCode'].upper()
    dep_time = link['departure']['scheduledTime']
    arr_iata = link['arrival']['iataCode'].upper()
    arr_icao = link['arrival']['icaoCode'].upper()
    arr_time = link['arrival']['scheduledTime']
    dep_t = datetime.strptime(dep_time, '%H:%M')
    arr_t = datetime.strptime(arr_time, '%H:%M')
    time_diff = (arr_t - dep_t)
    time_diff = (datetime.min + time_diff).time().strftime('%H:%M')

    print(f"""
DEPARTURE:\t{dep_iata} ({dep_icao})\tdeparture: {dep_time}
ARRIVAL:\t{arr_iata} ({arr_icao})\tdeparture: {arr_time}
--------------
Airline: {link['airline']['name'].upper()} ({link['airline']['icaoCode'].upper()})\t| time: {time_diff}
    """)


# data = generate_future_flights_request('departure', 'WRO', '2024-02-20')
# save_data_to_file(data, f"departure_test.json")
departures = read_data_from_file("departure_test.json")
link = return_links(departures, 'BCN')
format_return_links(link) #format

