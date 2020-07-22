# external modules
import pymongo

# files
from shared.singleton_meta import Singleton


class DBClient(metaclass=Singleton):
    connection = None

    def connect(self, mongodb_url):
        if self.connection is None:
            connection = pymongo.MongoClient(mongodb_url)
            self.database = connection.get_database('')
        return self.connection

    def get_collection(self, name):
        return self.database[name]
