import steamapi


class SteamController(object):
    """Borg Pattern"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        steamapi.core.APIConnection(
            api_key="C726096ADF06343A0EDD6A17F626DD17",
            validate_key=True)

    def get_steamuser_from_username(self, username):
        try:
            user = steamapi.user.SteamUser(userurl=username)
        except steamapi.errors.UserNotFoundError:
            user = None
        return user
