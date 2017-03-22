"""
  Define the project routes
  config.add_route('[route_name]', 'url_path')
    url_path --> expanse.com/url_path

  Created in 22/03/2017
"""

def includeme(config):
    # Routes:
    config.add_route('index', '/')
    config.add_route('about', '/about')

    config.scan()
