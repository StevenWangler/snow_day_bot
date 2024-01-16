"""
OpenAI API Interaction Module

This module provides functionalities to interact with the OpenAI API, focusing 
on generating chat responses and potentially other capabilities such as image 
creation. It facilitates communication with various OpenAI models, including 
the latest GPT-4 Turbo, to obtain AI-generated text completions.

Key Features:
- Chat Response Generation: Leverages the OpenAI's ChatCompletion endpoint for generating conversational responses.
- (If applicable) Image Creation: Ability to create images using OpenAI's DALL-E model or similar endpoints. (Note: Include this only if your module has such functionality)

Dependencies:
- json: Utilized for parsing and constructing JSON payloads.
- logging: Employed for logging application events and errors.
- requests: Required for making HTTP requests to OpenAI's API endpoints.
(Note: Include this only if your module directly makes HTTP requests)
- openai: The official Python client provided by OpenAI.
- settings: A module to access application-specific settings (from 'settings' package).
- general_functions: A module comprising utility functions for the
application (from 'general_functions' package).

Example:
To generate a chat response, the `generate_chat_response`
function can be used with a properly formatted JSON message,
which interacts with the OpenAI's chat completion API to return a response.

Note:
Ensure that the OpenAI API key is correctly configured in the environment variables to
authenticate requests to the OpenAI services.

Author: [Your Name/Your Organization]
Version: [Version of your module]
"""
import os
import logging
import openai
from settings import settings

def generate_chat_response(json_message):
    """
    Generates a chat response using OpenAI's GPT-4 Turbo chat completion endpoint.
    Validates the response and logs any exceptions encountered.

    Parameters:
    json_message (list of dict): The list of message dicts to be 
    sent to the chat completion endpoint.

    Returns:
    str or None: The chat response with newline characters removed, or None if an error occurs.
    """
    try:
        logging.info('Generating the OpenAI chat completion message')
        openai.api_key = os.environ.get("OPENAI_API_KEY")

        response = openai.chat.completions.create(
            model=settings.ENGINE_NAME,  # Using the engine name from settings
            messages=json_message  # Already in the expected format
        )

        # Extracting and formatting the response
        if response.choices:
            last_choice = response.choices[-1]
            # Accessing the 'content' attribute directly from the 'message' object
            chat_content = last_choice.message.content.strip() if last_choice.message and last_choice.message.content else ''
            if chat_content:
                return chat_content.replace('\n', '')

        logging.warning('Empty or invalid chat content received.')
        return None

    except Exception as ex:
        logging.error('Error in generate_chat_response: %s', ex)
        return None

def get_assistant():
    """
    Fetches the ID of the assistant named 'Blizzard' or
    'Blizzard_Testing' based on the testing mode.

    Returns:
        str: The ID of the relevant assistant, or None if not found.
    """
    # Determine the name of the assistant based on the testing mode
    target_assistant_name = 'Blizzard_Testing' if settings.TESTING_MODE else 'Blizzard'
    current_assistants = openai.beta.assistants.list()

    # Search for the assistant by name
    for assistant in current_assistants.data:
        if assistant.name == target_assistant_name:
            return assistant.id

    # Log if the assistant was not found
    logging.warning("Assistant named '%s' not found.", target_assistant_name)
    return None

def create_thread():
    """
    Creates a new conversation thread using the OpenAI Assistants API.

    Args:
        client (openai.OpenAI): The OpenAI client instance.

    Returns:
        openai.Thread: The created thread object.
    """
    thread = openai.beta.threads.create()
    return thread

def add_message_to_thread(thread_id, content):
    """
    Adds a message to a specific thread using the OpenAI Assistants API.

    Args:
        client (openai.OpenAI): The OpenAI client instance.
        thread_id (str): The ID of the thread to which the message will be added.
        role (str): The role of the message sender ('user' or 'assistant').
        content (str): The content of the message.

    Returns:
        openai.ThreadMessage: The created message object.
    """
    file_ids = []
    file_id = get_helping_files()
    file_ids.append(file_id)
    message = openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content,
        file_ids=file_ids
    )
    return message

def run_assistant_on_thread(thread_id, assistant_id, instructions=None):
    """
    Runs the assistant on a specific thread using the OpenAI Assistants API.

    Args:
        client (openai.OpenAI): The OpenAI client instance.
        thread_id (str): The ID of the thread on which the assistant will run.
        assistant_id (str): The ID of the assistant to be used.
        instructions (str, optional): New instructions for this specific run, if any.

    Returns:
        openai.Run: The Run object created by executing the assistant.
    """
    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions=instructions
    )
    return run

def check_run_status(thread_id, run_id):
    """
    Checks the status of a run on a specific thread using the OpenAI Assistants API.

    Args:
        client (openai.OpenAI): The OpenAI client instance.
        thread_id (str): The ID of the thread.
        run_id (str): The ID of the run to check.

    Returns:
        str: The status of the run ('queued', 'running', 'succeeded', 'failed', etc.).
    """
    run_status = openai.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id
    )
    return run_status.status

def get_messages(thread_id):
    """
    Retrieves a list of messages from a specified thread using the OpenAI API.

    This function calls the OpenAI API to fetch all messages belonging to a given thread,
    identified by its unique thread ID. If the API call is successful, it returns a list of
    messages. In case of an error (such as a network issue or invalid thread ID), it catches
    the exception, prints an error message, and returns None.

    Parameters:
    thread_id (str): The unique identifier of the thread from which messages are to be retrieved.

    Returns:
    dict or None: Returns a dictionary containing the list of messages if the API call is successful.
                  Returns None if an error occurs during the API call.

    Raises:
    Exception: Outputs an error message to the console if an exception occurs during the API call.
    """
    try:
        return openai.beta.threads.messages.list(
            thread_id=thread_id
        )
    except Exception as e:
        print(f'Error getting messages! Error: {e}')
        return None

def get_helping_files():
    """
    Uploads a file to OpenAI and returns the file ID.
    Assumes the file is located in the root directory of the GitHub project.
    """
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Go up one level to the root directory of the project
    root_directory = os.path.dirname(current_directory)
    file_path = os.path.join(root_directory, 'rockford_snow_day_factor_information.txt')

    with open(file_path, "rb") as file_data:
        file = openai.files.create(file=file_data, purpose="assistants")
    return file.id
