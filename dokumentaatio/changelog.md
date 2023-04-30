## Viikko 3

- Käyttöliittymän ensimmäinen versio on valmis, mutta näkymät hajoavat vielä pahasti  sovellusta  eri koneilta käyttäessä. Tämä on 
syytä korjata seuraavaksi.
- Käyttäjä pystyy valitsemaan päävalikosta uuden pelin (mutta ei 
kuitenkaan vielä aloittamaan peliä).
- Käyttäjä pystyy siirtymään sääntösivulle ja palaamaan sieltä takaisin 
päävalikkoon.
- Käyttäjä pystyy lopettamaan sovelluksen valikosta (tai palaamaan 
lopettamisen sijaan takaisin päävalikkoon).


## Viikko 4

- Karsittu aiemman koodin toistoa laittamalla luokat käyttöliittymän näkymistä vastaavat luokat perimään näkymät vanhemmalta 
luokalta.
- Yritetty parantaa käyttöliittymän näkymien yhtenäisyyttä eri käyttöjärjestelmissä/koneilla (vaatii vielä lisätyötä).
- Yritetty eriyttää sovelluslogiikka käyttöliittymästä. (Tämäkin vaatii edelleen lisätyötä).
- Lisätty 20 kysymystä csv-tiedostoon, jonka sisältö tuodaan peliin sanakirjan muodossa sovelluksen avaamisen yhteydessä. 
Kysymykset esitetään pelissä satunnaisessa järjestyksessä.
- Uusia luokkia lisätty pelinkulkua ja kysymysten käsittelyä varten.
- Luotu varsinaisen kyselypelin toiminnallisuuksia: Käyttäjä näkee nyt pelin aloitettuaan kysymyksen sekä siihen liittyvät 
vastausvaihtoehdot ja pystyy valitsemaan oman vastauksensa. Peli jatkuu seuraavaan kysymykseen, jos vastaus on oikein.


## Viikko 5

- Pelin yhteydessä näkyy pelaajan pistemäärä. Jokaisesta oikeasta 
vastauksesta saa tässä vaiheessa yhden pisteen.
- Paras tähänastinen pistemäärä/tulos (high score) talletetaan csv-tiedostoon.
- Paras tähänastinen pistemäärä/tulos näytetään ennen jokaisen pelin alkua.
- Käyttäjä voi palata väärän vastauksen jälkeen päävalikkoon.

## Viikko 6

- Pelin kysymyksille, vastausvaihtoehdoille ja muille pelinaikaisille 
ruudulla näkyville elementeille on luotu omat kehykset.
- Pidemmätkin kysymykset näkyvät ruudulla nyt paremmin, koska ne on jaettu 
useammalle riville.
- Dokumentaatiota edistetty lisäämällä reilusti docstringiä.
