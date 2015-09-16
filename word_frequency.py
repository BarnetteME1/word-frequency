def word_frequency(book):
    book = words(book)
    word_count = {}
    n = 0
    while n < len(book):
        for word in useless_words:
            if word in book[n]:
                book.remove(book[n])
        n+=1
    for word in book:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def top_twenty(book):
    word_count = word_frequency(book)
    count_word = {}
    count_word = sorted(word_count.items(), key=lambda x: x[1], reverse = True)
    n=0
    top_twenty = []
    while n <= 20:
        top_twenty.append(count_word[n])
        n+=1
    return dict(top_twenty)

#words(book)
#word_frequency(book)
#top_twenty(book)
print(top_twenty(book))
