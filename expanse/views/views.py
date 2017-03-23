from pyramid.view import view_config, view_defaults

@view_defaults(route_name='site')
class ExpanseViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'ExpanseViews'

    @view_config(route_name='index', renderer='templates/mytemplate.jinja2')
    def index(request):
        # Do something

        # Return aways a dict:
        return {'title': 'expanse'}

    @view_config(route_name='about', renderer='json')
    def about(request):
        a = 15
        return {'value': a}
