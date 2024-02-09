from src.ILecteur import ILecteur

class LecteurFake(ILecteur):

    def __init__(self, badge_detecte=False, badge_detecte_prochain_appel=False, badge_bloque=False):
        self._badge_detecte = badge_detecte
        self._badge_detecte_prochain_appel = badge_detecte_prochain_appel
        self._badge_bloque = badge_bloque


    @property
    def badge_detecte(self):
        res = self._badge_detecte_prochain_appel
        self._badge_detecte_prochain_appel = False
        return res

    @property
    def badge_bloque(self):
        return self._badge_bloque

    def simuler_presentation_badge(self):
        self._badge_detecte_prochain_appel = True

    def bloquer(self):
        self._badge_bloque = True

    def debloquer(self):
        self._badge_bloque = False
