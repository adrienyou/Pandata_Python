import TwitterManager
import TextAnalysis
import MongoManager
import pymongo
import Constants

""" Use this command line in shell (not mongo shell) """
# mongoexport --db tester --collection tester --out F:\Projects\Pandata_Python\Pandata_Python\Pandata_Python\tester.json

# Test the TextAnalysis.getEmotion(tweet) ||| Success
def test_A():
    print("Starting test...")

    tweetPos = {}
    tweetPos[Constants.TwitterField.TEXT] = 'abounds abundance abominably'
    responsePos = {} 
    responsePos[Constants.AbstractConstants.POSITIVE] = dict()
    responsePos[Constants.AbstractConstants.NEGATIVE] = dict()       
    responsePos[Constants.AbstractConstants.POSITIVE]['abounds'] = 1
    responsePos[Constants.AbstractConstants.POSITIVE]['abundance'] = 1
    responsePos[Constants.AbstractConstants.NEGATIVE]['abominably'] = 1
    responsePos[Constants.ResearchField.EMOTION] = Constants.AbstractConstants.POSITIVE

    if(TextAnalysis.getTextEmotion(tweetPos) == responsePos):
        print("Test Positif OK")

    tweetNeg = {}
    tweetNeg[Constants.TwitterField.TEXT] = 'abounds abundance abolish abominable abominably'
    responseNeg = {} 
    responseNeg[Constants.AbstractConstants.POSITIVE] = dict()
    responseNeg[Constants.AbstractConstants.NEGATIVE] = dict()
        
    responseNeg[Constants.AbstractConstants.POSITIVE]['abounds'] = 1
    responseNeg[Constants.AbstractConstants.POSITIVE]['abundance'] = 1
    responseNeg[Constants.AbstractConstants.NEGATIVE]['abolish'] = 1
    responseNeg[Constants.AbstractConstants.NEGATIVE]['abominable'] = 1
    responseNeg[Constants.AbstractConstants.NEGATIVE]['abominably'] = 1
    responseNeg[Constants.ResearchField.EMOTION] = Constants.AbstractConstants.NEGATIVE

    if(TextAnalysis.getTextEmotion(tweetNeg) == responseNeg):
        print("Test Negatif OK")

    tweetNeu = {}
    tweetNeu[Constants.TwitterField.TEXT] = 'abounds abundance abominable abominably'
    responseNeu = {} 
    responseNeu[Constants.AbstractConstants.POSITIVE] = dict()
    responseNeu[Constants.AbstractConstants.NEGATIVE] = dict()

    responseNeu[Constants.AbstractConstants.POSITIVE]['abounds'] = 1
    responseNeu[Constants.AbstractConstants.POSITIVE]['abundance'] = 1
    responseNeu[Constants.AbstractConstants.NEGATIVE]['abominable'] = 1
    responseNeu[Constants.AbstractConstants.NEGATIVE]['abominably'] = 1
    responseNeu[Constants.ResearchField.EMOTION] = Constants.AbstractConstants.NEUTRAL

    if(TextAnalysis.getTextEmotion(tweetNeu) == responseNeu):
        print("Test Neutral OK")
    
    print("Ending test...")

# Test the creation of a database, a collection and the creation & insertion of a default document in this database + method TwitterManager.to_JSON(doc) ||| Success
def test_B():
    print("Starting test...")

    client = pymongo.MongoClient()
    print("Opened MongoClient")

    client.drop_database(Constants.Test.DB_NAME)
    print("Dropped database: " + Constants.Test.DB_NAME)

    doc = MongoManager.createDefaultDoc(Constants.Test.COLL_ID, Constants.Test.COLL_USER_ID, Constants.Test.COLL_NAME, Constants.Test.DURATION, Constants.Test.WORDS)
    print("Created Default Document: " + TwitterManager.to_JSON(doc))

    MongoManager.createNewResearchColl(doc, Constants.Test.COLL_NAME, Constants.Test.DB_NAME, client)
    print("Inserted doc in collection: " + Constants.Test.COLL_NAME + " in database: " + Constants.Test.DB_NAME)

    client.disconnect()
    print("Client disconnect")

    print("Ending test...")

# Test the insertion of a tweet in the tweet array when empty ||| Success
def test_C1():
    print("Starting test...")

    client = pymongo.MongoClient()
    print("Opened MongoClient")
    
    tweet = {}
    tweet['a'] = 'blabla'
    tweet['b'] = 'dookie'
    print("Created tweet:" + TwitterManager.to_JSON(tweet))

    MongoManager.insertTweetInCollection(tweet, Constants.Test.COLL_NAME, Constants.Test.DB_NAME, client)
    print("Inserted tweet in collection: " + Constants.Test.COLL_NAME + " in database: " + Constants.Test.DB_NAME)
    
    client.disconnect()
    print("Client disconnect")

    print("Ending test...")

# Test the insertion of a tweet in the tweet array when not empty ||| Success
def test_C2():
    print("Starting test...")

    client = pymongo.MongoClient()
    print("Opened MongoClient")
    
    tweet = {}
    tweet['c'] = 'wooolalalala azofda'
    tweet['trucbidule'] = 'muhahahaha'
    print("Created tweet:" + TwitterManager.to_JSON(tweet))

    MongoManager.insertTweetInCollection(tweet, Constants.Test.COLL_NAME, Constants.Test.DB_NAME, client)
    print("Inserted tweet in collection: " + Constants.Test.COLL_NAME + " in database: " + Constants.Test.DB_NAME)
    
    client.disconnect()
    print("Client disconnect")

    print("Ending test...")

# Test the incrementation of global variable, doesn't use functions, all hardcoded ||| Success => MongoManager.modifyMacro work
def test_D():
    print("Starting test...")

    client = pymongo.MongoClient()
    print("Opened MongoClient")

    db = client[Constants.Test.DB_NAME]
    collection = db[Constants.Test.COLL_NAME]
    collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {"size" : 111}})
    collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {Constants.ResearchField.POSEMO : 1}})
    collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {Constants.ResearchField.NEGEMO : 10}})
    collection.update({"_id" : Constants.Database.COLL_ID}, {"$inc": {Constants.ResearchField.NEUEMO : 100}})
    print("Increment size by 111, positive_emotion by 1, negative_emotion by 10 and neutral_emotion by 100")

    client.disconnect()
    print("Client disconnect")

    print("Ending test...")

# Test if inserting a word in the emotion dictionnary when empty ||| Success
def test_E1():
    print("Starting test...")

    client = pymongo.MongoClient()
    print("Opened MongoClient")

    db = client[Constants.Test.DB_NAME]
    collection = db[Constants.Test.COLL_NAME]
    print("Get collection: " + Constants.Test.COLL_NAME + " in database: " + Constants.Test.DB_NAME)
     
    dictPos = dict()
    dictPos["zippy"] = 5
    collection.update({"_id" : Constants.Database.COLL_ID, Constants.ResearchField.POSDICTIO : {"$elemMatch" : {"_id" : "zippy"}} }, 
                      {"$inc" : {Constants.ResearchField.POSDICTIO + ".$.count":  dictPos["zippy"]}})
    print("Update Positive Dictio")

    dictNeg = dict()
    dictNeg["abnormal"] = 7
    collection.update({"_id" : Constants.Database.COLL_ID, Constants.ResearchField.NEGDICTIO : {"$elemMatch" : {"_id" : "abnormal"}} }, 
                      {"$inc" : {Constants.ResearchField.NEGDICTIO + ".$.count":  dictNeg["abnormal"]}})
    print("Update Negative Dictio")

    client.disconnect()
    print("Client disconnect")

    print("Ending test...")

# Test if inserting a word in the emotion dictionnary when not empty ||| Success
def test_E2():
    print("Starting test...")

    client = pymongo.MongoClient()
    print("Opened MongoClient")

    db = client[Constants.Test.DB_NAME]
    collection = db[Constants.Test.COLL_NAME]
    print("Get collection: " + Constants.Test.COLL_NAME + " in database: " + Constants.Test.DB_NAME)
     
    dictPos = dict()
    dictPos["zippy"] = 100
    collection.update({"_id" : Constants.Database.COLL_ID, Constants.ResearchField.POSDICTIO : {"$elemMatch" : {"_id" : "zippy"}} }, 
                      {"$inc" : {Constants.ResearchField.POSDICTIO + ".$.count":  dictPos["zippy"]}})
    print("Update Positive Dictio")

    dictNeg = dict()
    dictNeg["abnormal"] = 57
    dictNeg["abolish"] = 12
    for i in dictNeg:
        collection.update({"_id" : Constants.Database.COLL_ID, Constants.ResearchField.NEGDICTIO : {"$elemMatch" : {"_id" : i}} }, 
                          {"$inc" : {Constants.ResearchField.NEGDICTIO + ".$.count":  dictNeg[i]}})
    print("Update Negative Dictio")

    client.disconnect()
    print("Client disconnect")

    print("Ending test...")
    
# Test the modifyMacroInCollection function ||| Success
def test_F():
    print("Starting test...")

    client = pymongo.MongoClient()
    print("Opened MongoClient")

    tweet = {}
    tweet[Constants.TwitterField.TEXT] = 'abounds abundance zippy abominably'
    print("Created Tweet")

    response = TextAnalysis.getTextEmotion(tweet)
    print("Get response of getTextEmotion")

    MongoManager.modifyMacroInCollection(response, Constants.Test.COLL_NAME, Constants.Test.DB_NAME, client)
    print("Modify Macro")

    client.disconnect()
    print("Client disconnect")

    print("Ending test...")

if __name__ == '__main__':
    #test_A()
    test_B()
    test_C1()
    test_C2()
    #test_D()
    #test_E1()
    #test_E2()
    #test_F()
