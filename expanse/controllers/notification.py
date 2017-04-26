from ..dao.notification import NotificationDAOMongo
from ..utils.security import SecurityTools


class NotificationController(object):
    """Controller Layer for Notification Object"""

    def __init__(self):
        self.security_tools = SecurityTools()
        self.notification_dao = NotificationDAOMongo()

    def add(self, notification):
        err = self.validate(notification)
        if not err:
            inserted_id = self.notification_dao.insert(notification)
            if not inserted_id.is_valid():
                return {'db_error': True}
            notification.id = inserted_id
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
