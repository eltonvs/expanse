import abc

from pymongo import MongoClient
from expanse.design_pattern.patterns import Singleton

class UserDAO():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def insertUser(self, user):
        return

    @abc.abstractmethod
    def removeUser(self, user):
        return

    @abc.abstractmethod
    def updateUser(self, user):
        return

    @abc.abstractmethod
    def getUser(self, user):
        return

    @abc.abstractmethod
    def listUsers(self, user):
        return


class UserDAOMongo(Singleton, UserDAO):

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
        return True

    def removeUser(self, user):
        print "Not implemented yet"
        return

    def updateUser(self, user):
        print "Not implemented yet"
        return

    def getUser(self, user):
        print "Not implemented yet"
        return

    def listUsers(self, user):
        print "Not implemented yet"
        return
