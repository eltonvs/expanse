from ..dao.user import UserDAOMongo
from ..utils.security import SecurityTools


class UserController(object):
    """Controller Layer for User Object"""

    def __init__(self):
        self.security_tools = SecurityTools()
        self.user_dao = UserDAOMongo()

    def register(self, user):
        err = self.validate(user)
        if not err:
            user.password = self.security_tools.hash_password(user.password)
            inserted_id = self.user_dao.insert(user)
            if not inserted_id:
                return {'db_error': True}
            # Add new id to tournament object
            user.id = inserted_id
        return err

    def validate(self, user):
        err = {}
        if not user.name:
            err['empty_name'] = True
        if not user.username:
            err['empty_username'] = True
        if not user.email:
            err['empty_email'] = True
        elif self.get_user_id_from_email(user.email) is not None:
            err['duplicate_email'] = True
        if not user.password:
            err['empty_password'] = True
        if not user.locale:
            err['empty_locale'] = True

        return err

    def get_users(self):
        users = self.user_dao.list()
        return users

    def get_user_from_email(self, email):
        return self.user_dao.get_user_from_email(email)

    def get_user_id_from_email(self, email):
        return self.user_dao.get_user_id_from_email(email)
