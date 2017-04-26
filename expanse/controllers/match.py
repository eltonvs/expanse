from bson import ObjectId

from ..dao.match import MatchDAOMongo
from ..dao.team import TeamDAOMongo


class MatchController(object):

    def __init__(self):
        self.match_dao = MatchDAOMongo()

    def register(self, match):
        err = self.validate(match)
        if not err:
            inserted_id = self.match_dao.insert(match)
            if not inserted_id:
                return {'db_error': True}
            match.id = inserted_id
        return err

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
            team_dao = TeamDAOMongo()

            teams = []
            teams.append(team_dao.get_one({"_id": ObjectId(match.team1)}))
            teams.append(team_dao.get_one({"_id": ObjectId(match.team2)}))

            return teams
        return []

    def set_score(self, match, score1, score2):
        query = {'_id': ObjectId(match)}
        update = {'$set': {'score': [score1, score2]}}
        self.match_dao.update(query, update)

    def set_time(self, match, time):
        query = {'_id': ObjectId(match)}
        update = {'time': time}
        self.match_dao.update(query, update)

    def get_matches(self):
        return self.match_dao.list()

    def get_matches_from_tournament(self, tournament):
        return self.match_dao.get({"tournament": ObjectId(tournament)})
