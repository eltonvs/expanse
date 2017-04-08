from abc import ABCMeta, abstractmethod

from ..models.database import MongoDatabase
from ..models.tournament import Tournament
from .generic import GenericDAO


class TournamentDAO(GenericDAO):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_team(self, team, tournament):
        pass


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

    def remove(self, query):
        self.db.tournaments.remove(query)

    def update(self, query, update):
        self.db.tournaments.update(query, update)

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
                tournament = Tournament(
                    t['name'],
                    t['organizer_id'],
                    t.get('locale', ''))
                tournament.id = t['_id']
                tournament.teams = t['teams']
                tournament.matches = t.get('matches', [])
                tournament_list.append(tournament)
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
