import unittest
from unittest.mock import Mock
from vastustaja_tekoaly import Vastustaja
from malli import Malli

class Malli1Stub:
    def __init__(self):
        self.seuraava = "k"
        self.syvyys = 1

    def pisteet(self):
        return 1
    
    def paivita_pisteet(self, syote):
        return syote == "k"

    def hae_seuraava(self, syote):
        pass

class Malli2Stub:
    def __init__(self):
        self.seuraava = "k"
        self.syvyys = 5

    def pisteet(self):
        return 2
    
    def paivita_pisteet(self, syote):
        return syote == "k"

class TestVastustaja(unittest.TestCase):
    def setUp(self):
        lista = [2, 4, 3]
        self.vastustaja = Vastustaja(lista)

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
        
    def test_paivita_pisteet_malleihin(self):
        malli_mock = Mock()
        malli_mock.syvyys = 1
        malli_mock2 = Mock()
        malli_mock2.syvyys = 5
        vastustaja = Vastustaja([malli_mock, malli_mock2])
        vastustaja.paivita_mallit("pk")
        malli_mock.paivita_pisteet.assert_called_with("k")
        malli_mock2.paivita_pisteet.assert_called_with("k")
        malli_mock.hae_seuraava.assert_called_with("pk")
