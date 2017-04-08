from abc import ABCMeta

from .generic import GenericDAO
from ..models.database import MongoDatabase
from ..models.team import Team
from ..dao.user import UserDAOMongo


class TeamDAO(GenericDAO):
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

    def remove(self, user):
        print("Not implemented yet")
        pass

    def update(self, query, update):
        print(query, update, self.db.teams.update(query, update))

    def get(self, query):
        teams = list(self.db.teams.find(query))
        if teams:
            teams_list = []
            user_dao = UserDAOMongo()
            for t in teams:
                team_manager = user_dao.get_one({"_id": t["team_manager_id"]})
                team = Team(t['name'], team_manager)
                team.id = t['_id']
                team.lines = t['lines']
                teams_list.append(team)
            return teams_list
        return []

    def get_one(self, query):
        team = self.db.teams.find_one(query)
        if team:
            team_obj = Team(
                team['name'],
                team['team_manager_id'])
            team_obj.id = team['_id']
            team_obj.lines = team['lines']
            return team_obj

    def list(self):
        return self.get({})
