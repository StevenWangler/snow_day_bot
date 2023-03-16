'''
This file takes weather data that has already been selected from an API call, puts it into a string,
then will put it into a json object which can be used by the ai engine. Because this is a 
linguistic mode, we need to build input as if we are physically speaking to someone. The more 
information and the more context that is provided, the more accurate of an answer 
we can get back from the model.
'''
import json
import random
import logging
import settings
import open_ai_api_calls as openai


def create_open_ai_snow_day_message(current_weather_data, snow_day_policy):
    '''
    this method is used to create the json message we are
    going to send to the open ai engine
    '''
    logging.info('Creating the request message to send to openai')
    try:
        message = f'''
        Respond with a percentage chance that a snow day will occur tomorrow for {settings.SCHOOL_NAME} Also, provide a one to two sentence
        explanation of how you came to that conclusion. Please respond in the tone of {random.choice(settings.AI_RESPONSE_THEMES)}
        
        Below you will find the weather conditions.

        The minimum temperature for the day will be {current_weather_data['current_day_mintemp_f']} degrees Fahrenheit, with
        a maximum temperature of {current_weather_data['current_day_maxtemp_f']} degrees Fahrenheit. The maximum wind speed
        for the day will be {current_weather_data['current_day_maxwind_mph']}MPH. The wind chill (or "feels like") is currently
        {current_weather_data['current_day_feelslike_f']} degrees Fahrenheit. As of now, there is a {current_weather_data['current_day_daily_chance_of_snow']}%
        chance that it will snow today. There is also a {current_weather_data['current_day_daily_chance_of_rain']}% chance that it will rain today.
        The total amount of precipitation today is going to be around {current_weather_data['current_day_totalprecip_in']} inches. The average humidity
        for today is {current_weather_data['current_day_daily_avghumidity']}%. The current day conditions are {current_weather_data['current_day_conditions']}.

        Tomorrow, the minimum temperature for the day will be {current_weather_data['next_day_mintemp_f']} degrees Fahrenheit, with
        a maximum temperature of {current_weather_data['next_day_maxtemp_f']} degrees Fahrenheit. The maximum wind speed
        for tomorrow will be {current_weather_data['next_day_maxwind_mph']}MPH. The wind chill (or "feels like") for tomorrow will be
        {current_weather_data['next_day_feelslike_f']} degrees Fahrenheit. As of now, there is a {current_weather_data['next_day_daily_chance_of_snow']}% 
        chance that it will snow tomorrow. There is also a {current_weather_data['next_day_daily_chance_of_rain']}% chance that it will rain tomorrow. 
        The total amount of precipitation tomorrow is going to be around {current_weather_data['next_day_totalprecip_in']} inches. The average humidity 
        for tomorrow will be {current_weather_data['next_day_daily_avghumidity']}%. The conditions for tomorrow are {current_weather_data['next_day_conditions']}.

        Below you will find the current weather alert information (if any):

        Weather alert event: {current_weather_data['weather_alert_event'] if 'weather_alert_event' in current_weather_data else 'no data available'}
        Weather alert event description: {current_weather_data['weather_alert_desc'] if 'weather_alert_desc' in current_weather_data else 'no data available'}
        Weather alert severity: {current_weather_data['weather_alert_severity'] if 'weather_alert_severity' in current_weather_data else 'no data available'}
        Weather alert certainty: {current_weather_data['weather_alert_certainty'] if 'weather_alert_certainty' in current_weather_data else 'no data available'}
        Weather alert urgency: {current_weather_data['weather_alert_urgency'] if 'weather_alert_urgency' in current_weather_data else 'no data available'}
        
        Here is some information about the schools snow day policy:

        {snow_day_policy}
        '''
        message = message.replace("\n", "\\n")
        message = message.strip()
        message_object = json.loads(json.dumps(
            [{"role": "user", "content": message}]))
    except KeyError as ex:
        logging.error('An error occurred while creating message: %s',str(ex))
        message_object = None

    return message_object


def create_open_ai_image_prompt():
    '''
    this method comes up with a prompt to generate our image from
    '''
    try:
        message = f'''
        Response with only a prompt for an image generation. Please use the following items in
        your prompt: {settings.SCHOOL_MASCOT}, {settings.SCHOOL_COLORS}.In addition, try to 
        incorporate snow in your prompt as well. Please specify the style of the image you want
        to create as well (i.e. pencil drawing)
        '''
        message = message.replace("\n", "\\n")
        message = message.strip()
        message_object = json.loads(json.dumps(
            [{"role": "user", "content": message}]))
        return openai.generate_chat_completion(message_object)
    except Exception as ex:
        logging.error('An error occurred whole creating the image prompt. Error: %s', str(ex))
        return None
