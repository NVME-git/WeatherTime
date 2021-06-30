import json
import requests

def firstValidValue(response):
    countries = response.json()
    return next((country['capital'], country['alpha2Code']) for country in countries if country['capital'])

def countryCapital(countryName):
    URL = f'https://restcountries.eu/rest/v2/name/{countryName}'
    
    response = requests.get(url = URL)

    payload = {
        'statusCode': response.status_code,
        'reason': response.reason}

    if response.status_code == 200:
        payload['Capital'], payload['CountryCode'] = firstValidValue(response)

    return payload

if __name__ == '__main__':
    response = countryCapital('United States')
    print(json.dumps(response, indent=4, sort_keys=True))