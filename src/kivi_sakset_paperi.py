from vastustaja_tekoaly import Vastustaja
from tulokset import Tulokset
from puu import Puu
from malli import Malli

class KiviSaksetPaperi:
    """Pelilogiikka

    """
    def __init__(self):
        self.tulokset = Tulokset()
        self.puu = Puu()
        vaikuttavat_pelit = 5
        self.mallit = []
        mallien_maara = 5
        for i in range(mallien_maara):
            self.mallit.append(Malli(mallien_maara-i, vaikuttavat_pelit, self.puu))
        self.vastustaja = Vastustaja(self.mallit)

    def kivi_sakset_paperi_peli(self):
        self.aloita_peli()
        print(self.tulokset.lopputilasto())

    def aloita_peli(self):
        print("\nKIVI, SAKSET, PAPERI!")
        pelaaja = input("\nValitse kivi (k), sakset (s) tai paperi (p), muilla lopettaa  ")
        pelatut = ""
        while self._peli_loppuu(pelaaja):
            if self._peli_jatkuu(pelaaja):
                vastustajan_valinta = self.vastustaja.anna_valinta()
                print(f"\n{self.pelaajan_valinta(pelaaja)} "\
                    f"vastaan {self.pelaajan_valinta(vastustajan_valinta)}")
                pelatut += pelaaja
                self.vuoro(pelatut)
                self.tulokset.tulos(pelaaja, vastustajan_valinta)
                print(self.tulokset)
            pelaaja = input("\nValitse kivi (k), sakset (s) tai paperi (p), (x) lopettaa  ")

    def vuoro(self, edelliset):
        for malli in self.mallit:
            if len(edelliset) >= malli.syvyys:
                malli.hae_seuraava(edelliset)
        self.puu.lisaa(edelliset)
        for malli in self.mallit:
            malli.paivita_pisteet(edelliset[-1])

    def pelaajan_valinta(self, kirjain):
        pelaajan_valinta = ""
        if kirjain == "k":
            pelaajan_valinta = "kivi"
        elif kirjain == "s":
            pelaajan_valinta = "sakset"
        elif kirjain == "p":
            pelaajan_valinta = "paperi"
        return pelaajan_valinta

    def _peli_loppuu(self, siirto):
        return siirto not in ("x", "X")
        #return siirto != "x" and siirto != "X"

    def _peli_jatkuu(self, siirto):
        return siirto in ("k", "s", "p")
        #return siirto == "k" or siirto == "s" or siirto == "p"
