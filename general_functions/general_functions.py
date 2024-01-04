"""
General Functions Module

This module contains utility functions that support the main application's operations.
It includes functionalities for logging configuration, reading application settings, 
managing user data, and recording predictions. File-based operations are temporary 
and serve as placeholders until database integrations are complete.

Dependencies:
- logging: To log application events and errors.
- datetime: To record timestamps.
- os: For file and directory operations.
- settings.settings: To access application-specific settings.
"""

import logging
import datetime
import os
from settings import settings

BASE_SETTINGS_PATH = os.path.join('settings')

def configure_logging():
    """
    Configures logging settings and initiates a new log session.
    Clears the log file before each run.
    """
    log_file_path = os.path.join(BASE_SETTINGS_PATH, 'application_log.log')

    # Clear log file contents
    with open(log_file_path, 'w', encoding="utf-8") as log_file:
        log_file.truncate(0)

    # Setup logging
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    current_time = datetime.datetime.now()
    logging.info('---- APPLICATION START (current date/time is: %s) ----', current_time)

def get_snow_day_policy():
    """
    Fetches the snow day policy from a text file.
    """
    logging.info('Getting the snow day policy for: %s', settings.SCHOOL_NAME)
    file_path = os.path.join(BASE_SETTINGS_PATH, 'snow_day_policy.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        policy = file.read()
    return policy

def write_prediction_to_file(prediction):
    """
    Records the provided prediction to a text file for historical tracking.
    Writes to 'historical_predictions.txt' in the root directory of the project.
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Go up one level to the root directory of the project
    root_directory = os.path.dirname(current_directory)
    file_path = os.path.join(root_directory, 'prediction.txt')

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f'{prediction}\n')
