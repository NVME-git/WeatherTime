# WeatherTime API

## by Nabeel Vandayar

## Overview

Provide a small web application that produces a simple API with 2 endpoints that returns JSON with the following characteristics.
![Overview](images/overview.png)

The problem will be broken down into three parts:

1. Country API: Convert country name to corresponding capital city name.
    * Certain city names are both the capital of a country and a city in another country. For example Dublin in the capital of Ireland and also a city in the USA.
    * Therefore when using the country API, the search must be limited to the country specified. It is not sufficient to search using city name alone.
    * [RESTCountries](https://restcountries.eu/#api-endpoints-all) open API can be used to get the name of a capital city of any country.
        * The API allows searching by native or partial country name eg (Deutschland/Germany or United States)
        * The API returns a list of countries where the desired country may not be the first item. Therefoe a function is required to parse the results and return the first valid country containing a capital.
1. City API: Get current local temperature of a given city as well as timezone.
    * [OpenWeatherMap](https://openweathermap.org/current#current_JSON) is used to obtain the current data for each city.
    * [API reference documentation](Open_Weather_Map.md) containing response parameters is documented here.
    * The timezone is returned as a shift in seconds from UTC time.
    * Temperature Units are an optional parameter that is blank if not specified. When not specified, metric units are used.
1. Time Delta function: Get time difference between the timezone of the person calling the API and the city they search for.
    * Valid time zones occer in the range of [-11; +14] hours inclusively.
    * Timezone calculations should ideally return a time difference in hours.
    * Therefore both the UserTimeZone (which is provided in minutes) and city time must be converted to hours WRT UTC GMT.

## Performance aspects that are considered

* Caching
* Distribution

## Usage considerations

* Language options
* Bad request handling
    * Consistent schema returned for both good and bad requests.
* API Key usage management
    * access
    * monitoring
    * throtling
