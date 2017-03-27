class Line(object):
    """User Model to store line data in runtime"""

    def __init__(self, name, locale, avalible_mach_time):
        self._name = name
        self._locale = locale
        self._avalible_mach_time = avalible_mach_time
        

    def __str__(self):
        return (self.name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value

    @property
    def avalible_mach_time(self):
        return self._avalible_mach_time

    @avalible_mach_time.setter
    def avalible_mach_time(self, value):
        self._avalible_mach_time = value
