#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 06:26:24 2018

@author: petermoore
"""

import nltk


## bag of n-grams example
#words = "the cat sat on the mat"
#word_list = words.split()
#n=3
#bag_of_ngrams = nltk.ngrams(word_list, n) #bag is a telling word here: it's a set, order is unimportant
#for _ in bag_of_ngrams:
#    print(_)
#
#
#import numpy as np
#
## one hot encoding examples
#samples = ["the cat sat on the mat.", "the dog ate my homework."]
#
### word level
#token_index = {}
#for sample in samples:
#    for word in sample.split():
#        if word not in token_index:
#            token_index[word] = len(token_index) + 1 #NB no index 0
#max_length = 10
#results = np.zeros(shape=(len(samples), max_length, max(token_index.values()) + 1))#2x10x10 but why do we add one to the third dimension when we only have nine words
#for i, sample in enumerate(samples):
#    for j, word in list(enumerate(sample.split()))[:max_length]:
#        index=token_index.get(word)
#        results[i,j,index] = 1
#
### character level
#import string
#characters = string.printable
#token_indexchar = dict(zip(range(1, len(characters)+1), characters))
#max_lengthchar = 50
#resultschar = np.zeros(shape=(len(samples), max_lengthchar, max(token_indexchar.keys()) + 1)) #2x50x101
#for i, sample in enumerate(samples):
#    for j, character in enumerate(sample):
#        index = token_indexchar.get(character)
#        resultschar[i,j,index] = 1
#
#
### using keras
#from keras.preprocessing.text import Tokenizer
#tokenizer = Tokenizer(num_words=1000)
#
#tokenizer.fit_on_texts(samples) # builds word index
#
#sequences = tokenizer.texts_to_sequences(samples) # turns strings into lists of integer indices
#
#one_hot_results = tokenizer.texts_to_matrix(samples, mode="binary") # direct way of getting one hot binary representations
#
#word_index = tokenizer.word_index
#
#print("found %s unique tokens" % len(word_index))
#
## word-level with 'hashing trick'
#dimensionality = 1000
#max_length = 10
#
#results = np.zeros((len(samples), max_length, dimensionality))
#for i, sample in enumerate(samples):
#    for j, word in list(enumerate(sample.split()))[:max_length]:
#        index = abs(hash(word)) % dimensionality # hashes the word into an integer between 0 and 1000
#        results[i, j, index] = 1  # just a personal thought: this is what I do when I am showing off.
#
#
#
#from keras.layers import Embedding
#embedding_layer = Embedding(1000, 64) # okay, this is gnarly but fun, from Chollet: the Embedding layer maps integer indices
## to dense vectors (path is roughly integer ==> word ==> associated vectors) (like a dictionary lookup)
#
#from keras.datasets import imdb
#from keras import preprocessing
#
#max_features = 10000 # top 10000 most common words
#maxlen = 20 # cut off reviews after 20 words
#
#(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features) # loads data into list of integers
#x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen) #turn list into 2D tensor
#x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen) #François Chollet. Deep Learning with Python (Kindle Locations 3848-3851). Manning Publications. Kindle Edition.
#
## now use the embedding layer
#from keras.models import Sequential
#from keras.layers import Flatten, Dense
#
#model = Sequential()
#model.add(Embedding(10000, 8, input_length=maxlen)) # eight-dimensional embeddings
#model.add(Flatten()) # flatten 3D tensor into 2d of shape samples, maxlen * 8
#
#model.add(Dense(1, activation="sigmoid")) # add the classifier on top
#model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["acc"])
#model.summary()
#
#history = model.fit(x_train,
#                    y_train,
#                    epochs=10,
#                    batch_size=32,
#                    validation_split=0.2)


import os

imdb_dir = "/Users/downloads/petermoore/DFownloads/aclImdb"
train_dir = os.path.join(imdb_dir, "train")

labels = []
texts = []

for label_type in ["neg", "pos"]:
    dir_name = os.path.join(train_dir, label_type)
    for fname in os.listdir(dir_name):
        if fname[-4] = ".txt":
            f = open(os.path.join(dir_name, fname))
            texts.append(f.read())
            f.close()
            if label_type == "neg":
                labels.append(0)
            else:
                labels.append(1)




