# Voice_Spot - Spotify Voice Assistant(Python Desktop App)

A voice-controlled Spotify desktop assistant built with Python that allows us to control Spotify using natural speech, including:

## What it can do

- Wake-word activation with Porcupine
- Play, pause, resume, next, and previous track
- Play a specific song by voice
- Play a playlist from the signed-in Spotify account
- Volume up, volume down, mute, and set a percentage
- Desktop GUI built with Tkinter

## Features

1. Voice Control

- Wake word activation (e.g. jarvis, computer)
- Continuous listening loop (wakeword -> command -> wakeword)
- Natural language commands

2. Spotify Playback

- play / pause / resume
- Next / Previous song
- Play a specific song
- Play a playlist from users library
- Volume up/ down / mute / set percentage

3. NLP - Driven Understanding

- Regex based parsing for structured commands
- SpaCy NLP (NER) for entity recognition
- Fuzzy matching for tolerant song & playlist search

4. Desktop Application

- Tkinter GUI
- Start / Stop wake word listener
- Spotify login via OAuth

## Architecture Overview

Wake Word (Porcupine)
↓
Speech-to-Text (Google)
↓
Intent Detection
↓
NLP Extraction
(Regex + SpaCy + Fuzzy)
↓
Spotify Web API
↓
Playback / Volume / Playlist Control

This program runs wake-word detection in the background thread to ensure the GUI remains responsive.

## Project Structure

```text
./
├── app.py                     # Tkinter GUI and app flow
├── auth.py                    # Spotify OAuth configuration
├── wakeword.py                # Wake-word listener using Porcupine
├── voice.py                   # Speech recognition and intent detection
├── playlist_extractor.py      # Playlist name extraction helper
├── spotify_control.py         # Playback and volume control helpers
├── spotify_playlists.py       # Playlist lookup and matching
├── spotify_search.py          # Spotify track search helper
├── intend_extractor/
│   ├── extractor.py
│   ├── fuzzy_search.py
│   ├── regex_extractor.py
│   └── spacy_extractor.py
├── .env.example
├── spotify_client_secret.txt
└── README.md
```

## Technologies Used

- Wake word -> Picovoice Porcupine
- Speech Recognition -> Google
- NLP -> Regex, SpaCy, Fuzzy Matchmaking
- GUI -> Tkinter
- API -> Spotify Web API
- Auth -> OAuth 2.0

## Prerequisites

- Spotify Premium Account
- Spotify Developer Account
- Microphone enabled
- A Picovoice access key for wake-word detection
- A OpenAI API Key

## Installation

1. Clone the Repository

```
git clone https://github.com/Sora-developer/Voice_Spot.git
cd Voice_Spot

```

2. Installing Dependencies

```
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm

```

3. Create a Spotify App

- Go to https://developers.spotify.com/dashboard
- Create a new app
- Set Redirect URL: http://127.0.0.1:8888/callback
- Copy : Client ID, Client Secret

4. Configure Environment Variables:
   Edit the .env file with

```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
OPENAI_API_KEY=your_openai_api_key
PICOVOICE_ACCESS_KEY=your_picovoice_access_key
REDIRECT_URI = http://127.0.0.1:8888/callback
```

5. Run the Application

```
python app.py

```

6. In the GUI:
- Click "Login to Spotify"
- Click "Start Wake Word Listener"
- Speak the wake word (for example, "jarvis") followed by a command such as:
  - "play song"
  - "pause"
  - "next song"
  - "volume up"
  - "play playlist"

## Permissions (Spotify Scope)

```
user-modify-playback-state
user-read-playback-state
playlist-read-private
streaming

```

## Notes
- The wake-word detector must be configured with a valid Picovoice key.
- Speech recognition depends on a working microphone and internet access for Google Speech Recognition.
- Some dependencies such as PyAudio may require additional system setup on Windows.

## Future Enhancements

- Voice feedback (TTS)
- Album & artist playback
- GUI album art + now playing
- Playlist caching
- System tray support
- offline SST support
- Create an .exe applicaton

## Author

Om G<br>
Built as a real-world demonstation of voice interfaces + NLP + APIs
