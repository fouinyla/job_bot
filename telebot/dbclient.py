import pymongo
import sqlite3


class DBClient:
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if DBClient.__instance == None:
           DBClient()
        return DBClient.__instance

    def __init__(self, mongodb_url):
        client = pymongo.MongoClient(mongodb_url)
        self.db = client.get_database('job_bot')
        """ Virtually private constructor. """
        if DBClient.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DBClient.__instance = self

    def find_user(self, id):
        users = self.db.users
        user = users.find_one({
            "id": id
        })

        return user is not None

    def create_user(self, id, first_name, last_name):
        users = self.db.users
        users.insert_one({
            "id": id,
            "firstName": first_name,
            "lastName": last_name
        })

s = DBClient()
print(s)

s = DBClient.getInstance()
print(s)

s = DBClient.getInstance()
print(s)
