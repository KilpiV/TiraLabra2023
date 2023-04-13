class Puu:
    def __init__(self):
        self.puu = {}

    def etsi(self, valinta): #malli = syvyys???
        #valinta = valinnat[len(valinnat)-malli:]
        # hae yleisin vaihtoehto kyseiselle suoralle ja mallille
        # esim kkkp , malli 2 eli kp - > 
        print(self.puu[valinta])
        pass

    def kaikki(self):
        return self.puu
        #tarviiko???
        
    def lisaa(self, valinnat):
        pituus = len(valinnat)
        for i in range(pituus):
            #osa = valinnat[pituus-i:]
            osa = valinnat[i:]
            if osa not in self.puu:
                self.puu[osa] = 1
                print(osa, "on nyt 1")
            else:
                self.puu[osa] += 1
                print(osa, "on jo kasvatetaan, nyt", self.puu[osa])


