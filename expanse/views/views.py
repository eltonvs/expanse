from pyramid.view import view_config, view_defaults

from expanse.controllers.user_controller import UserController


@view_defaults(route_name='site')
class ExpanseViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'ExpanseViews'

    @view_config(route_name='index', renderer='templates/index.jinja2')
    def index(self):
        # Do something

        # Return aways a dict:
        return {'title': 'expanse'}

    @view_config(route_name='signup', renderer='templates/signup.jinja2')
    def signup(self):


        prs = self.request.POST

        _return = {
            'title': 'Register User'
        }

        user_controller = UserController()
        users = user_controller.getUsers()

        if users:
            _return['users'] = users

        if not prs:
            return _return

        params = self.request.params

        user_first_name = params.get('first-name', '')
        user_last_name = params.get('last-name', '')
        user_email = params.get('email', '')
        user_password = params.get('password', '')
        user_address = params.get('address', '')

        user_name = user_first_name + " " + user_last_name
        user_username = (user_name.lower()).replace(" ", "")

        user = user_controller.signup(user_username, user_name, user_password, user_email, user_address)

        if user:
            _return['success'] = True
            _return['user'] = user

        else:
            _return['success'] = False

        return _return