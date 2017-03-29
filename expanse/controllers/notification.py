from ..dao.notification import NotificationDAO
from ..utils.security import SecurityTools


class NotificationController(object):
    """Controller Layer for Notification Object"""

    def __init__(self, request):
        self.request = request
        self.security_tools = SecurityTools()
        self.notification_dao = NotificationDAO()

    def add(self, notification):
        err = self.validate(notification)
        if not err:
            err = self.notification_dao.insert(notification)
        return err

    def validate(self, notification):
        err = {}
        if not notification.user_id:
            err['empty_user'] = True
        if not notification.title:
            err['empty_title'] = True
        if not notification.message:
            err['empty_message'] = True

        return err

    def get_notifications(self, user_id):
        return self.notification_dao.get_notifications_from_user(user_id)
