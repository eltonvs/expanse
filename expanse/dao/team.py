from ..models.database import MongoDatabase
from .generic import GenericDAO


class TeamDAO(GenericDAO):
    """Team Data Access Object implementing Borg Pattern"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, team):
        team_to_insert = {
            "name": team.name,
            "lines": team.lines,
            "team_manager_id": team.team_manager.user_id,
        }
        self.db.teams.insert(team_to_insert)

        return{}

    def remove(self, user):
        print("Not implemented yet")
        pass

    def update(self, user):
        print("Not implemented yet")
        pass

    def get(self, search):
        teams = list(self.db.teams.find(search))
        return teams

    def list(self):
        teams = list(self.db.teams.find())
        return teams


class TeamManagerDAO(GenericDAO):
    """Team Data Access Object implementing Borg Pattern"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, team):
        print("Not implemented yet")
        pass
        '''
        team_manager_to_insert = {
            "username": team_manager.username,
            "name": team_manager.name,
            "password": team_manager.password,
            "email": team_manager.email,
            "locale": team_manager.locale,
            "teams": team_manager.teams,
        }
        self.db.teams.insert(team_manager_to_insert)
        '''

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
