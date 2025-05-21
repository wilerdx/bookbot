import sys
from stats import count_words, count_char, sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    relative_path = sys.argv[1]
    book_text = get_book_text(relative_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")    

    word_count = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    character_count = count_char(book_text)

    filtered_char_count = {char: count for char, count in character_count.items() if char.isalpha()}

    sorted_chars = sorted_dict(filtered_char_count)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()
