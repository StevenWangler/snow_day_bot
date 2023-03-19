'''
this file contains general functions for the application.
'''
import logging
import datetime
import os
import settings.settings as settings


def configure_logging():
    '''
    This method configures our log file
    '''
    log_file_path = os.path.join('settings', 'application_log.log')
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    current_time = datetime.datetime.now()
    logging.info('---- APPLICATION START (current date/time is: %s) ----', current_time)

    
def get_snow_day_policy():
    '''
    this function reads the snow day policy text file
    '''
    logging.info('Getting the snow day policy for: %s', settings.SCHOOL_NAME)
    policy = ''
    file_path = os.path.join('settings', 'snow_day_policy.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        policy = file.read()

    return policy


def get_user_emails():
    '''
    TEMP METHOD. Until we hook the app up to a database, we are going to read
    our beta user information from a .txt file stored in the project. This is
    included in the .gitignore.
    '''
    logging.info('Getting email addresses for the users. **NOTE** this is a temp method.')
    email_dict = {}
    try:
        file_path = os.path.join('settings', 'user_emails.txt')
        with open(file_path, 'r', encoding='utf-8') as _f:
            lines = _f.readlines()

        for line in lines:
            line = line.strip()
            if line:
                name, email = line.split(',')
                email_dict[name.strip()] = email.strip()  # switch key and value
    except FileNotFoundError:
        logging.error('Error: Could not find user_emails.txt file.')
    except ValueError:
        logging.error('Error: Malformed user_emails.txt file.')

    return email_dict


def write_prediction_to_file(prediction):
    '''
    This file writes the given prediction to a text file as a record
    '''
    file_path = os.path.join('settings', 'historical_predictions.txt')
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f'{prediction}\n')
