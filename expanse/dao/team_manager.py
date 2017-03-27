from abc import ABCMeta, abstractmethod
from ..models.database import MongoDatabase


class TeamManagerDAO(GenericDAO):
    """Team Data Access Object implementing Borg Pattern"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, team):
        team_manager_to_insert = {
            "username": team_manager.username,
            "name": team_manager.name,
            "password": team_manager.password,
            "email": team_manager.email,
            "locale": team_manager.locale,
            "teams": team_manager.teams,
        }
        self.db.teams.insert(team_manager_to_insert)

        return{}


    def remove(self, user):
        print("Not implemented yet")
        pass

    def update(self, user):
        print("Not implemented yet")
        pass

    def get(self, user):
        print("Not implemented yet")
        pass

    def list(self):
        team_managers = list(self.db.team_managers.find())
        return team_managers
