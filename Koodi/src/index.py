from kivi_sakset_paperi import KiviSaksetPaperi
from puu import Puu
from malli import Malli

def main():
    uusi_peli = KiviSaksetPaperi()
    uusi_peli.kivi_sakset_paperi_peli()
    puu = Puu()
    puu.lisaa("k")
    puu.lisaa("kp")
    puu.lisaa("kpk")
    puu.lisaa("kpkp")
    puu.lisaa("kpkps")
    print("loppu")
    print(puu.kaikki())
    malli = Malli(2, 3, puu)
    print(malli.pisteet())

if __name__ == "__main__":
    main()