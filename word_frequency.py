with open("sample.txt") as hounds_of_the_baskerville:
    book = hounds_of_the_baskerville.read()

from string import punctuation
from string import whitespace

def words(book):
    for char in book:
        if char in punctuation:
            book = book.replace(char, '')
        if char in whitespace:
            book = book.replace(char, ' ')
    return book.lower().split()

def word_frequency(book):
    book = words(book)
    word_count = {}
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
    return top_twenty

top_twenty(book)
#print(word_list)
