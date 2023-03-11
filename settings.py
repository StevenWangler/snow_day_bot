'''
This is the settings file that contains information needed to run the application,
talk to API's, etc.
'''
import os

# Weather API data
WEATHER_API_KEY = os.environ['WEATHERAPI_KEY']
ZIP_CODE = '49341'
WEATHER_API_BASE = 'http://api.weatherapi.com/v1/'

# OpenAI data
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
ENGINE_NAME = 'gpt-3.5-turbo'
ENGINE_TEMPERATURE = 1
ENGINE_TOP_P = 1
ENGINE_N = 1
ENGINE_STREAM = False
ENGINE_STOP = None
ENGINE_MAX_TOKENS = float('inf')
ENGINE_PRESENCE_PENALTY = 0
ENGINE_FREQUENCY_PENALTY = 0
ENGINE_LOGIT_BIAS = None
ENGINE_USER = None
CHAT_COMPLETIONS_URL = 'https://api.openai.com/v1/chat/completions'
