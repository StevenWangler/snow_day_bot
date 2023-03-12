'''
This file contains different API calls to the openai engine
'''
import json
import requests
import openai
import settings

def generate_chat_completion(message):
    '''
    This method calls the chat completion endpoint from openai
    '''
    try:
        url = settings.CHAT_COMPLETIONS_URL
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {settings.OPENAI_API_KEY}'
        }
        data = {
            'model': settings.ENGINE_NAME,
            'messages': message,
        }
        response = requests.post(url,
                headers=headers,
                data=json.dumps(data),
                timeout=30)            
        response_data = json.loads(response.text)
        return response_data['choices'][0]['message']['content']
        
    except (requests.exceptions.RequestException, json.JSONDecodeError) as ex:
        print(
            f"An error occurred while calling the OpenAI chat completion endpoint: {ex}")
        return None


def generate_image(image_prompt):
    '''
    this method calls the image generation endpoint from openai
    '''
    try:
        response = openai.Image.create(
            prompt = image_prompt,
            n = 1,
            size = "1024x1024",
            response_format = 'b64_json'
            )
        return response['data'][0]['b64_json']
    except (requests.exceptions.RequestException, json.JSONDecodeError) as ex:
        print(
            f"An error occurred while calling the OpenAI chat completion endpoint: {ex}")
        return None
