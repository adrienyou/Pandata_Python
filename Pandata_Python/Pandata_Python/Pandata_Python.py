"""
@authors: YOU
"""

import MongoManager
import TwitterManager
import Constants
import pymongo

if __name__ == '__main__':

    if(not Constants.AbstractConstants.EXISTING_COLL):
        # Connect to the default host and port. Can be specified : MongoClient('localhost', 27017)
        client = pymongo.MongoClient()

        # Create the default document structure in which the tweets will be uploaded
        doc = MongoManager.createDefaultDoc(Constants.Database.COLL_ID, Constants.Database.COLL_USER_ID, Constants.Database.COLL_NAME, Constants.Database.DURATION, Constants.Database.WORDS)

        # Create a new research collection (and the database if it's the first time)
        MongoManager.createNewResearchColl(doc, Constants.Database.COLL_NAME, Constants.Database.DB_NAME, client)
    
        # Disconnect this client because we're using an other one in on_success
        client.disconnect()

    # Create the stream with a filter on the following tracks
    #streamer = TwitterManager.TweetStreamer(Constants.Connexion.CONSUMER_KEY, Constants.Connexion.CONSUMER_SECRET, Constants.Connexion.ACCESS_TOKEN_KEY, Constants.Connexion.ACCESS_TOKEN_SECRET)
    #streamer.statuses.filter(track = Constants.Stream.TRACK, language = Constants.Stream.LANG)
    
    

