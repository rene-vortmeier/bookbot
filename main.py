def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(i):
    words=i.split()
    return len(words)

def main():
    path="./books/frankenstein.txt"
    words=0
    words=count_words(get_book_text(path))
    print(f"{words} words found in the document")
    return None

main()