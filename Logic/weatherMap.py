import sys
import json
import requests

def weatherMap(cityName, units):
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    APPID = '0682b1fe6a0ef574f8f18e3bf49fc2f0'
    if not units: units = 'metric'
    if units not in ['standard', 'metric', 'imperial']: raise Exception('Invalid Units')
    
    PARAMS = {'q':cityName, 'APPID':APPID, 'units':units}
    response = requests.get(url = URL, params = PARAMS)

    if response.status_code != 200: raise Exception('Invalid City')
        
    data = response.json()

    return {
        'CountryCode' : data['sys']['country'],
        'City' : data['name'],
        'CityTimeZone' : int(data['timezone']/60),
        'CurrentTemperature' : data['main']['temp']
    }
    
    return payload

if __name__ == '__main__':
    if len(sys.argv) > 1:
        response = weatherMap(sys.argv[1])
        print(json.dumps(response, indent=4, sort_keys=True))