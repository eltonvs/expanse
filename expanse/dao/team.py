from abc import ABCMeta

from ..models.database import MongoDatabase
from .generic import GenericDAO
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

        return{}

    def remove(self, user):
        print("Not implemented yet")
        pass

    def update(self, query, update):
        print(query, update, self.db.teams.update(query, update))

    def get(self, query):
        teams = list(self.db.teams.find(query))
        if teams:
            teams_list = []
            for team in teams:
                new_team = Team(
                    team['name'],
                    team['team_manager_id'])
                new_team.lines = team['lines']
                new_team.my_id = team['_id']
                teams_list.append(new_team)
            return teams_list

    def get_one(self, query):
        team = self.db.teams.find_one(query)
        if team:
            new_team = Team(
                team['name'],
                team['team_manager_id'])
            new_team.lines = team['lines']
            new_team.my_id = team['_id']
            return new_team

    def list(self):
        teams = list(self.db.teams.find())
        if teams:
            teams_list = []
            user_dao = UserDAOMongo()
            for team in teams:
                team_manager = user_dao.get_one(
                    {"_id": team["team_manager_id"]})
                new_team = Team(team['name'], team_manager)
                new_team.lines = team['lines']
                new_team.my_id = team['_id']
                teams_list.append(new_team)
            return teams_list
