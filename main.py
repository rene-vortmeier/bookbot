from stats import get_book_text,count_words,count_letters,sort_on,sorting

def main():
    path="./books/frankenstein.txt"
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