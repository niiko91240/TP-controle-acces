from datetime import datetime
from src.ILog import ILog

class LogSpy(ILog):

    def __init__(self, log=[]):
        self._log = log

    @property
    def log(self):
        return self._log

    def create_log(self, lecteur, statut):
        self.log.append({
            'horodatage': datetime.now().strftime("%d/%m/%Y - %H:%M"),
            'lecteur_id': lecteur.id,
            'badge_id': lecteur._badge_id,
            'statut': statut
        })
