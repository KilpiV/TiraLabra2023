import random
from vastustaja_tekoaly import Vastustaja
from tulokset import Tulokset

class KiviSaksetPaperi:
    """Pelilogiikka

    """

    def kivi_sakset_paperi_peli(self):
        tulokset = Tulokset()
        vastustaja = Vastustaja()
        print("KIVI, SAKSET, PAPERI!")

        pelaaja = input("Valitse kivi (k), sakset (s) tai paperi (p), muilla lopettaa  ")
        vastustajan_valinta = vastustaja.anna_valinta()
        while self._peli_jatkuu(pelaaja):
            print(f"{self.pelaajan_valinta(pelaaja)} vastaan {self.pelaajan_valinta(vastustajan_valinta)}")
            
            tulokset.tulos(pelaaja, vastustajan_valinta)
            print(tulokset)
            pelaaja = input("Valitse kivi (k), sakset (s) tai paperi (p), muilla lopettaa  ")
            vastustajan_valinta = vastustaja.anna_valinta()
          
    def pelaajan_valinta(self, kirjain):
        pelaajan_valinta = ""
        if kirjain == "k":
            pelaajan_valinta = "kivi"
        elif kirjain == "s":
            pelaajan_valinta = "sakset"
        elif kirjain == "p":
            pelaajan_valinta = "paperi"
        return pelaajan_valinta

    def _peli_jatkuu(self, siirto):
        return siirto == "k" or siirto == "s" or siirto == "p"
