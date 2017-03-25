from pymongo import MongoClient

class UserDAO():
    def __init__(self):
        client = MongoClient()
        db = client.expanse

        self.db = db

    def insertUser(self, user):
        db = self.db

        user_to_insert = {
            "username": user.username,
            "name": user.name,
            "password": user.password,
            "email": user.email,
            "locale": user.locale,
        }

        print db.users.insert(user_to_insert)
