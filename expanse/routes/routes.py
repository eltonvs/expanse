"""
  Define the project routes
  config.add_route('[route_name]', 'url_path')
    url_path --> expanse.com/url_path

  Created in 22/03/2017
"""


def includeme(config):
    # ExpanseViews Routes
    config.add_route('index', '/')

    # UserViews Routes
    config.add_route('list_users', '/users')
    config.add_route('register_user', '/users/register')

    config.scan()
