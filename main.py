'''
This main file is the entry point to the program
'''
import weather_api_calls as Weather_API
import weather_data

def main():
    '''This function is the main entry point
    of the application.
    '''
    forecast_data = Weather_API.get_forecast()
    current_weather_data = weather_data.get_relevant_weather_information(forecast_data)


if __name__ == "__main__":
    main()
