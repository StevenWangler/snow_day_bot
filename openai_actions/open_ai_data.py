"""
OpenAI Message Creation Module

This module prepares messages tailored for interaction with OpenAI's engine.
It takes into account weather data, school settings, and linguistic models to craft
messages that seek predictions about snow days, image generation prompts, and more.

Dependencies:
- json: For parsing and creating JSON payloads.
- logging: To log application events and errors.
- settings: To access application-specific settings.
- openai_actions.open_ai_api_calls: To make calls to OpenAI's API.
"""

import json
import random
import logging
import datetime
from settings import settings

def create_hourly_weather_summary(current_weather_data):
    '''
    Creates a summary string of detailed hourly weather data.
    '''
    hourly_summary = ""

    # Loop for 7 PM to Midnight (19 to 23 hours)
    for hour in range(19, 24):
        summary = " ".join([
            f"Hour {hour}:",
            f"Condition: {current_weather_data.get(f'hour_{hour}_condition', 'No data')},",
            f"Temp: {current_weather_data.get(f'hour_{hour}_temp_f', 'No data')}°F,",
            f"Chance of Snow: {current_weather_data.get(f'hour_{hour}_chance_of_snow', 'No data')}%,",
            f"Chance of Rain: {current_weather_data.get(f'hour_{hour}_chance_of_rain', 'No data')}%,",
            f"Wind Speed: {current_weather_data.get(f'hour_{hour}_wind_mph', 'No data')}MPH,",
            f"Visibility: {current_weather_data.get(f'hour_{hour}_visibility_miles', 'No data')} miles,",
            f"Snowfall: {current_weather_data.get(f'hour_{hour}_snow_cm', 'No data')}cm,",
            f"Humidity: {current_weather_data.get(f'hour_{hour}_humidity', 'No data')}%,",
            f"Cloud Cover: {current_weather_data.get(f'hour_{hour}_cloud', 'No data')}%,",
            f"Pressure: {current_weather_data.get(f'hour_{hour}_pressure_in', 'No data')}in,",
            f"Feels Like: {current_weather_data.get(f'hour_{hour}_feelslike_f', 'No data')}°F,",
            f"Wind Chill: {current_weather_data.get(f'hour_{hour}_windchill_f', 'No data')}°F,",
            f"Gusts: {current_weather_data.get(f'hour_{hour}_gust_mph', 'No data')}MPH,",
            f"UV Index: {current_weather_data.get(f'hour_{hour}_uv', 'No data')}"
        ])
        hourly_summary += summary + " "

    # Loop for Midnight to 8 AM (0 to 7 hours)
    for hour in range(0, 8):
        summary = " ".join([
            f"Hour {hour}:",
            f"Condition: {current_weather_data.get(f'hour_{hour}_condition', 'No data')},",
            f"Temp: {current_weather_data.get(f'hour_{hour}_temp_f', 'No data')}°F,",
            f"Chance of Snow: {current_weather_data.get(f'hour_{hour}_chance_of_snow', 'No data')}%,",
            f"Chance of Rain: {current_weather_data.get(f'hour_{hour}_chance_of_rain', 'No data')}%,",
            f"Wind Speed: {current_weather_data.get(f'hour_{hour}_wind_mph', 'No data')}MPH,",
            f"Visibility: {current_weather_data.get(f'hour_{hour}_visibility_miles', 'No data')} miles,",
            f"Snowfall: {current_weather_data.get(f'hour_{hour}_snow_cm', 'No data')}cm,",
            f"Humidity: {current_weather_data.get(f'hour_{hour}_humidity', 'No data')}%,",
            f"Cloud Cover: {current_weather_data.get(f'hour_{hour}_cloud', 'No data')}%,",
            f"Pressure: {current_weather_data.get(f'hour_{hour}_pressure_in', 'No data')}in,",
            f"Feels Like: {current_weather_data.get(f'hour_{hour}_feelslike_f', 'No data')}°F,",
            f"Wind Chill: {current_weather_data.get(f'hour_{hour}_windchill_f', 'No data')}°F,",
            f"Gusts: {current_weather_data.get(f'hour_{hour}_gust_mph', 'No data')}MPH,",
            f"UV Index: {current_weather_data.get(f'hour_{hour}_uv', 'No data')}"
        ])
        hourly_summary += summary + " "

    return hourly_summary.strip()  # Remove any trailing space

def create_open_ai_snow_day_message(current_weather_data):
    '''
    This method is used to create the JSON message we are
    going to send to the OpenAI engine.
    '''
    logging.info('Creating the request message to send to OpenAI')
    try:
        hourly_summary = create_hourly_weather_summary(current_weather_data)
        theme = random.choice(settings.AI_RESPONSE_THEMES)
        month = datetime.date.today().month
        school_state = settings.SCHOOL_DISTRICT_STATE
        school_name = settings.SCHOOL_NAME

        message = f'''
        Respond with a percentage chance that a snow day will occur tomorrow for {school_name}.

        Here are the rules I would like you to follow:
        1) You must respond in the tone of {theme}
        2) Use the information below to make up your opinion
        3) Provide a SHORT explanation of the percentage chance you came up with
        4) Work your answer into the short explanation
        5) Be logical and honest in your answer
        6) If you don't think there is any chance, just say that there is a 0% chance.

        Additional information to consider:
        - The school is located in the state of {school_state}
        - Current month: {month} (of 12)

        Hourly weather conditions from 7 PM to 8 AM:
        {hourly_summary}

        Weather alerts (if applicable):
        - Event: {current_weather_data.get('weather_alert_event', 'No data')}
        - Description: {current_weather_data.get('weather_alert_desc', 'No data')}
        - Severity: {current_weather_data.get('weather_alert_severity', 'No data')}
        - Certainty: {current_weather_data.get('weather_alert_certainty', 'No data')}
        - Urgency: {current_weather_data.get('weather_alert_urgency', 'No data')}
        '''
        message = message.replace("\n", "\\n").strip()
    except KeyError as ex:
        logging.error('An error occurred while creating message: %s', str(ex))
        message = None

    return message

def create_open_ai_prediction_check_message(prediction_message):
    """
    Generates a formatted message to check OpenAI's prediction about the chance of a snow day.

    Parameters:
    - prediction_message (str): A message containing prediction details.

    Returns:
    - dict: A JSON-like dictionary object containing a formatted message for OpenAI's analysis.
    
    Raises:
    - Exception: If any error occurs during message formatting or JSON conversion.

    Note:
    The response from OpenAI should be either "True" or "False", indicating if there's a greater
    than 50% chance of a snow day.
    """
    try:
        message = f'''
        Analyze the following message and respond with ONLY the word "True" or "False". Tell me
        if there is a greater than or equal to 50% chance of a snow day. Here is the message:
        {prediction_message}
        '''
        message = message.replace("\n", "\\n")
        message = message.strip()
        message_object = json.loads(json.dumps([{"role": "user", "content": message}]))
        return message_object
    except Exception as ex:
        logging.error(f'There was an error in create_open_ai_prediction_check_message. Error: {ex}')
        return None
