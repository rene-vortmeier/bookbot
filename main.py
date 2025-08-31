from stats import get_book_text,count_words,count_letters

def main():
    path="./books/frankenstein.txt"
    text=get_book_text(path)
    words=count_words(text)
    letters=count_letters(text)
    print(f"{words} words found in the document")
    for letter in letters:
        print(f"'{letter}': {letters[letter]}")
    return None

main()