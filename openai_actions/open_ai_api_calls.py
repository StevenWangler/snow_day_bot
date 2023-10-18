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
    Generates chat response using OpenAI's chat completion endpoint.
    """
    try:
        logging.info('Generating the open ai chat completion message')
        response = get_chat_completion_response(json_message)
        response_data = json.loads(response.text)
        general_functions.write_prediction_to_file(response_data['choices'][0]['message']['content'])
        completion_message = response_data['choices'][0]['message']['content']
        return completion_message.replace('\n', '')
    except (requests.exceptions.RequestException, json.JSONDecodeError) as ex:
        logging.error('Error in generate_chat_response: %s', ex)
        return None
