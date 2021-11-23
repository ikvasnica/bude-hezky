import argparse
import os
import sys

from dotenv import load_dotenv
from requests.exceptions import RequestException

from bude_hezky.content import content_builder
from bude_hezky.weather import weather_forecast

CITY_OPTION_KEY = 'mesto'
EMAIL_OPTION_KEY = 'email'
CHAT_OPTION_KEY = 'chat'

parser = argparse.ArgumentParser()
parser.add_argument(CITY_OPTION_KEY, help='Město, kde bydlíš a kód státu (např. Prague,CZ). Můžeš zkusit i vesnici.')
parser.add_argument(f'--{EMAIL_OPTION_KEY}', help='E-mail, na který pošleme informaci, zda bude hezky.')
parser.add_argument(f'--{CHAT_OPTION_KEY}', help='Telegram chat ID (ideálně skupina), kam se zašle informace o hezkém počasí.')
cli_arguments = vars(parser.parse_args())

load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')

city = cli_arguments[CITY_OPTION_KEY]
to_email = cli_arguments[EMAIL_OPTION_KEY]
chat = cli_arguments[CHAT_OPTION_KEY]
try:
    tomorrow_forecasts = weather_forecast.get_forecasts_for_city(api_key, city)
except RequestException as e:
    print(f'Počasí nezjištěno kvůli chybě: {e}')
    sys.exit(1)

sunny_hours = weather_forecast.get_sunny_like_hours(tomorrow_forecasts)
if not sunny_hours:
    print(':( Zítra raději zůstaň doma.')
    sys.exit()

hours_string = ', '.join(str(s) for s in content_builder.build_sunny_ranges(sunny_hours))
final_message = content_builder.rreplace(f'Hurá! Zítra bude ve městě {city} hezky mezi {hours_string}. Běž ven s kočárkem!', ', ', ' a ', 1)
print(final_message)

is_error = False
if to_email:
    from sendgrid.helpers.mail import Mail
    from bude_hezky.sender import email_sender

    print('Posílám e-mail...')
    message = Mail(
        from_email='ivan@ikvasnica.com',
        to_emails=to_email,
        subject='Zítra bude hezky',
        html_content=final_message
    )
    try:
        email_sender.send_mail(message)
    except email_sender.EmailNotSentException as e:
        print(f'E-mail nemohl být poslán kvůli chybě: {e}')
        is_error = True

if chat:
    from bude_hezky.sender import telegram_sender

    print('Posílám zprávu přes Telegram...')
    try:
        telegram_sender.send(chat, final_message)
    except RequestException as e:
        print(f'Posílání zprávy přes Telegram selhalo kvůli chybě: {e}')
        is_error = True

if is_error:
    sys.exit(1)
