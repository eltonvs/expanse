from abc import ABCMeta, abstractmethod
from bson import ObjectId


class MatchController(object):
    __metaclass__ = ABCMeta

    def __init__(self, factory_dao):
        self.factory_dao = factory_dao
        self.match_dao = self.factory_dao.match_DAO()

    def register(self, match):
        err = self.validate(match)
        if not err:
            inserted_id = self.match_dao.insert(match)
            if not inserted_id:
                return {'db_error': True}
            match.id = inserted_id
        return err

    def set_score(self, match, score1, score2):
        query = {'_id': ObjectId(match)}
        update = {'$set': {'score': [score1, score2]}}
        self.match_dao.update(query, update)

    def get_matches_from_tournament(self, tournament):
        return self.match_dao.get({"tournament": ObjectId(tournament)})

    def get_matches(self):
        return self.match_dao.list()

    @abstractmethod
    def validate(self, match):
        pass
