import unittest
from unittest.mock import Mock
from vastustaja_tekoaly import Vastustaja
from malli import Malli

class Malli1Stub:
    def __init__(self):
        self.seuraava = "k"

    def pisteet(self):
        return 1

class Malli2Stub:
    def __init__(self):
        self.seuraava = "k"

    def pisteet(self):
        return 2

class TestVastustaja(unittest.TestCase):
    def setUp(self):
        lista = [2, 4, 3]
        self.vastustaja = Vastustaja(lista)
        print("testataan!!!")

    def test_konstruktori_mallit(self):
        pituus = len(self.vastustaja.mallit)
        self.assertEqual(3, pituus)

    def test_konstruktori_eka_malli(self):
        eka = self.vastustaja.nyt_malli
        self.assertEqual(2, eka)

    def test_anna_valinta(self):
        malli_mock1 = Malli1Stub()
        malli_mock2 = Malli2Stub()
        vastustaja = Vastustaja([malli_mock1, malli_mock2])
        seuraava = vastustaja.anna_valinta()
        self.assertEqual(seuraava, "k")
        pass
