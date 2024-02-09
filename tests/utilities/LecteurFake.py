from src.ILecteur import ILecteur

class LecteurFake(ILecteur):

    def __init__(self, badge_detecte=False, badge_detecte_prochain_appel=False):
        self._badge_detecte = badge_detecte
        self._badge_detecte_prochain_appel = badge_detecte_prochain_appel

    @property
    def badge_detecte(self):
        res = self._badge_detecte_prochain_appel
        self._badge_detecte_prochain_appel = False
        return res

    def simuler_presentation_badge(self):
        self._badge_detecte_prochain_appel = True
