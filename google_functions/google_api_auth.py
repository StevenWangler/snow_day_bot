'''
This module contains general functions surrounding authentication
in the Google API
'''
import logging
from google.auth.transport.requests import Request as GoogleRequest
from google.oauth2.credentials import Credentials
from settings import app_secrets


def refresh_google_credentials():
    '''
    This function checks to see if your api credentials are expired.
    if they are, it refreshes them.
    '''
    credentials_path = app_secrets.GOOGLE_CREDENTIALS_PATH
    try:
        # Load the existing credentials from a file
        creds = Credentials.from_authorized_user_file(credentials_path)
        # Check if the access token has expired
        if creds.expired:
            # Refresh the access token
            creds.refresh(GoogleRequest())
            # Save the new credentials to a file
            with open(f'{credentials_path}', 'w', encoding="utf-8") as _f:
                _f.write(creds.to_json())
    except FileNotFoundError as _e:
        logging.error("Error: %s. Please make sure the credentials file exists at %s.", _e, credentials_path)
    except Exception as _e:
        logging.error("Error: %s. An unknown error occurred while trying to refresh Google API credentials.", _e)
