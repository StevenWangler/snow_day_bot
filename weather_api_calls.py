'''
Add a description later
'''
import requests
import settings


def get_forecast():
    '''
    THIS IS A TEST
    '''
    try:
        url = (f'{settings.WEATHER_API_BASE}'
               f'forecast.json?key={settings.WEATHER_API_KEY}'
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
