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
        self.assertEqual(1, porte.nb_appels_methode_ouvrir)

    def test_cas_sans_interrogation(self):
        # ETANT DONNE un lecteur ayant détecté un badge
        lecteur = LecteurFake()
        lecteur.simuler_presentation_badge()
        # ET une porte lui étant liée
        porte = PorteSpy()
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur = MoteurOuverture(porte)
        # ALORS cette porte ne s'ouvre pas
        self.assertEqual(0, porte.nb_appels_methode_ouvrir)

    def test_cas_sans_presentation_badge(self):
        # ETANT DONNE un lecteur
        lecteur = LecteurFake()
        # ET une porte lui étant liée
        porte = PorteSpy()
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur = MoteurOuverture(porte)
        moteur.interroger(lecteur)
        # ALORS cette porte ne s'ouvre pas
        self.assertEqual(0, porte.nb_appels_methode_ouvrir)

    def test_cas_2_presentation(self):
        # ETANT DONNE un lecteur ayant detecté un badge
        lecteur = LecteurFake()
        lecteur.simuler_presentation_badge()
        # ET une porte lui étant liée
        porte = PorteSpy()
        # QUAND le moteur d'ouverture interroge deux fois ce lecteur
        moteur = MoteurOuverture(porte)
        moteur.interroger(lecteur)
        moteur.interroger(lecteur)
        # ALORS cette porte ne s'ouvre pas
        self.assertEqual(1, porte.nb_appels_methode_ouvrir)

    def test_cas_plusieurs_portes(self):
        # ETANT DONNE un lecteur ayant detecté un badge
        lecteur = LecteurFake()
        lecteur.simuler_presentation_badge()
        # ET deux portes lui étant liées
        porte1 = PorteSpy()
        porte2 = PorteSpy()
        # QUAND le moteur d'ouverture interroge deux fois ce lecteur
        moteur = MoteurOuverture(porte1, porte2)
        moteur.interroger(lecteur)
        # ALORS ces portes s'ouvrent
        self.assertEqual(1, porte1.nb_appels_methode_ouvrir)
        self.assertEqual(1, porte2.nb_appels_methode_ouvrir)

    def test_cas_plusieurs_lecteurs(self):
        # ETANT DONNE deux lecteurs ayant detecté un badge
        lecteur1 = LecteurFake()
        lecteur2 = LecteurFake()
        lecteur2.simuler_presentation_badge()
        # ET deux portes lui étant liées
        porte = PorteSpy()
        # QUAND le moteur d'ouverture interroge deux fois ce lecteur
        moteur = MoteurOuverture(porte)
        moteur.interroger([lecteur1, lecteur2])
        # ALORS ces portes s'ouvrent
        self.assertEqual(1, porte.nb_appels_methode_ouvrir)

    def test_detecter_badge_bloque(self):
        # ETANT DONNE un lecteur ayant détecté un badge bloqué
        lecteur = LecteurFake()
        lecteur.bloquer()
        lecteur.simuler_presentation_badge()
        # ET une porte lui étant liée
        porte = PorteSpy()
        moteur = MoteurOuverture(porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger(lecteur)
        # ALORS cette porte ne s'ouvre pas
        self.assertEqual(0, porte.nb_appels_methode_ouvrir)
