# Käyttöohje

1. Asenna Python3 ja Poetry
2. Kloonaa repositorio tai lataa uusin [release](https://github.com/KilpiV/TiraLabra2023/releases/tag/Tiralabra_loppupalautus)

### Ohjelma

3. Aloita ohjelma terminaalissa juurikansiosta käsin käskyllä:
```bash
python3 src/index.py
```

### Testit:

3. Siirry virtuaaliympäristöön käskyllä: 
```bash
poetry shell
```

4. Tee unit-testaus ja luo testikattavuusraportti käskyllä:
```bash
coverage run --branch -m pytest; coverage html
```
   tai tee testaus ja katso testikattavuus terminalissa komennolla:
```bash
coverage run --branch -m pytest; coverage report -m
```

### Pika-peli-ohje
1. Peli kysyy haluttavien mallien lukumäärän, eli kuinka monen mittaisia Markovin ketjuja käytetään. Maksimi on 9 ja oletusarvona on 5.  
   Syötä jokin luku 1-9 väliltä, muilla syötteillä peli valitsee arvoksi 5.

2. Seuraavaksi ohjelma kysyy käyttäjältä kuinka monta kierrosta otetaan huomioon pisteytettäessä malleja, tekoälyn käyttämää valintaa tehtäessä. Maksimi on 7, oletusarvo on 5.  
   Syötä jokin luku väliltä 1-7, muilla syötteillä peli valitsee arvoksi 5.
   
3. Tämän jälkeen peli alkaa ja voit syöttää k, p, s syötteitä pelataksesi kiven, paperin tai sakset.

4. Kun syötät x:n peli päättyy ja ohjelma tulostaa lopputilastot.
