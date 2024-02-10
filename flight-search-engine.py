import os
import requests
from helper import *
import json

FL_KEY = os.getenv('FLK')

def generate_request():
    response = requests.get(
        # f"https://app.goflightlabs.com/flights?access_key=" + FL_KEY
        f"https://app.goflightlabs.com/advanced-future-flights?access_key={FL_KEY}&type=departure&iataCode=WRO&date=2024-02-20"
    )
    data = response.json()['data']
    return data



data = generate_request()
save_data_to_file(data, "test.json")
