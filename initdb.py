from pymongo import MongoClient
from expanse.utils.security import SecurityTools


security_tools = SecurityTools()
client = MongoClient()
client.drop_database('expanse_csgo')

db = client.expanse_csgo

users = db.users
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

games = db.games
games.insert({
    "name": "Counter Strike Global Offensive",
    "abbreviation": "CSGO",
    "steamid": "730",
})
