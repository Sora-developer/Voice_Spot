import requests

def search_song(song_name, artist_name, token):
    query = song_name
    if artist_name:
        query += f" {artist_name}"

    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers).json()

    try:
        track = response["tracks"]["items"][0]
        return track["uri"], track["name"], track["artists"][0]["name"]
    except:
        return None, None, None


