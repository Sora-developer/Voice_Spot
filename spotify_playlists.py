import requests
from difflib import SequenceMatcher

def get_user_playlists(token):
    url = "https://api.spotify.com/v1/me/playlists?limit=50"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers).json()

    playlists = {}

    for item in response.get("items", []):
        playlists[item["name"].lower()] = item["uri"]

    return playlists


def fuzzy_match_playlist(name, playlist_dict):
    best_score = 0
    best_match = None

    for playlist in playlist_dict.keys():
        score = SequenceMatcher(None, name.lower(), playlist.lower()).ratio()
        if score > best_score:
            best_score = score
            best_match = playlist

    if best_score > 0.5:  # good enough similarity
        return best_match
    return None
