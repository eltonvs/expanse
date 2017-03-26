from pyramid.view import view_config, view_defaults


@view_defaults(route_name='index')
class ExpanseViews(object):

    def __init__(self, request):
        self.request = request
        self.view_name = 'ExpanseViews'

    @view_config(renderer='index.jinja2')
    def index(self):
        return {'page_title': 'Home'}
