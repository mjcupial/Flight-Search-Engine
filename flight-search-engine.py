import os
import requests
from helper import *
import json

fl_key = os.getenv('FLK')

def generate_request():
    response = requests.get(
        f"https://app.goflightlabs.com/flights?access_key=" + fl_key
    )
    data = response.json()['data']
    return data



data = generate_request()
save_data_to_file(data, "WRO_dep.json")
