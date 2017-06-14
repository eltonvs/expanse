from abc import ABCMeta


class Score(object):
    """Team Model to store user data in runtime"""
    __metaclass__ = ABCMeta

    def __init__(self, points):
        self._id = None
        self._points = points

    def __str__(self):
        return 'X'.join(str(p) for p in self.points)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value
