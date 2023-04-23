class Tulokset:
    """Luokka, joka huolehtii tulosten tallennuksen ja haut

    Attribuutit: 
        pelaajan pisteet: Integer, joka kertoo käyttäjän pisteet
        vastustajan pisteet: Integer, joka kertoo tekoälyn pisteet
        tasapeli: Integer, joka kertoo tasapelien määrän
        tulokset: lista, jossa tuplet; pelaajan valinta ja lopputulos
    """
    def __init__(self):
        self.pelaaja_pisteet = 0
        self.vastustaja_pisteet = 0
        self.tasapeli = 0
        self.tulokset = []

    def __str__(self):
        return f"\n Pistetilanne:\n pelaaja - tekoäly \n \
            {self.pelaaja_pisteet:7} - {self.vastustaja_pisteet}"

    def tulos(self, pelaaja, vastustaja):
        self.tulokset += pelaaja
        if self._tasapeli(pelaaja, vastustaja):
            self.tasapeli = self.tasapeli + 1
        elif self._pelaaja_voittaa(pelaaja, vastustaja):
            self.pelaaja_pisteet = self.pelaaja_pisteet + 1
        else:
            self.vastustaja_pisteet += 1

    def _tasapeli(self, pelaaja, vastustaja):
        return pelaaja == vastustaja

    def _pelaaja_voittaa(self, pelaaja, vastustaja):
        if pelaaja == "k" and vastustaja == "s":
            return True
        if pelaaja == "s" and vastustaja == "p":
            return True
        if pelaaja == "p" and vastustaja == "k":
            return True
        return False

    def lopputilasto(self):
        palautus = "\nLopputulokset:\n\n"
        palautus +=(f"Pelejä yhteensä {len(self.tulokset)}\n")
        palautus += (f"Pelaajan voitot: {self.pelaaja_pisteet}\n")
        palautus += (f"Pelaajan tappiot: {self.vastustaja_pisteet}\n")
        palautus += (f"Tasapelit: {self.tasapeli}\n")
        if self.pelaaja_pisteet > self.vastustaja_pisteet:
            return palautus + "Pelaaja voittaa"
        if self.pelaaja_pisteet < self.vastustaja_pisteet:
            return palautus + "Tekoäly voittaa"
        return palautus + "Tuli tasapeli"
      