#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import string
import pandas as pd
import math
from __future__ import print_function

# turn of data table rendering
pd.set_option('display.notebook_repr_html', False)
sys.version

# ## What is TF-IDF?
# Computer systems are great with numbers, but not so much with textual data. If we want to perform calculations on words, [n-grams](http://en.wikipedia.org/wiki/N-gram), sentences or whole catalogs, we need to somehow convert these into numbers. Term Frequency – Inverse Document Frequency ([TF-IDF](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)) does just that. A TF-IDF score is a numerical representation of how important a word is to a document in a [text corpus](http://en.wikipedia.org/wiki/Text_corpus) (collection). It effectively lowers the weight of stopwords in favor of words that are much more meaningful in describing the document.
# 
# The **TF score** of a word is the number of times the term $t$ appears in a document $d$ divided by the total number of words $w$ in the document:
# 
# $$
# tf_{(t,d)}=\frac{f_d(t)}{\max\limits_{w\in d}f_d(w)}
# $$
# 
# The **IDF score** is the log of the number of documents $D$ (corpus) divided by the number of documents $d$ that contain term $t$. We take the log to emphasise the importance of non-common terms. These are describing terms occurring only in some of the documents in the corpus. 
# 
# $$
# idf_{(t,D)}=\log\Bigg({\frac{|D|}{|\{d\in D:t\in d\}|}}\Bigg)
# $$
# 
# The **TF-IDF** score is the multiplication of the TF and the IDF score:
# 
# $$
# tfidf_{(t, d, D)}=tf_{(t,d)}\cdot idf_{(t,D)}
# $$
# 

# ## Simple Example
# In the example below we calculate the TF-IDF scores of the words in a corpus of three documents with nine words each (for simplicity).

# In[2]:


# Corpus of three documents
doc1 = 'The man bought a pair of shoes while on a holiday in French'
doc2 = 'A young girl went on a short holiday to the islands'
doc3 = 'The man and the girl formed a nice young couple'

doc1 = doc1.lower().split()
doc2 = doc2.lower().split()
doc3 = doc3.lower().split()
print(doc1)

# ## Term Frequency
# First we focus on each document separately. Count the number of times a word appears in the text. Normalize the scores for each word in the dictionary by dividing by the total number of words in the document.

# In[3]:


# Calculate Term Frequency for a document
def tf(doc):
    result = {}
    doc_size = len(doc)
    
    for term in doc:
        if term in result:
            result[term] += 1
        else:
            result[term] = 1
    
    for term in result:
        result[term] = result[term] / doc_size
        
    return result

tf_doc1 = tf(doc1)
tf_doc2 = tf(doc2)
tf_doc3 = tf(doc3)
tf_doc1

# The term 'a' has the highest frequency of 0.15 in document 1 because it appears twice.

# ## Inverse Document Frequency
# Calculate the Inverse Document Frequency for each word in each document. We do this by dividing the size of the document corpus by the number of documents containing the term.

# In[4]:


def idf(doc, corpus):
    result = {}
    corpus_size = len(corpus)
    words_done = []
    
    for term in doc:
        if term in words_done:
            continue

        for corpus_doc in corpus:
            if term in corpus_doc:
                if term in result:
                    result[term] += 1
                else:
                    result[term] = 1

            words_done.append(term)

    for term in result:
        result[term] = math.log10(corpus_size / result[term])

    return result
        
idf_doc1 = idf(doc1, [doc1, doc2, doc3])
idf_doc2 = idf(doc2, [doc1, doc2, doc3])
idf_doc3 = idf(doc3, [doc1, doc2, doc3])
idf_doc1

# The term 'a' and 'the' have a IDF score of zero, because they appear in each document. The term 'shoes', however, has a much higher score, since it only appears in one document in the corpus.

# ## TF-IDF Scores for each Document
# By multiplying the TF and IDF we get a score for each word relative to the document *and* the corpus. The higher the score, the higher the importance of the word.

# In[5]:


def tf_idf(tf, idf):
    result = {}
    
    for term in tf:
        result[term] = idf[term] * tf[term]
    
    return result

tf_idf(tf_doc1, idf_doc1)

# We see that doc1 is mostly about shoes, French, bought, pair. Note that stopwords like 'in' and 'on' would be filtered out in a real-world corpus with scores close to zero.

# In[6]:


tf_idf(tf_doc2, idf_doc2)

# When we look at doc2, we see it's about short, went, islands.

# In[7]:


tf_idf(tf_doc3, idf_doc3)

# Finally doc3 is about nice, couple and formed.
