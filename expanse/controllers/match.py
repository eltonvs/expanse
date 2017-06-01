from bson import ObjectId

from framework import MatchController

from ..dao import MongoFactoryDAO


class MatchControllerCSGO(MatchController):

    def __init__(self):
        super(MatchControllerCSGO, self).__init__(MongoFactoryDAO())

    def validate(self, match):
        err = {}
        if not match.tournament:
            err['empty_tournament'] = True
        if not match.team1 or not match.team2:
            err['empty_team'] = True
        elif match.team1 == match.team2:
            err['against_himself'] = True

        return err

    def set_match_teams(self, match, team1, team2):
        query = {'_id': ObjectId(match)}
        update = {'team1': ObjectId(team1), 'team2': ObjectId(team2)}
        self.match_dao.update(query, update)

    def get_match_teams(self, match_id):
        match = self.match_dao.get_one({"_id": ObjectId(match_id)})
        if match:
            team_dao = self.factory_dao.team_DAO()

            teams = []
            teams.append(team_dao.get_one({"_id": ObjectId(match.team1)}))
            teams.append(team_dao.get_one({"_id": ObjectId(match.team2)}))

            return teams
        return []

    def set_time(self, match, time):
        query = {'_id': ObjectId(match)}
        update = {'time': time}
        self.match_dao.update(query, update)
