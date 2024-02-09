import unittest
from utilities.LecteurFake import LecteurFake
from utilities.PorteSpy import PorteSpy
from src.MoteurOuverture import MoteurOuverture


class TestMain(unittest.TestCase):

    def test_cas_nominal(self):
        # ETANT DONNE un lecteur ayant détecté un badge
        lecteur = LecteurFake()
        lecteur.simuler_presentation_badge()
        # ET une porte lui étant liée
        porte = PorteSpy()
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur = MoteurOuverture(porte)
        moteur.interroger(lecteur)
        # ALORS cette porte s'ouvre
        self.assertTrue(porte.methode_ouvrir_appelee)

    def test_cas_sans_interrogation(self):
        # ETANT DONNE un lecteur ayant détecté un badge
        lecteur = LecteurFake()
        lecteur.simuler_presentation_badge()
        # ET une porte lui étant liée
        porte = PorteSpy()
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur = MoteurOuverture(porte)
        # ALORS cette porte ne s'ouvre pas
        self.assertFalse(porte.methode_ouvrir_appelee)