from framework import TeamController

from ..dao import MongoFactoryDAO
from ..models import Notification
from ..controllers import NotificationController


class TeamControllerSoccer(TeamController):
    """Controller Layer for Team Object"""

    def __init__(self):
        super(TeamControllerSoccer, self).__init__(MongoFactoryDAO())

    def validate(self, team):
        err = {}
        if not team.name:
            err['empty_name'] = True
        if not team.team_manager:
            err['empty_team_manager'] = True

        return err

    def append_lines(self, value):
        self.team_dao.lines.append(value)

    def extend_lines(self, value):
        self.team_dao.lines.extend(value)

    def invite_player(self, team_id, player_id):
        notification_controller = NotificationController()
        team = self.get_team_from_id(team_id)
        notification = Notification(
            player_id, "Team invitation", "\"" + team.name +
            "\" want you on the team! Do you accept the invitation?",
            "/teams/dashboard/" + str(team_id),
            True, team_id)
        notification_controller.add(notification)
