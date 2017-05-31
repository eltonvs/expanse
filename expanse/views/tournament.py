from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults

from ..controllers.tournament import TournamentController
from ..controllers.team import TeamControllerCSGO
from ..controllers.game import GameController
from ..controllers.match import MatchControllerCSGO
from ..models.tournament import Tournament, TournamentPhase, TournamentStatus


@view_defaults(route_name='list_tournaments')
class TournamentViews(object):

    def __init__(self, request):
        self.tournament_controller = TournamentController()
        self.request = request
        self.is_logged_in = request.authenticated_userid is not None
        self.view_name = 'TournamentViews'

    @view_config(renderer='tournament/list.jinja2')
    def list_tournaments(self):
        # Redirect to Index if the user isn't logged in
        if not self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        return {
            'page_title': 'List Tournaments',
            'tournaments': self.tournament_controller.get_tournaments(),
        }

    @view_config(
        route_name='register_tournament',
        renderer='tournament/register.jinja2')
    def register_tournament(self):
        # Redirect to Index if the user isn't logged in
        if not self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        game_controller = GameController()
        games = game_controller.list()
        return {
            'page_title': 'Register Tournament',
            'games': games
        }

    @view_config(
        route_name='register_tournament',
        request_method='POST',
        renderer='tournament/register_confirmation.jinja2')
    def register_tournament_request(self):
        # Redirect to Index if the user isn't logged in
        if not self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        params = self.request.params

        tournament_name = params.get('name', '')
        tournament_type = params.get('type', '')
        tournament_status = TournamentStatus.OPENED
        tournament_game = params.get('game', '')

        tournament_phases = [TournamentPhase(tournament_type)]

        tournament = Tournament(
            tournament_name,
            self.request.authenticated_userid,
            self.request.logged_user.locale,
            tournament_status,
            tournament_phases,
            tournament_game,)

        register_tournament = self.tournament_controller.register(tournament)

        return {
            'page_title': 'Registered Tournament',
            'errors': register_tournament,
            'tournament': tournament,
        }

    @view_config(
        route_name='dashboard_tournament',
        renderer='tournament/dashboard.jinja2')
    def dashboard(self):
        logged_user = self.request.authenticated_userid
        _return = {'page_title': 'Dashboard'}

        if logged_user:
            team_controller = TeamControllerCSGO()
            teams = team_controller.get_teams()
            _return['teams'] = teams

            tournament_id = self.request.matchdict['tournament_id']

            tournament_phases = self.tournament_controller.get_tournament_schedule(
                tournament_id)

            for phase in tournament_phases:
                for round in phase.schedule:
                    for match in round:
                        if match:
                            match.team1 = team_controller.get_team_from_id(
                                match.team1)
                            match.team2 = team_controller.get_team_from_id(
                                match.team2)
            _return['tournament_phases'] = tournament_phases

            tournament_teams = self.tournament_controller.get_tournament_teams(
                tournament_id)
            _return['tournament_teams'] = tournament_teams

        return _return

    @view_config(
        route_name='dashboard_tournament',
        renderer='tournament/dashboard.jinja2',
        request_method='POST')
    def dashboard_request(self):
        params = self.request.params
        tournament_id = self.request.matchdict['tournament_id']

        if params.get('team'):
            team_id = params.get('team', '')
            self.tournament_controller.add_team(tournament_id, team_id)

        if params.get('btn_generate'):
            self.tournament_controller.generate_schedule(tournament_id)

        return {'page_title': 'Dashboard', 'errors': None}

    @view_config(
        route_name="dashboard_match",
        renderer="tournament/match_dashboard.jinja2")
    def match_dashboard(self):
        match_id = self.request.matchdict['match_id']
        match_controller = MatchControllerCSGO()
        teams = match_controller.get_match_teams(match_id)

        return{'page_title': 'Match Dashboard', 'teams': teams}

    @view_config(
        route_name="dashboard_match",
        request_method="POST",
        renderer="tournament/match_dashboard.jinja2")
    def match_dashboard_request(self):
        params = self.request.params
        match_id = self.request.matchdict['match_id']

        valueTeamA = params.get('result_team_a')
        valueTeamB = params.get('result_team_b')

        match_controller = MatchControllerCSGO()

        match_controller.set_score(match_id, valueTeamA, valueTeamB)
        teams = match_controller.get_match_teams(match_id)

        return{'page_title': 'Match Dashboard', 'teams': teams}
