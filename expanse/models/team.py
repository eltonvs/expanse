from framework.models.team import Team


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
