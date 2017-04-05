"""
  Define the project routes
  config.add_route('[route_name]', 'url_path')
    url_path --> expanse.com/url_path

  Created in 22/03/2017
"""


def includeme(config):
    # ExpanseViews Routes
    config.add_route('index', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    # UserViews Routes
    config.add_route('list_users', '/users')
    config.add_route('register_user', '/users/register')

    # TeamViews Routes
    config.add_route('list_teams', '/teams')
    config.add_route('register_team', '/teams/register')
    config.add_route('dashboard_team', '/teams/dashboard/{team_id}')

    # Tournament Routes
    config.add_route('list_tournaments', '/tournaments')
    config.add_route('register_tournament', '/tournaments/register')
    config.add_route(
        'dashboard_tournament',
        '/tournaments/dash/{tournament_id}')

    config.scan()
