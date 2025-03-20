from stats import get_word_count, get_character_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")

    character_counts = get_character_counts(text)

    for count in character_counts:
        print(f"{count["char"]}: {count["count"]}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    
    return contents

main()