'''
This is the settings file that contains information needed to run the application,
talk to API's, etc.
'''
import os

# General data
SCHOOL_NAME = 'Rockford Public Schools'
SCHOOL_COLORS = 'Orange and black'
SCHOOL_MASCOT = 'Ram'

# Weather API data
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
ZIP_CODE = '49341'
WEATHER_API_BASE = 'http://api.weatherapi.com/v1/'

# OpenAI data
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
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
IMAGE_GENERATION_URL = 'https://api.openai.com/v1/images/generations'

# Communication data
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = os.environ.get('SNOW_DAY_SENDER_EMAIL')
SENDER_EMAIL_PASSWORD = os.environ.get('SNOW_DAY_SENDER_PASSWORD')
VERIZON_DOMAIN = '@vtext.com'
ATT_DOMAIN = '@txt.att.net'
TMOBILE_DOMAIN = '@tmomail.net'
SPRINT_DOMAIN = '@messaging.sprintpcs.com'

