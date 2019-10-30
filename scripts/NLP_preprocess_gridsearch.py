# Importing modules

import pandas as pd
import numpy as np
import time
import re
from pprint import pprint
import joblib

#NLP
import sklearn
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

#plotting
import matplotlib.pyplot as plt
import pyLDAvis
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()
import matplotlib.pyplot as plt





def get_wordnet_pos(word):
    '''
    tags parts of speech to tokens
    Expects a string and outputs the string and its part of speech
    '''

    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def word_lemmatizer(text):
    '''
    lemamtizes the tokens based on their part of speech
    Expects a lits of tokens and outputs a list of lemmatized tokens
    '''

    lemmatizer = WordNetLemmatizer()
    text = lemmatizer.lemmatize(text, get_wordnet_pos(text))
    return text

def get_stopwords():
    stop_words = stopwords.words('english')
    stop_words.extend(['mr', 'mrs', 'miss', 'ms', 'ahh', 'ah', 'want', 'feel', 'want', 'goal', 'ela', 'go', 'get', 'like','grade', 'use', 'make',
                  'next', 'well', 'lea', 'also', 'thing', 'one', 'try', 'end', 'turn', 'work', 'math', 'try', 'sol', 'science','week', 'would',
                 'class', 'need', 'exit', 'ticket', 'sure', 'strategy', 'exit','grade', 'good', 'best', 'able', 'lot', 'think', 'help',
                'could', 'really', 'improve', 'time'])
    return stop_words


def reflection_tokenizer(text):
    '''
    Tokenizes a list of string, expects a list of strings and outputs a list of strings.
    before tokenizing:
    1)removes the non-alphanumeric charcaters like emojies
    2)removes the numbers
    3)lower cases the words
    4)tokenizes the sentences
    5)lemmatizes teh tokens
    6)removes the tokens in stop words list
     '''

    text=re.sub(r'[\W_]+', ' ', text) #keeps just alphnumeric characters
    text=re.sub(r'\d+', '', text) #removes numbers
    text = text.lower()
    tokens = [word for word in word_tokenize(text)]
    tokens = [word for word in tokens if len(word) >= 3]#removes smaller than 3 character
    tokens = [word_lemmatizer(w) for w in tokens]
    tokens = [s for s in tokens if s not in get_stopwords()]
    return tokens
