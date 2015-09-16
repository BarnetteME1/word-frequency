with open("sample.txt") as hounds_of_the_baskerville:
    book = hounds_of_the_baskerville.read()

from string import punctuation
from string import whitespace
from operator import itemgetter

useless_words = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am',
                 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been',
                 'but', 'by', 'can', 'cannot','could','dear','did','do','does','either'
                 ,'else','ever','every','for','from','get','got','had','has','have',
                 'he','her','hers','him','his','how','however','i','if','in','into',
                 'is','it','its','just','least','let','like','likely','may','me',
                 'might','most','must','my','neither','no','nor','not','of','off',
                 'often','on','only','or','other','our','own','rather','said',
                 'say','says','she','should','since','so','some','than','that',
                 'the','their','them','then','there','these','they','this','tis',
                 'to','too','twas','us','wants','was','we','were','what','when',
                 'where','which','while','who','whom','why','will','with','would',
                 'yet','you','your','more','before','man','see','very','now',
                 'out','over','upon','well','here','came','come','much']

def words(book):
    for char in book:
        if char in punctuation:
            book = book.replace(char, '')
        if char in whitespace:
            book = book.replace(char, ' ')
    book = book.lower().split()
    new_book = []
    for word in book:
        if word not in useless_words:
            new_book.append(word)
    return(new_book)

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
    return dict(top_twenty)

#words(book)
#word_frequency(book)
#top_twenty(book)
print(top_twenty(book))
