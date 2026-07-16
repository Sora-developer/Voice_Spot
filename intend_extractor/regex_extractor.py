import re

def extract_with_regex(text):
    text = text.lower()

    # Pattern: play <song> by <artist>
    match = re.search(r"play (.+?) by (.+)", text)
    if match:
        return match.group(1).strip(), match.group(2).strip()

    # Pattern: play the song <song>
    match = re.search(r"play (?:the )?song (.+)", text)
    if match:
        return match.group(1).strip(), None

    # Pattern: play <song>
    match = re.search(r"play (.+)", text)
    if match:
        return match.group(1).strip(), None

    return None, None
