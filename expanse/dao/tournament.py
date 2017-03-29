from ..models.database import MongoDatabase
from .generic import GenericDAO


class TournamentDAO(GenericDAO):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, tournament):
        tournament_to_insert = {
            "name": tournament.name,
            "teams": [],
            "organizer_id": tournament.organizer
        }
        self.db.tournaments.insert(tournament_to_insert)

    def remove(self, tournament):
        print("Not implemented yet")
        pass

    def update(self, querry, update):
        print "update", self.db.tournaments.update(querry, update)

    def add_team(self, team, tournament):
        # add new team to a tournamet
        # need to find the _id of the current tournament
        # insert team_id in the list of teams in db
        print("Not implented yet")
        pass

    def get(self, querry):
        tournaments = list(self.db.tournaments.find(querry))
        return tournaments

    def list(self):
        tournaments = list(self.db.tournaments.find())
        return tournaments
