def fuzzy_search_query(text):
    text = text.lower()

    filler_words = [
        "play", "song", "music", "put on", "can you", "please",
        "the", "a", "some", "computer", "hey", "assistant"
    ]

    for word in filler_words:
        text = text.replace(word, "")

    cleaned = " ".join(text.split()).strip()

    if cleaned:
        return cleaned

    return None
