"""
@authors: YOU
"""

from twython import TwythonStreamer
import Constants
import json



class Tweet:
    """ Tweet class representing a tweet that will be inserted into the mongo collection """
    def __init__(self, v_created_at, v_entities, v_favorited, v_lang, v_place, v_retweet_count, v_text, v_user):
        self.created_at = v_created_at
        self.entities = v_entities  
        self.favorited = v_favorited
        self.lang = v_lang
        self.place = v_place
        self.retweet_count = v_retweet_count
        self.text = v_text
        self.user = v_user


class Date:
    """ Date class representing the created_at field for a tweet """
    def __init__(self, hour, day, month, year):
        self.h = hour
        self.d = day
        self.m = month
        self.y = year

class Entities:
    """ Entites class representing the entities field for a tweet """

    def __init__(self, hashList, symbList):
        self.hashtags = hashList
        self.symbols = symbList

class TweetStreamer(TwythonStreamer):
    """ Method on_success will be called when tweets are received """
    def on_success(self, data):
        #tweet = dataWorker(data)
        # Work with tweet
        if 'text' in data:
            #print(data[Constants.TwitterField.TEXT].encode('utf-8'))
            print(data[Constants.TwitterField.CREATED].encode('utf-8'))
            print(data[Constants.TwitterField.ENTITIES][Constants.TwitterField.HASHTAGS], flush = True)

    def on_error(self, status_code, data):
        print(status_code)

    # Want to stop trying to get data because of the error?
    # Uncomment the next line!
    # self.disconnect()


""" Worker applied to the data from the stream """
def dataWorker(data):
    tweet = Tweet(created_atWorker(data[Constants.TwitterField.CREATED].encode('utf-8')), 
                  entitiesWorker(data[Constants.TwitterField.ENTITIES][Constants.TwitterField.HASHTAGS], data[Constants.TwitterField.ENTITIES][Constants.TwitterField.SYMBOLS]), 
                  favoritedWorker(data[Constants.TwitterField.FAVORITED].encode('utf-8')),
                  langWorker(data[Constants.TwitterField.LANG].encode('utf-8')),
                  placeWorker(data[Constants.TwitterField.PLACE].encode('utf-8')),
                  retweetWorker(data[Constants.TwitterField.RETWEET].encode('utf-8')),
                  textWorker(data[Constants.TwitterField.TEXT].encode('utf-8')),
                  userWorker(data[Constants.TwitterField.USER].encode('utf-8'))
                  )
    
    return tweet  

""" Worker applied to the 'created_at' field from the data from the stream """
def created_atWorker(field):
    #"created_at":"Wed Aug 27 13:08:45 +0000 2008"
    arrField = field.split(' ')

    hour = arrField[3].split(':')[0]
    day = arrField[2]
    month = getMonth(arrField[1])
    year =  arrField[5]
    date = Date(hour, day, month, year)

    return date  

""" Worker applied to the 'entites' field from the data from the stream """
def entitiesWorker(hashtagsField, symbolsField):
    hashList = []
    symbList = []
    for hash in hastagsField:
        hashList.append.hash.text
    for symb in symbolsField:
        symbList.append.symb.text

    #TODO : use a set maybe

    entities = Entities(hashList, symbList)
    




""" Return obj with a JSON format """
def to_JSON(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)

""" Return the month number """
def getMonth(strMonth):
    if strMonth == Jan:
        return 1
    elif strMonth == Feb:
        return 2
    elif strMonth == Mar:
        return 3
    elif strMonth == Apr:
        return 4
    elif strMonth == May:
        return 5
    elif strMonth == Jun:
        return 6
    elif strMonth == Jul:
        return 7
    elif strMonth == Aug:
        return 8
    elif strMonth == Sep:
        return 9
    elif strMonth == Oct:
        return 10
    elif strMonth == Nov:
        return 11
    else:
        return 12