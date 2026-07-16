import spacy
nlp = spacy.load("en_core_web_sm")

def extract_with_spacy(text):
    doc = nlp(text)

    song = None
    artist = None

    for ent in doc.ents:
        if ent.label_ == "WORK_OF_ART" and song is None:
            song = ent.text
        if ent.label_ in ["PERSON", "ORG"] and artist is None:
            artist = ent.text

    return song, artist
