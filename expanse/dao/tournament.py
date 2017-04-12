from abc import ABCMeta

from ..models.database import MongoDatabase
from ..models.tournament import Tournament, TournamentPhase
from .generic import GenericDAO


class TournamentDAO(GenericDAO):
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
            "status": tournament.status,
            "phases": [
                {
                    "type": phase.type,
                    "teams": phase.teams,
                    "schedule": phase.schedule
                } for phase in tournament.phases]
        }
        self.db.tournaments.insert(tournament_to_insert)

    def remove(self, query):
        self.db.tournaments.remove(query)

    def update(self, query, update):
        self.db.tournaments.update(query, update)

    def get(self, query):
        tournaments = list(self.db.tournaments.find(query))
        if tournaments:
            tournament_list = []
            for t in tournaments:
                tournament_list.append(self._get_object_from_dictionary(t))
            return tournament_list
        return []

    def get_one(self, query):
        tournament = self.db.tournaments.find_one(query)
        if tournament:
            return self._get_object_from_dictionary(tournament)

    def list(self):
        return self.get({})

    def _get_object_from_dictionary(self, tournament):
        tournament_phases = tournament.get('phases', [])
        tournament_phases_list = []

        for phase in tournament_phases:
            tournament_phases_list.append(
                TournamentPhase(
                    phase.get('type', ''),
                    phase.get('teams', ''),
                    phase.get('schedule', '')
                )
            )

        tournament_obj = Tournament(
            tournament.get('name', ''),
            tournament.get('organizer_id', ''),
            tournament.get('locale', ''),
            tournament.get('status', ''),
            tournament_phases_list)
        tournament_obj.id = tournament.get('_id', '')
        tournament_obj.teams = tournament.get('teams', '')
        tournament_obj.matches = tournament.get('matches', [])

        return tournament_obj
