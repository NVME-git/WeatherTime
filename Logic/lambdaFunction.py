from weatherMap import weatherMap
from countryCapital import countryCapital
import json

def main(event, context):
    print(event)

    if 'Country' in event.keys(): 
        capital = countryCapital(event['Country'])
        if capital['statusCode'] != 200:
            raise Exception('Country Not Found')
        # Generate city query with country code.
        city = f'''{capital['Capital']}, {capital['CountryCode']}'''
    elif 'City' in event.keys():
        city = event['City']

    weather = weatherMap(city)
    if weather['statusCode'] != 200:
        raise Exception('City Not Found')
    
    # TODO UserTimeZone validation
    body = {
        'City': weather['City'],
        'CountryCode': weather['CountryCode'],
        'Temperature': weather['CurrentTemperature'],
        'TimeDifference' : int(event['UserTimeZone']) - weather['CityTimeZone']}

    return body


if __name__ == '__main__':
    event = {
        "Country" : "South Africa",
        "UserTimeZone" : 60
    }
    res = main(event,'context')
    print(json.dumps(res, indent=4, sort_keys=True))