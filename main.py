def main():
    path = "books/frankenstein.txt"
    text = get_book(path)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count(text)} words found in the document.")

    character_counts = get_character_counts(text)

    for character in character_counts:
        print(f"The character {character} was found {character_counts[character]} times")

    print("--- End report ---")



def get_book(path):
    with open(path) as f:
        contents = f.read()
    
    return contents

def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    lowered = ''.join(char.lower() for char in text if char.isalpha())
    
    return {char: lowered.count(char) for char in set(lowered)}

main()