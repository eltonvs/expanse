from pymongo import MongoClient


client = MongoClient()
db = client.expanse
users = db.users
users.drop()
users.insert_many([
    {
        "name": "Administrator",
        "username": "admin",
        "email": "admin@example.com",
        "password": "admin",
        "locale": "Locale"
    },
    {
        "name": "User",
        "username": "user",
        "email": "user@example.com",
        "password": "user",
        "locale": "Locale"
    }
])
print users.inserted_ids
