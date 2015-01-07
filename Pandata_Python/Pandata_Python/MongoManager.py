"""
@authors: YOU
"""

import pymongo
import Constants

# Create the default document structure in which the tweets will be uploaded
def createDefaultDoc(_id, user_id, name, duration, words):
    # Create doc
    doc = {}
    doc[Constants.ResearchField._ID] = _id
    doc[Constants.ResearchField.USER_ID] = user_id
    doc[Constants.ResearchField.NAME] = name
    doc[Constants.ResearchField.DURATION] = duration
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
    except:
        print("Unexpected error:", sys.exc_info())

# Modify the macro data
def modifyMacroInCollection(tweet, coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]
    try:
        # Add one to the size
        collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {"size" : 1}})

        if(getTextEmotion(tweet) == Constants.AbstractConstants.POSITIVE):
            # Positive emotion
            collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {"positive_emotion" : 1}})
        
        elif(getTextEmotion(tweet) == Constants.AbstractConstants.NEGATIVE):
            # Negative emotion
            collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {"negative_emotion" : 1}})
        
        else: 
            # Neutral emotion
            collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {"neutral_emotion" : 1}})
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
