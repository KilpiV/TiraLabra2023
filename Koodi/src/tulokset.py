from puu import Puu
from malli import Malli

class Tulokset:
    """Luokka, joka huolehtii tulosten tallennuksen ja haut

    Attribuutit: 
        pelaajan pisteet: Integer, joka kertoo käyttäjän pisteet
        vastustajan pisteet: Integer, joka kertoo tekoälyn pisteet
        tasapeli: Integer, joka kertoo tasapelien määrän
        tulokset: lista, jossa tuplet; pelaajan valinta ja lopputulos
    """
    def __init__(self):#, mallien_maara):
        self.pelaaja_pisteet = 0
        self.vastustaja_pisteet = 0
        self.tasapeli = 0
        self.tulokset = []
        self.mallit = []
        #for i in range(mallien_maara):
        #    self.mallit.append(Malli(i+1, 5))
        # self.viimeiset = "" # esim kkpks

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
