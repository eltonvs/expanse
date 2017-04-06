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
        if notifications:
            notifications_list = []
            for n in notifications:
                new_notification =  Notification(
                    n['user_id'],
                    n['title'],
                    n['message'])
                new_notification.my_id = n['id']
                notifications_list.append(new_notification)
                   
            return notifications_list

    def get_one(self, query):
        notification = self.db.teams.find_one(query)
        if notification:
            new_notification = Notification(
                notification['user_id'],
                notification['title'],
                notification['message'])
            new_notification.my_id = notification['id']
            return new_notification

    def get_notifications_from_user(self, user_id):
        notifications = self.get({"user_id": user_id})
        if notifications:
            notifications_list = []
            for n in notifications:
                new_notification =  Notification(
                    n['user_id'],
                    n['title'],
                    n['message'])
                new_notification.my_id = n['id']
                notifications_list.append(new_notification)
            return notifications_list

    def list(self):
        return self.get({})
