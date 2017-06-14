from pymongo import MongoClient
from expanse.utils.security import SecurityTools


security_tools = SecurityTools()
client = MongoClient()
client.drop_database('expanse_soccer')

db = client.expanse_soccer

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
