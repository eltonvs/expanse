from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults

from ..controllers import UserController
from ..models import User


@view_defaults(route_name='list_users')
class UserViews(object):

    def __init__(self, request):
        self.user_controller = UserController()
        self.request = request
        self.is_logged_in = request.authenticated_userid is not None
        self.view_name = 'UserViews'

    @view_config(renderer='user/list.jinja2')
    def list_users(self):
        # Redirect to Index if the user isn't logged in
        if not self.is_logged_in:
            url = self.request.route_url('index')
            return HTTPFound(location=url)

        return {
            'page_title': 'List Users',
            'users': self.user_controller.get_users()
        }

    @view_config(
        route_name='register_user',
        renderer='user/register.jinja2')
    def register_user(self):
        return {'page_title': 'Sign up'}

    @view_config(
        route_name='register_user',
        request_method='POST',
        renderer='user/register_confirmation.jinja2')
    def register_user_request(self):
        params = self.request.params

        in_name = params.get('name', '')
        in_username = params.get('username', '')
        in_email = params.get('email', '')
        in_password = params.get('password', '')
        in_locale = params.get('locale', '')

        user = User(in_name, in_username, in_email, in_password, in_locale)

        register_user = self.user_controller.register(user)

        return {
            'page_title': 'Registered User',
            'errors': register_user,
            'user': user
        }
