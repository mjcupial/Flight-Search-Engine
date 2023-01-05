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

req = requests.get(f"https://app.goflightlabs.com/{fl_request['flight schedules']}?access_key="+fl_key)
print(req.json())
