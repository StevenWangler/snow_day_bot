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
