from framework import Score


class ScoreCSGO(Score):

    def __init__(self, team1=None, team2=None):
        super(ScoreCSGO, self).__init__([team1, team2])

class ScoreFutebol(Score):
	def __init__(self, team1=None, team2=None):
		super(ScoreFutebol, self).__init__([team1, team2])
