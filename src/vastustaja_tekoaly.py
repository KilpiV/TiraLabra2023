class Vastustaja:
    """Luokka, joka huolehtii vastustajan valinnoista.
    
    Attribuutit:
        valinta: Vastustajan valinta.
    """

    def __init__(self, mallit):
        self.mallit = mallit
        self.nyt_malli = self.mallit[0]

    def paivita_mallit(self, edelliset):
        for malli in self.mallit:
            malli.paivita_pisteet(edelliset[-1])
        for malli in self.mallit:
            if len(edelliset) >= malli.syvyys:
                malli.hae_seuraava(edelliset)

    def anna_valinta(self):
        paras = self.nyt_malli.pisteet()
        for malli in self.mallit:
            # testauksen tulostukset
            #print("mallin",malli.syvyys,"pisteet on:", malli.pisteet(), \
             #   "ja valinta olisi:", malli.seuraava)
            if malli.pisteet() > paras:
                paras = malli.pisteet()
                self.nyt_malli = malli
            # testauksen tulostukset
            #    print("vaihtuu malli", malli.syvyys, "pisteet:", paras)
        print("tekoälyn valinta on: ",self.nyt_malli.seuraava)
        return self.nyt_malli.seuraava
