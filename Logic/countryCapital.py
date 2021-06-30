import sys
import json
import requests

def firstValidValue(response):
    countries = response.json()
    return next((country['capital'], country['alpha2Code']) for country in countries if country['capital'])

def countryCapital(countryName):
    URL = f'https://restcountries.eu/rest/v2/name/{countryName}'
    
    response = requests.get(url = URL)

    payload = {
        'statusCode': response.status_code}

    if response.status_code == 200:
        payload['reason'] = 'OK'
        payload['Capital'], payload['CountryCode'] = firstValidValue(response)
    else:
        payload['reason'] = 'Not Found'

    return payload

if __name__ == '__main__':
    if len(sys.argv) > 1:
        response = countryCapital(sys.argv[1])
        print(json.dumps(response, indent=4, sort_keys=True))