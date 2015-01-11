"""
@authors: YOU
"""

import Constants
import re

positive_words = open('positive_words', 'r').read()
positive_wordsList=(list(positive_words.split()))
negative_words = open('negative_words', 'r').read()
negative_wordsList=(list(negative_words.split()))

def getTextEmotion(tweet):

    text = tweet['text']
    words = re.findall(r"[\w']+", text)
    count = 0

    for i in words:
        if i in positive_wordsList:
            count = count + 1
        elif i in negative_wordsList: 
            count = count - 1
    
    print(count)
    if count > 0:
        return Constants.AbstractConstants.POSITIVE
    elif count < 0:
        return Constants.AbstractConstants.NEGATIVE
    else:
        return Constants.AbstractConstants.NEUTRAL
