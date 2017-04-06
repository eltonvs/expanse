class User(object):
    """User Model to store user data in runtime"""

    def __init__(self, name, username, email, password, locale):
        self._name = name
        self._username = username
        self._email = email
        self._password = password
        self._locale = locale
        self._my_id = None

    def __str__(self):
        return (self._name)

    @property
    def username(self):
        return self._name

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value

    @property
    def my_id(self):
        return self._my_id

    @my_id.setter
    def my_id(self, value):
        self._my_id = value
