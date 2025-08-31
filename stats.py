def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(i):
    words=i.split()
    return len(words)

def count_letters(text):
    lower_text=text.lower()
    count={}
    for letter in lower_text:
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1
    return count