from framework import Score


class ScoreSoccer(Score):
	def __init__(self, team1=None, team2=None):
		super(ScoreSoccer, self).__init__([team1, team2])
