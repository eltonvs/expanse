class Game(object):
    """Game Model to store user data in runtime"""

    def __init__(self, name, abbreviation, steamid=None):
        self._id = None
        self._name = name
        self._steamid = steamid
        self._abbreviation = abbreviation

    def __str__(self):
        return self._name

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
    def abbreviation(self):
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, value):
        self._abbreviation = value

    @property
    def steamid(self):
        return self._steamid

    @steamid.setter
    def steamid(self, value):
        self._steamid = value
