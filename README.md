# Gridiron Genius: An NFL Trivia Game

Gridiron Genius on visailupeli, jossa käyttäjä pääsee testaamaan tietojaan 
liittyen amerikkalaisen jalkapallon NFL-sarjaan.

## Huomio Python-versiosta

Sovellus on testattu Python-versiolla `3.8`, joten vanhempien versioiden kanssa saattaa ilmetä ongelmia.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](./dokumentaati/arkkitehtuuri.md)

- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

- [Changelog](./dokumentaatio/changelog.md)

## GitHub-release

- [Versio 1.0](https://github.com/danieldenial/ot-harjoitus/releases/tag/viikko5)

- [Versio 1.1](https://github.com/danieldenial/ot-harjoitus/releases/tag/viikko6)

## Asennus

1. Riippuvuuksien asentamisen komento:

```bash
poetry install
```

2. Sovelluksen käynnistämisen komento:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman suorittamisen komento:

```bash
poetry run invoke start
```

### Testaus

Testien suorittamisen komento:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin generoimisen komento:

```bash
poetry run invoke coverage-report
```

Raportti generoituu hakemistoon _htmlcov_.

Mikäli haluaa tarkastella testikattavuusraporttia suoraan komentoriviltä, saa sen luotua seuraavalla komennolla:

```bash
poetry run invoke coverage-rprt
```

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemien tarkistusten suorittamisen komento:

```bash
poetry run invoke lint
```
