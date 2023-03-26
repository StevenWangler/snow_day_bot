'''
In this file we are generating our credentials file to use 
for the the Google API.
'''
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
from settings import app_secrets

# Set the API scopes that your application needs to access
scopes = ['https://www.googleapis.com/auth/forms']

# Set the path to your client_secret.json file
CLIENT_SECRET_PATH = app_secrets.GOOGLE_CLIENT_SECRET_PATH

# Set the path to the file where the user's credentials will be stored
CREDENTIALS_PATH = app_secrets.GOOGLE_CREDENTIALS_PATH

# Create the flow object and authorize the user
flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRET_PATH, scopes=scopes)
creds = flow.run_local_server(port=0)

# Save the credentials to disk
with open(CREDENTIALS_PATH, 'w', encoding="utf-8") as credentials_file:
    credentials_file.write(creds.to_json())

# Use the credentials object to make authorized requests to the API
response = requests.get(
    'https://forms.googleapis.com/v1/forms/[FORM_ID]/responses',
    headers={'Authorization': f'Bearer {creds.token}'},
    timeout=30
)
