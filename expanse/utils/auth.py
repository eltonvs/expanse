from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from ..controllers import UserController


class MyAuthenticationPolicy(AuthTktAuthenticationPolicy):

    def authenticated_userid(self, request):
        user = request.logged_user
        if user is not None:
            user_controller = UserController()
            return user_controller.get_user_id_from_email(user.email)


def get_logged_user(request):
    user_email = request.unauthenticated_userid
    if user_email is not None:
        user_controller = UserController()
        user = user_controller.get_user_from_email(user_email)
        return user


def includeme(config):
    settings = config.get_settings()
    authn_policy = MyAuthenticationPolicy(
        settings['expanse.secret'],
        hashalg='sha512')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_logged_user, 'logged_user', reify=True)
