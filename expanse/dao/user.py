import re
from abc import ABCMeta, abstractmethod

from framework import GenericDAO

from ..models import MongoDatabase, User


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
        return self.db.users.insert(user_to_insert)

    def remove(self, query):
        self.db.users.remove(query)

    def update(self, query, update):
        self.db.users.update(query, update)

    def get(self, query):
        users = list(self.db.users.find(query))
        if users:
            user_list = []
            for u in users:
                user = User(
                    u.get('name', ''),
                    u.get('username', ''),
                    u.get('email', ''),
                    u.get('password', ''),
                    u.get('locale', '')
                )
                user.id = u.get('_id', '')
                user_list.append(user)
            return user_list
        return []

    def get_one(self, query):
        user = self.db.users.find_one(query)
        if user:
            user_obj = User(
                user.get('name', ''),
                user.get('username', ''),
                user.get('email', ''),
                user.get('password', ''),
                user.get('locale', '')
            )
            user_obj.id = user.get('_id', '')
            return user_obj

    def get_user_from_email(self, email):
        return self.get_one({"email": email})

    def get_user_id_from_email(self, email):
        user = self.get_one({"email": email})
        if user:
            return user.id

    def get_users_from_locale(self, locale):
        return self.get({"locale": re.compile(locale, re.IGNORECASE)})

    def list(self):
        return self.get({})
