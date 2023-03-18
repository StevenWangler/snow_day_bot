'''
This is the settings file that contains information needed to run the application,
talk to API's, etc.
'''
import settings.app_secrets as app_secrets

# General data
SCHOOL_NAME = 'Rockford Public Schools'
SCHOOL_COLORS = 'Orange and black'
SCHOOL_MASCOT = 'Ram'
AI_RESPONSE_THEMES = ['Cool high school student',
                      'Pirate', 
                      'Bugs bunny',
                      'Scooby-doo',
                      'Surfer dude',
                      'First grader',
                      'Cowboy',
                      'Superhero',
                      'Mad scientist',
                      'Mario',
                      'Robot',
                      'Hippie',
                      'Caveman',
                      'Detective']

# Weather API data
WEATHER_API_KEY = app_secrets.WEATHERAPI_KEY
ZIP_CODE = '49341'
WEATHER_API_BASE = 'http://api.weatherapi.com/v1/'

# OpenAI data
OPENAI_API_KEY = app_secrets.OPENAI_API_KEY
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
SENDER_EMAIL = app_secrets.SENDER_EMAIL
SENDER_EMAIL_PASSWORD = app_secrets.SENDER_EMAIL_PASSWORD
VERIZON_DOMAIN = '@vtext.com'
ATT_DOMAIN = '@txt.att.net'
TMOBILE_DOMAIN = '@tmomail.net'
SPRINT_DOMAIN = '@messaging.sprintpcs.com'
