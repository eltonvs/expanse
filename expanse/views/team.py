from pyramid.view import view_config, view_defaults

from ..controllers.team import TeamController
from ..models.team import Team


@view_defaults(route_name='list_teams')
class TeamViews(object):

    def __init__(self, request):
        self.team_controller = TeamController()
        self.request = request
        self.view_config = "TeamViews"

    @view_config(renderer='team/list.jinja2')
    def list_teams(self):
        return {
            'page_title': 'List Users',
            'teams': self.team_controller.getTeams()
        }

    @view_config(
        route_name='register_team',
        renderer='team/register.jinja2')
    def register_team(self):
        return {'page_title': 'Sign up'}

    @view_config(
        route_name='register_team',
        request_method='POST',
        renderer='team/register_confirmation.jinja2')
    def register_team_request(self):
        params = self.request.params

        in_name = params.get('name', '')

        team = Team(in_name)

        register_team = self.team_controller.register(team)

        return {
            'page_title': 'Registered Team',
            'errors': register_team,
            'team': team
        }
