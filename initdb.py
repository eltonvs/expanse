from pymongo import MongoClient


client = MongoClient()
db = client.expanse
users = db.users
users.drop()
users.insert_many([
    {
        "name": "Administrator",
        "username": "admin",
        "password": "admin"
    },
    {
        "name": "User",
        "username": "user",
        "password": "user"
    }
])
print users.inserted_ids
