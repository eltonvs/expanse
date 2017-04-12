class TournamentType:
    """Enum to represent Tournament Types"""
    ROUND_ROBIN = 0
    KNOCKOUT = 1
    GROUP = 2


class TournamentStatus:
    """Enum to represent Tournament Status"""
    OPENED = 0
    RUNNING = 1
    FINISHED = 2


class TournamentPhase(object):

    def __init__(self, type, teams=[], schedule=[]):
        self._type = int(type)
        self._teams = teams
        self._schedule = schedule

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def teams(self):
        return self._teams

    @teams.setter
    def teams(self, value):
        self._teams = value

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value


class Tournament(object):
    """Tournament model to store tournament data in runtime"""

    def __init__(self, name, organizer, locale, status=0, phases=[]):
        self._id = None
        self._name = name
        self._organizer = organizer
        self._locale = locale
        self._teams = []
        self._matches = []
        self._status = status
        self._phases = phases

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

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def phases(self):
        return self._phases

    @phases.setter
    def phases(self, value):
        self._phases = value
