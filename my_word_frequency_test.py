with open("sample.txt") as hounds_of_the_baskerville:
    book = hounds_of_the_baskerville.read()

from string import punctuation
from string import whitespace

def words(book):
    for char in book:
        if char in punctuation:
            book = book.replace(char, ' ')
        if char in whitespace:
            book = book.replace(char, ' ')
        return book.lower().split()

def top_twenty(book):
    word_count = {}
    count_word = {}
    for word in book:
        if word not in word_count:
            word_count[word]=1
        else:
            word_count[word]+=1
    word_list = []
    for word in word_count:
        word_list.append([word_count[word], word])
    for word in word_list:
        if word[0] not in count_word:
            count_word[word[0]] = word[1]
        else:
            count_word[word[0]] += ', '+word[1]
    count = sorted(count_word)
    count = count[::-1]
    n=0
    word = ''
    top_twenty = []
    while n <= 20:
        word = count_word[count[n]]
        top_twenty.append([count[n], count_word[count[n]]])
        n+=1
    for word, count in top_twenty:
        return ("{}: {}".format(word, count))

print (top_twenty(words(book)))
