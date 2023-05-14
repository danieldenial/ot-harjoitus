# Käyttöohje

## Päävalikko

Sovellus käynnistyy päävalikon näkymään:

![](./kuvat/main_menu.png)

Käyttäjä voi valita uuden pelin painamalla "NEW GAME" -painiketta.

Parhaat tulokset saa nähtäville "SCORES" -painiketta painamalla.

Pelin sääntöjä pääsee lukemaan painamalla "RULES" -painiketta.

Sovelluksen voi sulkea painamalla "QUIT"-painiketta.

## Uuden pelin aloitus

Pelin alkamista edeltää näkymä, jossa käyttäjä pääsee valitsemaan 
joukkueensa ja näkee pelin parhaan talletetun tuloksen:

![](./kuvat/new_game.png)

Uusi peli alkaa käyttäjän painettua "START" -painiketta. Takaisin 
päävalikkoon voi palata painamalla "BACK"-painiketta.

## Vastauksen valitseminen

Pelin alettua vaihtuu näkymä seuraavanlaiseksi:

![](./kuvat/question.png)

Käyttäjä näkee ruudulta kysymyksen, siihen liittyvät vastausvaihtoehdot 
sekä oman senhetkisen tuloksensa ("Score").

Käyttäjä voi vastata kysymykseen painamalla painiketta "A", "B", "C" tai 
"D" sen vaihtoehdon kohdalla, jonka uskoo olevan oikein.

## Seuraavaan kysymykseen siirtyminen

Mikäli käyttäjän vastaus on oikein, pelikerta jatkuu ja näkymä päivittyy 
seuraavanlaiseksi:

![](./kuvat/correct_answer.png)

Käyttäjä voi huomata vastauksensa menneen oikein painikkeen vihreäksi 
muuttuneesta väristä sekä lyhyestä tekstimuotoisesta vahvistuksesta. 
Käyttäjä voi lukea ruudulta myös pienen vastaukseen liittyvän lisätiedon.

Käyttäjän pistemäärä ("Score") on kasvanut tässä näkymässä myös yhdellä 
oikein menneen vastauksen myötä.

Käyttäjä voi jatkaa seuraavaan kysymykseen painamalla 
"CONTINUE"-painiketta.

## Pelin päättyminen

Mikäli käyttäjän valitsema vastaus on väärin, päättyy peli ja näkymä 
päivittyy seuraavanlaiseksi:

![](./kuvat/wrong_answer.png)

Käyttäjä voi huomata vastauksensa menneen väärin painikkeen punaiseksi 
muuttuneesta väristä sekä lyhyestä tekstimuotoisesta vahvistuksesta. 
Mikäli käyttäjän tulos on korkeampi kuin aiempi korkein talletettu tulos, 
kerrotaan se myös käyttäjälle ruudulla (kuten esimerkkikuvassa).

Käyttäjä voi valita uuden pelin painamalla "NEW GAME"-painiketta, palata 
takaisin päävalikkoon painamalla "MAIN MENU" -painiketta, tai sulkea 
sovelluksen painamalla "QUIT"-painiketta.

## Parhaiden tulosten tarkastelu

Taulukon parhaista talletetuista tuloksista sisältävä näkymä on 
seuraavankaltainen:

![](./kuvat/high_scores.png)

Käyttäjä voi halutessaan nollata tulostaulukon "RESET"-painikkeesta. Tämän 
jälkeen taulukko ja näkymä päivittyy seuraavankaltaiseksi:

![](./kuvat/high_scores_reset.png)

Käyttäjä voi palata takaisin päävalikkoon painamalla "MAIN MENU".

## Sovelluksen sulkeminen

Ennen sovelluksen sulkemista siirrytään näkymään, jossa varmistetaan 
käyttäjän valinta:

![](./kuvat/quitting.png)

Käyttäjä voi sulkea sovelluksen painamalla "YES"-painiketta. 
"NO"-painikkeen painaminen vie takaisin päävalikkoon.
