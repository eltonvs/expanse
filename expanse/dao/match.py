from framework import MatchDAO

from ..models import MongoDatabase, MatchCSGO


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
            "score": match.score.points,
            "time": match.time
        }
        return self.db.matches.insert(match_to_insert)

    def remove(self, query):
        self.db.matches.remove(query)

    def update(self, query, update):
        self.db.matches.update(query, update)

    def get(self, query):
        matches = list(self.db.matches.find(query))
        if matches:
            match_list = []
            for m in matches:
                match = MatchCSGO(
                    m.get('tournament', ''),
                    m.get('team1', None),
                    m.get('team2', None),
                    m.get('score', []),
                    m.get('time', 0)  # it will change to the type time
                )
                match.id = m.get('_id', '')
                match_list.append(match)
            return match_list
        return []

    def get_one(self, query):
        match = self.db.matches.find_one(query)
        if match:
            match_obj = MatchCSGO(
                match.get('tournament', ''),
                match.get('team1', None),
                match.get('team2', None),
                match.get('score', []),
                match.get('time', 0)  # it will change to the type time
            )
            match_obj.id = match.get('_id', '')
            return match_obj

    def list(self):
        return self.get({})
