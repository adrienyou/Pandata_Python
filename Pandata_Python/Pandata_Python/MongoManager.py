"""
@authors: YOU
"""

import pymongo

# Insert a document in a given collection in a database and a client
def insertDocInCollection(doc, coll_name, db_name, client):
    db = client[db_name]
    collection = db[coll_name]
    try:
        collection.insert(doc)
    except:
        print("Unexpected error:", sys.exc_info())

