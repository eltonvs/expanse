from .team import Team

class Match(object):
	"""Mach Model to store user data in runtime"""
	def __init__(self, team1, team2):
		self._teams = [team1, team2]
        self._score = [0, 0]
        self._my_id = None

	def __str__(self):
		return (self._name)

    @property
    def teams(self):
    	return self._teams

    @teams.setter
    def teams(self, team1, team2):
    	self._teams = [team1, team2]

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def my_id(self):
        return self._my_id

    @my_id.setter
    def my_id(self, value):
        self._my_id = value

