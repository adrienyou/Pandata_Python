"""
@authors: YOU
"""

import Constants
import re

positive_words = open('positive_words', 'r').read()
positive_wordsList= (list(positive_words.split()))
negative_words = open('negative_words', 'r').read()
negative_wordsList= (list(negative_words.split()))

def getTextEmotion(tweet):

    response = {}
    response[Constants.AbstractConstants.POSITIVE] = dict()
    response[Constants.AbstractConstants.NEGATIVE] = dict()

    text = tweet['text']
    words = re.findall(r"[\w']+", text)
    count = 0

    for i in words:
        if i in positive_wordsList:
            count = count + 1
            if(i in response[Constants.AbstractConstants.POSITIVE]):
                actualsize = response[Constants.AbstractConstants.POSITIVE][i]
                response[Constants.AbstractConstants.POSITIVE][i] = actualsize + 1
            else:
                response[Constants.AbstractConstants.POSITIVE][i] = 1
        elif i in negative_wordsList: 
            count = count - 1
            if(i in response[Constants.AbstractConstants.NEGATIVE]):
                actualsize = response[Constants.AbstractConstants.NEGATIVE][i]
                response[Constants.AbstractConstants.NEGATIVE][i] = actualsize + 1
            else:
                response[Constants.AbstractConstants.NEGATIVE][i] = 1
    
    # print(count)
    if count > 0:
        response[Constants.ResearchField.EMOTION] = Constants.AbstractConstants.POSITIVE
    elif count < 0:
        response[Constants.ResearchField.EMOTION] = Constants.AbstractConstants.NEGATIVE
    else:
        response[Constants.ResearchField.EMOTION] = Constants.AbstractConstants.NEUTRAL
    return response
