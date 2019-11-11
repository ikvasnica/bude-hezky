import os

from sendgrid import SendGridAPIClient

SAFE_STATUS_CODE_THRESHOLD = 299

class EmailNotSentException(Exception):
    pass

def send_mail(message, send_grid_client=None):
    try:
        send_grid_client = send_grid_client or SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = send_grid_client.send(message)
    except Exception as e:
        raise EmailNotSentException(e) from e
    else:
        if response.status_code > SAFE_STATUS_CODE_THRESHOLD:
            raise EmailNotSentException(
                'E-mail could not be sent, status code %d, exiting.' % (response.status_code)
            )

        return response
