from ..models.database import MongoDatabase
from .generic import GenericDAO

class TournamentDAO(GenericDAO):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, tournamet):
        tournamet_to_insert = {
            "name": tournamet.name,
            "teams": [],
            #"tournament_organizer_id": tournament_organizer
        }
        self.db.tournamets.insert(tournamet_to_insert)

    def remove(self, tournamet):
        print("Not implemented yet")
        pass

    def update(self, tournamet):
        print("Not implemented yet")
        pass

    def add_team(self, team, tournamet):
        # add new team to a tournamet
        # need to find the _id of the current tournament
        # insert team_id in the list of teams in db
        print("Not implented yet")
        pass

    def get(self, tournamet):
        print("Not implemented yet")
        pass

    def list(self):
        tournamets = list(self.db.tournamets.find())
        return tournamets