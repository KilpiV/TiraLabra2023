from vastustaja_tekoaly import Vastustaja
from tulokset import Tulokset
from puu import Puu
from malli import Malli

class KiviSaksetPaperi:
    """Pelilogiikka

    """
    def __init__(self, mallien_maara, vaikuttavat_pelit, tulokset = Tulokset(), puu=Puu()):
        self.tulokset = Tulokset()
        self.puu = Puu()
        mallit = []
        for i in range(mallien_maara):
            mallit.append(Malli(mallien_maara-i, vaikuttavat_pelit, self.puu))
        self.vastustaja = Vastustaja(mallit)

    def tilanne(self, pelaaja, vastustaja):
        self.tulokset.tulos(pelaaja, vastustaja)
        return self.tulokset

    def lopputilasto(self):
        return self.tulokset.lopputilasto()

    def vuoro(self, edelliset):
        self.vastustaja.paivita_mallit(edelliset)
        self.puu.lisaa(edelliset)

    def pelaajan_valinta(self, kirjain):
        valinnat = {"k": "kivi", "s": "sakset", "p": "paperi"}
        return valinnat[kirjain]
        #korvattu sanakirjalla ehdotetusti...
#        pelaajan_valinta = ""
 #       if kirjain == "k":
  #          pelaajan_valinta = "kivi"
   #     elif kirjain == "s":
    #        pelaajan_valinta = "sakset"
     #   elif kirjain == "p":
      #      pelaajan_valinta = "paperi"
       # return pelaajan_valinta

    def _peli_loppuu(self, siirto):
        return siirto not in ("x", "X")
        #return siirto != "x" and siirto != "X"

    def _peli_jatkuu(self, siirto):
        return siirto in ("k", "s", "p")
        #return siirto == "k" or siirto == "s" or siirto == "p"
