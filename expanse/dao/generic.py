from abc import ABCMeta, abstractmethod


class GenericDAO():
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, thing):
        pass

    @abstractmethod
    def remove(self, thing):
        pass

    @abstractmethod
    def update(self, thing):
        pass

    @abstractmethod
    def get(self, thing):
        pass

    @abstractmethod
    def list(self, thing):
        pass
