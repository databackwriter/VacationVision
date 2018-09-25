from __future__ import division

import nltk
# nltk.download()

from nltk.book import *

##region earlu
#text1.concordance("algae")
#text1.similar("monstrous")
#text2.similar("monstrous")
#text4.name
#text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
#text3.name
#set(text3)
#sorted(set(text3))
#len(set(text3))
#len(text3) / len(set(text3))
#text3.count("smote")
#def lexical_diversity(text):
#    return len(text) / len(set(text))
#def mypercentage(count, total):
#    return (100 * count / total)
#lexical_diversity(text2)
#x = text4.count('a')
#mypercentage(x,len(text4))
##endregion early
#print(sent6)
#len(text6)
#text6.index("elderberries")
#text6[4982:4993]
#text6[-9:]
#saying = ['After', 'all', 'is', 'said', 'and', 'done',  'more', 'is', 'said', 'than', 'done']
#tokens = set(saying)
#tokens = sorted(tokens)
#tokens[-2:]



fdist1= FreqDist(text1)
vocabulary = list(fdist1.keys())
vocabulary[:5]
