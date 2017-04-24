from pymongo import MongoClient
from expanse.utils.security import SecurityTools


security_tools = SecurityTools()
client = MongoClient()
db = client.expanse

users = db.users
users.drop()
users.insert_many([
    {
        "name": "Administrator",
        "username": "admin",
        "email": "admin@example.com",
        "password": security_tools.hash_password("admin"),
        "locale": "Locale"
    },
    {
        "name": "User",
        "username": "user",
        "email": "user@example.com",
        "password": security_tools.hash_password("user"),
        "locale": "Locale"
    }
])
print(users.inserted_ids)

# Insert games:
games = db.games
games.drop()
games.insert_many([
    {
        "name": "Counter Strike Global Offensive",
        "abbreviation": "CSGO",
        "steamid": "730",
    },
    {
        "name": "League of Legends",
        "abbreviation": "LOL",
    }
])