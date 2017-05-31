from abc import ABCMeta


class Team(object):
    """Team Model to store user data in runtime"""
    __metaclass__ = ABCMeta

    def __init__(self, name, manager, players=[]):
        self._id = None
        self._name = name
        self._team_manager = manager
        self._players = players

    def __str__(self):
        return (self._name)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = value


class TeamCSGO(Team):
    """Team Model to store user data in runtime"""

    def __init__(self, name, manager):
        super(TeamCSGO, self).__init__(name, manager)
        self._lines = []

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value
