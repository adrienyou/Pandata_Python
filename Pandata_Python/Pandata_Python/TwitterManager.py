"""
@authors: YOU
"""

from twython import TwythonStreamer
import json
import pymongo
import Constants
import MongoManager
import TextAnalysis

class TweetStreamer(TwythonStreamer):
    """ Method on_success will be called when tweets are received """
    def on_success(self, data):

        # Connect to the default host and port. Can be specified : MongoClient('localhost', 27017)
        client = pymongo.MongoClient()

        # Create the tweet under the format we want
        tweet = dataWorker(data)

        # Call the text analysis worker and get the response (dictPosWords, dictNegWords, emotion)
        response = TextAnalysis.getTextEmotion(tweet)

        # Add new field to tweet
        tweet[Constants.ResearchField.EMOTION] = response[Constants.ResearchField.EMOTION]

        # Insert the tweet ine the research collection we want
        MongoManager.insertTweetInCollection(tweet, Constants.Database.COLL_TITLE, Constants.Database.DB_NAME, client)
        
        # Modify the macro data with the response from emotion analysis
        MongoManager.modifyMacroInCollection(response, Constants.Database.COLL_TITLE, Constants.Database.DB_NAME, client)

    def on_error(self, status_code, data):
        print(status_code)

    # Want to stop trying to get data because of the error?
    # Uncomment the next line!
    # self.disconnect()


""" Worker applied to the data from the stream """
def dataWorker(data):
    tweet = createTweet(created_atWorker(data[Constants.TwitterField.CREATED].encode('utf-8')), 
                  entitiesWorker(data[Constants.TwitterField.ENTITIES][Constants.TwitterField.HASHTAGS], data[Constants.TwitterField.ENTITIES][Constants.TwitterField.SYMBOLS]), 
                  data[Constants.TwitterField.FAVORITED],
                  data[Constants.TwitterField.LANG],
                  placeWorker(data[Constants.TwitterField.PLACE]),
                  data[Constants.TwitterField.RETWEET],
                  data[Constants.TwitterField.TEXT].encode('utf-8'),
                  userWorker(data[Constants.TwitterField.USER])
                  )
    
    return tweet  

""" Return the month number """
def getMonth(strMonth):
    if strMonth == 'Jan':
        return "01"
    elif strMonth == 'Feb':
        return "02"
    elif strMonth == 'Mar':
        return "03"
    elif strMonth == 'Apr':
        return "04"
    elif strMonth == 'May':
        return "05"
    elif strMonth == 'Jun':
        return "06"
    elif strMonth == 'Jul':
        return "07"
    elif strMonth == 'Aug':
        return "08"
    elif strMonth == 'Sep':
        return "09"
    elif strMonth == 'Oct':
        return "10"
    elif strMonth == 'Nov':
        return "11"
    else:
        return "12"

""" Worker applied to the 'created_at' field from the data from the stream """
def created_atWorker(field):
    #"created_at":"Wed Aug 27 13:08:45 +0000 2008"
    strField = str(field, encoding='utf-8')
    arrField = strField.split(' ')

    date = {}
    date['hour'] = arrField[3].split(':')[0]
    date['day'] = arrField[2]
    date['month'] = getMonth(arrField[1])
    date['year'] =  arrField[5]
    
    return date  

""" Worker applied to the 'entites' field from the data from the stream """
def entitiesWorker(hashtagsField, symbolsField):
    hashList = []
    symbList = []
    for hash in hashtagsField:
        if hash['text']:
            hashList.append(hash['text'])
    for symb in symbolsField:
        if symb['text']:
            symbList.append(symb['text'])

    entities = {}
    entities['hashtags'] = hashList
    entities['symbols'] = symbList

    return entities
 
""" Worker applied to the place field from the data from the stream """   
def placeWorker(place):
    if place:
        if place['country']:
            return place['country']
        elif place['country_code']:
            return place['country_code']
        else:
            return 'null'
    else:
        return 'null'

""" Worker applied to the user field from the data from the stream """
def userWorker(user):
    userV = {}
    
    if user:
        if user['name']:
            userV['name'] = user['name']
        else:
            userV['name'] = 'null'
        
        if user['followers_count']:
            userV['followers_count'] = user['followers_count']
        else:
            userV['followers_count'] = 'null'
        
        if user['time_zone']:
            userV['time_zone'] = user['time_zone']
        else:
            userV['time_zone'] = 'null'

    return userV

def createTweet(v_created_at, v_entities, v_favorited, v_lang, v_place, v_retweet, v_text, v_user): 
    
    tweet = {}
    tweet['created_at'] = v_created_at
    tweet['entities'] = v_entities
    tweet['favorited'] = v_favorited
    tweet['lang'] = v_lang
    tweet['place'] = v_place
    tweet['retweet'] = v_retweet
    tweet['text'] = str(v_text, encoding='utf-8')
    tweet['user'] = v_user

    return tweet

""" Return obj with a JSON format """
def to_JSON(obj):
    return json.dumps(obj, sort_keys=True, indent=4)
