from abc import ABCMeta
from ..models.score import Score
class FrameworkMatch(object):
    """Mach Model to store user data in runtime"""
    __metaclass__ = ABCMeta

    def __init__(self, tournament, score = Score(), time=None):
        self._id = None
        self._tournament = tournament
        self._score = score
        self._time = time

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

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time




class Match(object):
    """Mach Model to store user data in runtime"""

    def __init__(self, tournament, team1, team2, score=[], time=None):
        self._id = None
        self._tournament = tournament
        self._team1 = team1
        self._team2 = team2
        self._score = score
        self._time = time

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
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time
