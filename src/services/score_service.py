
from random import choice
from repositories.high_score_repository import HighScoreRepository


class ScoreService:
    """Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, score_repo: HighScoreRepository):
        """Luokan konstruktori. Asettaa pistemäärän ja alustavasti valitun joukkueen.

        Args:
            score_repo: Pisteytykseen liittyvän tiedon käsittelystä vastaavan luokan olio.
        """

        self._current_score = 0
        self._score_repo = score_repo
        self._selected_team = choice(self._score_repo.get_team_name_list())

    def get_current_score(self):
        """Palauttaa pelin senhetkisen pistemäärän.

        Returns:
            Palauttaa senhetkistä pistemäärää kuvaavan kokonaisluvun.
        """

        return self._current_score

    def get_current_score_text(self):
        """Palauttaa pelin senhetkisen pistemäärän tekstimuodossa.

        Returns:
            Palauttaa merkkijonon, johon on sisällytetty senhetkinen pistemäärä.
        """

        return f"Score: {self._current_score}"

    def reset_current_score(self):
        """Nollaa pelin pistemäärän uutta pelikertaa varten.
        """

        self._current_score = 0

    def get_high_score(self):
        """Hakee ja palauttaa pelin korkeimman talletetun pistesuorituksen. 

        Returns:
            Palauttaa korkeinta talletettua pistesuoritusta edustavan kokonaisluvun.
        """

        return self._score_repo.get_high_score()

    def get_high_scores_list(self):
        """Hakee ja palauttaa korkeimman talletettujen pistesuoritusten listan.

        Returns:
            Palauttaa korkeimmat talletetut pistesuoritukset listana tupleja.
        """

        return self._score_repo.get_high_scores_list()

    def reset_high_scores_list(self):
        """Nollaa parhaiden pistesuoritusten listan.
        """

        self._score_repo.reset_high_scores()

    def get_team_names(self):
        """Palauttaa pelissä valittavien joukkueiden nimien listan.

        Returns:
            Palauttaa pelissä valittavat joukkueet listana merkkijonoja.
        """

        return self._score_repo.get_team_name_list()

    def get_selected_team(self):
        """Palauttaa sillä hetkellä valittuna olevan joukkueen.

        Returns:
            Palauttaa valitun joukkueen nimen merkkijonona.
        """

        return self._selected_team

    def change_selected_team(self, new_team):
        """Vaihtaa valitun joukkueen nimen.

        Args:
            new_team: 
                Käyttäjän valitsema uusi joukkue merkkijonona.
        """

        self._selected_team = new_team

    def increase_score(self):
        """Lisää pistemäärää yhdellä käyttäjän vastattua kysymykseen oikein.
        """

        self._current_score += 1

    def evaluate_score(self):
        """Arvioi käyttäjän arvioiman pistemäärää suhteessa parhaisiin tuloksiin.

        Mikäli käyttänän saavuttama pistemäärä on suurempi kuin huonoin 
        parhaiden tulosten listalla oleva pistemäärä, lisätään suoritus listalle.
        """

        if self._current_score > self._score_repo.get_lowest_high_score_on_list():
            self._score_repo.add_new_score_to_list(
                self._current_score, self._selected_team)

    def store_high_scores(self):
        """Tallettaa parhaat pistesuoritukset.
        """

        self._score_repo.write_high_scores_to_file()
