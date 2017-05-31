from abc import ABCMeta, abstractmethod
class Score(object):
    """Team Model to store user data in runtime"""
    __metaclass__ = ABCMeta

    def __init__(self):
        self._id = None

    def __str__(self):
        """Real score (int?)"""
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value