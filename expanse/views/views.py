from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from pyramid.view import view_config, view_defaults

from ..controllers.expanse import ExpanseController
from ..controllers.team import TeamController
from ..controllers.tournament import TournamentController


@view_defaults(route_name='index')
class ExpanseViews(object):

    def __init__(self, request):
        self.expanse_controller = ExpanseController(request)
        self.request = request
        self.is_logged_in = request.authenticated_userid is not None
        self.view_name = 'ExpanseViews'

    @view_config(renderer='index.jinja2')
    def index(self):
        logged_user = self.request.authenticated_userid
        return_dict = {'page_title': 'Home'}
        if logged_user:
            team_controller = TeamController(self.request)
            user_teams = team_controller.getUserTeams(logged_user)
            if user_teams:
                return_dict['user_teams'] = user_teams

            tournament_controller = TournamentController(self.request)
            user_tournaments = tournament_controller.getUserTournaments(logged_user)
            if user_tournaments:
                return_dict['user_tournaments'] = user_tournaments


        return return_dict

    @view_config(route_name='login', renderer='login.jinja2')
    def login(self):
        # Redirect to Index if the user is already logged in
        if self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        return {
            'page_title': 'Login',
        }

    @view_config(
        route_name='login',
        request_method='POST',
        renderer='login.jinja2')
    def login_request(self):
        # Redirect to Index if the user is already logged in
        if self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        request = self.request
        params = request.params

        in_email = params.get('email', '')
        in_password = params.get('password', '')

        # Try to log in user
        err = self.expanse_controller.login(in_email, in_password)
        if not err:
            url = request.route_url('index')
            headers = remember(request, in_email)
            return HTTPFound(location=url, headers=headers)

        return {
            'page_title': 'Login',
            'errors': err,
            'email': in_email,
        }

    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url('index')

        return HTTPFound(location=url, headers=headers)
