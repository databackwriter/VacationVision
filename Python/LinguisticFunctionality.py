#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 06:26:24 2018

@author: petermoore
"""

import nltk


# bag of n-grams example
words = "the cat sat on the mat"
word_list = words.split()
n=3
bag_of_ngrams = nltk.ngrams(word_list, n) #bag is a telling word here: it's a set, order is unimportant
for _ in bag_of_ngrams:
    print(_)


import numpy as np

# one hot encoding examples
samples = ["the cat sat on the mat.", "the dog ate my homework."]

## word level
token_index = {}
for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index) + 1 #NB no index 0
max_length = 10
results = np.zeros(shape=(len(samples), max_length, max(token_index.values()) + 1))#2x10x10 but why do we add one to the third dimension when we only have nine words
for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index=token_index.get(word)
        results[i,j,index] = 1

## character level
import string
characters = string.printable
token_indexchar = dict(zip(range(1, len(characters)+1), characters))
max_lengthchar = 50
resultschar = np.zeros(shape=(len(samples), max_lengthchar, max(token_indexchar.keys()) + 1)) #2x50x101
for i, sample in enumerate(samples):
    for j, character in enumerate(sample):
        index = token_indexchar.get(character)
        resultschar[i,j,index] = 1

## using keras
from keras.preprocessing.text import Tokeniser # NB this is a big deal because it strips special characters and allows selection of only most common words

tokenizer = Tokeniser(num_words=1000)


