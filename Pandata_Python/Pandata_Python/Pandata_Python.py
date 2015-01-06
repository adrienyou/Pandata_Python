"""
@authors: YOU
"""

import MongoManager
import TwitterManager
import Constants
import pymongo


consumer_key = Constants.Connexion.CONSUMER_KEY
consumer_secret = Constants.Connexion.CONSUMER_SECRET
access_token = Constants.Connexion.ACCESS_TOKEN_KEY
access_token_secret = Constants.Connexion.ACCESS_TOKEN_SECRET

doc = {}
doc["_id"] = 1
doc["name"] = 'Adrien You'

if __name__ == '__main__':

    # Connect to the default host and port. Can be specified : MongoClient('localhost', 27017)
    client = pymongo.MongoClient()

    # Create db, coll et insert car si pas de docs, la db et la coll ne sont pas save
    MongoManager.createDatabase("premierTest" , client)
    MongoManager.createCollection("premierCollTest", "premierTest", client)
    MongoManager.insertDocInCollection(doc, "premierCollTest", "premierTest", client)
    
    # Create the stream with a filter on the following tracks
    #streamer = TwitterManager.TweetStreamer(consumer_key, consumer_secret, access_token, access_token_secret)
    #streamer.statuses.filter(track = 'samsung, apple', language = 'en, fr')
    
    

