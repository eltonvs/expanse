from abc import ABCMeta, abstractmethod
from bson import ObjectId

from framework import TournamentType, TournamentStatus, AbstractTournamentTypeController

from ..dao import MongoFactoryDAO
from ..models import Notification, MatchSoccer
from ..controllers import NotificationController, MatchControllerSoccer


class RoundRobinController(AbstractTournamentTypeController):
    """Controller to Round Robin Tournaments"""

    def __init__(self, tournament_id, teams):
        self._tournament_id = tournament_id
        self._teams = teams

    def generate_schedule(self):
        if len(self._teams) % 2 != 0:
            self._teams.append(None)

        matches = []
        for it in range(len(self._teams) - 1):
            matches.append([
                        MatchSoccer(
                            self._tournament_id,
                            self._teams[i],
                            self._teams[i + len(self._teams) // 2])
                            for i in range(len(self._teams) // 2)])
            self._teams.insert(1, self._teams.pop())

        # if away_home:
        #     return matches + [[a[::-1] for a in m] for m in matches]

        return matches


class TournamentController(object):
    """Controller layer for Tournament object"""

    def __init__(self):
        self.factory_dao = MongoFactoryDAO()
        self.tournament_dao = self.factory_dao.tournament_DAO()

    def register(self, tournament):
        err = self.validate(tournament)
        if not err:
            inserted_id = self.tournament_dao.insert(tournament)
            if not inserted_id:
                return {'db_error': True}
            # Add new id to tournament object
            tournament.id = inserted_id
            self.notify_near_users(tournament)
        return err

    def validate(self, tournament):
        err = {}
        if not tournament.name:
            err['empty_name'] = True
        if not tournament.organizer:
            err['empty_organizer'] = True
        if not tournament.locale:
            err['empty_locale'] = True

        return err

    def notify_near_users(self, tournament):
        user_dao = self.factory_dao.user_DAO()
        notification_controller = NotificationController()
        nearest_users = user_dao.get_users_from_locale(tournament.locale)
        for nu in nearest_users:
            usr_id = nu.id
            if usr_id == tournament.organizer:
                continue
            notification = Notification(
                usr_id,
                "Near Tournament",
                "\"" + tournament.name + "\" is near from you!",
                "/tournaments/dash/" + str(tournament.id)
            )
            notification_controller.add(notification)

    def add_team(self, tournament_id, team_id):
        if tournament_id and team_id:
            query = {'_id': ObjectId(tournament_id)}
            update = {'$addToSet': {'teams': ObjectId(team_id)}}

            self.tournament_dao.update(query, update)

            # team = tournament.team
            # team.append(team_id)
            # tournament.team = team

    def add_match(self, tournament_id, match_id):
        if tournament_id and match_id:
            query = {'_id': ObjectId(tournament_id)}
            update = {'$addToSet': {'matches': ObjectId(match_id)}}

            self.tournament_dao.update(query, update)

    def get_tournaments(self):
        return self.tournament_dao.list()

    def get_organized_tournaments(self, user):
        return self.tournament_dao.get({"organizer_id": user})

    def get_tournament_teams(self, tournament_id):
        tournament = self.tournament_dao.get_one(
            {"_id": ObjectId(tournament_id)})
        tournament_teams = tournament.teams

        if tournament_teams:
            team_dao = self.factory_dao.team_DAO()
            teams = []

            for team_id in tournament_teams:
                team = team_dao.get_one({"_id": team_id})
                if team:
                    teams.append(team)

            return teams
        return []

    def get_tournament_matches(self, tournament_id):
        tournament = self.tournament_dao.get_one(
            {"_id": ObjectId(tournament_id)})

        if tournament.matches:
            match_dao = self.factory_dao.match_DAO()
            matches = []

            for match_id in tournament.matches:
                match = match_dao.get_one({"_id": match_id})
                if match:
                    matches.append(match)

            return matches
        return []

    def get_tournament_schedule(self, tournament_id):
        # TODO: Improve this code
        tournament = self.tournament_dao.get_one(
            {'_id': ObjectId(tournament_id)})

        if tournament:
            schedule = []
            match_dao = self.factory_dao.match_DAO()
            for phase in tournament.phases:
                schedule.append(
                    [[match_dao.get_one({"_id": match_id})
                      for match_id in tournament_round]
                     for tournament_round in phase.schedule])
            for i in range(len(schedule)):
                tournament.phases[i].schedule = schedule[i]

            return tournament.phases

        return []

    def generate_schedule(self, tournament_id):
        tournament = self.tournament_dao.get_one(
            {"_id": ObjectId(tournament_id)})

        update = {'$set': {'status': TournamentStatus.RUNNING}}
        self.tournament_dao.update({'_id': tournament.id}, update)

        for phase in tournament.phases:
            schedule_generator = None
            if phase.type is TournamentType.ROUND_ROBIN:
                schedule_generator = RoundRobinController(
                    tournament_id, tournament.teams)
            elif phase.type is TournamentType.KNOCKOUT:
                # Do what need to be done
                pass
            elif phase.type is TournamentType.GROUP:
                # Do what need to be done
                pass

            if schedule_generator:
                phase.schedule = schedule_generator.generate_schedule()

        # Need to create on db each match on schedule and update tournament db
        match_controller = MatchControllerSoccer()
        for phase in tournament.phases:
            for tournament_round in phase.schedule:
                for match in tournament_round:
                    match_controller.register(match)

        self.put_schedule_on_db(tournament)

        return tournament.phases

    def put_schedule_on_db(self, tournament):
        # TODO: Remove idx
        idx = 0
        for phase in tournament.phases:
            update = {'phases.{}.teams'.format(idx): phase.teams, 'phases.{}.schedule'.format(
                idx): [[match.id for match in tournament_round] for tournament_round in phase.schedule]}

            self.tournament_dao.update({'_id': tournament.id}, {'$set': update})

            idx += 1
