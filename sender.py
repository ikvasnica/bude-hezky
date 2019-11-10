#!/usr/bin/python3

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendMail(toEmail, subject, content):
    message = Mail(
        from_email='ivan@ikvasnica.com',
        to_emails=toEmail,
        subject=subject,
        html_content=content
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        
        if response.status_code > 299:
            print('E-mail could not be sent, status code %d, exiting.' % (response.status_code))
            exit(1)

    except Exception as e:
        print(e)
        exit(1)