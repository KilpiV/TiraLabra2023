import unittest
from unittest.mock import Mock
from vastustaja_tekoaly import Vastustaja

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
