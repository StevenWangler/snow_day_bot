'''
This main file is the entry point to the program
'''
import logging
import weatherapi.weather_api_calls as weather_api
import weatherapi.weather_data as weather_data
from openai_actions import open_ai_api_calls as openai_api
from openai_actions import open_ai_data as openai_data
import general_functions.general_functions as general_functions
from email_functions import email_delivery


def main():
    '''
    This function is the main entry point
    of the application.
    '''
    logging.info('---- APPLICATION START ----')
    snow_day_policy = general_functions.get_snow_day_policy()
    message = openai_data.create_open_ai_snow_day_message(weather_data.get_relevant_weather_information(weather_api.get_forecast()), snow_day_policy)
    email_message = openai_api.generate_chat_completion(message)
    #Below is a temp method - eventually, we will setup a database for this
    emails = general_functions.get_user_emails()
    email_delivery.send_email_to_user(emails, email_message)
    logging.info('---- APPLICATION END ----')

if __name__ == "__main__":
    general_functions.configure_logging()
    main()
