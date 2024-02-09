from datetime import datetime
from src.ILog import ILog

class LogSpy(ILog):

    def __init__(self, log=[]):
        self._log = log

    @property
    def log(self):
        return self._log

    def create_log(self, statut):
        self.log.append({
            'statut': statut
        })
