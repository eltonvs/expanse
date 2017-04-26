from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget
from pyramid.security import remember
from pyramid.view import view_config
from pyramid.view import view_defaults

from ..controllers.expanse import ExpanseController
from ..controllers.team import TeamController
from ..controllers.tournament import TournamentController
from ..controllers.notification import NotificationController
from ..controllers.steam import SteamController


@view_defaults(route_name='index')
class ExpanseViews(object):

    def __init__(self, request):
        self.expanse_controller = ExpanseController()
        self.request = request
        self.is_logged_in = request.authenticated_userid is not None
        self.view_name = 'ExpanseViews'

    @view_config(renderer='index.jinja2')
    def index(self):
        _return = {'page_title': 'Home'}
        logged_user = self.request.authenticated_userid

        if logged_user:
            # List user teams
            team_controller = TeamController()
            user_teams = team_controller.get_managed_teams(logged_user)
            _return['user_teams'] = user_teams

            # List user tournaments
            tournament_controller = TournamentController()
            user_tournaments = tournament_controller.get_organized_tournaments(
                logged_user)
            _return['user_tournaments'] = user_tournaments

            # List user notifications
            notification_controller = NotificationController()
            user_notifications = notification_controller.get_notifications(
                logged_user)
            _return['user_notifications'] = user_notifications

        return _return

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

    @view_config(
            request_method='POST',
            renderer='index.jinja2')
    def accept_invite(self):
        params = self.request.params

        notification_controller = NotificationController()
        notification_id = params.get('notification_id')

        if params.get('accept') == 'Yes':
            team_controller = TeamController()
            team_id = params.get('team_id')
            logged_user = self.request.authenticated_userid

            team_controller.add_player(team_id, logged_user)

        #     notification_controller.remove(notification_id)
        # elif params.get('accept') == 'No':
        #     notification_controller.remove(notification_id)

        return self.index()

    @view_config(route_name='steam_data', renderer='steam_data.jinja2')
    def steam_data(self):
        return {'page_title': "Steam Data"}

    @view_config(
        route_name='steam_data',
        request_method='POST',
        renderer='steam_data.jinja2')
    def steam_data_request(self):
        params = self.request.params

        username = params.get('steam_username', '')
        print("'" + username + "'")

        steam_controller = SteamController()

        player = steam_controller.get_steamuser_from_username(username)

        return {
            "page_title": "Steam Data - Results",
            "username": username,
            "player": player
        }
