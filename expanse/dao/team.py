from ..models.database import MongoDatabase
from .generic import GenericDAO


class TeamDAO(GenericDAO):
    """Team Data Access Object implementing Borg Pattern"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, team):
        team_to_insert = {
            "name": team.name,
            "team_manager": team.team_manager,
            "lines":team.lines,
        }
        self.db.teams.insert(team_to_insert)

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

    def list(self, user):
        teams = list(self.db.teams.find())
        pass
