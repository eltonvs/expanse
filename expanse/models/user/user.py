class User(object):
    username = ""
    email = ""
    password = ""
    locale = ""

    def __init__(self, name, username, email, password, locale):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.locale = locale

    def __str__(self):
        return (self.username)