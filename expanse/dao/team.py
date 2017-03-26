from ..models.database import MongoDatabase
from .generic import GenericDAO


class TeamDAO():
    __metaclass__ = ABCMeta

    @abstractmethod
    def insertTeam(self, user):
        pass

    @abstractmethod
    def removeTeam(self, user):
        pass

    @abstractmethod
    def updateTeam(self, user):
        pass

    @abstractmethod
    def getTeam(self, user):
        pass

    @abstractmethod
    def listTeams(self, user):
        pass

class TeamDAOMongo(TeamDAO):
    """Team Data Access Object implementing Borg Pattern"""
    __shared_state = {}

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

    def listTeams(self):
        teams = list(self.db.teams.find())
        return teams
