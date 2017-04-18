class Notification(object):
    """Notification Model to store notifications data in runtime"""

    def __init__(self, user_id, title, message, url):
        self._id = None
        self._user_id = user_id
        self._title = title
        self._message = message
        self._url = url

    def __str__(self):
        return '[' + self._user_id + '] - ' + self._title + ': ' + self._message

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
