from bson import ObjectId

from ..dao.team import TeamDAOMongo
from ..dao.user import UserDAOMongo


class TeamController(object):
    """Controller Layer for Team Object"""

    def __init__(self):
        self.team_dao = TeamDAOMongo()

    def register(self, team):
        err = self.validate(team)
        if not err:
            err = self.team_dao.insert(team)
        return err

    def validate(self, team):
        err = {}
        if not team.name:
            err['empty_name'] = True
        if not team.team_manager:
            err['empty_team_manager'] = True

        return err

    def get_teams(self):
        return self.team_dao.list()

    def get_managed_teams(self, user):
        return self.team_dao.get({"team_manager_id": user})

    def append_lines(self, value):
        self.team_dao.lines.append(value)

    def extend_lines(self, value):
        self.team_dao.lines.extend(value)

    def add_player(self, team_id, player):
        query = {'_id': ObjectId(team_id)}
        update = {'$addToSet': {'players': player}}
        self.team_dao.update(query, update)

    def get_players(self, team_id):
        team = self.team_dao.get_one({"_id": ObjectId(team_id)})
        players = []
        if team:
            user_dao = UserDAOMongo()
            for p in team.players:
                if (ObjectId.is_valid(p)):
                    players.append(user_dao.get_one({"_id": ObjectId(p)}))
                else:
                    players.append(p)
        return players
