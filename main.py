from stats import get_book_text,count_words,count_letters

def main():
    path="./books/frankenstein.txt"
    words=0
    words=count_words(get_book_text(path))
    letters=count_letters(get_book_text(path))
    print(f"{words} words found in the document")
    for letter in letters:
        print(f"'{letter}': {letters[letter]}")
    return None

main()