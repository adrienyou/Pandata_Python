"""
@authors: YOU
"""


class Database:
    """Contains the Database constants, such as db_name and coll_name"""
    """Contains the Database varaibles, such as python_id, existing_coll and user_id"""

    DB_NAME = "mean-dev"
    COLL_NAME = "researches"
    RESEARCH_PYTHON_ID = 3 # Need to increment it everytime
    EXISTING_RESEARCH = False
    RESEARCH_USER_ID = "54689fc0b456057800046d6f" #{ "$oid" : "54689fc0b456057800046d6f" } 
    RESEARCH_TITLE = "Microsoft and Windows 10, research 2"
    RESEARCH_DESC = "This is a second research about Microsoft and Windows 10 over Twitter only"
    DURATION = 3
    WORDS = ["microsoft", "windows", "windows10"]