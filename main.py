'''
This main file is the entry point to the program
'''
import weather_api_calls as weather_api
import weather_data
import open_ai_api_calls as open_ai

def main():
    '''This function is the main entry point
    of the application.
    '''
    forecast_data = weather_api.get_forecast()
    current_weather_data = weather_data.get_relevant_weather_information(forecast_data)

    open_ai.generate_chat_completion('gpt-3.5-turbo', messages, temperature = 0.5)


if __name__ == "__main__":
    main()
