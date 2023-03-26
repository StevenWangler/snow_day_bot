'''
This module contains google form functions
'''
import logging
import requests
from google.oauth2.credentials import Credentials
from settings import app_secrets


def get_sign_up_responses():
    '''
    This method will get the list of people who want to sign up for Blizzard alerts
    '''
    try:
        scopes = ['https://www.googleapis.com/auth/forms',
                  'https://www.googleapis.com/auth/script.external_request']
        creds = Credentials.from_authorized_user_file(
            app_secrets.GOOGLE_CREDENTIALS_PATH, scopes)
        url = f"https://forms.googleapis.com/v1/forms/{app_secrets.GOOGLE_SIGN_UP_FORM_ID}/responses"
        headers = {'Authorization': f'Bearer {creds.token}',
                   'Accept': 'application/json'}
        params = {'key': app_secrets.GOOGLE_ACCOUNT_API_KEY}
        response = requests.get(url, headers=headers,
                                params=params, timeout=30)
        response.raise_for_status()  # Raise an exception if status code is not 200 OK
        return response.json()
    except (requests.HTTPError, ConnectionError, requests.Timeout) as ex:
        logging.error('An error occurred in get_sign_up_responses. Error: %s', ex)
        return None
    