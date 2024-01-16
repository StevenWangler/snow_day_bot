"""
This module provides functionalities for generating and sending emails based on
the output of OpenAI's GPT-4 model. 
It interfaces with various services including OpenAI's API, email delivery systems,
and Google Forms to manage the process of constructing, deciding, and sending emails.
The module's capabilities extend to generating email content using GPT-4,
determining whether to send an email based on its content, fetching email recipients,
and sending the emails. It's designed to work in both testing and production environments,
with special handling for testing scenarios.

Functions:
    generate_email_content(message): Generates email content using OpenAI's GPT-4.
    should_send_email(message): Determines if an email should be sent based on its content.
    fetch_email_recipients(): Fetches email recipients from Google Forms or testing settings.
    fetch_email_recipients_for_testing(): Fetches email recipients specifically
    for testing purposes.
    send_emails(recipients, message): Sends emails to the provided recipients.

The module utilizes external modules such as 'os', 'json', 'logging', 
and custom modules for OpenAI actions, 
email functions, Google functionalities, and settings. This modular
design allows for easy maintenance and 
scalability, while also encapsulating various aspects of email generation and delivery process.
"""

import os
import json
import logging
import time
from openai_actions import open_ai_api_calls as openai_api
from openai_actions import open_ai_data as openai_data
from email_functions import email_delivery
from google_functions import google_forms
from settings import settings

def generate_email_content(message):
    """
    Generate the content for the email based on the provided message.
    
    Args:
        message (str): The base message for the email content.
    
    Returns:
        str: The generated email content.
    """
    assistant = openai_api.get_assistant()
    thread = openai_api.create_thread()
    openai_api.add_message_to_thread(thread.id, message)
    run = openai_api.run_assistant_on_thread(thread.id, assistant)
    while True:
        status = openai_api.check_run_status(thread.id, run.id)
        if status == 'completed':
            break
        print('Waiting for Blizzard response...')
        time.sleep(10)

    response = openai_api.get_messages(thread.id)
    prediction = response.data[0]
    for content in prediction.content:
        if not hasattr(content, 'type'):
            continue

        if content.type == 'text' and hasattr(content, 'text') and hasattr(content.text, 'value'):
            prediction = content.text.value
            break

    print(f'\n\n\n{prediction}')

    return prediction

def should_send_email(message):
    """
    Determine if an email should be sent based on the provided message.
    
    Args:
        message (str): The email content.
    
    Returns:
        bool: True if the email should be sent, False otherwise.
    """
    # Analyze the message to determine the likelihood of a snow day
    analyze_message = openai_data.create_open_ai_prediction_check_message(message)
    result = str(openai_api.generate_chat_response(analyze_message))

    return result.lower() == "true"

def fetch_email_recipients():
    """
    Fetch email recipients based on the TESTING flag.
    
    Returns:
        dict: A dictionary containing email addresses and associated names.
    """
    if settings.TESTING_MODE:
        return fetch_email_recipients_for_testing()

    return google_forms.get_sign_up_responses()

def fetch_email_recipients_for_testing():
    """
    Fetch email recipients for testing purposes.
    
    Returns:
        dict: A dictionary containing email addresses and associated names.
    """
    # Fetching the email recipients from an environment variable
    personal_testing_emails_str = os.environ.get('PERSONAL_TESTING_EMAILS', '{}')
    logging.info('Personal testing emails: %s', personal_testing_emails_str)

    # Convert the string to a dictionary
    try:
        personal_testing_emails = json.loads(personal_testing_emails_str)
    except json.JSONDecodeError as ex:
        # In case of any error in decoding JSON, return an empty dictionary
        logging.error('Error fetching test emails. Error: %s', ex)
        personal_testing_emails = {}

    return personal_testing_emails

def send_emails(recipients, message):
    """
    Send emails to the provided recipients with the given message.
    
    Args:
        recipients (dict): A dictionary containing email addresses and associated names.
        message (str): The content of the email.
    """
    email_delivery.send_email_to_user(recipients, message)
