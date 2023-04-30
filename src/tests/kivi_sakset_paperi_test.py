import unittest
from kivi_sakset_paperi import KiviSaksetPaperi
from unittest.mock import Mock, patch

class TestKiviSaksetPaperi(unittest.TestCase):
    def setUp(self):
        self.ksp = KiviSaksetPaperi()
        syotteet = ["k", "x"]
        mock_input = Mock(side_effect=syotteet)
        pass
        

    def test_aloita_peli(self):
        self.ksp.aloita_peli()

    pass