import sys
from stats import word_count, characters_count, sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

path_to_file = sys.argv[1]


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text(path_to_file)
    num_words = word_count(text)
    char_counts = characters_count(text)
    sorted_chars = sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_chars:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

main()		 
