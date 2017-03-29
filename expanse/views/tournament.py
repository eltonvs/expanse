from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults

from ..controllers.tournament import TournamentController
from ..models.tournament import Tournament


@view_defaults(route_name='list_tournaments')
class TournamentViews(object):

    def __init__(self, request):
        self.tournament_controller = TournamentController(request)
        self.request = request
        self.is_logged_in = request.authenticated_userid is not None
        self.view_name = 'TournamentViews'

        # Just for debugging purposes
        print(self.view_name)
        print(self.request.authenticated_userid)
        print(self.request.unauthenticated_userid)
        print(self.request.logged_user)

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

        tournament = Tournament(name)

        register_tournament = self.tournament_controller.register(tournament)

        return {
            'page_title': 'Registered Tournament',
            'errors': register_tournament,
            'tournament': tournament,
        }
