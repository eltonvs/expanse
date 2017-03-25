from expanse.models.user.user import User
from expanse.dao.user_dao import UserDAO

class UserController(object):

    def __init__(self):
        pass

    def signup(self, username, name, password, email, address):
        print "controller signup"
        if username != '' and name != '' and password != '' and address != '' and email != '':
            user = User(name, username, email, password, address)

            user_dao = UserDAO()
            user_dao.insertUser(user)

            return user

        else:
            return None
