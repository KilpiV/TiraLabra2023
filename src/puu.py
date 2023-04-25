class Puu:
    def __init__(self):
        self.puu = {}

    def kaikki(self):
        return self.puu

    def lisaa(self, valinnat):
        pituus = len(valinnat)
        for i in range(pituus):
            osa = valinnat[i:]
            if osa not in self.puu:
                self.puu[osa] = 1
            else:
                self.puu[osa] += 1

    def hae(self, valinnat):
        if valinnat in self.puu:
            return self.puu[valinnat]
        return 0

    def hae_lapset(self, valinnat):
        lisays = "ksp"
        lista = []
        for i in range(3):
            valinta = valinnat + lisays[i]
            listalle = self.hae(valinta)
            lista.append(listalle)
        return lista
