from src.ILecteur import ILecteur

class LecteurFake(ILecteur):

    def __init__(self, id, badge_detecte=False, badge_detecte_prochain_appel=False, badge_bloque=False, badge_id=0):
        self._badge_detecte = badge_detecte
        self._badge_detecte_prochain_appel = badge_detecte_prochain_appel
        self._badge_bloque = badge_bloque
        self._id = id
        self._badge_id = badge_id


    @property
    def badge_detecte(self):
        res = self._badge_detecte_prochain_appel
        self._badge_detecte_prochain_appel = False
        return res

    @property
    def badge_bloque(self):
        return self._badge_bloque

    @property
    def id(self):
        return self._id

    def simuler_presentation_badge(self, badge_id):
        self._badge_detecte_prochain_appel = True
        self._badge_id = badge_id

    def bloquer(self):
        self._badge_bloque = True

    def debloquer(self):
        self._badge_bloque = False
