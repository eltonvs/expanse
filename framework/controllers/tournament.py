from abc import ABCMeta, abstractmethod


class AbstractTournamentTypeController(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_schedule(self):
        pass




