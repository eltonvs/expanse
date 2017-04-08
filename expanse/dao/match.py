from abc import ABCMeta

from .generic import GenericDAO
from ..models.database import MongoDatabase
from ..models.match import Match


class MatchDAO(GenericDAO):
    __metaclass__ = ABCMeta


class MatchDAOMongo(MatchDAO):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, match):
        match_to_insert = {
            "tournament": match.tournament,
            "team1": match.team1,
            "team2": match.team2,
            "score": match.score,
            "time": match.time
        }
        self.db.matches.insert(match_to_insert)

    def remove(self, query):
        self.db.matches.remove(query)

    def update(self, query, update):
        self.db.matches.update(query, update)

    def get(self, query):
        matches = list(self.db.matches.find(query))
        if matches:
            match_list = []
            for m in matches:
                match = Match(
                    m['tournament'],
                    m['team1'],
                    m['team2'],
                    m['score'],
                    m['time'])
                match.id = m['_id']
                match_list.append(match)
            return match_list
        return []

    def get_one(self, query):
        match = list(self.db.matches.find(query))
        if match:
            match_obj = Match(
                match['tournament'],
                match['team1'],
                match['team2'],
                match['score'],
                match['time']
            )
            match_obj.id = match['_id']
            return match_obj

    def list(self):
        return self.get({})
