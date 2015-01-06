"""
@authors: YOU
"""

import pymongo

# Create a database
def createDatabase(db_name, client):
    db = client[db_name]
    print("Creating database : " + db_name)

# Create a collection in a given database and a client
def createCollection(coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]
    print("Creating collection : " + coll_name)

# Insert a document in a given collection in a database and a client
def insertDocInCollection(doc, coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]
    try:
        collection.insert(doc)
    except:
        print("Unexpected error:", sys.exc_info())

