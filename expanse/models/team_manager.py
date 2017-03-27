from ..models.user import User
class TeamManager(User):
	"""User Model to store team manager data in runtime"""
	def __init__(self, name, username, email, password, locale, team):
		User.__init__(self, name, username, email, password, locale)
		self._teams = [team]

	@property
	def teams(self):
		return self._teams

	@teams.setter
	def teams(self, value):
		self._teams = value