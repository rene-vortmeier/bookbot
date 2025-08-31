def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    location="./books/frankenstein.txt"
    print(get_book_text(location))
    return None

main()