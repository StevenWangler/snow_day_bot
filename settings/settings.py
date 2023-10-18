'''
This is the settings file that contains information needed to run the application,
talk to API's, etc.
'''
from settings import app_secrets

# School data
SCHOOL_NAME = 'Rockford Public Schools'
SCHOOL_COLORS = 'Orange and black'
SCHOOL_MASCOT = 'Ram'
SCHOOL_DISTRICT_STATE = 'Michigan'


# Weather API data
WEATHER_API_KEY = app_secrets.WEATHERAPI_KEY
ZIP_CODE = '49341'
WEATHER_API_BASE = 'http://api.weatherapi.com/v1/'


# OpenAI data
OPENAI_API_KEY = app_secrets.OPENAI_API_KEY
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
AI_RESPONSE_THEMES = ['Student trying to use homework as a snow shovel',
                      'Pirate with a snow treasure map leading to the playground', 
                      'Bunny making a giant snow-carrot',
                      'Mystery gang tracking the legendary Snow Yeti',
                      'Kid trying to surf down a snowy hill on a lunch tray',
                      'Young wizard casting snowball-fighting spells',
                      'Cowboy having a snowball showdown outside the school',
                      'Plumber sliding on icy levels to save the snow princess',
                      'Robot with snowflake-shaped gears',
                      'Nature lover making snow peace signs on the lawn',
                      'Caveman using a tablet (stone) to predict snow days',
                      'Superhero flying around to collect the best snowflakes',
                      'Sponge creature building a snow house under the sea',
                      'Space explorer reporting "It\'s snowing on the moon!"',
                      'Vampire wearing sunscreen for a day in the snow',
                      'Detective on the case of the missing snowman\'s nose',
                      'Scientist experimenting with snowflake designs',
                      'Ninja leaving no footprints in the snow',
                      'Dancer performing the "Snowflake Ballet"',
                      'Gladiator hosting the great snow fort battle',
                      'Musician composing the "Epic Snow Day Symphony"',
                      'Prince/Princess awaiting a snowy royal ball',
                      'Zombie with a sign: "Will work for snow cones"',
                      'Alien sending postcards: "First Earth Snow!"',
                      'Knight defending the grand snow castle',
                      'Explorer on a quest for the magical snowflake',
                      'Merfolk hosting an underwater snow festival',
                      'Samurai practicing with a blade of solid ice',
                      'Superhero donning a cape made of snowflakes',
                      'Hunter on the trail of the elusive snow fox',
                      'Adventurer searching for the lost city of Snowlantis',
                      'Chef hosting a "Snowy Treats" cooking show']


# Communication data
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = app_secrets.SENDER_EMAIL
SENDER_EMAIL_PASSWORD = app_secrets.SENDER_EMAIL_PASSWORD
VERIZON_DOMAIN = '@vtext.com'
ATT_DOMAIN = '@txt.att.net'
TMOBILE_DOMAIN = '@tmomail.net'
SPRINT_DOMAIN = '@messaging.sprintpcs.com'
