from expanse.models.user.user import User
from expanse.dao.user_dao import UserDAOMongo

class UserController(object):

    def __init__(self):
        pass

    def signup(self, username, name, password, email, address):
        if username != '' and name != '' and password != '' and address != '' and email != '':
            user = User(name, username, email, password, address)

            user_dao = UserDAOMongo()
            user_dao.insertUser(user)

            return user

        else:
            return None

    def getUsers(self):
        user_dao = UserDAOMongo()
        users = user_dao.listUsers()

        return users
