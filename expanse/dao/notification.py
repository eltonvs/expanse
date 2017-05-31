from abc import ABCMeta, abstractmethod

from framework.dao.generic import GenericDAO

from ..models.database import MongoDatabase
from ..models.notification import Notification


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
            "url": notification.url,
            "invitation": notification.invitation,
            "team_id": notification.team_id
        }
        return self.db.notifications.insert(notification_to_insert)

    def remove(self, query):
        self.db.notifications.remove(query)

    def update(self, query, update):
        self.db.notifications.update(query, update)

    def get(self, query):
        notifications = list(self.db.notifications.find(query))
        if notifications:
            notifications_list = []
            for n in notifications:
                new_notification = Notification(
                    n.get('user_id', ''),
                    n.get('title', ''),
                    n.get('message', ''),
                    n.get('url', ''),
                    n.get('invitation', False),
                    n.get('team_id', '')
                )
                new_notification.id = n.get('_id', '')
                notifications_list.append(new_notification)
            return notifications_list
        return []

    def get_one(self, query):
        notification = self.db.teams.find_one(query)
        if notification:
            new_notification = Notification(
                notification.get('user_id', ''),
                notification.get('title', ''),
                notification.get('message', ''),
                notification.get('url', ''),
                notification.get('invitation', False),
                notification.get('team_id', '')
            )
            new_notification.id = notification.get('_id', '')

            return new_notification

    def get_notifications_from_user(self, user_id):
        return self.get({"user_id": user_id})

    def list(self):
        return self.get({})
