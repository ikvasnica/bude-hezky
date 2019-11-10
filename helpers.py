#!/usr/bin/python3

import argparse, sys, os
from dotenv import load_dotenv

def parse_arguments():
    city_key = 'mesto'
    email_key = 'email'

    parser = argparse.ArgumentParser()
    parser.add_argument(city_key, help='Město, kde bydlíš. Můžeš zkusit i vesnici.')
    parser.add_argument('--' + email_key, help='E-mail, kam pošlu informaci o hezkém počasí.')
    
    arguments = vars(parser.parse_args())
    city = arguments[city_key]
    email = arguments[email_key] if (email_key in arguments) else None

    return [city, email]


def get_weather_api_key():
    load_dotenv()

    return os.getenv('WEATHER_API_KEY')