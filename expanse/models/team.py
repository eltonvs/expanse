from .user import User


class Team(object):
    """Team Model to store user data in runtime"""

    def __init__(self, name, user):
        self._name = name
        self._team_manager = user
        self._lines = []
        self._my_id = None

    def __str__(self):
        return (self._name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def team_manager(self):
        return self._team_manager

    @team_manager.setter
    def team_manager(self, value):
        self._team_manager = value

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value

    @property
    def my_id(self):
        return self._my_id

    @my_id.setter
    def my_id(self, value):
        self._my_id = value
