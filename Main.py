#put a description here
import WeatherAPI_Calls as Weather_API
import Weather_Data

def main():
    Weather_API.set_weather_api_class_variables()
    forecast_data = Weather_API.get_one_day_forecast()
    Weather_Data.get_relevant_weather_information(forecast_data) 


if __name__ == "__main__":
    main()
