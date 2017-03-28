from pyramid.view import view_config, view_defaults

@view_defaults(route_name='list_tournaments')
class TournamentViews(object):

    def __init__(self, request):
        #self.tournament_controller = TournamentController()
        self.request = request
        self.view_name = 'TournamentViews'

    @view_config(renderer='tournament/list.jinja2')
    def list_tournaments(self):
        return {
            'page_title': 'List Tournaments',
        }

