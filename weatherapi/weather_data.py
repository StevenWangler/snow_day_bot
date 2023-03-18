'''
This file contains functions that parse through weather data.
The weather data that we get will be used to pass to our ai engine to
determine the percentage chance of a snowday.
'''
import logging

def get_relevant_weather_information(forecast_data):
    '''
    This function gets the weather data we need to calculate a snow day.
    '''
    logging.info('Getting the relevant weather info from the forecast')
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
        weather_data['current_day_feelslike_f'] = forecast_data['current']['feelslike_f']
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
        weather_data['next_day_feelslike_f'] = forecast_data['forecast']['forecastday'][1]['hour'][6]['feelslike_f']

        #Get any weather alerts if applicable
        if len(forecast_data['alerts']['alert']) > 0:
            weather_alert_data = forecast_data['alerts']['alert'][0]
            weather_data['weather_alert_event'] = weather_alert_data['event']
            weather_data['weather_alert_severity'] = weather_alert_data['severity']
            weather_data['weather_alert_certainty'] = weather_alert_data['certainty']
            weather_data['weather_alert_urgency'] = weather_alert_data['urgency']
            weather_data['weather_alert_desc'] = weather_alert_data['desc']

    except KeyError as ex:
        logging.error('Not found in forecast_data. Error: %s', ex)

    return weather_data
