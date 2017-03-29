class Tournament(object):
    """Tournament model to store tournament data in runtime"""

    def __init__(self, name, organizer):
        self._name = name
        self._organizer = organizer
        self._teams = []

    def __str__(self):
        return (self._name)

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
    def teams(self):
        return self._teams

    @teams.setter
    def teams(self, value):
        self._teams = value
