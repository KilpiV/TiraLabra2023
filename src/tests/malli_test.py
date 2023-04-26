import unittest
from malli import Malli
from unittest.mock import Mock

class TestMalli(unittest.TestCase):
    def setUp(self):
        puu = {"k":1, "kp":1, "p":2, "kpp":1, "pp":1}
        self.malli = Malli(1, 3, puu)

    def test_konstruktorin_eka_oikein(self):
        eka = self.malli.seuraava
        self.toinenMalli = Malli(1, 3, {}, "p")
        toisenEka = self.toinenMalli.seuraava
        self.assertEqual(eka, "k")
        self.assertEqual(toisenEka, "p")

    def test_konstruktorin_arvot_oikein(self):
        malliNro = self.malli.syvyys
        pisteet = self.malli.pisteet()
        self.assertEqual(malliNro, 1)
        self.assertEqual(pisteet, 0)

    def test_voittaja_palauttaa_oikein(self):
        pelaaja = "k"
        tekoaly = "p"
        tulos = self.malli.voittaja(pelaaja, tekoaly)
        self.assertEqual(tulos, 1)
        tekoaly = "s"
        tulos = self.malli.voittaja(pelaaja, tekoaly)
        self.assertEqual(tulos, -1)
        tekoaly = "k"
        tulos = self.malli.voittaja(pelaaja, tekoaly)
        self.assertEqual(tulos, 0)
        pelaaja = "p"
        tekoaly = "s"
        tulos = self.malli.voittaja(pelaaja, tekoaly)
        self.assertEqual(tulos, 1)
        pelaaja = "s"
        tekoaly = "k"
        tulos = self.malli.voittaja(pelaaja, tekoaly)
        self.assertEqual(tulos, 1)

    def test_tn_voittajan_paivitys(self):
        taulu = [3, 0, 5]
        self.malli.paivita_tn_voittaja(taulu)
        tnSeuraava = self.malli.seuraava
        self.assertEqual(tnSeuraava, "s")
        taulu = [0, 2, 0]
        self.malli.paivita_tn_voittaja(taulu)
        tnSeuraava = self.malli.seuraava
        self.assertEqual(tnSeuraava, "k")
        taulu = [3, 0, 0]
        self.malli.paivita_tn_voittaja(taulu)
        tnSeuraava = self.malli.seuraava
        self.assertEqual(tnSeuraava, "p")

    def test_tn_voittajaa_ei_vaihdeta(self):
        taulu = [0, 0, 0]
        self.malli.paivita_tn_voittaja(taulu)
        tnSeuraava = self.malli.seuraava
        self.assertEqual(tnSeuraava, "k")

    def test_paivittaa_pisteet(self):
        self.malli.paivita_pisteet("p")
        pisteet = self.malli.pisteet()
        self.assertEqual(pisteet, -1)

    def test_paivittaa_pisteet_useasti(self):
        self.malli.paivita_pisteet("p")
        self.malli.paivita_pisteet("p")
        self.malli.paivita_pisteet("p")
        self.malli.paivita_pisteet("p")
        pisteet = self.malli.pisteet()
        self.assertEqual(pisteet, -3)