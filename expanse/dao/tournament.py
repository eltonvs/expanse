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
            "matches":[]
        }
        self.db.tournaments.insert(tournament_to_insert)

    def remove(self, tournament):
        print("Not implemented yet")
        pass

    def update(self, querry, update):
        print("update", self.db.tournaments.update(querry, update))

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
            for tournament in tournaments:
                new_tournamant = Tournament(
                    tournament['name'],
                    tournament['organizer_id'],
                    tournament.get('locale',''))
                new_tournamant.teams = tournament['teams']
                new_tournamant.matches = tournament.get('matches', [])
                new_tournamant.my_id = tournament['_id']
                tournament_list.append(new_tournamant)
            return tournament_list

    def get_one(self, query):
        tournament =  self.db.tournaments.find_one(query)
        if tournament:
            new_tournamant = Tournament(
                tournament['name'],
                tournament['organizer_id'],
                tournament.get('locale',''))
            new_tournamant.teams = tournament['teams']
            new_tournamant.matches = tournament.get('matches', [])
            new_tournamant.my_id = tournament['_id']
            return new_tournamant

    def list(self):
        return self.get({})


class MatchDAOMongo(MatchDAO):

    __shered_state = {}

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
            for match in matches:
                new_match = Match()
                new_match.teams = match['teams']
                new_match.score = match['score']
                new_match.time = match['time']
                new_match.my_id = match['_id']
                match_list.append(new_match)
            return match_list

    def get_one(self, query):
        matches = list(self.db.matches.find(query))
        if matches:
            new_match = Match()
            new_match.teams = match['teams']
            new_match.score = match['score']
            new_match.time = match['time']
            new_match.my_id = match['_id']
            return new_match

    def list(self):
        return self.get({})


