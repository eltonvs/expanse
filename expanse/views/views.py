from pyramid.view import view_config, view_defaults

@view_defaults(route_name='site')
class ExpanseViews(object):
    users = []
    
    def __init__(self, request):
        self.request = request
        self.view_name = 'ExpanseViews'
        # self.users = []

    @view_config(route_name='index', renderer='templates/mytemplate.jinja2')
    def index(self):
        # Do something
        
        # Return aways a dict:
        return {'title': 'expanse'}

    @view_config(route_name='register_user', renderer='templates/register_user.jinja2')
    def register_user(self):
        params = self.request.params
        username = params.get('username', '')

        if not params.get('username'):
            return {'success': False, 'users': self.users}

        self.users.append(username)

        return {'title': 'Register User', "success": True, "username": username, "users": self.users}