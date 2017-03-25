from expanse.models.user.user import User

class UserController(object):

    def __init__(self):
        pass

    def signup(self, username, name, password, email, address):
        print "controller signup"
        if username != '' and name != '' and password != '' and address != '' and email != '':
            user = User(name, username, email, password, address)

            ## Save user on db

            return user

        else:
            return None
