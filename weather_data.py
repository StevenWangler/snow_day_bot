'''
This file contains functions that parse through weather data.
The weather data that we get will be used to pass to our ai engine to
determine the percentage chance of a snowday.
'''


def get_relevant_weather_information(forecast_data):
    '''
    This function gets the weather data we need to calculate a snow day.
    '''
    weather_data = {}
    try:
        # Current day forecast information
        current_day = forecast_data['forecast']['forecastday'][0]['day']
        weather_data['current_day_mintemp_f'] = current_day['mintemp_f']
        weather_data['current_day_maxtemp_f'] = current_day['maxtemp_f']
        weather_data['current_day_maxwind_mph'] = current_day['maxwind_mph']
        weather_data['current_day_totalprecip_in'] = current_day['totalprecip_in']
        weather_data['current_day_daily_chance_of_snow'] = current_day['daily_chance_of_snow']
        weather_data['current_day_daily_chance_of_rain'] = current_day['daily_chance_of_rain']
        weather_data['current_day_daily_avghumidity'] = current_day['avghumidity']
        weather_data['current_day_conditions'] = current_day['condition']['text']

        # Next day forecast information
        next_day = forecast_data['forecast']['forecastday'][1]['day']
        weather_data['next_day_mintemp_f'] = next_day['mintemp_f']
        weather_data['next_day_maxtemp_f'] = next_day['maxtemp_f']
        weather_data['next_day_maxwind_mph'] = next_day['maxwind_mph']
        weather_data['next_day_totalprecip_in'] = next_day['totalprecip_in']
        weather_data['next_day_daily_chance_of_snow'] = next_day['daily_chance_of_snow']
        weather_data['next_day_daily_chance_of_rain'] = next_day['daily_chance_of_rain']
        weather_data['next_day_daily_avghumidity'] = next_day['avghumidity']
        weather_data['next_day_conditions'] = next_day['condition']['text']
    except KeyError as ex:
        print(f"Error: {ex} not found in forecast_data")

    return weather_data
