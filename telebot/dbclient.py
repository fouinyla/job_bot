import pymongo


class DBClient:
    def __init__(self, mongodb_url):
        client = pymongo.MongoClient(mongodb_url)
        self.db = client.get_database('job_bot')

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
