def get_word_count(text):
    return len(text.split())

def sort_on(dict):
    return dict["count"]

def get_character_counts(text):
    lowered = ''.join(char.lower() for char in text if char.isalpha())

    counts = []

    for letter in set(lowered):
        counts.append({"char": letter, "count": lowered.count(letter)})

    counts.sort(reverse=True, key=sort_on)

    return counts