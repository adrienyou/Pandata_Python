"""
@authors: YOU
"""
class AbstractConstants:
    POSITIVE = "pos"
    NEGATIVE = "neg"
    NEUTRAL = "neu"
    EXISTING_COLL = True

class Connexion:
    """Contains the connexion constants, such as access_token key/secret and consumer key/secret """

    ACCESS_TOKEN_KEY = "2962133872-eO1UD26mhgdjr4h01IWZaLwgR7RphGQvIY0z3rC"
    ACCESS_TOKEN_SECRET = "EP0Kyo8beg1hYIcp6UU4KyPvFbxlQjhfVh8vE4qImThr2"
    CONSUMER_KEY = "lVla8b4EftXbhuR3cHCnI3KZv"
    CONSUMER_SECRET = "w5qwgBYkhFa6z8Z146wVrPDLxQ6JJRFBhTzK73CevVhWXVuliU"


class Database:
    """Contains the Database constants, such as db_name, collection_name"""

    #DB_NAME = "Researches"
    DB_NAME = "dbtest2"
    COLL_ID = 1
    COLL_USER_ID = 1
    COLL_NAME = "colltest2"
    DURATION = 3
    WORDS = ["samsung", "apple"]

class ResearchField:
    """Contains the Research constants, such as _id, user_id..."""

    _ID = '_id'
    USER_ID = 'user_id'
    NAME = 'name'
    DURATION = 'duration'
    POSDICTIO = 'positive_dictio'
    NEGDICTIO = 'negative_dictio'
    WORDS = 'words'
    EMOTION = 'emotion'
    POSEMO = 'positive_emotion'
    NEGEMO = 'negative_emotion'
    NEUEMO = 'neutral_emotion'
    SIZE = 'size'
    TWEETS = 'tweets'

class Stream:
    """Contains the Stream parameters"""
    TRACK = 'samsung, apple'
    LANG = 'en, fr'

class TwitterField:
    """Contains the Twitter fields used """

    CREATED = "created_at"
    ENTITIES = "entities"
    HASHTAGS = "hashtags"
    SYMBOLS = "symbols"
    FAVORITED = "favorited"
    LANG = "lang"
    PLACE = "place" 
    RETWEET = "retweet_count"
    TEXT = "text"
    USER = "user"