# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on eräänlainen tietovisapeli, jonka teemana on amerikkalaisen 
jalkapallon ammattilaissarja NFL. Pelaaminen etenee seuraavalla tavalla: 
Käyttäjä aloittaa pelin ja vastaa yksitellen kysymyksiin. Jokaiselle 
kysymykselle annetaan neljä eri vastausvaihtoehtoa, joista yksi on oikein. 
Pelaaminen jatkuu niin kauan kuin käyttäjä vastaa kysymyksiin oikein tai 
kysymykset loppuvat kesken. Jälkimmäinen ei ole todennäköistä, sillä jo 
ensimmäisessä versiossa kysymyksiä on 100. Yksittäinen peli päättyy 
väärään vastaukseen.

## Käyttäjät

Tällä erää sovelluksen ainoa käyttäjärooli on pelaaja eli 
_normaali käyttäjä_. Mikäli laajempia käyttöoikeuksia hyödyntävä 
_pääkäyttäjä_ alkaa vaikuttaa jossain vaiheessa tarpeelliselta roolilta, 
on se mahdollista lisätä myöhemmin mukaan sovellukseen.

## Sovelluksen toiminnallisuudet

### Päävalikko

- Käyttäjä voi siirtyä aloittamaan uuden pelin
- Käyttäjä voi siirtyä tarkastelemaan parhaita tuloksia
- Käyttäjä voi siirtyää katsomaan pelin ohjeita
- Käyttäjä voi sulkea sovelluksen

### Ennen pelin alkua

- Käyttäjä voi valita listalta joukkueen, jonka nimissä peliä pelaa
- Käyttäjä näkee ruudulla pelin parhaan talletetun tuloksen
- Käyttäjä voi käynnistää pelin
- Käyttäjä voi siirtyä takaisin päävalikkoon

### Varsinainen peli

- Ruudulla näkyy kysymyksiä yksi kerrallaan
	- Kysymykset esitetään satunnaisessa järjestyksessä
	- Yksikään kysymyksistä ei toistu saman yksittäisen pelikerran 
aikana, (peräkkäisissä peleissä toistoa voi alkaa jo esiintyä)
- Ruudulla näkyy aina neljä kysymykseen liittyvää 
vastausvaihtoehtoa
	- Kunkin kysymyksen vaihtoehdot esitetään aina satunnaisessa järjestyksessä
	- Käyttäjä voi valita oikeaksi uskomansa vastausvaihtoehdon 
painikkeesta 'A', 'B', 'C' tai 'D'
- Vastauksen jälkeen sovellus näyttää ja kertoo menikö vastaus oikein vai 
väärin
	- Oikean vastauksen jälkeen valittu painike muuttuu vihreäksi ja 
väärän vastauksen jälkeen punaiseksi
	- Oikean vastauksen jälkeen ruudulle ilmestyy teksti, joka kertoo 
vastauksen menneen oikein sekä lyhyt kysymykseen ja/tai vastaukseen 
liittyvä lisätieto
	- Väärän vastauksen jälkeen ruudulle ilmestyy teksti, joka kertoo 
vastauksen menneen väärin (mikäli käyttäjä teki uuden ennätyksen, ilmestyy 
ruudulle myös tästä kertova lyhyt teksti)
- Käyttäjä saa oikeasta vastauksesta pisteen ja pystyy jatkamaan 
seuraavaan kysymykseen "CONTINUE"-painikkeesta
- Peli päättyy väärään vastaukseen
	- Pelin päättymisen jälkeen käyttäjä valita uuden 
pelin, palata päävalikkoon tai sulkea sovelluksen

### Parhaiden tulosten tarkastelu

- Käyttäjä näkee ruudun taulukosta 10 parasta saavutettua tulosta ja 
joukkueet, joiden nimissä ne saavutettiin
- Käyttäjä voi halutessaan nollata tulostaulukon

## Sovelluksen muut keskeiset ominaisuudet

### Tiedostot

- Sovelluksen uusin versio sisältää tsv-tiedoston, johon on talletettu pelin kysymysaineisto version 
julkaisuhetkellä
- Sovellus tarkastaa käynnistyessään, että tiedosto löytyy määritellystä paikallisesta kansiosta
	- Mikäli tiedosto jostain syystä puuttuu, lataa sovellus sen automaattisesti verkosta määritellystä 
osoitteesta (Google Sheets) ja tallentaa tämän version paikallisesti sille tarkoitettuun kansioon
	- Mikäli tiedosto löytyy jo paikallisesta kansiosta, tarkastaa sovellus automaattisesti, ettei 
saatavilla ole uudempaa versiota kysymystiedostosta
	- Mikäli verkko-osoitteesta löytyvä tiedosto on uudempi, lataa ja tallettaa sovellus sen

## Jatkokehitysideoita

Sovellusta on tarkoitus täydentää ainakin vielä joillain seuraavista 
toiminnallisuuksista.

- Taulukko parhaista suorituksista verkkoon, jotta käyttäjät voivat 
kilpailla myös muilla tietokoneilla pelaavia vastaan
- Mahdollisuus pelata joukkueen nimien lisäksi omalla nimellä tai 
nimimerkillä
	- Myös mahdollisuus luoda käyttäjätili ja tallentaa omia 
suorituksia
	- Periaatteessa jokainen voi jo tässä vaiheessa pelata myös omalla 
nimellään lisäämällä sen csv-tiedostoon, josta sovellus nimet lukee 
käynnistymisen yhteydessä
- Mahdollisuus valita eri vaikeustasoja
- Aikaraja kysymyksiin vastaamisessa
	- Mahdollisesti myös oikean vastauksen pisteiden määräytyminen 
vastauksen nopeuden mukaan
- Paljon, todella paljon lisää kysymyksiä, sillä ne ovat lopulta tämän 
sovelluksen sydän
