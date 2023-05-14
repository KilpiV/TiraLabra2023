# Käyttöohje

1. Asenna Python3 ja Poetry
2. Kloonaa repositorio tai lataa uusin release
... tulossa ...
### Pika-peli-ohje
Ohjelma kysyy haluttavien mallien lukumäärän, eli kuinka monen mittaisia Markovin ketjuja käytetään. Maksimi on 9 ja oletusarvo on 5.
Seuraavaksi ohjelma kysyy käyttäjältä kuinka monta kierrosta otetaan huomioon pisteytettäessä malleja, tekoälyn käyttämää valintaa tehtäessä.
Maksimi on 7, oletusarvo on 5.
Tämän jälkeen peli alkaa ja käyttäjä syöttää k, p, s syötteitä pelatakseen kiven, paperin tai sakset.
Kun hän syöttää x:n peli päättyy ja ohjelma tulostaa lopputilastot.

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

