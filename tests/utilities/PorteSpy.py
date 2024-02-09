from src.IPorte import IPorte

class PorteSpy(IPorte):

    def __init__(self, nb_appels_methode_ouvrir=0):
        self._nb_appels_methode_ouvrir = nb_appels_methode_ouvrir

    @property
    def nb_appels_methode_ouvrir(self):
        return self._nb_appels_methode_ouvrir

    def ouvrir(self):
        self._nb_appels_methode_ouvrir = self._nb_appels_methode_ouvrir + 1