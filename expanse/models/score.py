from framework import Score


class ScoreSoccer(Score):

    def __init__(self, team1=None, team2=None):
        super(ScoreSoccer, self).__init__([team1, team2])

    @property
    def team1(self):
        return self._points[0]

    @team1.setter
    def team1(self, value):
        self._points[0] = value

    @property
    def team2(self):
        return self._points[1]

    @team2.setter
    def team2(self, value):
        self._points[1] = value
