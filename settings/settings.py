'''
This is the settings file that contains information needed to run the application,
talk to API's, etc.
'''

# General settings
TESTING_MODE = True

# School data
SCHOOL_NAME = 'Rockford Public Schools'
SCHOOL_COLORS = 'Orange and black'
SCHOOL_MASCOT = 'Ram'
SCHOOL_DISTRICT_STATE = 'Michigan'

# Weather API data
ZIP_CODE = '49341'
WEATHER_API_BASE = 'http://api.weatherapi.com/v1/'

# OpenAI data
ENGINE_NAME = 'gpt-4'
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
AI_RESPONSE_THEMES = [
                      'A weather man'
                      ]

# Communication data
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
VERIZON_DOMAIN = '@vtext.com'
ATT_DOMAIN = '@txt.att.net'
TMOBILE_DOMAIN = '@tmomail.net'
SPRINT_DOMAIN = '@messaging.sprintpcs.com'
