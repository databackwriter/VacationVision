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

imdb_dir = "/Users/petermoore/Downloads/aclImdb"
train_dir = os.path.join(imdb_dir, "train")

labels = []
texts = []

for label_type in ["neg", "pos"]:
    dir_name = os.path.join(train_dir, label_type)
    for fname in os.listdir(dir_name):
        if fname[-4:] == ".txt":
            f = open(os.path.join(dir_name, fname))
            texts.append(f.read())
            f.close()
            if label_type == "neg":
                labels.append(0)
            else:
                labels.append(1)


from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

maxlen = 100 # cut off review after 100 words
training_samples = 200 # train on 200 samples
validation_samples = 10000 # validate on 10000 samples
max_words = 10000 # consider only 10000 words in the data set

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)

word_index = tokenizer.word_index

data = pad_sequences(sequences, maxlen=maxlen) #shape is 25000 x 100

labels = np.asarray(labels) # shape is 25000,

indices= np.arange(data.shape[0]) #Chollet: splits data into training set and calidation set
np.random.shuffle(indices) # but first shuffles it because you are starting with data in which samples are ordered
data = data[indices]
labels = labels[indices]

x_train = data[:training_samples]
y_train = labels[:training_samples]
x_val = data[training_samples:training_samples + validation_samples]
y_val = labels[training_samples:training_samples + validation_samples]

# this bit takes teh file from glove and builds an index that maps words to their vector representation
glove_dir = "/Users/petermoore/Downloads/glove.6B"
embeddings_index = {}
f = open(os.path.join(glove_dir, "glove.6B.100d.txt"))
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype = "float32")
    embeddings_index[word] = coefs
f.close()

# now buyld an embedding matrix
embedding_dim = 100 # going to build a matrix of max_words x 100; an entry at position "i" is a 100-d vector of that word
embedding_matrix = np.zeros((max_words, embedding_dim))
for word, i in word_index.items():
    if i < max_words:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector


# now use the embedding layer in a similar way to the above (but there is an extra layer and we don't compile)
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense

model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=maxlen)) # 100-dimensional embeddings
model.add(Flatten()) # flatten 3D tensor into 2d of shape samples, maxlen * 100
model.add(Dense(32, activation="relu")) # add the classifier on top
model.add(Dense(1, activation="sigmoid")) # add the classifier on top
model.summary()

# load pre-trained word embedings from GloVe into embedding layer
model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False # FFS don't retrain the pretrain with your randomly initialised layer

# compile and train
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["acc"])
model.summary()

history = model.fit(x_train,
                    y_train,
                    epochs=10,
                    batch_size=32,
                    validation_data=(x_val, y_val))

model.save_weights("pre_trained_glove_model.h5")



import matplotlib.pyplot as plt
acc = history.history["acc"]
val_acc = history.history["val_acc"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, "bo", label="Training acc")
plt.plot(epochs, val_acc, "b", label="Validation acc")
plt.title("Training and validation accuracy")
plt.legend()

plt.figure()


plt.plot(epochs, loss, "bo", label="Training loss")
plt.plot(epochs, val_loss, "b", label="Validation loss")
plt.title("Training and validation loss")
plt.legend()

plt.show()
