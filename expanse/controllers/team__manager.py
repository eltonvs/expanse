from ..dao.team_manager import TeamManagerDAOMongo


class TeamManagerController(object):
    """Controller Layer for Team Object"""

    def __init__(self):
         self.team_manager_dao = TeamManagerDAO()

    def register(self, team):
        err = self.validate(team_manager)
        if not err:
            err = self.team_manager_dao.insertTeamManager(team_manager)
        return err

    def validate(self, team):
        err = {}
        if not team_manager.name:
            err['empty_name'] = True
        if not team_manager.username:
            err['empty_username'] = True
        if not team_manager.email:
            err['empty_email'] = True
        if not team_manager.password:
            err['empty_password'] = True
        if not team_manager.locale:
            err['empty_locale'] = True

        return err

    def getTeamManager(self):
        return self.team_manager_dao.list()