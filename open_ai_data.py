'''
This file takes weather data that has already been selected from an API call, puts it into a string,
then will put it into a json object which can be used by the ai engine. Because this is a 
linguistic mode, we need to build input as if we are physically speaking to someone. The more 
information and the more context that is provided, the more accurate of an answer 
we can get back from the model.
'''
import json
import datetime


def create_open_ai_snow_day_caption(current_weather_data, snow_day_policy):
    '''
    this method is used to create the json message we are
    going to send to the open ai engine
    '''
    try:
        message = f'''
        Respond with a percentage chance that a snowday will occur tomorrow. Also, provide a one to three sentence
        explanation of how you came to that conclusion. If tomorrow is Saturday or Sunday, return (0%). The current day of the week
        is {datetime.datetime.now().strftime("%A")}. Below you will find the weather conditions.

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

        Here is some information about the schools snow day policy:
        {snow_day_policy}  
        '''
        message = message.replace("\n", "\\n")
        message = message.strip()
        message_object = json.loads(f'[{{"role": "user", "content": "{message}"}}]')
    except KeyError as ex:
        print(f"An error occurred while creating message: {str(ex)}")
        message_object = None

    return message_object
