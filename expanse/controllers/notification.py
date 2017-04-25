from ..dao.notification import NotificationDAOMongo
from ..utils.security import SecurityTools


class NotificationController(object):
    """Controller Layer for Notification Object"""

    def __init__(self):
        self.security_tools = SecurityTools()
        self.notification_dao = NotificationDAOMongo()

    def remove(self, notification_id):
        self.notification_dao.remove({'_id': notification_id})

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
        # see if there is any repeated ivitation
        if notification.invitation == True:
            my_notifications = self.notification_dao.get_notifications_from_user(notification.user_id)
            if  my_notifications != []:
                for my_notification in my_notifications:
                    if my_notification.team_id == notification.team_id:
                        err['repeated_invitation'] = True

        return err

    def get_notifications(self, user_id):
        return self.notification_dao.get_notifications_from_user(user_id)
