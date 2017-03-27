from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from pyramid.view import view_config, view_defaults

from ..controllers.expanse import ExpanseController


@view_defaults(route_name='index')
class ExpanseViews(object):

    def __init__(self, request):
        self.request = request
        self.expanse_controller = ExpanseController()
        self.logged_in = request.authenticated_userid
        self.view_name = 'ExpanseViews'

    @view_config(renderer='index.jinja2')
    def index(self):
        return {'page_title': 'Home'}

    @view_config(route_name='login', renderer='login.jinja2')
    def login(self):
        return {
            'page_title': 'Login',
        }

    @view_config(
        route_name='login',
        request_method='POST',
        renderer='login.jinja2')
    def login_request(self):
        request = self.request
        params = request.params

        in_email = params.get('email', '')
        in_password = params.get('password', '')

        # Try to log in user
        err = self.expanse_controller.login(in_email, in_password)
        if not err:
            url = request.route_url('index')
            headers = remember(request, in_email)
            return HTTPFound(location=url, headers=headers)

        return {
            'page_title': 'Login',
            'errors': err,
            'email': in_email,
        }

    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url('index')

        return HTTPFound(location=url, headers=headers)
