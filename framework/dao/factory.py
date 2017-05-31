from abc import ABCMeta, abstractmethod


class AbstractFactoryDAO(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def match_DAO(self):
        pass

    @abstractmethod
    def notification_DAO(self):
        pass

    @abstractmethod
    def team_DAO(self):
        pass

    @abstractmethod
    def tournament_DAO(self):
        pass
