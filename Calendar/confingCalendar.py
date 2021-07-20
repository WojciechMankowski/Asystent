from __future__ import print_function
 # type: ignore
from googleapiclient.discovery import build # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore
from google.auth.transport.requests import Request # type: ignore
from google.oauth2.credentials import Credentials # type: ignore
import os
from oauth2client import file, client, tools # type: ignore


class Config:

    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.creds = None
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())