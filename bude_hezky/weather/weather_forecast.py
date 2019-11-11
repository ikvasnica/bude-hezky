import dateutil.parser
from requests.exceptions import RequestException

from bude_hezky.date import tomorrow_checker
from bude_hezky.request import request_maker

API_URL = 'http://dataservice.accuweather.com'
DAILY_FORECASTS_KEY ='DailyForecasts'
API_KEY_KEY = 'apiKey'

class NoForecastRetrievedException(Exception):
    pass

def get_city_code(api_key, city_name, response_content=None):
    try:
        response_content = response_content or request_maker.make_request(
            API_URL + '/locations/v1/cities/search', 
            {API_KEY_KEY: api_key, 'q': city_name}
        )
    except RequestException as e:
        raise NoForecastRetrievedException(e) from e
    else:
        if not response_content:
            raise NoForecastRetrievedException('City %s not found. ' % (city_name))

        return response_content[0].get('Key')

def extract_tomorrow_forecast(all_forecasts, datetime_of_forecast=None): 
    for one_day_forecast in all_forecasts:
        datetime_of_forecast = datetime_of_forecast or dateutil.parser.parse(one_day_forecast.get('Date'))
        if tomorrow_checker.is_tomorrow(datetime_of_forecast):
            return one_day_forecast

    raise NoForecastRetrievedException('No forecast for tomorrow found.')

def get_forecast_for_city(api_key, city_name, response_content=None, city_code=None):
    city_code = city_code or get_city_code(api_key, city_name)
    
    try:
        response_content = response_content or request_maker.make_request(
            '%s/forecasts/v1/daily/5day/%s' % (API_URL, city_code), 
            {API_KEY_KEY: api_key}
        )
    except RequestException as e:
        raise NoForecastRetrievedException(e) from e
    else:
        all_daily_forecasts = response_content.get(DAILY_FORECASTS_KEY)
        tomorrow_forecast = extract_tomorrow_forecast(all_daily_forecasts)
        
        return tomorrow_forecast.get('Day').get('Icon')
