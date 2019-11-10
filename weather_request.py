#!/usr/bin/python3

import requests, datetime, dateutil.parser
from requests.exceptions import HTTPError

def make_request(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        if response.status_code != 200:
            print('Request not successful (status code %d), exiting.' % (response.status_code))
            exit(1)

        return response.json()

def get_city_code(api_key, city_name):
    responseContent = make_request(
        'https://dataservice.accuweather.com/locations/v1/cities/search', 
        {'apikey': api_key, 'q': city_name}
    )

    if not responseContent:
        print('Sorry! City %s not found. ' % (city_name))
        exit(1)

    return responseContent[0].get('Key')

def extract_tomorrow_forecast(allForecasts):
    tomorrowDate = datetime.date.today() + datetime.timedelta(days=1)
    for oneDayForecast in allForecasts:
        dateOfForecast = dateutil.parser.parse(oneDayForecast.get('Date')).date()
        if dateOfForecast == tomorrowDate:
            return oneDayForecast

    raise Exception('No forecast for tomorrow found.')

def city_forecast(api_key, city_name):
    city_code = get_city_code(api_key, city_name)
    requestUrl = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' + city_code
    responseContent = make_request(requestUrl, {'apikey': api_key})

    allDailyForecasts = responseContent.get('DailyForecasts')
    tomorrowForecast = extract_tomorrow_forecast(allDailyForecasts)
    
    return tomorrowForecast.get('Day').get('Icon')