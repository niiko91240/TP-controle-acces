from abc import ABC, abstractmethod

class ILog(ABC):

    @property
    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def create_log(self):
        pass