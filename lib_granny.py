def bigrams(text):
    return zip(text[0:-1], text[1:])
def trigrams(text):
    return zip(text[0:-2], text[1:-1], text[2:])
def count(grams):
    dictionary = {}
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for a in letters:
        for b in letters:
            dictionary[(a,b)] = 0

    for gram in grams:
        dictionary[gram] = dictionary[gram] + 1
    return dictionary

def bigramScore(count, word):
    bgs = bigrams(word)
    score = 0
    for g in bgs:
        score = score + (count[g] if g in count else 0)
    return float(score) / len(bgs)

dictionary_bigrams = {}

import re

f = open('shakesphere.txt', 'r')
str = f.read()
str = re.sub('[^a-z]+', '', str)

dictionary_bigrams = count(bigrams(str))
