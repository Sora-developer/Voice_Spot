from spotipy.oauth2 import SpotifyOAuth

import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "your_spotify_client_id")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "your_spotify_client_secret")
REDIRECT_URI = "http://127.0.0.1:8888/callback"

SCOPE = "user-modify-playback-state user-read-playback-state streaming"

def get_spotify_auth():
    sp_oauth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    )
    return sp_oauth

def get_token():
    sp_oauth = get_spotify_auth()
    token_info = sp_oauth.get_access_token(as_dict=False)
    return token_info
