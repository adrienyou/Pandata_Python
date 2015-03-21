"""
@authors: YOU
"""

import MongoManager
import TwitterManager
import Constants
import Variables
import pymongo

if __name__ == '__main__':

    if(not Variables.Database.EXISTING_RESEARCH):
        # Connect to the default host and port. Can be specified : MongoClient('localhost', 27017)
        client = pymongo.MongoClient()

        # Create the default document structure in which the tweets will be uploaded
        doc = MongoManager.createDefaultDoc(Variables.Database.RESEARCH_PYTHON_ID, Variables.Database.RESEARCH_USER_ID, Variables.Database.RESEARCH_TITLE, Variables.Database.RESEARCH_DESC, Variables.Database.DURATION, Variables.Database.WORDS)

        # Create a new research collection (and the database if it's the first time) and insert the doc into it
        MongoManager.createNewResearchColl(doc, Variables.Database.COLL_NAME, Variables.Database.DB_NAME, client)
    
        # Disconnect this client because we're using an other one in on_success
        client.disconnect()

    # Create the stream with the different Twitter keys/access tokens
    streamer = TwitterManager.TweetStreamer(Constants.Connexion.CONSUMER_KEY, Constants.Connexion.CONSUMER_SECRET, Constants.Connexion.ACCESS_TOKEN_KEY, Constants.Connexion.ACCESS_TOKEN_SECRET)
    # Add a filter to the stream, about the track to keep (words) and the language
    streamer.statuses.filter(track = Variables.Database.TRACK, language = Constants.Stream.LANG)


    
    

