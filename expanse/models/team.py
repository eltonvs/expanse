from framework import Team


class TeamSoccer(Team):
    """Team Model to store user data in runtime"""

    def __init__(self, name, manager):
        super(TeamSoccer, self).__init__(name, manager)