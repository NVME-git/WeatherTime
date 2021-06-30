from weatherMap import *
from countryCapital import *

def lambda_handler(event, context):
    if 'Country' in event.keys(): 
        capital = countryCapital(event['Country'])
        if capital['statusCode'] != 200:
            return capital
        # Generate city query with country code.
        city = f'''{capital['Capital']}, {capital['CountryCode']}'''
    elif 'City' in event.keys():
        city = event['City']

    weather = weatherMap(city)
    if weather['statusCode'] != 200:
        return weather
    
    response = {
        'statusCode':200,
        'reason':'OK',
        'City': weather['City'],
        'CountryCode': weather['CountryCode'],
        'Temperature': weather['CurrentTemperature'],
        'TimeDifference' : event['UserTimeZone'] - weather['CityTimeZone']}

    return response


if __name__ == '__main__':
    event = {
        'Country':'South Africa',
        'City':'Dublin',
        'UserTimeZone': 120
    }
    res = lambda_handler(event,'context')
    print(json.dumps(res, indent=4, sort_keys=True))