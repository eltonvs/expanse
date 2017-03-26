from abc import ABCMeta, abstractmethod
from ..models.database import MongoDatabase


class UserDAO():
    __metaclass__ = ABCMeta

    @abstractmethod
    def insertUser(self, user):
        pass

    @abstractmethod
    def removeUser(self, user):
        pass

    @abstractmethod
    def updateUser(self, user):
        pass

    @abstractmethod
    def getUser(self, user):
        pass

    @abstractmethod
    def listUsers(self, user):
        pass


class UserDAOMongo(UserDAO):
    """User Data Access Object implementing Borg Pattern"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

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
        users = list(self.db.users.find())
        return users
