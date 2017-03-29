from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults

from ..controllers.tournament import TournamentController
from ..controllers.team import TeamController
from ..models.tournament import Tournament


@view_defaults(route_name='list_tournaments')
class TournamentViews(object):

    def __init__(self, request):
        self.tournament_controller = TournamentController(request)
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
            'tournaments': self.tournament_controller.getTournaments(),
        }

    @view_config(
        route_name='register_tournament',
        renderer='tournament/register.jinja2')
    def register_tournament(self):
        # Redirect to Index if the user isn't logged in
        if not self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        return {
            'page_title': 'Register Tournament'
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

        name = params.get('name', '')
        tournament = Tournament(name, self.request.authenticated_userid)

        register_tournament = self.tournament_controller.register(tournament)

        return {
            'page_title': 'Registered Tournament',
            'errors': register_tournament,
            'tournament': tournament,
        }

    @view_config(route_name='dashboard_tournament', renderer='tournament/dashboard.jinja2')
    def dashboard(self):
        logged_user = self.request.authenticated_userid
        return_dict = {'page_title': 'Home'}

        if logged_user:
            team_controller = TeamController(self.request)
            teams = team_controller.getTeams()
            if teams:
                return_dict['teams'] = teams

        return return_dict

    @view_config(
        route_name='dashboard_tournament',
        renderer='tournament/dashboard.jinja2',
        request_method='POST')
    def dashboard_request(self):
        params = self.request.params

        tournament_id = self.request.matchdict['tournament_id']
        team_id = params.get('team', '')

        self.tournament_controller.addTeam(tournament_id, team_id)

        return {'page_title': 'Dashboard'}
