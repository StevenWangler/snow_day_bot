'''
This main file is the entry point to the program
'''
import logging
import weather_api_calls as weather_api
import weather_data
import open_ai_api_calls as open_ai
import open_ai_data
import general_functions
import communication_functions


def main():
    '''
    This function is the main entry point
    of the application.
    '''
    logging.info('Application start!')
    snow_day_policy = general_functions.get_snow_day_policy()
    message = open_ai_data.create_open_ai_snow_day_message(weather_data.get_relevant_weather_information(weather_api.get_forecast()), snow_day_policy)
    text_message = open_ai.generate_chat_completion(message)
    chunked_text_message = general_functions.split_text_message(text_message)
    #Below is a temp method - eventually, we will setup a database for this
    phone_numbers = general_functions.get_user_phone_numbers()
    communication_functions.send_text_message(phone_numbers, chunked_text_message)
    logging.info('---- APPLICATION END ----')

if __name__ == "__main__":
    general_functions.configure_logging()
    main()
