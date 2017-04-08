from bson import ObjectId

from ..dao.team import TeamDAOMongo
from ..dao.tournament import TournamentDAOMongo
from ..dao.user import UserDAOMongo
from ..models.notification import Notification
from ..controllers.notification import NotificationController


class TournamentController(object):
    """Controller layer for Tournament object"""

    def __init__(self):
        self.tournament_dao = TournamentDAOMongo()

    def register(self, tournament):
        err = self.validate(tournament)
        if not err:
            err = self.tournament_dao.insert(tournament)
            self.notify_near_users(tournament)
        return err

    def validate(self, tournament):
        err = {}
        if not tournament.name:
            err['empty_name'] = True
        if not tournament.organizer:
            err['empty_organizer'] = True
        if not tournament.locale:
            err['empty_locale'] = True

        return err

    def notify_near_users(self, tournament):
        user_dao = UserDAOMongo()
        notification_controller = NotificationController()
        nearest_users = user_dao.get_users_from_locale(tournament.locale)
        for nu in nearest_users:
            usr_id = nu.id
            if usr_id == tournament.organizer:
                continue
            notification = Notification(
                usr_id,
                "Near Tournament",
                "\"" + tournament.name + "\" is near from you!")
            notification_controller.add(notification)

    def add_team(self, tournament_id, team_id):
        if tournament_id and team_id:
            query = {'_id': ObjectId(tournament_id)}
            update = {'$addToSet': {'teams': ObjectId(team_id)}}

            self.tournament_dao.update(query, update)

            # team = tournament.team
            # team.append(team_id)
            # tournament.team = team

    def add_match(self, tournament_id, match_id):
        if tournament_id and match_id:
            query = {'_id': ObjectId(tournament_id)}
            update = {'$addToSet': {'matches': ObjectId(match_id)}}

            self.tournament_dao.update(query, update)

    def get_tournaments(self):
        return self.tournament_dao.list()

    def get_user_tournaments(self, user):
        return self.tournament_dao.get({"organizer_id": user})

    def get_tournament_teams(self, tournament_id):
        tournament = self.tournament_dao.get_one(
            {"_id": ObjectId(tournament_id)})
        tournament_teams = tournament.teams

        if tournament_teams:
            team_dao = TeamDAOMongo()
            teams = []

            for team_id in tournament_teams:
                team = team_dao.get_one({"_id": team_id})
                if team:
                    teams.append(team)

            return teams
        return []

    def get_tournament_matches(self, tournament_id):
        tournament = self.tournament_dao.get_one(
            {"_id": ObjectId(tournament_id)})
        tournament_matches = tournament.matches

        if tournament_matches:
            match_dao = TeamDAOMongo()
            matches = []

            for match_id in tournament_matches:
                match = match_dao.get_one({"_id": match_id})
                if match:
                    matches.append(match)

            return matches
        return []
