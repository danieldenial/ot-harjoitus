# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on eräänlainen tietovisapeli, jonka teemana on amerikkalaisen 
jalkapallon ammattilaissarja NFL. Pelin pelaaminen tulee etenemään 
seuraavalla tavalla: Käyttäjä aloittaa pelin ja vastaa yksitellen 
kysymyksiin, joista jokaiselle annetaan neljä eri vastausvaihtoehtoa. 
Pelaaminen jatkuu niin kauan kuin käyttäjä vastaa oikein tai läpäisee 
pelin. Peli päättyy puolestaan väärään vastaukseen.

## Käyttäjät

Lähtökohtaisesti sovelluksen ainoa käyttäjärooli on pelaaja eli 
_normaali käyttäjä_. Mikäli suurempia käyttöoikeuksia hyödyntävä 
_pääkäyttäjä_ alkaa vaikuttaa jossain vaiheessa hyödylliseltä roolilta, 
lisätään sellainen  mukaan sovellukseen.

## Perusversion suunnitellut toiminnallisuudet

### Päävalikko

- Käyttäjä voi aloittaa uuden pelin
- Käyttäjä voi katsoa pelin ohjeita
- Käyttäjä voi sulkea sovelluksen
- Käyttäjä näkee ruudulta parhaan tähän asti tehdyn tuloksen
 
### Varsinainen peli

- Ruudulle tulee kysymyksiä yksi kerrallaan ja satunnaisessa 
järjestyksessä.
	- Yksikään kysymyksistä ei toistu saman yksittäisen pelikerran 
aikana (kysymykset saattavat kuitenkin toistua, jos käyttäjä pelaa monta 
peräkkäistä peliä).
- Jokaisella kysymyksellä on 4 vastausvaihtoehtoa, joista käyttäjä 
valitsee yhden.
	- Sovellus kertoo tai näyttää menikö vastaus oikein vai väärin. 
-  Oikean vastauksen jälkeen peli jatkuu seuraavaan kysymykseen.
- Oikeasta vastauksesta tulee käyttäjälle piste lisää (tai pisteitä, 
riippuen lopullisesta toteutustavasta).
- Peli päättyy joko väärään vastaukseen tai viimeistään siinä vaiheessa, 
kun käyttäjä on vastannut kaikkiin kysymyksiin oikein sillä 
pelikerralla.
	- Pelin päättymisen jälkeen käyttäjä voi aloittaa suoraan uuden 
pelin, palata päävalikkoon tai lopettaa sovelluksen käytön.

## Jatkokehitysideoita

- Taulukko parhaista suorituksista pistemäärän mukaan (high scores)
	- Ehkä jopa verkkoon, jotta käyttäjä voi kilpailla myös muilla 
koneilla pelaavia vastaan?
- Käyttäjätunnuksen luominen omien suoritusten tallentamiseksi (joko 
paikallisesti tai verkkoon)
- Vaikeustason valinta
- Aikaraja kysymyksiin vastaamisessa
	- Mahdollisesti myös oikean vastauksen pisteyden määräytyminen 
vastauksen nopeuden mukaan
- Jonkun kiinnostavan ja kysymykseen liittyvän tarkentavan tiedon 
antaminen pelaajalle oikean vastauksen jälkeen (esimerkiksi jos kysytään 
eniten maaleja kerännyttä pelaajaa, niin oikean vastauksen jälkeen 
kerrotaan tarkka maalimäärä).
