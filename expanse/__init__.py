from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # Jinja Settings
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path('templates/')

    # Add new routes file
    config.include('.routes.routes')

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.scan()
    return config.make_wsgi_app()
