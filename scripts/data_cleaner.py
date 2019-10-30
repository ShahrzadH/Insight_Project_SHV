#Importing spell chacking and language detection packages
from enchant.checker import SpellChecker
from langdetect import detect
#importing necessary nltk packages
from nltk.tokenize import word_tokenize


def spell_check(text):       
    '''
    spell_check: function for correcting the spelling of the description
    Expects:  a string
    Returns: a list
    '''
    corr_descrip = []
    #Grab each individual description
    #for descrip in text.split():
    for descrip in text:
        #Check to see if the words are in the dictionary
        chkr = SpellChecker("en_US", descrip)
        for err in chkr:
            #for the identified errors or words not in dictionary get the suggested correction
            #and replace it in the description string
            if len(err.suggest()) > 0:
                sug = err.suggest()[0]
                err.replace(sug)
        corr_descrip.append(chkr.get_text())
        #return the dataframe with the new corrected description column
    #return ' '.join(corr_descrip)
    return corr_descrip


def lang_detect(text):
    '''
    lang_detect: function for detecting the languauge of the reflections
    Expects: a string
    Returns: a list of the detected languages
    '''
    lang = []
    for refl in text:
        lang.append(detect(refl))
    return lang


def word_count(text):
    '''
    word_count: function for counting the number of the words in the reflections
    Expects:  a string
    Returns: a list of words count in each reflection
    '''
    refl_wordcount = []
    for refl in text:
        refl_wordcount.append(len(word_tokenize(refl)))
    return refl_wordcount
