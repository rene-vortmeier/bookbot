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
        if letter.isalpha() == True:
            if letter in count:
                count[letter]+=1
            else:
                count[letter]=1
    return count


def sorting(dictionary):
    list_count=[]
    for ch, num in dictionary.items():
        temp_1={}
        temp_1["char"]=ch
        temp_1["num"]=num
        list_count.append(temp_1)
    list_count.sort(reverse=True, key=list_count.item["num"])
    return list_count
