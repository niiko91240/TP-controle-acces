from .ILecteur import ILecteur
from .IPorte import IPorte

class MoteurOuverture:
    def __init__(self, *portes: IPorte):
        self._portes = portes

    def interroger(self, lecteurs):
        for lecteur in lecteurs:
            if lecteur.badge_detecte and not lecteur.badge_bloque:
                for porte in self._portes:
                    porte.ouvrir()