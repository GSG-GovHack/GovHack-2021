from geojson import loads
from json import dumps
import requests

FILE = "HobartParks.geojson"
NAME_KEY = "Park_Name"
CATEGORY_KEY = "ASSET_CATEGORY"
URL = "http://127.0.0.1:8000/places"

with open(FILE, 'r') as f:
    data = loads(f.read())
    f.close()

for feature in data['features']:
    name = feature['properties'][NAME_KEY]
    #category = feature['properties'][CATEGORY_KEY]
    points = feature['geometry']['coordinates']
    try:
        resp = requests.post(URL, json={
            "name": name,
            "type": 'park',
            "bounds": [points],
        })
    except:
        print(f"Park {name} failed!")
    else:
        if resp.status_code >= 200 and resp.status_code < 300:
            print(f"Saved park {name}")
        else:
            print(f"Park {name} failed! Code {resp.status_code}")

print(resp.text)
