"""
This Python script sets up authentication and access to the Google Forms API using OAuth 2.0. 

Key components of the script include:
- Importing necessary modules from `apiclient`, `httplib2`, and `oauth2client` for
  API interaction and OAuth 2.0 authentication.
- Defining the OAuth 2.0 scope (`SCOPES`) for readonly access to Google Forms responses.
- Specifying the Discovery Document (`DISCOVERY_DOC`) URL to identify the methods available in the
  Google Forms API.
- Checking for existing valid credentials stored in 'token.json'. If none are found or if 
  they are invalid, the script generates new credentials using the OAuth 2.0 
  client secrets from 'credentials.json'.
- Finally, the script builds a service object (`form_service`) for 
  interacting with the Google Forms API.

Usage:
- Ensure 'credentials.json' is available with the necessary OAuth 2.0 client secrets.
- The script will handle authentication and create a 'token.json' for subsequent authentications.
- Use `form_service` to interact with Google Forms through the API.
"""

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

# OAuth 2.0 scope for Google Forms. This allows for full access to form creation and management.
SCOPES = ["https://www.googleapis.com/auth/forms.responses.readonly"]

# Discovery document to identify the available methods in the API.
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

# Check if valid credentials are saved in 'token.json'. If not, generate new ones.
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)

# Build the service object for the API
form_service = discovery.build('forms', 'v1', http=creds.authorize(Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)
