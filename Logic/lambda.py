from weatherMap import *
from countryCapital import *

def lambda_handler(event, context):
    if 'Country' in event.keys(): 
        capital = countryCapital(event['Country'])
        # TODO Capital error handling
        city = f'''{capital['Capital']}, {capital['CountryCode']}'''
    elif 'City' in event.keys():
        city = event['City']

    weather = weatherMap(city)
    # TODO Weather error handling
    
    response = {
        'City': weather['City'],
        'Country': weather['Country'],
        'Temperature': weather['CurrentTemperature'],
        'TimeDifference' : event['UserTimeZone'] - weather['CityTimeZone']}

    return response


if __name__ == '__main__':
    event = {
        'Country':'United States',
        'City':'Dublin',
        'UserTimeZone': 120
    }
    res = lambda_handler(event,'context')
    print(json.dumps(res, indent=4, sort_keys=True))