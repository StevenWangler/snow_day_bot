'''
This file holds functions that handle communication to the users
'''
import smtplib
import time
import settings

def send_text_message(phone_numbers, message_chunks):
    '''
    this function sends a text message to the specified user
    '''
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
            print(len(message))
            smtp_connection.sendmail(username, number, message)
            time.sleep(4)

    # Close the SMTP connection
    smtp_connection.quit()
