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


def split_text_message(full_text_message):
    '''
    SMS only supports 160 characters per text message. Given our text will
    likely always be greater than 160 characters, we need to break this up
    to send in multiple text messages. There seems to be some other junk added
    onto the messages when we send, so we're making the cutoff earlier, hence
    the 130 characters. This function also splits on full words, which create
    easier to read text messages.
    '''
    logging.info('Splitting the text message')
    chunks = []
    while full_text_message:
        if len(full_text_message) <= 130:
            chunks.append(full_text_message)
            break
        if full_text_message[129] == ' ':
            chunks.append(full_text_message[:130])
            full_text_message = full_text_message[130:]
        else:
            i = 129
            while i >= 0 and full_text_message[i] != ' ':
                i -= 1
            if i < 0:
                chunks.append(full_text_message[:130])
                full_text_message = full_text_message[130:]
            else:
                chunks.append(full_text_message[:i])
                full_text_message = full_text_message[i+1:]

    modified_chunks = add_page_numbers(chunks)
    return modified_chunks


def add_page_numbers(text_chunks):
    '''
    This function will append page numbers to the end of each
    text chunk and return the modified array
    '''
    logging.info('Adding page numbers to the text messages')
    try:
        page_counter = 1
        modified_chunks = []
        for chunk in text_chunks:
            chunk = chunk.replace('\n', '')
            modified_chunk = chunk + f' ({page_counter}/{len(text_chunks)})'
            modified_chunks.append(modified_chunk)
            page_counter += 1
    except TypeError:
        logging.error("Please provide a list of strings as input.")

    return modified_chunks


def get_user_phone_numbers():
    '''
    TEMP METHOD. Until we hook the app up to a database, we are going to read
    our beta user information from a .txt file stored in the project. This is
    included in the .gitignore.
    '''
    logging.info('Getting the phone numbers for the users. **NOTE** this is a temp method.')
    phone_numbers = []
    try:
        file_path = os.path.join('settings', 'user_phone_numbers.txt')
        with open(file_path, 'r', encoding='utf-8') as _f:
            lines = _f.readlines()

        for line in lines:
            line = line.strip()
            if line:
                number, domain = line.split(',')
                phone_numbers.append(f"{number.strip()}{domain.strip()}")

    except FileNotFoundError:
        logging.error('Error: Could not find user_phone_numbers.txt file.')
    except ValueError:
        logging.error('Error: Malformed user_phone_numbers.txt file.')

    return phone_numbers


def write_prediction_to_file(prediction):
    '''
    This file writes the given prediction to a text file as a record
    '''
    file_path = os.path.join('settings', 'historical_predictions.txt')
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f'{prediction}\n')
