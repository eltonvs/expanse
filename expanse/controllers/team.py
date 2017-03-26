from ..dao.team import TeamDAOMongo


class TeamController(object):
    """Controller Layer for Team Object"""

    def __init__(self):
         self.team_dao = TeamDAOMongo()

    def register(self, team):
        err = self.validate(team)
        if not err:
            err = self.team_dao.insertTeam(team)
        return err

    def validate(self, team):
        err = {}
        if not team.name:
            err['empty_name'] = True
        if not team.team_manager:
            err['empty_team_manager'] = True
        if team.lines == []:
            err['empty_lines'] = True

        return err

    def getTeams(self):
        return self.team_dao.listTeams()