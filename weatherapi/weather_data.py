'''
This file contains functions that parse through weather data.
The weather data that we get will be used to pass to our AI engine to
determine the percentage chance of a snow day.
'''
import logging

def get_hourly_forecast_data(hourly_data, start_hour, end_hour):
    '''
    Extracts relevant weather data from hourly forecast between given hours.
    '''
    relevant_data = {}
    for hour in hourly_data:
        hour_time = hour['time']
        hour_of_day = int(hour_time.split(' ')[1].split(':')[0])  # Extracting the hour part

        if start_hour <= hour_of_day < end_hour:
            relevant_data[f'hour_{hour_of_day}_temp_f'] = hour['temp_f']
            relevant_data[f'hour_{hour_of_day}_chance_of_snow'] = hour['chance_of_snow']
            relevant_data[f'hour_{hour_of_day}_chance_of_rain'] = hour['chance_of_rain']
            relevant_data[f'hour_{hour_of_day}_wind_mph'] = hour['wind_mph']
            relevant_data[f'hour_{hour_of_day}_visibility_miles'] = hour['vis_miles']
            relevant_data[f'hour_{hour_of_day}_snow_cm'] = hour.get('snow_cm', 0)
            relevant_data[f'hour_{hour_of_day}_humidity'] = hour['humidity']
            relevant_data[f'hour_{hour_of_day}_cloud'] = hour['cloud']
            relevant_data[f'hour_{hour_of_day}_pressure_in'] = hour['pressure_in']
            relevant_data[f'hour_{hour_of_day}_feelslike_f'] = hour['feelslike_f']
            relevant_data[f'hour_{hour_of_day}_windchill_f'] = hour['windchill_f']
            relevant_data[f'hour_{hour_of_day}_dewpoint_f'] = hour['dewpoint_f']
            relevant_data[f'hour_{hour_of_day}_gust_mph'] = hour['gust_mph']
            relevant_data[f'hour_{hour_of_day}_uv'] = hour['uv']
            relevant_data[f'hour_{hour_of_day}_condition'] = hour['condition']['text']

    return relevant_data

def get_relevant_weather_information(forecast_data):
    '''
    Gets the weather data from 7 PM on the current day to 8 AM the next day for snow day prediction.
    '''
    logging.info('Getting the relevant weather info from the evening to the next morning')
    weather_data = {}

    try:
        # Data from 7 PM to Midnight of the current day (forecast day 0)
        current_day_hourly_data = forecast_data['forecast']['forecastday'][0]['hour']
        weather_data.update(get_hourly_forecast_data(current_day_hourly_data, 19, 24))  # 7 PM to Midnight

        # Data from Midnight to 8 AM of the next day (forecast day 1)
        next_day_hourly_data = forecast_data['forecast']['forecastday'][1]['hour']
        weather_data.update(get_hourly_forecast_data(next_day_hourly_data, 0, 8))  # Midnight to 8 AM

        # Get any weather alerts if applicable
        if 'alerts' in forecast_data and len(forecast_data['alerts']['alert']) > 0:
            weather_alert_data = forecast_data['alerts']['alert'][0]
            weather_data['weather_alert_event'] = weather_alert_data['event']
            weather_data['weather_alert_severity'] = weather_alert_data['severity']
            weather_data['weather_alert_certainty'] = weather_alert_data['certainty']
            weather_data['weather_alert_urgency'] = weather_alert_data['urgency']
            weather_data['weather_alert_desc'] = weather_alert_data['desc']

    except KeyError as ex:
        logging.error('Key not found in forecast_data: %s', ex)

    return weather_data
