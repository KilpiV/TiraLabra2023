import unittest
from kivi_sakset_paperi import KiviSaksetPaperi
from tulokset import Tulokset
from puu import Puu
from unittest.mock import Mock, patch

class TuloksetStub:
    def __init__(self, tulostukset):
        self.tulostus = "lapi meni"
        pass

    def lopputilasto(self):
        return self.tulostus

class VastustajaStub:
    def __init__(self):
        self.syotteet = ""
        pass

    def paivita_mallit(self, syote):
        self.syotteet += syote

class PuuStub:
    def __init__(self):
        pass

class TestKiviSaksetPaperi(unittest.TestCase):
    def setUp(self):
        stub_tulokset = TuloksetStub([])
        stub_puu = PuuStub()
        self.mock_peli = Mock(wraps=KiviSaksetPaperi(1, 1, stub_tulokset, stub_puu))
        #self.mock_peli_tulos = TuloksetStub()
        #self.mock_peli_vastus = VastustajaStub()
        #self.peli = KiviSaksetPaperi(1, 1)
        pass
        
    def test_tilanne(self):
        #tulos_mock = Mock(wraps=KiviSaksetPaperi(1, 1))
        tilanne = self.mock_peli.tilanne("k", "k")
        self.mock_peli.tilanne.assert_called_with("k", "k")
        self.mock_peli.tilanne.return_value = "testi läpi"
        tilanne = self.mock_peli.tilanne("k", "k")
        self.assertEqual("testi läpi", tilanne)
    
    def test_lopputilasto(self):
        lapi = self.mock_peli.lopputilasto()
        palautus = "\nLopputulokset:\n\n"
        palautus +=(f"Pelejä yhteensä 0\n")
        palautus += (f"Pelaajan voitot: 0\n")
        palautus += (f"Pelaajan tappiot: 0\n")
        palautus += (f"Tasapelit: 0\n")
        palautus += "Tuli tasapeli"
        self.assertEqual(lapi, palautus)

    def test_vuoro(self):
        self.mock_peli.vuoro("kk")
        self.mock_peli.vuoro.assert_called_with("kk")
    
    def test_peli_loppuu(self):
        testit_ei_lopu = "k","a", "kk", " ", "K"
        testit_loppuu = "x","X"
        for i in testit_ei_lopu:
            self.assertTrue(self.mock_peli._peli_loppuu(i))
        self.assertFalse(self.mock_peli._peli_loppuu(testit_loppuu[0]))
        self.assertFalse(self.mock_peli._peli_loppuu(testit_loppuu[1]))
    
    def test_peli_jatkuu(self):
        jatkuu = "k", "s", "p"
        for i in jatkuu:
            self.assertTrue(self.mock_peli._peli_jatkuu(i))
        ei_jatku = "seis", 3, "kk", " ", "K", "a", "x"
        for i in ei_jatku:
            self.assertFalse(self.mock_peli._peli_jatkuu(i))

    def test_pelaajan_valinta(self):
        valinta = self.mock_peli.pelaajan_valinta("k")
        self.assertEqual(valinta, "kivi")
        valinta = self.mock_peli.pelaajan_valinta("s")
        self.assertEqual(valinta, "sakset")
        valinta = self.mock_peli.pelaajan_valinta("p")
        self.assertEqual(valinta, "paperi")
        