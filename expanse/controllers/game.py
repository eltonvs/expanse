from ..dao.game import GameDAOMongo

class GameController(object):

    def __init__(self):
        self.game_dao = GameDAOMongo()

    def list(self):
        return self.game_dao.list()