# Toteutusdokumentti

## Yleisrakenne

1. Ohjelma käynnistetään terminaalissa juurikansiosta käsin käskyllä *"python3 src/index.py"*, ja se toimii terminalissa (voidaan ajaa myös esim. VS Codessa).

2. Kun ohjelma käynnistetään kysyy se ensimmäiseksi kuinka monta mallia tekoälyn halutaan käyttävän. Mallit ovat eri mittaisia markovin-ketjuja. Käyttäjä voi valita 1 ja 9 väliltä ja oletusarvona on 5. 

3. Seuraavaksi ohjelma kysyy käyttäjältä kuinka monta kierrosta otetaan huomioon pisteytettäessä malleja, tekoälyn käyttämää valintaa tehtäessä. Käyttäjä voi valita 1 ja 7 väliltä, 5 on oletusarvona.

4. Sitten itse peli alkaa ja tulostuu ensimmäiseksi otsikko  
		  **"KIVI, SAKSET, PAPERI!"**  

   ja tulostaa ohjeen jolla pyydetään käyttäjältä valintaa:  
		  **"Valitse kivi (k), sakset (s) tai paperi (p), (x):llä lopettaa  "**  
   jos käyttäjä syöttää jotain muuta ohjelma tulostaa ohjeen uudestaan, kunnes käyttäjä syöttää jonkin hyväksytyistä valinnoista (k, s, p tai x).

5. Kierros:
	* peli tarkistaa onko syöte x eli lopetetaanko tähän
	* tarkistaa seuraavaksi onko syöte hyväksytty pelivalinta eli siirto (esim **_"p"_**)
	* peli hakee vastustajan eli tekoälyn tämän hetkisen valinnan
		- tarkistaa viimeisten m-kierroksen parhaimmin pärjänneen mallin, vaihtaa uuteen jos jokin on parempi kuin nykyinen
		- hakee valitun mallin siirron
		- tulostaa sen käyttäjän nähtäväksi  
		  **"tekoälyn valinta on:  k"**  
	* peli tulostaa valitut siirrot esim.  
	  **"paperi vastaan kivi"**
 	* peli tallentaa käyttäjän syöttämän valinnan
		- taulukkoon testauksia varten
		- merkkijonoon puuta varten  
	* peli päivittää mallien pisteet sen mukaan miten ne olisivat pärjänneet valinnallaan pelaajaa vastaan (-1, 0, 1)(häviö, tasapeli, voitto)
	* Peli käy läpi tekoälyn mallit ja päivittää näiden valinnat seuraavaa kierrosta varten
	* syötteen mukaan kasvattaa puun viimeiset (1, 2, ... , k)-mittaisia ketjuja (tai luo uuden arvolla 1 jos sellaista ei vielä ole)
	* peli tallentaa tuloksen tuloksiin
	* peli tulostaa kierroksen tilanteen:  
	  **"Pistetilanne:"**  
	  **"pelaaja - tekoäly"**  
	  **"1 - 0"**
	* peli kysyy taas pelaajan valintaa ja kierros alkaa alusta
6. Kun pelaaja syöttää x eli haluaa lopettaa peli tulostaa lopputilaston:  
	  
	  **"Lopputulokset:"**  
	  
	  **"Pelejä yhteensä 1"**  
	  **"Pelaajan voitot: 1"**  
	  **"Pelaajan tappiot: 0"**  
	  **"Tasapelit: 0"**  
	  **"Pelaaja voittaa"**


Luokkakaavio

![luokkakaavio](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/luokkakaavio.png)


## Aika- ja tilavaatimukset

Aikavaativuus:

![aikavaativuuslaskelma](https://github.com/KilpiV/TiraLabra2023/blob/main/Dokumentaatio/kuvat/aikavaativuus.png)

Esitettynä kierroksen aikana käytettävän koodin aikavaativuus tasolla. koska kaikki muu koodi on peruskoodia jonka aikavaativuus on O(1) tai muutama silmukka jotka eivät riipu syötteen pituudesta, eli aikavaativuus on näiden osalta O(1) ja koska while silmukka eli montako kierrosta pelataan riippuu pelikerrasta niin, aikavaativuus on O(n) missä n on syötteiden määrä.
 
Tilavaativuus:
Puu-tallennuksen tilavaativuus on O(nk) jossa n on syötteiden määrä ja k on mallien lukumäärä +1.Tämä on Markovin-ketjuja kuvaavien sarjojen määrä.
Lisäksi tallennnetaan n-mittainen merkkijono-taulukko. Eli kokonaistilavaativuus on O(m), missä m = n*(k+1)
 
## Puutteet ja parannusajatukset

- [ ] Useamman pelikerran pelaaminen käynnistämättä ohjelmaa uudestaan.
- [ ] Jäi hieman toisteista koodia, jonka voisi yrittää poistaa tilaisuuden tullen.
- [ ] Joku tulostus jäänyt käyttiksen ulkopuolelle, sen voisi siirtää
- [ ] Mallien luonti Vastustaja-luokalle.
- [ ] Pelaajan tietojen tallennus, pelin nollaus vain pyynnöstä.

## Lähteet

1. Wikipedia:
	- Wikipedia, Markovin ketju, 2022 [https://fi.wikipedia.org/wiki/Markovin_ketju](https://fi.wikipedia.org/wiki/Markovin_ketju), luettu 15.3.2013
	- Wikipedia, Markov chain, 2023 [https://en.wikipedia.org/wiki/Markov_chain](https://en.wikipedia.org/wiki/Markov_chain), luettu 21.3.2023

2. Wang L, Huang W, Li Y, Evans j, He S. Multi‑Ai competing and winning against humans in iterated Rock‑paper‑Scissors game [-raportti](https://arxiv.org/pdf/2003.06769.pdf), doi: https://doi.org/10.1038/s41598-020-70544-7, luettu 20.3.2023

