# Toteutusdokumentti

## Yleisrakenne

Ohjelma käynnistetään terminaalissa juurikansiosta käsin käskyllä *"python3 src/index.py"*, ja se toimii terminalissa (voidaan ajaa myös esim. VS Codessa).
Kun ohjelma käynnistetään kysyy se ensimmäiseksi kuinka monta mallia tekoälyn halutaan käyttävän. Mallit ovat eri mittaisia markovin-ketjuja. Käyttäjä voi valita 1 ja 9 väliltä ja oletusarvona on 5. 
Seuraavaksi ohjelma kysyy käyttäjältä kuinka monta kierrosta otetaan huomioon pisteytettäessä malleja, tekoälyn käyttämää valintaa tehtäessä. Käyttäjä voi valita 1 ja 7 väliltä, 5 on oletusarvona.

Sitten itse peli alkaa ja tulostuu ensimmäiseksi otsikko 
**"KIVI, SAKSET, PAPERI!"** 
ja pyytää käyttäjältä valintaa tulostuksella:
**"Valitse kivi (k), sakset (s) tai paperi (p), (x):llä lopettaa  "**
kun pelaaja syöttää jonkin vuorollaan jonkin valinnoista, 

- tulossa...[kuva luokkakaaviosta....

## Aika- ja tilavaatimukset

- tulossa....
[kuva aikavaativuuslaskelmasta.....
 
Tilavaativuus:
Puu-tallennuksen tilavaativuus on O(nk) jossa n on syötteiden määrä ja k on mallien lukumäärä +1.Tämä on Markovin-ketjuja kuvaavien sarjojen määrä.
Lisäksi tallennnetaan n-mittainen merkkijono-taulukko
 
## Puutteet ja parannusajatukset

- Useamman pelikerran pelaaminen käynnistämättä ohjelmaa uudestaan.
- Jäi hieman toisteista koodia, jonka voisi yrittää poistaa tilaisuuden tullen.
- Joku tulostus jäänyt käyttiksen ulkopuolelle, sen voisi siirtää
- Mallien luonti Vastustaja-luokalle.
- Pelaajan tietojen tallennus, pelin nollaus vain pyynnöstä.

## Lähteet

Tärkeimpinä lähteinä toimivat: 

[Markovin_ketju Wikipedia](https://fi.wikipedia.org/wiki/Markovin_ketju)

[Markov_chain](https://en.wikipedia.org/wiki/Markov_chain)

[Multi-AI raportti](https://arxiv.org/pdf/2003.06769.pdf)

