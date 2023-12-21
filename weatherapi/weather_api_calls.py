'''
This file contains calls to the weather api
'''
import os
import requests
from settings import settings

def get_forecast():
    '''
    This function gets the weather forecast for the current day and
    the next day. It is also gathering weather alerts.
    '''
    try:
        url = (f'{settings.WEATHER_API_BASE}'
               f'forecast.json?key={os.environ.get("WEATHERAPI_KEY")}'
               f'&q={settings.ZIP_CODE}'
               f'&days=2'
               f'&aqi=no'
               f'&alerts=yes')

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as ex:
        print(f'There was an error in get_one_day_forecast. Error: {ex}')
        return None
