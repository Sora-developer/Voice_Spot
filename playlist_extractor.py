import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_playlist_regex(text):
    text = text.lower()

    # play my <playlist>
    match = re.search(r"(?:my )?playlist (.+)", text)
    if match:
        return match.group(1).strip()

    # play the playlist <playlist>
    match = re.search(r"(?:the )?playlist (.+)", text)
    if match:
        return match.group(1).strip()

    # play <playlist> playlist
    match = re.search(r"(.+) playlist", text)
    if match:
        return match.group(1).strip()

    return None


def extract_playlist_spacy(text):
    doc = nlp(text)
    playlist = None

    for ent in doc.ents:
        if ent.label_ in ["WORK_OF_ART", "ORG"]:
            playlist = ent.text

    return playlist


def extract_playlist_name(text):
    # 1. Regex
    name = extract_playlist_regex(text)
    if name:
        return name

    # 2. SpaCy
    name = extract_playlist_spacy(text)
    if name:
        return name

    # 3. Fuzzy fallback — remove filler words
    filler = ["play", "playlist", "my", "the", "computer", "please"]
    cleaned = text.lower()
    for w in filler:
        cleaned = cleaned.replace(w, "")
    cleaned = " ".join(cleaned.split()).strip()

    return cleaned if cleaned else None
