from pyramid.view import view_config

@view_config(route_name='index', renderer='templates/mytemplate.jinja2')
def index(request):
    # Do something

    # Return aways a dict:
    return {'title': 'expanse'}
