from weatherMap import weatherMap
from countryCapital import countryCapital
from response import response
import json

def main(event, context):

    request = json.loads(event['body'])

    if 'Country' in request.keys(): 
        capital = countryCapital(request['Country'])
        if capital['statusCode'] != 200:
            body = {'reason': 'Country Not Found'}
            return response(capital['statusCode'], body)
        # Generate city query with country code.
        city = f'''{capital['Capital']}, {capital['CountryCode']}'''
    elif 'City' in request.keys():
        city = request['City']

    weather = weatherMap(city)
    if weather['statusCode'] != 200:
        body = {'reason':'City Not Found'}
        return response(weather['statusCode'], body)
    
    body = {
        'City': weather['City'],
        'CountryCode': weather['CountryCode'],
        'Temperature': weather['CurrentTemperature'],
        'TimeDifference' : request['UserTimeZone'] - weather['CityTimeZone']}

    return response(200, body)


if __name__ == '__main__':
    event = {
        'body': '{\r\n    "Country":"South Africa",\r\n    "UserTimeZone": 120\r\n}'
    }
    res = main(event,'context')
    print(json.dumps(res, indent=4, sort_keys=True))