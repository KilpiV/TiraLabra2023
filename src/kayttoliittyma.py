from kivi_sakset_paperi import KiviSaksetPaperi

class Kayttoliittyma:
    """Käyttis
    """

    def __init__(self):
        syote = input("Anna mallien määrä (1-9), oletusarvo on 5 ")
        mallien_maara = 5
        if syote in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            mallien_maara = int(syote)
        syote = input("Anna malleihin vaikuttavien vuorojen määrä (1-7), oletusarvo on 5 ")
        vaikuttavat_pelit = 5
        if syote in ("1", "2", "3", "4", "5", "6", "7"):
            vaikuttavat_pelit = int(syote)
        self.peli = KiviSaksetPaperi(mallien_maara, vaikuttavat_pelit)
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
            self.tulosta_tilanne(pelaaja, vastustajan_valinta)
            self.pelatut += pelaaja
            self.peli.vuoro(self.pelatut[-6:])
            tilanne = self.peli.tilanne(pelaaja, vastustajan_valinta)
            print(tilanne)

    def tulosta_tilanne(self, pelaaja, vastustaja):
        print((f"\n{self.peli.pelaajan_valinta(pelaaja)} "\
            f"vastaan {self.peli.pelaajan_valinta(vastustaja)}"))

    def kysy_valinta(self):
        valinta = input("\nValitse kivi (k), sakset (s) tai paperi (p), muilla lopettaa  ")
        return valinta
