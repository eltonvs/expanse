from ..utils.security import SecurityTools
from ..dao.user import UserDAO


class ExpanseController(object):
    """Controller Layer for User Object"""

    def __init__(self, request):
        self.request = request
        self.user_dao = UserDAO()
        self.security_tools = SecurityTools()

    def login(self, email, password):
        err = self.validate_email(email)
        if not err:
            hashed_password = self.get_password_from_email(email)
            if (not hashed_password or not self.security_tools.check_password(
                    password, hashed_password)):
                err['invalid_user'] = True
        return err

    def validate_email(self, email):
        err = {}
        if not email:
            err['invalid_email'] = True

        return err

    def get_password_from_email(self, email):
        user = self.user_dao.get_user_from_email(email)
        if user:
            return user.password
