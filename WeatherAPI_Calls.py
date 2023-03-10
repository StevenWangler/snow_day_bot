#Add a description later

import requests
import settings

API_KEY = ''
API_BASE = ''
ZIP_CODE = ''

#This method sets the global variables for the weather api calls
def set_weather_api_class_variables():
    try:
        print('Setting weather API class variables')
        global API_KEY, API_BASE, ZIP_CODE
        API_KEY = settings.WEATHER_API_KEY
        API_BASE = settings.WEATHER_API_BASE
        ZIP_CODE = settings.ZIP_CODE
        return API_KEY, API_BASE, ZIP_CODE
    except Exception as ex:
        print(f'There was an error in set_api_class_variables. Error: {ex}')
        return None

#Method that gets the one day forecast
def get_one_day_forecast():
    try:
        url = f'{API_BASE}forecast.json?key={API_KEY}&q={ZIP_CODE}&days=1&aqi=no&alerts=no'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as ex:
        print(f'There was an error in get_one_day_forecast. Error: {ex}')
        return None


