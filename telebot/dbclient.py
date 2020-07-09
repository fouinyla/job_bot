import pymongo

client = pymongo.MongoClient("mongodb+srv://ur-business-bot:Fiqm29frqKS@job-bot.5ex1b.mongodb.net/job_bot?retryWrites=true&w=majority")
db = client.get_database('job_bot')
users = db.users

user = {
    "name": "John",
    "age": 55
}

inserted_id = users.insert_one(user).inserted_id
print(users.count_documents({}))
print(inserted_id)