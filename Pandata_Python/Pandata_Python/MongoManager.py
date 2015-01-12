"""
@authors: YOU
"""

import pymongo
import Constants
import TextAnalysis
import sys

# Create the default document structure in which the tweets will be uploaded
def createDefaultDoc(_id, user_id, name, duration, words):
    # Create doc
    doc = {}
    doc[Constants.ResearchField._ID] = _id
    doc[Constants.ResearchField.USER_ID] = user_id
    doc[Constants.ResearchField.NAME] = name
    doc[Constants.ResearchField.DURATION] = duration
    doc[Constants.ResearchField.POSDICTIO] = []
    doc[Constants.ResearchField.NEGDICTIO] = []
    doc[Constants.ResearchField.WORDS] = words
    doc[Constants.ResearchField.POSEMO] = 0
    doc[Constants.ResearchField.NEGEMO] = 0
    doc[Constants.ResearchField.NEUEMO] = 0
    doc[Constants.ResearchField.SIZE] = 0
    # Create the tweets field
    doc[Constants.ResearchField.TWEETS] = []

    return doc

# Create new research
def createNewResearchColl(doc, coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]
    try:
        collection.insert(doc)
    except:
        print("Unexpected error:", sys.exc_info())

# Insert a tweet in a given collection with a databasse and a client
def insertTweetInCollection(tweet, coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]
    try:
        collection.update({"_id" : Constants.Database.COLL_ID}, {"$push": {"tweets" : tweet}})
        print('Tweet inserted')
    except:
        print("Unexpected error:", sys.exc_info())

# Modify the macro data
def modifyMacroInCollection(response, coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]
   
    dictPos = response[Constants.AbstractConstants.POSITIVE]
    dictNeg = response[Constants.AbstractConstants.NEGATIVE]
    emotion = response[Constants.ResearchField.EMOTION]

    try:
        # Add one to the size
        collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {"size" : 1}})

        if(emotion == Constants.AbstractConstants.POSITIVE):
            # Positive emotion
            collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {Constants.ResearchField.POSEMO : 1}})
        
        elif(emotion == Constants.AbstractConstants.NEGATIVE):
            # Negative emotion
            collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {Constants.ResearchField.NEGEMO : 1}})
        
        elif(emotion == Constants.AbstractConstants.NEUTRAL): 
            # Neutral emotion
            collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {Constants.ResearchField.NEUEMO : 1}})

        # Add words to positive_dictio

        for word in dictPos:
            collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc" : {Constants.ResearchField.POSDICTIO + "." + word : dictPos[word]}})

        # Add words to negative_dictio
    except:
        print("Unexpected error:", sys.exc_info())


""" Not used """
# Create a database
def createDatabase(db_name, client):
    db = client[db_name]

# Create a collection in a given database and a client
def createCollection(coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]

# Insert a document in a given collection with a database and a client
def insertDocInCollection(doc, coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]
    try:
        collection.insert(doc)
    except:
        print("Unexpected error:", sys.exc_info())
