from framework import AbstractFactoryDAO

from .match import MatchDAOMongo
from .notification import NotificationDAOMongo
from .team import TeamDAOMongo
from .tournament import TournamentDAOMongo
from .user import UserDAOMongo


class MongoFactoryDAO(AbstractFactoryDAO):

    def match_DAO(self):
        return MatchDAOMongo()

    def notification_DAO(self):
        return NotificationDAOMongo()

    def team_DAO(self):
        return TeamDAOMongo()

    def tournament_DAO(self):
        return TournamentDAOMongo()

    def user_DAO(self):
        return UserDAOMongo()
