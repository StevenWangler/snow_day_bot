"""
OpenAI API Interaction Module

This module provides functionalities to interact with various OpenAI endpoints.
It includes methods for generating chat completions and creating images using 
the OpenAI engine.

Dependencies:
- json: For parsing and creating JSON payloads.
- logging: To log application events and errors.
- requests: For making HTTP requests to the OpenAI endpoints.
- openai: OpenAI's official Python client.
- settings.settings: To access application-specific settings.
- general_functions.general_functions: Utility functions for the application.
"""

import json
import logging
import requests
import openai
from settings import settings
from general_functions import general_functions

def _configure_openai_api():
    """
    Configures the OpenAI API with the provided API key.
    """
    openai.api_key = settings.OPENAI_API_KEY

def get_chat_completion_response(json_message):
    """
    Fetches chat completion response from OpenAI.
    """
    url = settings.CHAT_COMPLETIONS_URL
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.OPENAI_API_KEY}'
    }
    data = {
        'model': settings.ENGINE_NAME,
        'messages': json_message,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), timeout=30)
    return response

def generate_chat_response(json_message):
    """
    Generates a chat response using OpenAI's chat completion endpoint.
    Validates the response and logs any exceptions encountered.

    Parameters:
    json_message (str): The JSON message to be sent to the chat completion endpoint.

    Returns:
    str or None: The chat response with newline characters removed, or None if an error occurs.
    """
    try:
        logging.info('Generating the OpenAI chat completion message')
        response = get_chat_completion_response(json_message)
        response_data = parse_response(response)
        chat_content = response_data.get('choices', [{}])[0].get('message', {}).get('content', '')
        if chat_content.strip():
            return chat_content.replace('\n', '')

        logging.warning('Empty or invalid chat content received.')
        return None

    except (requests.exceptions.RequestException, json.JSONDecodeError) as ex:
        logging.error('Error in generate_chat_response: %s', ex)
        return None

def parse_response(response):
    """
    Parses the response from the chat completion endpoint.

    Parameters:
    response (Response): The response object from requests.

    Returns:
    dict: Parsed JSON data from the response.
    """
    try:
        return json.loads(response.text)
    except json.JSONDecodeError as ex:
        logging.error('Error parsing JSON response: %s', ex)
        return {}
