from src.IPorte import IPorte

class PorteSpy(IPorte):

    def __init__(self, methode_ouvrir_appelee):
        self._methode_ouvrir_appelee = methode_ouvrir_appelee

    @property
    def methode_ouvrir_appelee(self):
        return self._methode_ouvrir_appelee

    def ouvrir(self):
        self._methode_ouvrir_appelee = True