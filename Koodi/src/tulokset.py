class Tulokset:
    def __init__(self):
        self.pelaaja_pisteet = 0
        self.vastustaja_pisteet = 0
        self.tasapeli = 0
        self.tulokset = []

    def __str__(self):
        return f"Pistetilanne: {self.pelaaja_pisteet} - {self.vastustaja_pisteet}"

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
        elif pelaaja == "s" and vastustaja == "p":
            return True
        elif pelaaja == "p" and vastustaja == "k":
            return True
