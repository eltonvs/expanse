from ..models.database import MongoDatabase
from ..models.notification import Notification
from .generic import GenericDAO


class NotificationDAO(GenericDAO):
    """Notification Data Access Object implementing Borg Pattern"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, notification):
        print("Not implemented yet")
        pass

    def remove(self, notification):
        print("Not implemented yet")
        pass

    def update(self, notification):
        print("Not implemented yet")
        pass

    def get(self, query):
        notification = self.db.users.find(query)
        return notification

    def get_notifications_from_user(self, user_id):
        notifications = self.get({"user_id": user_id})
        if notifications is not None:
            notifications_list = []
            for n in notifications:
                notifications_list.append(
                    Notification(n['user_id'], n['title'], n['message']))
            return notifications_list

    def list(self):
        notifications = list(self.db.notifications.find())
        return notifications
