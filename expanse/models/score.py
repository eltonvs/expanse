from framework import Score


class ScoreCSGO(Score):

    def __init__(self, team1=None, team2=None):
        super(ScoreCSGO, self).__init__([team1, team2])
