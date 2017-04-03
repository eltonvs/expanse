from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults

from ..controllers.team import TeamController
from ..models.team import Team


@view_defaults(route_name='list_teams')
class TeamViews(object):

    def __init__(self, request):
        self.team_controller = TeamController(request)
        self.request = request
        self.is_logged_in = request.authenticated_userid is not None
        self.view_name = "TeamViews"

    @view_config(renderer='team/list.jinja2')
    def list_teams(self):
        # Redirect to Index if the user isn't logged in
        if not self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        return {
            'page_title': 'List Users',
            'teams': self.team_controller.get_teams()
        }

    @view_config(
        route_name='register_team',
        renderer='team/register.jinja2')
    def register_team(self):
        # Redirect to Index if the user isn't logged in
        if not self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        return {'page_title': 'Sign up'}

    @view_config(
        route_name='register_team',
        request_method='POST',
        renderer='team/register_confirmation.jinja2')
    def register_team_request(self):
        # Redirect to Index if the user isn't logged in
        if not self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        params = self.request.params

        in_name = params.get('name', '')
        logged_user = self.request.authenticated_userid

        team = Team(in_name, logged_user)

        register_team = self.team_controller.register(team)

        return {
            'page_title': 'Registered Team',
            'errors': register_team,
            'team': team
        }

    @view_config(
        route_name='dashboard_team',
        renderer='team/dashboard.jinja2')
    def dashboard(self):
        return {'page_title': 'Team Dashboard'}

    @view_config(
        route_name='dashboard_team',
        request_method='POST',
        renderer='team/dashboard.jinja2')
    def dashboard(self):
        params = self.request.params
        team_id = self.request.matchdict['team_id']

        return {'page_title': 'Team Dashboard'}
