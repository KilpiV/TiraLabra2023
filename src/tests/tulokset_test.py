import unittest
from tulokset import Tulokset

class TestTulokset(unittest.TestCase):
    def setUp(self):
        self.tulokset = Tulokset()

    def test_konstruktori_tyhjat(self):
        self.assertEqual(0, self.tulokset.pelaaja_pisteet)
        self.assertEqual(0, self.tulokset.vastustaja_pisteet)
        self.assertEqual(0, self.tulokset.tasapeli)
        self.assertEqual([], self.tulokset.tulokset)

    def test_antaa_tuloksen(self):
        self.assertEqual(f"\n Pistetilanne:\n pelaaja - tekoäly \
            \n       0 - 0", str(self.tulokset))

    def test_lisaa_tulos(self):
        pass