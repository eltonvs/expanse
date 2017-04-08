from abc import ABCMeta, abstractmethod

from ..models.database import MongoDatabase
from ..models.tournament import Tournament, Match
from .generic import GenericDAO


class TournamentDAO(GenericDAO):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_team(self, team, tournament):
        pass


class MatchDAO(GenericDAO):
    __metaclass__ = ABCMeta


class TournamentDAOMongo(TournamentDAO):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, tournament):
        tournament_to_insert = {
            "name": tournament.name,
            "teams": [],
            "locale": tournament.locale,
            "organizer_id": tournament.organizer,
            "matches": []
        }
        self.db.tournaments.insert(tournament_to_insert)

    def remove(self, tournament):
        print("Not implemented yet")
        pass

    def update(self, query, update):
        print("update", self.db.tournaments.update(query, update))

    def add_team(self, team, tournament):
        # add new team to a tournamet
        # need to find the _id of the current tournament
        # insert team_id in the list of teams in db
        print("Not implented yet")
        pass

    def get(self, query):
        tournaments = list(self.db.tournaments.find(query))
        if tournaments:
            tournament_list = []
            for t in tournaments:
                tournamant = Tournament(
                    t['name'],
                    t['organizer_id'],
                    t.get('locale', ''))
                tournamant.id = t['_id']
                tournamant.teams = t['teams']
                tournamant.matches = t.get('matches', [])
                tournament_list.append(tournamant)
            return tournament_list
        return []

    def get_one(self, query):
        tournament = self.db.tournaments.find_one(query)
        if tournament:
            tournament_obj = Tournament(
                tournament['name'],
                tournament['organizer_id'],
                tournament.get('locale', ''))
            tournament_obj.id = tournament['_id']
            tournament_obj.teams = tournament['teams']
            tournament_obj.matches = tournament.get('matches', [])
            return tournament_obj

    def list(self):
        return self.get({})


class MatchDAOMongo(MatchDAO):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, match):
        match_to_insert = {
            "teams": match.teams,
            "score": match.score
        }
        self.db.matches.insert(match_to_insert)

        return{}

    def remove(self, user):
        print("Not implemented yet")
        pass

    def update(self, query, update):
        print(query, update, self.db.matches.update(query, update))

    def get(self, query):
        matches = list(self.db.matches.find(query))
        if matches:
            match_list = []
            for m in matches:
                match = Match()
                match.id = m['_id']
                match.teams = m['teams']
                match.score = m['score']
                match.time = m['time']
                match_list.append(match)
            return match_list
        return []

    def get_one(self, query):
        match = list(self.db.matches.find(query))
        if match:
            match_obj = Match()
            match_obj.id = match['_id']
            match_obj.teams = match['teams']
            match_obj.score = match['score']
            match_obj.time = match['time']
            return match_obj

    def list(self):
        return self.get({})
