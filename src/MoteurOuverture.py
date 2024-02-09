from .ILecteur import ILecteur
from .IPorte import IPorte

class MoteurOuverture:
    def __init__(self, porte: IPorte):
        self._porte = porte

    def interroger(self, lecteur):
        if lecteur.badge_detecte:
            self._porte.ouvrir()