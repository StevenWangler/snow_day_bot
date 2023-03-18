'''
This file holds functions that handle communication to the users
'''
from email.mime.text import MIMEText
import smtplib
import time
import socket
import logging
from typing import List
import settings.settings as settings


def send_text_messages_to_user(phone_numbers: List[str], message_chunks: List[str]):
    '''
    this function sends a text message to the specified user
    '''
    logging.info('Sending our snowday prediction to %s people', len(phone_numbers))
    try:
        username = settings.SENDER_EMAIL
        smtp_connection = create_smtp_connection(username)
        for number in phone_numbers:
            send_sub_messages_to_user(smtp_connection, message_chunks, number, username)
            time.sleep(3)  # delay in between users

        close_smtp_connection(smtp_connection)
    except smtplib.SMTPException as _e:
        logging.error('An SMTP error occurred: %s', {_e})
    except socket.gaierror as _e:
        logging.error('A socket error occurred: %s', {_e})


def send_sub_messages_to_user(smtp_connection, message_chunks, number, username, max_retries: int = 3):
    '''
    This function will send all of the messages to the given user.
    because we often have more than 1 message to send (due to sms restrictions on length)
    we need to send the user separate text messages to get out the whole message.
    '''
    for message in message_chunks:
        recipient = f'{number}'
        message = f'{message}'
        msg = MIMEText(message)
        msg['From'] = username
        msg['To'] = recipient
        retries = 0
        while retries < max_retries:
            try:
                smtp_connection.send_message(msg)
                status = smtp_connection.noop()[0]
                if status == 250:
                    logging.info('Message delivered to %s', recipient)
                    break

                retries += 1
                logging.warning('Delivery failed for %s. Retrying... (retry %s of %s)', recipient, retries, max_retries)
            except smtplib.SMTPException as _e:
                retries += 1
                logging.warning('SMTPException occurred when delivering message to %s. Retrying... (retry %s of %s) (%s)',recipient, retries, max_retries, str(_e))
                time.sleep(2)  # delay before retrying
        if retries == max_retries:
            logging.error('Delivery failed for %s after %s retries', recipient, max_retries)

        time.sleep(5)  # delay in between messages



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
    smtp_connection.login(username, settings.SENDER_EMAIL_PASSWORD)
    return smtp_connection


def close_smtp_connection(smtp_connection):
    '''
    This function closes our smtp mail connection
    '''
    # Close the SMTP connection
    smtp_connection.quit()
