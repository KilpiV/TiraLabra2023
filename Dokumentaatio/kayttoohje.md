# Käyttöohje

... tulossa ...
Ohjelma kysyy haluttavien mallien lukumäärän, eli kuinka monen mittaisia Markovin ketjuja käytetään. Maksimi on 9 ja oletusarvo on 5.
Seuraavaksi ohjelma kysyy käyttäjältä kuinka monta kierrosta otetaan huomioon pisteytettäessä malleja, tekoälyn käyttämää valintaa tehtäessä.
Maksimi on 7, oletusarvo on 5.
Tämän jälkeen peli alkaa ja käyttäjä syöttää k, p, s syötteitä pelatakseen kiven, paperin tai sakset.
Kun hän syöttää x:n peli päättyy ja ohjelma tulostaa lopputilastot.

### Ohjelma

Asenna Python3 ja Poetry
Kloonaa repositorio
Aloita ohjelma terminaalissa juurikansiossa käskyllä:
```bash
python3 src/index.py
```

### Testit:

siirry virtuaaliympäristöön käskyllä: 
```bash
poetry shell
```

tee unit-testaus ja luo testikattavuusraportti käskyllä:
```bash
coverage run --branch -m pytest; coverage html
```


