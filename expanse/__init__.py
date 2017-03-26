from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # Security Policies
    authn_policy = AuthTktAuthenticationPolicy(
        settings['expanse.secret'],
        hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    # Jinja Settings
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path('templates/')

    # Add new routes file
    config.include('.routes.routes')

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.scan()
    return config.make_wsgi_app()
