import requests
import json


def getMAp(loaction):
    parameters = {
        "key": "ck6rRKwcx0ceB54fCot5ga6m6Gb9lWIv",
        "location": loaction,
        # "location": "hadror 38 , beer yakov",
    }
    response = requests.get(
        "http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    data = json.loads(response.text)['results']
    #lat = data[0]['locations'][0]['latLng']['lat']
    #lng = data[0]['locations'][0]['latLng']['lng']
    map = data[0]['locations'][0]['mapUrl']
    newMap = map.replace("size=225,160", "size=1200,700")
    newMap = newMap.replace("zoom=15", "zoom=14")
    print(newMap)
    return newMap
