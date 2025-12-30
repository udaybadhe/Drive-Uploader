import pickle
import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

def Create_Service():
    """
    Creates a Google API service object.
    Reads configuration from 'config.json'.
    """
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: 'config.json' not found. Please create it from 'config.json.example'.")
        return None

    CLIENT_SECRET_FILE = config.get('client_secret_file')
    API_NAME = config.get('api_name')
    API_VERSION = config.get('api_version')
    SCOPES = config.get('scopes')

    if not all([CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES]):
        print("Error: 'config.json' is missing one or more required fields.")
        return None

    pickle_file = f'token_{API_NAME}_{API_VERSION}.pickle'

    cred = None
    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            try:
                cred.refresh(Request())
            except Exception as e:
                print(f"Error refreshing token: {e}")
                # If refresh fails, fall back to re-running the flow
                cred = None
        if not cred:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                cred = flow.run_local_server(port=0)
            except FileNotFoundError:
                print(f"Error: Client secret file not found at '{CLIENT_SECRET_FILE}'.")
                print("Please update 'config.json' with the correct path.")
                return None
            except Exception as e:
                print(f"Error during authentication flow: {e}")
                return None

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_NAME, API_VERSION, credentials=cred)
        print(f"'{API_NAME}' service created successfully.")
        return service
    except Exception as e:
        print(f"Error building service: {e}")
        return None