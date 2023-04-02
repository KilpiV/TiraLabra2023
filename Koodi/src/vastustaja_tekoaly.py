import random

class Vastustaja:
    """Luokka, joka huolehtii vastustajan valinnoista.
    Attribuutit:
        valinta: Vastustajan valinta.
    """
  
    def __init__(self):
        self._valinta = 0

    def anna_valinta(self):
        self._valinta = random.randint(1, 3)

        if self._valinta == 1:
            return "k"
        elif self._valinta == 2:
            return "s"
        else:
            return "p"    
            