from regex_extractor import extract_with_regex
from spacy_extractor import extract_with_spacy
from fuzzy_search import fuzzy_search_query

def extract_song_and_artist(text):
    # 1. Try Regex
    song, artist = extract_with_regex(text)
    if song:
        return song, artist

    # 2. Try SpaCy NLP
    song, artist = extract_with_spacy(text)
    if song:
        return song, artist

    # 3. Fuzzy fallback
    fuzzy = fuzzy_search_query(text)
    if fuzzy:
        return fuzzy, None

    return None, None
