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

    def test_tasapeli(self):
        self.assertTrue(self.tulokset._tasapeli("k", "k"))
        self.assertFalse(self.tulokset._tasapeli("k", "p"))

    def test_voittaja(self):
        self.assertTrue(self.tulokset._pelaaja_voittaa("k", "s"))
        self.assertTrue(self.tulokset._pelaaja_voittaa("s", "p"))
        self.assertTrue(self.tulokset._pelaaja_voittaa("p", "k"))
        self.assertFalse(self.tulokset._pelaaja_voittaa("s", "k"))
    
    def test_tulos(self):
        self.tulokset.tulos("k", "p")
        self.assertEqual(self.tulokset.tulokset, ["k"])
        self.assertEqual(self.tulokset.vastustaja_pisteet, 1)
        self.assertEqual(self.tulokset.tasapeli, 0)
        self.assertEqual(self.tulokset.pelaaja_pisteet, 0)

    def test_lisaa_tulos(self):
        pass