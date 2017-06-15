from framework import Match

from .score import ScoreCSGO


class MatchCSGO(Match):
    """Mach Model to store user data in runtime"""

    def __init__(self, tournament, team1, team2, score=ScoreCSGO(), time=None):
        super(MatchCSGO, self).__init__(tournament, score)
        self._team1 = team1
        self._team2 = team2
        self._time = time

    @property
    def team1(self):
        return self._team1

    @team1.setter
    def team1(self, team1):
        self._team1 = team1

    @property
    def team2(self):
        return self._team2

    @team2.setter
    def team2(self, team2):
        self._team2 = team2

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time

    @property
    def winner(self):
        # No score set
        if not self.score.team1 or not self.score.team2:
            return None

        if self.score.team1 > self.score.team2:
            return self.team1
        elif self.score.team2 > self.score.team1:
            return self.team2
        return [self.team1, self.team2]
