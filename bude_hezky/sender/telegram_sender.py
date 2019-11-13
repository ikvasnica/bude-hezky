import os
import requests

def send(chat, message):
    bot_token = os.environ.get('TELEGRAM_API_KEY')
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat}&parse_mode=Markdown&text={message}'

    response = requests.get(send_text)
    response.raise_for_status()

    return response.json()