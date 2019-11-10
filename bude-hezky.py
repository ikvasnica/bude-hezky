#!/usr/bin/python3

import helpers
from weather_request import city_forecast

[city, email] = helpers.parse_arguments()
api_key = helpers.get_weather_api_key()

tomorrow_forecast = city_forecast(api_key, city)
sunnyLikeCodes = [1, 2, 3, 4, 5, 6, 20, 21, 30]

if tomorrow_forecast in sunnyLikeCodes:
    print('Hurá! Zítra bude hezky, běž na kolo!')
else:
    print(':( Zítra raději zůstaň doma.')