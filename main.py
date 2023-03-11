'''
This main file is the entry point to the program
'''
import weather_api_calls as weather_api
import weather_data
import open_ai_api_calls as open_ai
import open_ai_data

def main():
    '''
    This function is the main entry point
    of the application.
    '''
    message = open_ai_data.create_open_ai_message(weather_data.get_relevant_weather_information(weather_api.get_forecast()))
    chance_of_snowday = open_ai.generate_chat_completion(message)
    print(f'There is a {chance_of_snowday} chance of a snowday tomorrow')


if __name__ == "__main__":
    main()
