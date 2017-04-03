from abc import ABCMeta, abstractmethod

from ..models.database import MongoDatabase
from ..models.notification import Notification
from .generic import GenericDAO


class NotificationDAO(GenericDAO):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_notifications_from_user(self, user_id):
        pass

class NotificationDAOMongo(NotificationDAO):
    """Notification Data Access Object implementing Borg Pattern"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.db = MongoDatabase().instance()

    def insert(self, notification):
        notification_to_insert = {
            "user_id": notification.user_id,
            "title": notification.title,
            "message": notification.message,
        }
        self.db.notifications.insert(notification_to_insert)

    def remove(self, notification):
        print("Not implemented yet")
        pass

    def update(self, notification):
        print("Not implemented yet")
        pass

    def get(self, query):
        notifications = list(self.db.notifications.find(query))
        return notifications

    def get_one(self, query):
        notification = self.db.teams.find_one(query)
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
        return self.get({})
