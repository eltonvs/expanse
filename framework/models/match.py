from abc import ABCMeta, abstractmethod


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

    @abstractmethod
    def winner(self):
        pass
