import nltk
# nltk.download()

from nltk.book import *


text1.concordance("algae")

text1.similar("monstrous")

text2.similar("monstrous")

text4.name
text4.dispersion_plot(
    ["citizens", "democracy", "freedom", "duties", "America"])


text3.name

set(text3)

sorted(set(text3))

len(set(text3))


from __future__ import division


len(text3) / len(set(text3))


text3.count("smote")


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(count, total):
    return 100 * count / total


lexical_diversity(text2)


x = text4.count('a')

percentage(x, len(text4))
