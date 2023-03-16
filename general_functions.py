'''
this file contains general functions for the application.
'''


def get_snow_day_policy():
    '''
    this function reads the snow day policy text file
    '''
    policy = ''
    with open('snow_day_policy.txt', 'r', encoding='utf-8') as file:
        policy = file.read()

    return policy


def split_text_message(full_text_message):
    '''
    SMS only supports 160 characters per text message. Given our text will
    likely always be greater than 160 characters, we need to break this up
    to send in multiple text messages
    '''
    chunks = []
    while full_text_message:
        chunks.append(full_text_message[:130])
        full_text_message = full_text_message[130:]

    modified_chunks = add_page_numbers(chunks)
    return modified_chunks


def add_page_numbers(text_chunks):
    '''
    This function will append page numbers to the end of each
    text chunk and return the modified array
    '''
    try:
        page_counter = 1
        modified_chunks = []
        for chunk in text_chunks:
            chunk = chunk.replace('\n', '')
            modified_chunk = chunk + f' ({page_counter}/{len(text_chunks)})'
            modified_chunks.append(modified_chunk)
            page_counter += 1
    except TypeError:
        print("Please provide a list of strings as input.")

    return modified_chunks


def get_user_phone_numbers():
    '''
    TEMP METHOD. Until we hook the app up to a database, we are going to read
    our beta user information from a .txt file stored in the project. This is
    included in the .gitignore.
    '''
    phone_numbers = []
    try:
        with open('user_phone_numbers.txt', 'r', encoding='utf-8') as _f:
            lines = _f.readlines()

        for line in lines:
            line = line.strip()
            if line:
                number, domain = line.split(',')
                phone_numbers.append(f"{number.strip()} {domain.strip()}")

    except FileNotFoundError:
        print('Error: Could not find user_phone_numbers.txt file.')
    except ValueError:
        print('Error: Malformed user_phone_numbers.txt file.')

    return phone_numbers
