import requests

def make_request(url, params, response=None):
    response = response or requests.get(url, params=params)
    response.raise_for_status()

    return response.json()