from abc import ABCMeta

from framework.dao.generic import GenericDAO

from ..models.database import MongoDatabase
from ..models.game import Game


class GameDAO(GenericDAO):
    __metaclass__ = ABCMeta


class GameDAOMongo(GameDAO):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, game):
        game_to_insert = {
            "name": game.name,
            "abbreviation": game.abbreviation,
            "steamid": game.steamid,
        }
        return self.db.games.insert(game_to_insert)

    def remove(self, query):
        self.db.games.remove(query)

    def update(self, query, update):
        self.db.games.update(query, update)

    def get(self, query):
        games = list(self.db.games.find(query))
        if games:
            game_list = []
            for g in games:
                game = Game(
                    g.get('name', ''),
                    g.get('abbreviation', None),
                    g.get('steamid', None),
                )
                game.id = g.get('_id', '')
                game_list.append(game)
            return game_list
        return []

    def get_one(self, query):
        game = list(self.db.games.find(query))
        if game:
            game_obj = Game(
                game.get('name', ''),
                game.get('abbreviation', None),
                game.get('steamid', None),
            )
            game_obj.id = game.get('_id', '')
            return game_obj

    def list(self):
        return self.get({})
