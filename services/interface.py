from abc import ABCMeta, abstractmethod


class IService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        pass
