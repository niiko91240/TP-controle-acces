from abc import ABC, abstractmethod

class ILecteur(ABC):

    @property
    @abstractmethod
    def badge_detecte(self) -> bool:
        pass

    @property
    @abstractmethod
    def badge_bloque(self) -> bool:
        pass