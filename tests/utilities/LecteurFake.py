from src.ILecteur import ILecteur

class LecteurFake(ILecteur):

    def __init__(self, badge_detecte):
        self._badge_detecte = badge_detecte

    @property
    def badge_detecte(self):
        return self._badge_detecte

    def simuler_presentation_badge(self):
        self._badge_detecte = True