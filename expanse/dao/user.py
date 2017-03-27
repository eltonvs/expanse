from ..models.database import MongoDatabase
from .generic import GenericDAO


class UserDAO(GenericDAO):
    """User Data Access Object implementing Borg Pattern"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, user):
        user_to_insert = {
            "username": user.username,
            "name": user.name,
            "password": user.password,
            "email": user.email,
            "locale": user.locale,
        }
        self.db.users.insert(user_to_insert)

        return {}

    def remove(self, user):
        print("Not implemented yet")
        pass

    def update(self, user):
        print("Not implemented yet")
        pass

    def get(self, user):
        print("Not implemented yet")
        pass

    def get_user_from_email(self, email):
        user = self.db.users.find_one({"email": email})
        return user

    def list(self):
        users = list(self.db.users.find())
        return users
