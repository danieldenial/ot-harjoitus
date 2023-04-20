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
- Paras saavutettu pistemäärä (high score) talletetaan csv-tiedostoon.
- Käyttäjä voi palata väärän vastauksen jälkeen päävalikkoon.
