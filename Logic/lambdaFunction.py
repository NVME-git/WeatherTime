from weatherMap import weatherMap
from countryCapital import countryCapital
from timeZone import timeZone
import json

def main(event, context):
    print(event)

    if 'Country' in event.keys(): 
        capital = countryCapital(event['Country'])
        # Generate city query with country code.
        city = f'''{capital['Capital']}, {capital['CountryCode']}'''
    elif 'City' in event.keys():
        city = event['City']
    else:
        raise Exception('Invalid request parameters')

    units = event['Units']

    weather = weatherMap(city, units)
    
    UserTimeZone = timeZone(event['UserTimeZone'])
    
    response = {
        'City': weather['City'],
        'CountryCode': weather['CountryCode'],
        'Temperature': weather['CurrentTemperature'],
        'TimeDifference' : int(UserTimeZone - weather['CityTimeZone']/60)}
    
    print(response)

    return response


if __name__ == '__main__':
    event = {
        'Country' : 'South Africa',
        'UserTimeZone' : 60,
        'Units' : 'metric'
    }
    res = main(event,'context')
    print(json.dumps(res, indent=4, sort_keys=True))
