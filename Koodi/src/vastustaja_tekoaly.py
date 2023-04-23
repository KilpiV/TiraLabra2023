class Vastustaja:
    """Luokka, joka huolehtii vastustajan valinnoista.
    
    Attribuutit:
        valinta: Vastustajan valinta.
    """
  
    def __init__(self, mallit):
        self.mallit = mallit
        self.nyt_malli = self.mallit[0]
        
    def anna_valinta(self):
        paras = self.nyt_malli.pisteet()
        for malli in self.mallit:
            if malli.pisteet() > paras:
                paras = malli.pisteet()
                self.nyt_malli = malli
        print("tekoälyn valinta on: ",self.nyt_malli.seuraava)
        return self.nyt_malli.seuraava
