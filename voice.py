import speech_recognition as sr
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# def transcribe_audio():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()

#     with mic as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     print("Transcribing...")
#     try:
#         text = recognizer.recognize_google(audio)
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#         return None
#     except sr.RequestError as e:
#         print(f"Error with speech recognition service: {e}")
#         return None
#     print("You said:", text)
#     return text.lower()

# def detect_intent(text):
#     if "next" in text:
#         return "NEXT"
#     if "previous" in text or "back" in text:
#         return "PREVIOUS"
#     if "pause" in text or "stop" in text:
#         return "PAUSE"
#     if "resume" in text or "continue" in text or "play" in text or "start" in text:
#         return "PLAY"

#     return None

def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening for command...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    print("Transcribing command...")
    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error with speech recognition service: {e}")
        return None
    print("You said:", text)
    return text.lower()


def detect_intent(text):
    if "volume up" in text or ("increase" in text and "volume" in text):
        return "VOLUME_UP"

    if "volume down" in text or ("decrease" in text and "volume" in text):
        return "VOLUME_DOWN"

    if "mute" in text or "silence" in text:
        return "VOLUME_MUTE"

    # Set specific volume level: "set volume to 50%"
    if "volume" in text and any(str(i) in text for i in range(10)):
        return "VOLUME_SET"
    
    if "next" in text:
        return "NEXT"
    if "previous" in text or "back" in text:
        return "PREVIOUS"
    if "pause" in text or "stop" in text:
        return "PAUSE"
    if "resume" in text or "continue" in text:
        return "PLAY"
    if "play" in text:
        return "PLAY_SPECIFIC"
    
    if "playlist" in text or "my" in text or "list" in text:
        return "PLAY_PLAYLIST"

    return None

import re

def extract_volume_level(text):
    match = re.search(r"(\d{1,3})\s*(percent|%)?", text)
    if match:
        level = int(match.group(1))
        return max(0, min(level, 100))  # clamp 0–100
    return None
