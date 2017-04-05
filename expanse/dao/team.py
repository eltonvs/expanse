from abc import ABCMeta, abstractmethod

from ..models.database import MongoDatabase
from .generic import GenericDAO
from ..models.team import Team


class TeamDAO(GenericDAO):
    __metaclass__ = ABCMeta

class TeamManagerDAO(GenericDAO):
    __metaclass__ = ABCMeta

class TeamDAOMongo(TeamDAO):
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

    def update(self, query, update):
        print query, update, self.db.teams.update(query, update)

    def get(self, query):
        teams = list(self.db.teams.find(query))
        return teams

    def get_one(self, query):
        team = self.db.teams.find_one(query)
        if team:
            new_team = Team(
                team['name'],
                team['team_manager_id'])
            new_team.lines = team['lines']
            return new_team

    def list(self):
        return self.get({})


class TeamManagerDAOMongo(TeamManagerDAO):
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

    def get_one(self, user):
        print("Not implemented yet")
        pass 

    def list(self):
        return self.get({})
