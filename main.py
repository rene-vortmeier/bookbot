import sys
from stats import get_book_text,count_words,count_letters,sorting

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path=sys.argv[1]
    text=get_book_text(path)
    words=count_words(text)
    letters=count_letters(text)
    letter_list=sorting(letters) 
    print("============ BOOKBOT ============")
    print(f"analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for letter in letter_list:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")
    return None

main()