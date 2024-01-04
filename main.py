"""
Snow Day Notifier Module

This module integrates various functionalities to assess the possibility of a snow day based on 
current weather forecasts and predefined policies. Utilizing both weather data and OpenAI's GPT 
predictions, it determines the likelihood of a snow day and subsequently notifies users 
via email. For ease of testing and deployment, a TESTING flag is included to switch 
between hard-coded email recipients and those fetched from Google Forms.

Functions:
    - main(): The primary function which orchestrates the entire flow of the application.
    - fetch_snow_day_policy(): Retrieves the policy related to snow days.
    - create_snow_day_message(policy): Generates a message indicating the possibility of a snow day.
    - generate_email_content(message): Prepares the content for the notification email.
    - should_send_email(message): Determines if the conditions warrant sending out a
      snow day notification.
    - fetch_email_recipients(): Fetches email recipients based on the testing mode.
    - fetch_email_recipients_for_testing(): Provides hard-coded email recipients 
      for testing purposes.
    - send_emails(recipients, message): Sends out the snow day notification emails.

Dependencies:
    - weatherapi: Used to fetch and process weather-related data.
    - openai_actions: Interfaces with OpenAI's GPT for generating and analyzing messages.
    - general_functions: Contains utility functions and configurations.
    - email_functions: Manages email sending functionalities.
    - google_functions: Fetches email recipient data from Google Forms.
    
Note: 
    Before deploying to production, ensure the TESTING flag is set appropriately.
"""
import os
import json
import logging
import weatherapi.weather_api_calls as weather_api
from weatherapi import weather_data
from openai_actions import open_ai_api_calls as openai_api
from openai_actions import open_ai_data as openai_data
from general_functions import general_functions
from email_functions import email_delivery
from google_functions import google_forms
from settings import settings

def main():
    """
    The main function serving as the application's entry point.
    Orchestrates the process of fetching weather data, determining snow day possibilities,
    generating relevant messages, and sending emails.
    """
    logging.info('---- APPLICATION START ----')

    try:
        snow_day_policy = fetch_snow_day_policy()
        snowday_message = create_snow_day_message(snow_day_policy)
        email_message = generate_email_content(snowday_message)
        general_functions.write_prediction_to_file(email_message)

        if should_send_email(email_message):
            recipients = fetch_email_recipients()
            send_emails(recipients, email_message)
        else:
            logging.info('There is a less than 50 percent chance of a snow day. Not sending emails.')

            if settings.TESTING_MODE:
                logging.info('Application is in testing mode, sending the email anyways!')
                # TESTING ONLY: Send email even if the snow day chance is low
                recipients = fetch_email_recipients_for_testing()
                logging.info('Testing users: %s', recipients)
                send_emails(recipients, email_message)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    logging.info('---- APPLICATION END ----')

def fetch_snow_day_policy():
    """
    Fetch the policy related to snow days.
    
    Returns:
        dict: A dictionary or object containing the snow day policy.
    """
    return general_functions.get_snow_day_policy()

def create_snow_day_message(policy):
    """
    Generate a snow day message based on weather data and the given policy.
    
    Args:
        policy (dict): The snow day policy.
    
    Returns:
        str: The generated snow day message.
    """
    # Fetch the relevant weather information
    weather_info = weather_data.get_relevant_weather_information(weather_api.get_forecast())

    # Create a message based on the weather data and policy
    return openai_data.create_open_ai_snow_day_message(weather_info, policy)

def generate_email_content(message):
    """
    Generate the content for the email based on the provided message.
    
    Args:
        message (str): The base message for the email content.
    
    Returns:
        str: The generated email content.
    """
    return openai_api.generate_chat_response(message)

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
    else:
        return google_forms.get_sign_up_responses()

def fetch_email_recipients_for_testing():
    """
    Fetch email recipients for testing purposes.
    
    Returns:
        dict: A dictionary containing email addresses and associated names.
    """
    # Fetching the email recipients from an environment variable
    personal_testing_emails_str = os.environ.get('PERSONAL_TESTING_EMAILS', '{}')

    # Convert the string to a dictionary
    try:
        personal_testing_emails = json.loads(personal_testing_emails_str)
    except json.JSONDecodeError:
        # In case of any error in decoding JSON, return an empty dictionary
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

if __name__ == "__main__":
    # Configure logging settings
    general_functions.configure_logging()
    main()
