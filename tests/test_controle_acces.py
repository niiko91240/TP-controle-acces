import unittest
from utilities import LecteurFake, PorteSpy
from src.MoteurOuverture import MoteurOuverture


class TestMain(unittest.TestCase):

    def test_cas_nominal(self):
        # ETANT DONNE un lecteur ayant détecté un badge
        lecteur = LecteurFake()
        lecteur.simuler_presentation_badge()
        # ET une porte lui étant liée
        porte = PorteSpy()
        # QUAND le moteur d'ouverture interroge ce lecteur
        MoteurOuverture.interroger(lecteur)
        # ALORS cette porte s'ouvre
        self.assertTrue(porte.methode_ouvrir_appelee())