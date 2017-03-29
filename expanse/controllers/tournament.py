from bson import ObjectId

from ..dao.tournament import TournamentDAO
from ..dao.user import UserDAO
from ..models.notification import Notification
from ..controllers.notification import NotificationController


class TournamentController(object):
    """Controller layer for Tournament object"""

    def __init__(self, request):
        self.request = request
        self.tournament_dao = TournamentDAO()

    def register(self, tournament):
        err = self.validate(tournament)
        if not err:
            err = self.tournament_dao.insert(tournament)
            self.notify_nearest_teams(tournament)
        return err

    def validate(self, tournament):
        err = {}
        if not tournament.name:
            err['empty_name'] = True
        if not tournament.organizer:
            err['empty_organizer'] = True
        elif tournament.organizer != self.request.authenticated_userid:
            err['invalid_organizer'] = True
        if not tournament.locale:
            err['empty_locale'] = True

        return err

    def notify_nearest_teams(self, tournament):
        print("notification")
        user_dao = UserDAO()
        notification_controller = NotificationController(self.request)
        nearest_users = user_dao.get_users_from_locale(tournament.locale)
        print(nearest_users)
        for nu in nearest_users:
            usr_id = nu['_id']
            print(usr_id)
            notification = Notification(
                usr_id,
                "Nearest Tournament",
                tournament.name + " is near from you!")
            notification_controller.add(notification)
        pass

    def add_team(self, tournament_id, team_id):
        if tournament_id and team_id:
            querry = {'_id': ObjectId(tournament_id)}
            update = {'$addToSet': {'teams': ObjectId(team_id)}}

            self.tournament_dao.update(querry, update)

            # team = tournament.team
            # team.append(team_id)
            # tournament.team = team

    def get_tournaments(self):
        return self.tournament_dao.list()

    def get_user_tournaments(self, user):
        return self.tournament_dao.get({"organizer_id": user})
