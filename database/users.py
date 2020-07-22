# external modules
import pymongo

# files
from database.dbclient import DBClient


class Users:
    def __init__(self):
        self.users = DBClient().get_collection('users')

    def find_user(self, id):
        user = self.users.find_one({
            "id": id
        })

        return user is not None

    def create_user(self, id, first_name, last_name):
        result = self.users.insert_one({
            "id": id,
            "firstName": first_name,
            "lastName": last_name
        })

        return result is not None
