'''
This file holds functions that handle communication to the users
'''
import smtplib
import time
import settings


def send_text_message(carrier_email, message_chunks):
    '''
    this function sends a text message to the specified user
    '''
    smtp_server = settings.SMTP_SERVER
    smtp_port = settings.SMTP_PORT
    username = settings.SENDER_EMAIL
    password = settings.SENDER_EMAIL_PASSWORD
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(username, password)
    print(len(message_chunks))
    for message in message_chunks:
        message = f'Subject: \n\n{message}'
        print(len(message))
        smtp_connection.sendmail(username, carrier_email, message)
        time.sleep(4)

    # Close the SMTP connection
    smtp_connection.quit()
