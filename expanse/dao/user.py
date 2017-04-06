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
        if users:
            user_list = []
            for usr in users:
                user = User(
                    usr['name'],
                    usr['username'],
                    usr['email'],
                    usr['password'],
                    usr['locale'])
                user.my_id = usr['_id']
                user_list.append(user)
            return user_list

    def get_one(self, query):
        usr = self.db.users.find_one(query)
        if usr:
            user = User(
                usr['name'],
                usr['username'],
                usr['email'],
                usr['password'],
                usr['locale'])
            user.my_id = usr['_id']
            return user

    def get_user_from_email(self, email):
        usr = self.db.users.find_one({"email": email})
        if usr:
            user = User(
                usr['name'],
                usr['username'],
                usr['email'],
                usr['password'],
                usr['locale'])
            user.my_id = usr['_id']
            return user

    def get_user_id_from_email(self, email):
        usr = self.db.users.find_one({"email": email})
        if usr:
            return usr['_id']

    def get_users_from_locale(self, location):
        users = list(self.db.users.find({"locale": location}))
        return users

    def list(self):
        return self.get({})
