# Toteutusdokumentti

## Yleisrakenne

1. Ohjelma käynnistetään terminaalissa juurikansiosta käsin käskyllä *"python3 src/index.py"*, ja se toimii terminalissa (voidaan ajaa myös esim. VS Codessa).

2. Kun ohjelma käynnistetään, kysyy se ensimmäiseksi kuinka monta mallia tekoälyn halutaan käyttävän. Mallit käyttävät eri mittaisia markovin-ketjuja. Käyttäjä voi valita arvon 1 ja 9 väliltä ja oletusarvona on 5. 

3. Seuraavaksi ohjelma kysyy käyttäjältä, kuinka monta kierrosta otetaan huomioon pisteytettäessä malleja, tekoälyn käyttämää valintaa tehtäessä. Käyttäjä voi valita arvon 1 ja 7 väliltä, 5 on oletusarvona.

4. Sitten itse peli alkaa ja tulostuu ensimmäiseksi otsikko  
		  **"KIVI, SAKSET, PAPERI!"**  

   ja tulostaa ohjeen, jolla pyydetään käyttäjältä valintaa:  
		  **"Valitse kivi (k), sakset (s) tai paperi (p), (x):llä lopettaa  "**  
   Jos käyttäjä syöttää jotain muuta ohjelma tulostaa ohjeen uudestaan, kunnes käyttäjä syöttää jonkin hyväksytyistä valinnoista (k, s, p tai x).

5. Kierros:
	* peli tarkistaa onko syöte x eli lopetetaanko tähän
	* peli tarkistaa seuraavaksi onko syöte hyväksytty pelivalinta eli siirto (esim **_"p"_**)
	* peli hakee vastustajan eli tekoälyn tämän hetkisen valinnan
		- tarkistaa viimeisten m-kierroksen parhaimmin pärjänneen mallin, vaihtaa uuteen, jos jokin on parempi kuin nykyinen
		- hakee valitun mallin siirron
		- tulostaa sen käyttäjän nähtäväksi  
		  **"tekoälyn valinta on:  k"**  
	* peli tulostaa valitut siirrot esim.  
	  **"paperi vastaan kivi"**
 	* peli tallentaa käyttäjän syöttämän valinnan
		- taulukkoon testauksia varten
		- merkkijonoon puuta varten  
	* peli päivittää mallien pisteet sen mukaan, miten ne olisivat pärjänneet valinnallaan pelaajaa vastaan (-1, 0, 1)(häviö, tasapeli, voitto)
	* peli käy läpi tekoälyn mallit ja päivittää näiden valinnat seuraavaa kierrosta varten
	* syötteen mukaan kasvatetaan puun avainpari arvoja merkkijonon (1, 2, ... , k)-mittaisia osajonoja käyttäen (tai luo uuden arvolla 1, jos sellaista ei vielä ole)
	* peli tallentaa tuloksen tuloksiin
	* peli tulostaa kierroksen tilanteen:  
	  **"Pistetilanne:"**  
	  **"pelaaja - tekoäly"**  
	  **"1 - 0"**
	* peli kysyy taas pelaajan valintaa ja kierros alkaa alusta
6. Kun pelaaja syöttää x eli haluaa lopettaa, peli tulostaa lopputilaston:  
	  
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

Kuvassa on esitettynä kierroksen aikana käytettävän koodi, aikavaativuus tasolla. Koska kaikki muu koodi on peruskoodia, jonka aikavaativuus on O(1) muutamaa silmukkaa lukuunottamatta, jotka eivät riipu syötteen pituudesta (vaan ovat max 54 kierrosta) on kokonais aikavaativuus näiden osalta O(1). Lisäksi, koska while silmukka (eli, montako kierrosta pelataan) riippuu pelikerrasta ja pelaajasta, niin aikavaativuus koodillle on O(n), missä n on syötteiden määrä.
 
Tilavaativuus:
Puu-tallennuksen tilavaativuus on O(nk), jossa n on syötteiden määrä ja k on mallien lukumäärä +1. Tämä on Markovin-ketjuja kuvaavien sarjojen määrä.
Lisäksi tallennnetaan n-mittainen merkkijono-taulukko. Eli kokonaistilavaativuus on O(m), missä m = n*(k+1), (k+1) on maksimissaan 10.
 
## Puutteet ja parannusajatukset

- [x] Käyttöliittymän eriyttäminen.
- [ ] Useamman pelikerran pelaaminen käynnistämättä ohjelmaa uudestaan.
- [ ] Jäi hieman toisteista koodia, jonka voisi yrittää poistaa tilaisuuden tullen.
- [ ] Joku tulostus jäänyt käyttiksen ulkopuolelle, sen voisi siirtää
- [ ] Mallien luonti Vastustaja-luokalle.
- [ ] Pelaajan tietojen tallennus, pelin nollaus vain pyynnöstä.
- [ ] Testauksen ainestoa voisi miettiä lisää ja pidemmälle, esim että jokaisen mallin mittaisia osajonoja tulisi varmasti mukaan useampi. 
- [ ] Testata pelattujen kierrosten määrän vaikutusta AI:n voittojen suhteeseen. 

## Lähteet

1. Wikipedia:
	- Wikipedia, Markovin ketju, 2022 [https://fi.wikipedia.org/wiki/Markovin_ketju](https://fi.wikipedia.org/wiki/Markovin_ketju), luettu 15.3.2013
	- Wikipedia, Markov chain, 2023 [https://en.wikipedia.org/wiki/Markov_chain](https://en.wikipedia.org/wiki/Markov_chain), luettu 21.3.2023

2. Wang L, Huang W, Li Y, Evans j, He S. Multi‑Ai competing and winning against humans in iterated Rock‑paper‑Scissors game [-raportti](https://arxiv.org/pdf/2003.06769.pdf), doi: https://doi.org/10.1038/s41598-020-70544-7, luettu 20.3.2023

