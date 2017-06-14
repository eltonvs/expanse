from abc import ABCMeta, abstractmethod
from bson import ObjectId


class TeamController(object):
    __metaclass__ = ABCMeta

    def __init__(self, factory_dao):
        self.factory_dao = factory_dao
        self.team_dao = self.factory_dao.team_DAO()

    def register(self, team):
        err = self.validate(team)
        if not err:
            inserted_id = self.team_dao.insert(team)
            if not inserted_id:
                return {'db_error': True}
            team.id = inserted_id
        return err

    def get_teams(self):
        return self.team_dao.list()

    def get_team_from_id(self, team_id):
        return self.team_dao.get_one({"_id": ObjectId(team_id)})

    def get_managed_teams(self, user):
        return self.team_dao.get({"team_manager_id": user})

    def add_player(self, team_id, player):
        query = {'_id': ObjectId(team_id)}
        update = {'$addToSet': {'players': player}}
        self.team_dao.update(query, update)

    def get_players(self, team_id):
        team = self.get_team_from_id(team_id)
        players = []
        if team:
            user_dao = self.factory_dao.user_DAO()
            for p in team.players:
                if (ObjectId.is_valid(p)):
                    players.append(user_dao.get_one({"_id": ObjectId(p)}))
                else:
                    players.append(p)
        return players

    @abstractmethod
    def validate(self, match):
        pass
