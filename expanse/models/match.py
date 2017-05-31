from abc import ABCMeta
from ..models.score import ScoreCSGO


class Match(object):
    """Mach Model to store user data in runtime"""
    __metaclass__ = ABCMeta

    def __init__(self, tournament, score):
        self._id = None
        self._tournament = tournament
        self._score = score

    def __str__(self):
        return self._name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def tournament(self):
        return self._tournament

    @tournament.setter
    def tournament(self, tournament):
        self._tournament = tournament

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score


class MatchCSGO(Match):
    """Mach Model to store user data in runtime"""

    def __init__(self, tournament, team1, team2, score=ScoreCSGO(), time=None):
        super(MatchCSGO, self).__init__(tournament, score)
        self._team1 = team1
        self._team2 = team2
        self._time = time

    @property
    def team1(self):
        return self._team1

    @team1.setter
    def team1(self, team1):
        self._team1 = team1

    @property
    def team2(self):
        return self._team2

    @team2.setter
    def team2(self, team2):
        self._team2 = team2

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time
