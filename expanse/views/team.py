from pyramid.view import view_config, view_defaults

from ..controllers.team import TeamController
from ..models.team import Team

class TeamViews(object):

    def __init__(self, request):
        self.team_controller = TeamController()
        self.request = request
        self.view_config = "TeamViews"
    
    @view_config(renderer='user/list.jinja2')
    def list_teams(self):
        return {
            'page_title': 'List Users',
            'users': self.team_controller.getTeams()
        }