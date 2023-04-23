import unittest
from puu import Puu

class TestPuu(unittest.TestCase):
    def setUp(self):
        self.puu = Puu()
        print("testataan!!!")

    def test_konstruktori_luo_tyhjan_puun(self):
        self.assertEqual({}, self.puu.kaikki())
    
    def test_lisaa_oikein(self):
        self.puu.lisaa("k")
        self.puu.lisaa("kk")
        self.puu.lisaa("kkp")
        self.assertEqual(2, self.puu.hae("k"))
        self.assertEqual(1, self.puu.hae("p"))
        self.assertEqual(0, self.puu.hae("s"))
        self.assertEqual(1, self.puu.hae("kp"))

    def test_hae_lapset(self):
        self.puu.lisaa("kk")
        self.puu.lisaa("kk")
        self.puu.lisaa("kp")
        testi = self.puu.hae_lapset("k")
        self.assertEqual([2,0,1], self.puu.hae_lapset("k"))
