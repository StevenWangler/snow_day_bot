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

import logging
from general_functions import general_functions
from email_functions import email_helpers
from settings import settings

def main():
    """
    The main function serving as the application's entry point.
    Orchestrates the process of fetching weather data, determining snow day possibilities,
    generating relevant messages, and sending emails.
    """
    logging.info('---- APPLICATION START ----')

    try:
        snowday_message = general_functions.create_snow_day_message()
        email_message = email_helpers.generate_email_content(snowday_message)
        general_functions.write_prediction_to_file(email_message)

        if email_helpers.should_send_email(email_message):
            logging.info('Chance of a snow day is greater than 50%')
            recipients = email_helpers.fetch_email_recipients()
            email_helpers.send_emails(recipients, email_message)
        else:
            logging.info('There is a less than 50 percent chance of a snow day. Not sending emails.')
            if settings.TESTING_MODE:
                logging.info('Application is in testing mode, sending the email anyways!')
                # TESTING ONLY: Send email even if the snow day chance is low
                recipients = email_helpers.fetch_email_recipients_for_testing()
                logging.info('Testing users: %s', recipients)
                email_helpers.send_emails(recipients, email_message)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

    logging.info('---- APPLICATION END ----')

if __name__ == "__main__":
    general_functions.configure_logging()
    main()
