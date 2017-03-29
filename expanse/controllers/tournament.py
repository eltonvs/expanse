from ..dao.tournament import TournamentDAO


class TournamentController(object):
    """Controller layer for Tournament object"""

    def __init__(self, request):
        self.request = request
        self.tournament_dao = TournamentDAO()

    def register(self, tournament):
        err = self.validate(tournament)
        if not err:
            err = self.tournament_dao.insert(tournament)
        return err

    def validate(self, tournament):
        err = {}
        if not tournament.name:
            err['empty_name'] = True
        if not tournament.organizer:
            err['empty_organizer'] = True
        elif tournament.organizer != self.request.authenticated_userid:
            err['invalid_organizer'] = True

        return err

    def addTeam(self, tournament, team):
        if tournament and team:
            teams = tournament.teams
            teams.append(team)
            tournament.teams = teams

    def getTournaments(self):
        return self.tournament_dao.list()

    def getUserTournaments(self, user):
        return self.tournament_dao.get({"organizer_id": user})