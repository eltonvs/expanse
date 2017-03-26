import abc

from pymongo import MongoClient
from expanse.design_pattern.patterns import Singleton


class UserDAO():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def insertUser(self, user):
        pass

    @abc.abstractmethod
    def removeUser(self, user):
        pass

    @abc.abstractmethod
    def updateUser(self, user):
        pass

    @abc.abstractmethod
    def getUser(self, user):
        pass

    @abc.abstractmethod
    def listUsers(self, user):
        pass


class UserDAOMongo(Singleton, UserDAO):

    def __init__(self):
        client = MongoClient()
        db = client.expanse

        self.db = db

    def insertUser(self, user):
        user_to_insert = {
            "username": user.username,
            "name": user.name,
            "password": user.password,
            "email": user.email,
            "locale": user.locale,
        }
        self.db.users.insert(user_to_insert)

        return {}

    def removeUser(self, user):
        print("Not implemented yet")
        pass

    def updateUser(self, user):
        print("Not implemented yet")
        pass

    def getUser(self, user):
        print("Not implemented yet")
        pass

    def listUsers(self):
        users = list(self.db.users.find({}))

        return users
