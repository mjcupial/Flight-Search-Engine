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



# data = generate_request()

# day = datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
# data = generate_future_flights_request('departure', 'WRO', day)
# save_data_to_file(data, "test.json")

departures = read_data_from_file("test.json")

