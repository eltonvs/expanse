from pyramid.view import view_config, view_defaults


@view_defaults(route_name='site')
class ExpanseViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'ExpanseViews'
        # self.users = []

    @view_config(route_name='index', renderer='templates/index.jinja2')
    def index(self):
        # Do something

        # Return aways a dict:
        return {'title': 'expanse'}

    @view_config(route_name='signup', renderer='templates/signup.jinja2')
    def signup(self):
        params = self.request.params
        username = params.get('username', '')

        if not params.get('username'):
            return {
                'success': False,
                'users': self.request.db.users.find()
            }

        self.request.db.users.insert({"username": username})

        return {
            'title': 'Register User',
            "success": True,
            "username": username,
            "users": self.request.db.users.find()
        }
