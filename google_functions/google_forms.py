"""
Google Forms Interaction Module

This module provides functionalities to interact with Google Forms, specifically 
to fetch responses from a designated form. The primary purpose is to retrieve 
sign-up responses, which are then used in the main application for sending out 
notifications. 

Key Features:
- Authentication using OAuth2 to ensure secure access to Google Forms data.
- Ability to refresh expired tokens automatically.
- Parsing of form responses to extract relevant data, such as email addresses and names.

Dependencies:
- google.oauth2.credentials: For handling OAuth2 credentials.
- google.auth.transport.requests: To make authorized requests.
- requests: For making HTTP requests to the Google Forms API.
- settings.app_secrets: To access application-specific secrets and configurations.

Note: 
Ensure that the 'token.json' file with authentication credentials is present in the root directory 
before using this module. Additionally, replace placeholders like 'YOUR_FORM_ID' with actual values 
before deploying.
"""

import logging
import os.path
import requests
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from settings import app_secrets

GOOGLE_FORMS_API_BASE_URL = "https://forms.googleapis.com/v1/forms"

def _load_credentials(scopes):
    """
    Load or refresh Google API credentials.
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    return creds

def get_sign_up_responses():
    """
    Fetches sign-up responses from a specified Google Form.
    
    This function retrieves form responses using the Google Forms API.
    It returns a dictionary where the keys are the emails of the respondents
    and the values are their corresponding names.
    
    The method first checks for valid credentials and refreshes them if needed.
    Then, it queries the Google Forms API and processes the received responses.
    
    Returns:
        dict: A dictionary with emails as keys and names as values. 
              If there are any errors or if no data is found, it'll return an empty dictionary.
              
    Raises:
        ValueError: If there are invalid or missing credentials.
        requests.HTTPError: If there's an HTTP error when making the request.
        ConnectionError: If there's a connection issue when making the request.
        requests.Timeout: If the request times out.
    """
    scopes = ["https://www.googleapis.com/auth/forms.responses.readonly"]
    creds = _load_credentials(scopes)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open('token.json', 'w', encoding="utf-8") as token:
                token.write(creds.to_json())
        else:
            raise ValueError("Invalid or missing credentials")

    url = f"{GOOGLE_FORMS_API_BASE_URL}/{app_secrets.GOOGLE_SIGN_UP_FORM_ID}/responses"
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Accept': 'application/json'
    }

    try:
        logging.info("Fetching sign-up responses from Google Form.")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        responses = data.get('responses', [])
        email_to_name = {}
        for resp in responses:
            email_answer = resp.get('respondentEmail')
            # Using a placeholder for the key; replace with the actual key from your form
            name_answer_key = '778b574a'  
            name_answer = resp.get('answers', {}).get(name_answer_key, {}).get('textAnswers', {}).get('answers', [{}])[0].get('value')

            if email_answer and name_answer:
                email_to_name[email_answer] = name_answer

        return email_to_name
    except (requests.HTTPError, ConnectionError, requests.Timeout) as ex:
        logging.error('Specific error in get_form_responses: %s', ex)
    except Exception as ex:
        logging.error('Unexpected error in get_form_responses: %s', ex)

    return {}
