from ..dao.user import UserDAO


class UserController(object):
    """Controller Layer for User Object"""

    def __init__(self):
        self.user_dao = UserDAO()

    def register(self, user):
        err = self.validate(user)
        if not err:
            err = self.user_dao.insert(user)
        return err

    def validate(self, user):
        err = {}
        if not user.name:
            err['empty_name'] = True
        if not user.username:
            err['empty_username'] = True
        if not user.email:
            err['empty_email'] = True
        if not user.password:
            err['empty_password'] = True
        if not user.locale:
            err['empty_locale'] = True

        return err

    def getUsers(self):
        return self.user_dao.list()
