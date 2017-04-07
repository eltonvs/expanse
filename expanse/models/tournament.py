class Tournament(object):
    """Tournament model to store tournament data in runtime"""

    def __init__(self, name, organizer, locale):
        self._id = None
        self._name = name
        self._organizer = organizer
        self._locale = locale
        self._teams = []
        self._matches = []

    def __str__(self):
        return (self._name)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def organizer(self):
        return self._organizer

    @organizer.setter
    def organizer(self, value):
        self._organizer = value

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value

    @property
    def teams(self):
        return self._teams

    @teams.setter
    def teams(self, value):
        self._teams = value

    @property
    def matches(self):
        return self._matches

    @matches.setter
    def matches(self, value):
        self._matches = value


class Match(object):
    """Mach Model to store user data in runtime"""

    def __init__(self):
        self._id = None
        self._teams = []
        self._score = [0, 0]
        self._time = None

    def __str__(self):
        return (self._name)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time
