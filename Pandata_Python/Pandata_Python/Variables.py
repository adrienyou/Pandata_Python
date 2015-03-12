"""
@authors: YOU
"""


class Database:
    """Contains the Database constants, such as db_name and coll_name"""
    """Contains the Database varaibles, such as python_id, existing_coll and user_id"""

    # Do not change this
    DB_NAME = "mean-dev"
    COLL_NAME = "researches"

    # Change this
    RESEARCH_PYTHON_ID = 2 # Need to increment it everytime
    # Put to true if the current stream failed and you want to start it again. Else, let it at false.
    EXISTING_RESEARCH = True
    RESEARCH_USER_ID = "54689fc0b456057800046d6f" #{ "$oid" : "54689fc0b456057800046d6f" } 
    RESEARCH_TITLE = "Barack Obama"
    RESEARCH_DESC = "This is a research about Barack Obama"
    DURATION = 3
    WORDS = ["obama", "barack", "barackobama"]