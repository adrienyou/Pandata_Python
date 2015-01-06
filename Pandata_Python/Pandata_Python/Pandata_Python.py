"""
@authors: YOU
"""

import MongoManager
import TwitterManager
import Constants


consumer_key = Constants.Connexion.CONSUMER_KEY
consumer_secret = Constants.Connexion.CONSUMER_SECRET
access_token = Constants.Connexion.ACCESS_TOKEN_KEY
access_token_secret = Constants.Connexion.ACCESS_TOKEN_SECRET

if __name__ == '__main__':

    # Connect to the default host and port. Can be specified : MongoClient('localhost', 27017)
    #client = pymongo.MongoClient()
    
    # Create the stream with a filter on the following tracks
    streamer = TwitterManager.TweetStreamer(consumer_key, consumer_secret, access_token, access_token_secret)
    streamer.statuses.filter(track = 'samsung, apple', language = 'en, fr')
    
    

