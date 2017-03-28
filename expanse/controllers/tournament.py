from ..dao.tournament import TournamentDAO

class TournamentController(object):
    """Controller layer for Tournament object"""

    def __init__(self):
        self.tournament_dao = TournamentDAO()

    def register(self, tournament):
        err = self.validade(tournament)
        if not err:
            err = self.tournament_dao.insert(tournament)
        return err

    def validade(self, tournament):
        err = {}
        if not tournament.name:
            err['empty_name'] = True

        return err

    def addTeam(self, tournamet, team):
        if tournamet and team:
            teams = tournamet.teams
            teams.append(team)
            tournamet.teams = teams

    def getTournaments(self):
        return self.tournament_dao.list()
