import sys
import json
import requests

def weatherMap(cityName, units='standard'):
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    APPID = '0682b1fe6a0ef574f8f18e3bf49fc2f0'
    
    PARAMS = {'q':cityName, 'APPID':APPID, 'units':units}
    response = requests.get(url = URL, params = PARAMS)
    payload = {
        'statusCode': response.status_code,
        'reason': response.reason}

    if response.status_code == 200:
        data = response.json()
        payload['CountryCode'] = data['sys']['country']
        payload['City'] = data['name']
        payload['CityTimeZone'] = int(data['timezone']/60) 
        payload['CurrentTemperature'] = data['main']['temp']
    
    return payload

if __name__ == '__main__':
    if len(sys.argv) > 1:
        response = weatherMap(sys.argv[1])
        print(json.dumps(response, indent=4, sort_keys=True))