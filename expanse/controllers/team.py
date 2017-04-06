from bson import ObjectId

from ..dao.team import TeamDAOMongo
from ..dao.user import UserDAOMongo

from bson import ObjectId

class TeamController(object):
    """Controller Layer for Team Object"""

    def __init__(self, request):
        self.request = request
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
        teams = self.team_dao.list()
        user_dao = UserDAOMongo()

        # for team in teams:
            # team_manager = user_dao.get_one({"_id": team.team_manager})
            # team.team_manager = team_manager.name

        return teams


    def get_user_teams(self, user):
        return self.team_dao.get({"team_manager_id": user})

    def append_lines(self, value):
        self.team_dao.lines.append(value)

    def extend_lines(self, value):
        self.team_dao.lines.extend(value)

    def add_player(self, team_id, player):
        query = {'_id': ObjectId(team_id)}
        update = {'$addToSet': {'players': player}}
        self.team_dao.update(query, update)
