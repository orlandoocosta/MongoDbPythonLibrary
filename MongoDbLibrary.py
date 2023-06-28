import pymongo
from robot.api.deco import library, keyword
import json


@library(scope="GLOBAL", version="0.0.1")
class MongoDbLibrary():
    """
    MongoDb Robot Framework library
    """

    def __init__(self) -> None:
        self.connection = None

    @keyword("Connecto to MongoDb")
    def connect_to_mongodb(self, conn_str: str) -> None:
        """
        Connect to MongoDb database with connection string.

        Example:
        | `Connect to MongoDb` | ${conn_str}
        """

        self.connection = pymongo.MongoClient(
            conn_str, serverSelectionTimeoutMS=5000)

        try:
            print("Connecton successfull")
        except Exception:
            print("Unable to connect to the server.")

    @keyword("Execute MongoDb Query")
    def execute_mongodb_query(self, db_name, collection_name, json_query):
       """
        Perform mongoDb query and return a list of records containing all query results based on the JSON entered.

        Example:
        | `Execute MongoDb Query` | ${json_query}
        """

       db = self.connection.get_database(db_name)
       collection = db.get_collection(collection_name)
       return collection.find_one(json_query)

    @keyword("Disconnecto from MongoDb")
    def diconnect_from_mongodb(self) -> None:
        """
        Disconnect from MongoDb database.

        Example:
        | `Disconnect from MongoDb` |
        """

        self.connection.close()
        print("Connection closed.")

