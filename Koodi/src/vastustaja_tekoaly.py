import random
from puu import Puu
from tulokset import Tulokset

class Vastustaja:
    """Luokka, joka huolehtii vastustajan valinnoista.
    
    Attribuutit:
        valinta: Vastustajan valinta.
    """
  
    def __init__(self, syvyys = 3): # lisää syvyys eli mallien
        self._valinta = 0
        self._syvyys = syvyys
        self.puu = Puu()
        self.uusimmat = ""
        self.tulokset = Tulokset()
        # self.mallit = {}

    def paivita_uusimmat(self, uusin):
        pituus = len(self.uusimmat)

    def syota_valinta(self, uusin):
        self.paivita_uusimmat(uusin)
        self.puu.lisaa(self.uusimmat)
        pass

    def anna_valinta(self):     # anna valinta
        self._valinta = random.randint(1, 3)
        # tarkista mikä malli on ollu voittoisin 
        # katso tämän mallin ennustus ja valitse voittava
        if self._valinta == 1:
            return "k"          # return "p"
        elif self._valinta == 2:
            return "s"          # return "k"
        else:
            return "p"          # return "s"
