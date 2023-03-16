'''
This file holds functions that handle communication to the users
'''
import smtplib
import time
import socket
import logging
import settings


def send_text_message(phone_numbers, message_chunks):
    '''
    this function sends a text message to the specified user
    '''
    logging.info('Sending our snowday prediction to %s people', len(phone_numbers))
    try:
        # Here we are going to login to our mail server
        smtp_server = settings.SMTP_SERVER
        smtp_port = settings.SMTP_PORT
        username = settings.SENDER_EMAIL
        password = settings.SENDER_EMAIL_PASSWORD
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(username, password)
        for number in phone_numbers:
            for message in message_chunks:
                message = f'Subject: \n\n{message}'
                smtp_connection.sendmail(username, number, message)
                time.sleep(1)

        # Close the SMTP connection
        smtp_connection.quit()
    except smtplib.SMTPException as _e:
        logging.error('An SMTP error occurred: %s',{_e})
    except socket.gaierror as _e:
        logging.error('A socket error occurred: %s', {_e})
