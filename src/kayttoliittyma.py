from kivi_sakset_paperi import KiviSaksetPaperi
import random

class Kayttoliittyma:
    """Käyttis
    """

    def __init__(self):
        syote = input("Anna mallien määrä (1-9), oletusarvo on 5 ")
        self.mallien_maara = 5
        if syote in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            self.mallien_maara = int(syote)
        syote = input("Anna malleihin vaikuttavien vuorojen määrä (1-7), oletusarvo on 5 ")
        vaikuttavat_pelit = 5
        if syote in ("1", "2", "3", "4", "5", "6", "7"):
            vaikuttavat_pelit = int(syote)
        self.peli = KiviSaksetPaperi(self.mallien_maara, vaikuttavat_pelit)
        self.pelatut = ""

    def aloita_peli(self):
        print("\nKIVI, SAKSET, PAPERI!")
        pelaaja = self.kysy_valinta()
        while self.peli.peli_loppuu(pelaaja):
            self.vuoro(pelaaja)
            pelaaja = self.kysy_valinta()
        print(self.peli.lopputilasto())

    def vuoro(self, pelaaja):
        if self.peli.peli_jatkuu(pelaaja):
            vastustajan_valinta = self.peli.vastustaja.anna_valinta()
            self.tulosta_valinnat(pelaaja, vastustajan_valinta)
            self.pelatut += pelaaja
            k = self.mallien_maara
            self.peli.vuoro(self.pelatut[-k:])
            tilanne = self.peli.tilanne(pelaaja, vastustajan_valinta)
            print(tilanne)

    def tulosta_valinnat(self, pelaaja, vastustaja):
        print((f"\n{self.peli.pelaajan_valinta(pelaaja)} "\
            f"vastaan {self.peli.pelaajan_valinta(vastustaja)}"))

    def kysy_valinta(self):
        valinta = input("\nValitse kivi (k), sakset (s) tai paperi (p), (x):llä lopettaa  ")
        return valinta

    def tuota_saannolliset(self, siemen_luku):
        random.seed(siemen_luku)
        syote = ""
        valinnat = "kpskps", "ppskkk", "skkpsp", "kkppks", "kpsppp",\
            "kpskpk", "pspskk", "skkkps", "kkpspk", "kpspkp"
        for i in range(17): 
            syote += valinnat[random.randrange(10)]
        syote = syote[:100]+"x"
        return syote

    def testaa_sata(self, syote):
        indeksi = 0
        pelaaja = syote[indeksi]
        while self.peli.peli_loppuu(pelaaja):
            self.vuoro(pelaaja)
            indeksi += 1
            pelaaja = syote[indeksi]
        print(self.peli.lopputilasto())
        