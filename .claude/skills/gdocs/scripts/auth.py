"""Google Docs API OAuth2 authentication."""

import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive.file',
]

CREDENTIALS_SEARCH_PATHS = [
    'credentials.json',
    os.path.expanduser('~/.config/gdocs/credentials.json'),
]


def find_credentials() -> str | None:
    """Find credentials.json in known locations."""
    for path in CREDENTIALS_SEARCH_PATHS:
        if os.path.exists(path):
            return path
    return None


def get_token_path(credentials_path: str) -> str:
    """Get token.json path (same directory as credentials.json)."""
    return os.path.join(os.path.dirname(credentials_path) or '.', 'token.json')


def get_service(credentials_path: str = None):
    """Returns authenticated Google Docs API service.

    Args:
        credentials_path: Path to credentials.json. Auto-detected if None.

    Returns:
        googleapiclient.discovery.Resource for Docs API v1
    """
    if credentials_path is None:
        credentials_path = find_credentials()
        if credentials_path is None:
            raise FileNotFoundError(
                "credentials.json not found. Place it in project root or ~/.config/gdocs/"
            )

    token_path = get_token_path(credentials_path)
    creds = None

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('docs', 'v1', credentials=creds)


def get_drive_service(credentials_path: str = None):
    """Returns authenticated Google Drive API service for image uploads."""
    if credentials_path is None:
        credentials_path = find_credentials()
        if credentials_path is None:
            raise FileNotFoundError("credentials.json not found.")

    token_path = get_token_path(credentials_path)
    creds = None

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)


def verify_token(credentials_path: str = None) -> dict:
    """Verify that the current token is valid.

    Returns:
        dict with 'valid' (bool), 'email' (str or None), 'error' (str or None)
    """
    try:
        if credentials_path is None:
            credentials_path = find_credentials()
            if credentials_path is None:
                return {'valid': False, 'email': None, 'error': 'credentials.json not found'}

        token_path = get_token_path(credentials_path)
        if not os.path.exists(token_path):
            return {'valid': False, 'email': None, 'error': 'token.json not found. Run auth first.'}

        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())
            else:
                return {'valid': False, 'email': None, 'error': 'Token expired and cannot refresh'}

        return {'valid': True, 'email': creds.token, 'error': None}

    except Exception as e:
        return {'valid': False, 'email': None, 'error': str(e)}


def setup_credentials(source_path: str, target_dir: str = '.') -> str:
    """Copy credentials.json to target directory.

    Args:
        source_path: Path to downloaded credentials.json
        target_dir: Directory to copy to (default: current directory)

    Returns:
        Path to the copied credentials.json
    """
    import shutil
    target_path = os.path.join(target_dir, 'credentials.json')
    shutil.copy2(source_path, target_path)
    return target_path
