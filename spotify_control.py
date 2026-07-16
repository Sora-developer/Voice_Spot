import requests

def send_request(method, endpoint, token, json_data=None):
    url = f"https://api.spotify.com/v1/me/player/{endpoint}"
    headers = {"Authorization": f"Bearer {token}"}

    return requests.request(method, url, headers=headers, json=json_data)

def play(token):
    send_request("PUT", "play", token)

def pause(token):
    send_request("PUT", "pause", token)

def next_track(token):
    send_request("POST", "next", token)

def previous_track(token):
    send_request("POST", "previous", token)

def play_track_uri(token, track_uri):
    url = "https://api.spotify.com/v1/me/player/play"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"uris": [track_uri]}

    return requests.put(url, headers=headers, json=data)

import requests

def set_volume(token, level):
    url = f"https://api.spotify.com/v1/me/player/volume?volume_percent={level}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, headers=headers)

def volume_up(token):
    # Get current volume
    current = get_current_volume(token)
    new_volume = min(current + 10, 100)
    set_volume(token, new_volume)

def volume_down(token):
    current = get_current_volume(token)
    new_volume = max(current - 10, 0)
    set_volume(token, new_volume)

def mute_volume(token):
    set_volume(token, 0)

def get_current_volume(token):
    url = "https://api.spotify.com/v1/me/player"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers).json()

    try:
        return response["device"]["volume_percent"]
    except:
        return 50

def play_playlist(token, playlist_uri):
    url = "https://api.spotify.com/v1/me/player/play"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"context_uri": playlist_uri}
    return requests.put(url, headers=headers, json=data)

