"""
Email Communication Module

This module provides functionalities related to sending emails to users.
It encapsulates the SMTP logic and provides a cleaner interface for email communication.

Dependencies:
- email.mime.text: To construct MIME text messages.
- smtplib: To handle SMTP communication.
- time: To introduce delays for retries.
- socket: To handle socket-related errors.
- logging: To log application events and errors.
- settings.settings: To access application-specific settings.
"""

import os
from email.mime.text import MIMEText
import smtplib
import time
import socket
import logging
from settings import settings

def send_email_to_user(email_addresses, message):
    '''
    this function sends an email to the specified user
    '''
    logging.info('Sending our snowday prediction to %s people', len(email_addresses))
    try:
        username = os.environ.get('SENDER_EMAIL')
        smtp_connection = create_smtp_connection(username)
        for email in email_addresses:
            send_email(smtp_connection, message, email, email_addresses[email], username)

        close_smtp_connection(smtp_connection)
    except smtplib.SMTPException as _e:
        logging.error('An SMTP error occurred: %s', {_e})
    except socket.gaierror as _e:
        logging.error('A socket error occurred: %s', {_e})


def send_email(smtp_connection, message, email, first_name, username, max_retries: int = 3):
    '''
    This function will loop through all of our email addresses, sending the prediction
    to each one.
    '''
    recipient = f'{email}'
    message = f'{message}\n\nStay cool,\nBlizzard'
    msg = MIMEText(message)
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = f'{first_name}, your snow day prediction is here...'
    retries = 0
    while retries < max_retries:
        try:
            smtp_connection.send_message(msg)
            status = smtp_connection.noop()[0]
            if status == 250:
                logging.info('Message delivered')
                break

            retries += 1
            logging.warning('Delivery failed. Retrying... (retry %s of %s)', retries, max_retries)
        except smtplib.SMTPException as _e:
            retries += 1
            logging.warning('SMTPException occurred when delivering message. Retrying... (retry %s of %s) (%s)', retries, max_retries, str(_e))
            time.sleep(2)  # delay before retrying
    if retries == max_retries:
        logging.error('Delivery failed for %s after %s retries', recipient, max_retries)


def create_smtp_connection(username):
    '''
    This function creates the smtp connection that is used to 
    send an email to the user.
    '''
    # Here we are going to login to our mail server
    # In this particular case, it's a gmail server hooked to the bots email
    smtp_server = settings.SMTP_SERVER
    smtp_port = settings.SMTP_PORT
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(username, os.environ.get('SENDER_EMAIL_PASSWORD'))
    return smtp_connection


def close_smtp_connection(smtp_connection):
    '''
    This function closes our smtp mail connection
    '''
    # Close the SMTP connection
    smtp_connection.quit()
