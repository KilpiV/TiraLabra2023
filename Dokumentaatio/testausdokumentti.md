# Testaussokumentti

## Yksikkötestaus
Yksikkötestaus suoritetaan unittestiä käyttäen automaattisesti

![coverage report](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/testikattavuus_unittest.png)

![pylint](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/pylint_taso.png)

Tehty empiiristä tutkimusta ylimääräisten tulostusten avulla, että tekoäly toimisi varmasti oikein ja vaihtaa oikeassa kohtaa mallia. Alempana tarkempaa testausta.

## Yksinkertainen testi 
syötteenä toimi "kkkkkkkkkkkkkk"
*Ensin laskettuna taulukkoon mitä tulisi olla minkäkin mallin tulos ja tekoälyn valinta ja mallin vaihto. Ohjelma toimi oikein.*

![testiaineisto taulukko](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/KSP-testi-k-t.png)

## Toistuvilla syötteillä oikeellisuustestaus
![AI-toistuva syöte](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/Toistuva-syote-AI.png)

Tästä taulukosta nähdään, että ohjelma toimii oikein, sillä se voittaa selkeästi suurimman osan peleistä, kun käytetään toistuvaa syötettä.

## Mallien määrän ja kierrosten määrän vaikutukset
Testauksessa käytetty syöte:
```bash
skkpspkpspkpppskkkkpspppppskkkskkkpsskkkpsskkkpspspskkkkppksppskkkskkkpskpskpspspskkpspskkkpspkpkpskx
```



#### Mallien määrän vaikutus tekoälyn voittoihin, kun vaikuttavat kierrokset on 5 ja mallien määrä vaihtuu.
![mallit](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/mallien-maaran-vaikutus.png)


#### Mallien määrän vaikutus voittojen ja häviöiden suhteeseen, kun vaikuttavat kierrokset on 5 ja mallien määrä vaihtuu.
![mallit-ei-tasa](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/mallien-maaran-vaikutus-ei-tasapelia.png)


#### Häviöiden, voittojen ja tasapelien suhde, kun vaikuttavien kierrosten määrän vaihtuu ja mallien määrä on 5.
![kierrokset](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/vaikuttavien-kierrosten-testaus.png)


Testauksessa käytetty koodi muutos index.py tiedostossa.
```bash
index.py

def main():
    kayttis = Kayttoliittyma()
    syote = kayttis.tuota_saannolliset(1)
    syote = toistuva_syote*k + "x"
    kayttis.testaa_sata(syote)
    print(syote)
    #kayttis.aloita_peli()
```

Testaukseen vaikuttavat kayttoliittyma.py tiedostossa olevat osat (jotka eivät ole osa peli koodia).
```bash
kayttoliittyma.py

    def tuota_saannolliset(self, siemen_luku):
        random.seed(siemen_luku)
        syote = ""
        valinnat = "kpskps", "ppskkk", "skkpsp", "kkppks", "kpsppp",\
            "kpskpk", "pspskk", "skkkps", "kkpspk", "kpspkp"
        for i in range(17): 
            syote += valinnat[random.randrange(10)]
        syote = syote[:100]+"x"
        return syote

    def testaa_sata(self, syote):
        indeksi = 0
        pelaaja = syote[indeksi]
        while self.peli.peli_loppuu(pelaaja):
            self.vuoro(pelaaja)
            indeksi += 1
            pelaaja = syote[indeksi]
        print(self.peli.lopputilasto())
```
eli luodaan seedin avulla "satunnainen" syöte, joka koostuu kuuden mittaisista osajonoista, joten syötteeseen saadaan toisteisuutta ja siten tekoäly toimimaan, mutta testaus pystytään toisintamaan tarvittaessa.
