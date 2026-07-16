import tkinter as tk
from tkinter import messagebox

from auth import get_token
from spotify_control import play, pause, next_track, previous_track
from wakeword import WakeWordDetector
from voice import listen_for_command, detect_intent

import threading

from intend_extractor.extractor import extract_song_and_artist
from spotify_search import search_song
from spotify_control import play_track_uri

from spotify_control import volume_up, volume_down, mute_volume, set_volume
from voice import extract_volume_level

from playlist_extractor import extract_playlist_name
from spotify_playlists import get_user_playlists, fuzzy_match_playlist
from spotify_control import play_playlist

import os


token = None
wakeword_running = False

PICOVOICE_ACCESS_KEY = os.getenv("PICOVOICE_ACCESS_KEY", "your_picovoice_access_key")

detector = WakeWordDetector(
access_key=PICOVOICE_ACCESS_KEY,
    keyword="jarvis",
    on_detect=lambda: handle_wakeword()
)

def login_spotify():
    global token
    token = get_token()
    messagebox.showinfo("Login", "Spotify authentication successful!")

def handle_wakeword():
    global token

    text = listen_for_command()
    intent = detect_intent(text)

    if not intent:
        print("Could not detect intent.")
        return
    
    if intent == "VOLUME_UP":
        print("Increasing volume...")
        volume_up(token)

    elif intent == "VOLUME_DOWN":
        print("Decreasing volume...")
        volume_down(token)

    elif intent == "VOLUME_MUTE":
        print("Muting volume...")
        mute_volume(token)

    elif intent == "VOLUME_SET":
        level = extract_volume_level(text)
        if level is not None:
            print(f"Setting volume to {level}%...")
            set_volume(token, level)
        else:
            print("Could not determine volume level.")

    elif intent == "NEXT":
        next_track(token)

    elif intent == "PREVIOUS":
        previous_track(token)

    elif intent == "PAUSE":
        pause(token)

    elif intent == "PLAY":
        play(token)

    elif intent == "PLAY_SPECIFIC":
        song, artist = extract_song_and_artist(text)

        if not song:
            print("Could not extract song name.")
            return

        print(f"Searching for: Song = {song}, Artist = {artist}")

        uri, found_song, found_artist = search_song(song, artist, token)

        if uri:
            print(f"Playing: {found_song} - {found_artist}")
            play_track_uri(token, uri)
        else:
            print("Song not found on Spotify.")
    
    elif intent == "PLAY_PLAYLIST":
        print("Playlist command detected.")

        playlist_name = extract_playlist_name(text)

        if not playlist_name:
            print("Could not extract playlist name.")
            return

        print(f"Extracted playlist name: {playlist_name}")

        # Fetch user playlists
        playlists = get_user_playlists(token)

        print(playlists)

        # Find closest match
        match = fuzzy_match_playlist(playlist_name, playlists)

        if not match:
            print("No matching playlist found.")
            return

        playlist_uri = playlists[match]
        print(f"Playing your playlist: {match}")
        play_playlist(token, playlist_uri)


    print("Returning to wake-word listening...")
        


def toggle_wakeword():
    global wakeword_running

    if not token:
        messagebox.showerror("Error", "Please login to Spotify first!")
        return

    if wakeword_running:
        detector.stop()
        wakeword_running = False
        toggle_btn.config(text="Start Wake Word Listener")
    else:
        detector.start()
        wakeword_running = True
        toggle_btn.config(text="Stop Wake Word Listener")

def main():
    global toggle_btn

    root = tk.Tk()
    root.title("Spotify Voice Controller")
    root.geometry("400x400")

    tk.Button(root, text="Login to Spotify",
              command=login_spotify, width=30).pack(pady=10)

    toggle_btn = tk.Button(root, text="Start Wake Word Listener",
                           command=toggle_wakeword, width=30)
    toggle_btn.pack(pady=10)

    tk.Button(root, text="Play", command=lambda: play(token),
              width=30).pack(pady=5)
    tk.Button(root, text="Pause", command=lambda: pause(token),
              width=30).pack(pady=5)
    tk.Button(root, text="Next Song", command=lambda: next_track(token),
              width=30).pack(pady=5)
    tk.Button(root, text="Previous Song", command=lambda: previous_track(token),
              width=30).pack(pady=5)
    
    # -- - MANUAL SEARCH UI SECTION ---
    song_entry = tk.Entry(root, width=40)
    song_entry.pack(pady=5)
    song_entry.insert(0, "Song name")

    artist_entry = tk.Entry(root, width=40)
    artist_entry.pack(pady=5)
    artist_entry.insert(0, "Artist (optional)")

    def manual_search():
        song = song_entry.get().strip()
        artist = artist_entry.get().strip() or None

        if not song:
            messagebox.showerror("Error", "Please enter a song name.")
            return

        uri, found_song, found_artist = search_song(song, artist, token)


        if uri:
            play_track_uri(token, uri)
        else:
            messagebox.showerror("Error", "Song not found.")

    tk.Button(root, text="Search & Play", width=30, command=manual_search).pack(pady=10)

    tk.Button(root, text="Exit", command=root.quit, width=30).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
