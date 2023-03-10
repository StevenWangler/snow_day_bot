import json
import requests
import openai
import settings



openai.api_key = settings.OPENAI_API_KEY


def generate_chat_completion(model_id, messages, temperature=1, top_p=1, n=1, stream=False, stop=None, max_tokens=float('inf'), presence_penalty=0, frequency_penalty=0, logit_bias=None, user=None):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.OPENAI_API_KEY}'
    }
    data = {
        'model': model_id,
        'messages': messages,
        'temperature': temperature,
        'top_p': top_p,
        'n': n,
        'stream': stream,
        'stop': stop,
        'max_tokens': max_tokens,
        'presence_penalty': presence_penalty,
        'frequency_penalty': frequency_penalty,
        'logit_bias': logit_bias,
        'user': user
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), timeout=30)
    response_data = json.loads(response.text)
    print(response_data)
    
