from .IPorte import IPorte
from .ILog import ILog

class MoteurOuverture:
    def __init__(self, logs: ILog, *portes: IPorte):
        self._portes = portes
        self._logs = logs

    def interroger(self, lecteurs):
        for lecteur in lecteurs:
            if lecteur.badge_detecte and not lecteur.badge_bloque:
                self._logs.create_log(lecteur, 'ok')
                for porte in self._portes:
                    porte.ouvrir()
            else:
                self._logs.create_log(lecteur, 'ko')
