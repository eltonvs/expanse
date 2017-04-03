from abc import ABCMeta, abstractmethod

from ..models.database import MongoDatabase
from ..models.user import User
from .generic import GenericDAO


class UserDAO(GenericDAO):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_user_from_email(self, email):
        pass

    @abstractmethod     
    def get_user_id_from_email(self, email):
        pass

class UserDAOMongo(UserDAO):
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

    def get(self, query):
        users = list(self.db.users.find(query))
        return users

    def get_one(self, query):
        user = self.db.users.find_one(query)
        return user

    def get_user_from_email(self, email):
        usr = self.db.users.find_one({"email": email})
        if usr is not None:
            user = User(
                usr['name'],
                usr['username'],
                usr['email'],
                usr['password'],
                usr['locale'])
            return user

    def get_user_id_from_email(self, email):
        usr = self.db.users.find_one({"email": email})
        if usr is not None:
            return usr['_id']

    def get_users_from_locale(self, location):
        users = list(self.db.users.find({"locale": location}))
        return users

    def list(self):
        return self.get({})
