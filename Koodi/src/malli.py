from puu import Puu

class Malli:
    def __init__(self, malli, vaikuttavat_pelit, puu: Puu):
        self.puu = puu
        self.syvyys = malli
        self.__pisteet = []
        self.indeksi = 0

        # sum(self.pisteet) jos kyseisellä mallilla on jokin 
    def pisteet(self):
        return sum(self.__pisteet)

    def hae_tulos(self, viimeiset):
        valinta = viimeiset[-self.syvyys:]
        print(valinta)
        #self.puu.etsi(valinta)
        return 0 # hae puusta kyseisen syvyyden tulos ja 

    def paivita_pisteet(self, pelaajan_valinta, valinnat):
        # päivitä pisteet taulukko.... ja ....
        pass