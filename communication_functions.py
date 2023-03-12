'''
This file holds functions that handle communication to the users
'''
import smtplib
import settings


def send_text_message(carrier_email, message_body):
    '''
    this function sends a text message to the specified user
    '''
    message = f'Subject: \n\n{message_body}'
    # Log in to the SMTP server
    smtp_server = settings.SMTP_SERVER  # The SMTP server for your email provider
    smtp_port = settings.SMTP_PORT  # The port for the SMTP server
    username = settings.SENDER_EMAIL  # Your email address
    password = settings.SENDER_EMAIL_PASSWORD  # Your email password
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(username, password)

    # Send the email message
    smtp_connection.sendmail(username, carrier_email, message)

    # Close the SMTP connection
    smtp_connection.quit()
