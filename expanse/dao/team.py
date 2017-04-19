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
            "players": team.players,
            "team_manager_id": team.team_manager,
        }
        self.db.teams.insert(team_to_insert)

    def remove(self, user):
        self.db.teams.remove(query)

    def update(self, query, update):
        self.db.teams.update(query, update)

    def get(self, query):
        teams = list(self.db.teams.find(query))
        if teams:
            teams_list = []
            user_dao = UserDAOMongo()
            for t in teams:
                team_manager = user_dao.get_one({"_id": t["team_manager_id"]})
                team = Team(t['name'], team_manager)
                team.id = t.get('_id', '')
                team.lines = t.get('lines', [])
                team.players = t.get('players', [])
                teams_list.append(team)
            return teams_list
        return []

    def get_one(self, query):
        team = self.db.teams.find_one(query)
        if team:
            team_obj = Team(
                team.get('name', ''),
                team.get('team_manager_id', '')
            )
            team_obj.id = team.get('_id', '')
            team_obj.lines = team.get('lines', [])
            team_obj.players = team.get('players', [])
            return team_obj

    def list(self):
        return self.get({})
