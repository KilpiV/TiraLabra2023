from puu import Puu

class Malli:
    def __init__(self, malli, vaikuttavat_pelit, puu: Puu, eka = "k"):
        self.puu = puu
        self.syvyys = malli
        self.__pisteet = []
        for i in range(vaikuttavat_pelit):
            self.__pisteet.append(0)
        self.indeksi = 0
        self.seuraava = eka

    def pisteet(self):
        return sum(self.__pisteet)

    def hae_seuraava(self, viimeiset):
        valinta = viimeiset[-self.syvyys:]
        lapset = self.puu.hae_lapset(valinta)
        self.paivita_tn_voittaja(lapset)
        return self.seuraava

    def paivita_tn_voittaja(self, taulukko):
        k = taulukko[0]
        s = taulukko[1]
        p = taulukko[2]
        if k > s and k >= p:
            self.seuraava = "p"
        elif s > p and s >= k:
            self.seuraava = "k"
        elif p > k and p >= s:
            self.seuraava = "s"

    def paivita_pisteet(self, pelaajan_valinta):
        self.__pisteet[self.indeksi] = self.voittaja(pelaajan_valinta, self.seuraava)
        self.indeksi += 1
        if self.indeksi >= len(self.__pisteet):
            self.indeksi = 0

    def voittaja(self, pelaaja, malli):
        if pelaaja == malli:
            return 0
        if pelaaja == "k" and malli == "p":
            return 1
        if pelaaja == "p" and malli == "s":
            return 1
        if pelaaja == "s" and malli == "k":
            return 1
        return -1
