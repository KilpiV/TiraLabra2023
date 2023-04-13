import unittest
from vastustaja_tekoaly import Vastustaja

class TestVastustaja(unittest.TestCase):
    def setUp(self):
        self.vastustaja = Vastustaja()

    def test_aloitus_valinta_oikein(self):
        self.assertEqual(self.vastustaja._valinta, 0)

