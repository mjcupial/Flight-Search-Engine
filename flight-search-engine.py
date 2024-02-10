import os
import requests
import json

fl_key = os.getenv('FLK')

def generate_request():
    response = requests.get(
        # f"https://app.goflightlabs.com/flights?access_key=" + fl_key
        f"https://app.goflightlabs.com/advanced-flights-schedules?access_key={fl_key}&iataCode=WRO&type=departure"
    )
    data = response.json()['data']
    return data

def save_data_to_file(data, file_name):
    """To format json in PyCharm: Ctrl+Alt+L"""
    with open(f"{file_name}", "w") as file:
        file.write(str(data))
        file.close()

data = generate_request()
save_data_to_file(data, "WRO_dep.json")
