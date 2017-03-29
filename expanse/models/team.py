from .user import User


class Team(object):
    """Team Model to store user data in runtime"""

    def __init__(self, name, user):
        self._name = name
        self._team_manager = TeamManager(user, self)
        self._lines = []

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


class TeamManager(User):
    """User Model to store team manager data in runtime"""

    def __init__(self, user, team):
        # Will save just de logged user's '_id', because we need just this
        # information
        self._user_id = user
        self._team = team

    @property
    def teams(self):
        return self._team

    @teams.setter
    def teams(self, value):
        self._teams = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
