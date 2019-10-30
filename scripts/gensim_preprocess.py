#NLP
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *


def lemmatize_stemming(text):
    '''
    Create a new instance of a language specific subclass; here English
    '''
    stemmer = SnowballStemmer('english')
    #Lemmatize Single Word with the POS tag as VERB
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(text):
    '''
    gensim preprocess which processed documents split by whitespace, removes stopwords,
    strips numbers and multipel whitrspace, and short forms.
    tokens with less than 3 characters are removed.
    input: a list of tokens
    output: a list of tokens
    '''
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result
