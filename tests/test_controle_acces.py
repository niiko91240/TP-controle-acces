import unittest
from datetime import datetime
from utilities.LecteurFake import LecteurFake
from utilities.PorteSpy import PorteSpy
from utilities.LogSpy import LogSpy
from src.MoteurOuverture import MoteurOuverture
from src.ILog import ILog


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
        moteur.interroger([lecteur])
        # ALORS cette porte ne s'ouvre pas
        self.assertEqual(0, porte.nb_appels_methode_ouvrir)

    def test_detecter_badge_debloque(self):
        # ETANT DONNE un lecteur ayant détecté un badge bloqué
        lecteur = LecteurFake()
        lecteur.bloquer()
        lecteur.debloquer()
        lecteur.simuler_presentation_badge()
        # ET une porte lui étant liée
        porte = PorteSpy()
        moteur = MoteurOuverture(porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger([lecteur])
        # ALORS cette porte ne s'ouvre pas
        self.assertEqual(1, porte.nb_appels_methode_ouvrir)

    def test_detecter_badge_log_ok(self):
        # ETANT DONNE un lecteur ayant détecté un badge non bloqué
        lecteur = LecteurFake()
        lecteur.simuler_presentation_badge()
        log = LogSpy()
        # ET une porte lui étant liée
        porte = PorteSpy()
        moteur = MoteurOuverture(log, porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger([lecteur])
        # ALORS le log renvoit ok
        self.assertEqual('ok', moteur._logs.log[-1]['statut'])

    def test_detecter_badge_log_ko(self):
        # ETANT DONNE un lecteur ayant détecté un badge bloqué
        lecteur = LecteurFake()
        lecteur.simuler_presentation_badge()
        lecteur.bloquer()
        log = LogSpy()
        # ET une porte lui étant liée
        porte = PorteSpy()
        moteur = MoteurOuverture(log, porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger([lecteur])
        # ALORS le log renvoit ko
        self.assertEqual('ko', moteur._logs.log[-1]['statut'])

    def test_detecter_badge_log_id_lecteur(self):
        # ETANT DONNE un lecteur ayant détecté un badge non bloqué
        lecteur = LecteurFake(1)
        lecteur.simuler_presentation_badge()
        log = LogSpy()
        # ET une porte lui étant liée
        porte = PorteSpy()
        moteur = MoteurOuverture(log, porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger([lecteur])
        # ALORS le log renvoit l'id du lecteur
        self.assertEqual(lecteur.id, moteur._logs.log[-1]['lecteur_id'])

    def test_detecter_badge_log_id_lecteur_ko(self):
        # ETANT DONNE un lecteur ayant détecté un badge bloqué
        lecteur = LecteurFake(1)
        lecteur.simuler_presentation_badge(1)
        lecteur.bloquer()
        log = LogSpy()
        # ET une porte lui étant liée
        porte = PorteSpy()
        moteur = MoteurOuverture(log, porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger([lecteur])
        # ALORS le log renvoit l'id du lecteur
        self.assertEqual(lecteur.id, moteur._logs.log[-1]['lecteur_id'])
        self.assertEqual('ko', moteur._logs.log[-1]['statut'])


    def test_detecter_badge_log_id_badge(self):
        # ETANT DONNE un lecteur ayant détecté un badge non bloqué
        lecteur = LecteurFake(1)
        lecteur.simuler_presentation_badge(1)
        log = LogSpy()
        # ET une porte lui étant liée
        porte = PorteSpy()
        moteur = MoteurOuverture(log, porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger([lecteur])
        # ALORS le log renvoit l'id du badge passé dans la fonction simuler presentation badge
        self.assertEqual(1, moteur._logs.log[-1]['badge_id'])

    def test_detecter_badge_log_horodatage(self):
        # ETANT DONNE un lecteur ayant détecté un badge non bloqué
        lecteur = LecteurFake(1)
        lecteur.simuler_presentation_badge(1)
        log = LogSpy()
        # ET une porte lui étant liée
        porte = PorteSpy()
        moteur = MoteurOuverture(log, porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger([lecteur])
        # ALORS le log renvoit l'id du badge passé dans la fonction simuler presentation badge
        self.assertEqual(datetime.now().strftime("%d/%m/%Y - %H:%M"), moteur._logs.log[-1]['horodatage'])
