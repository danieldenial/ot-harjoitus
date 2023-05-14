
from pathlib import Path
import csv
from config import DATA_FOLDER


class HighScoreRepository:
    """Pisteytykseen liittyvän lukemisesta, talletuksesta ja käsittelystä vastaava luokka.
    """

    def __init__(self, score_file_name, team_file_name):
        """Luokan konstruktori. Luo pohjan pisteytykseen liittyvän tiedon käsittelylle. 

        Args:
            score_file_name: 
                Pelin parhaat pistesuoritukset sisältävän tiedoston nimi.
            team_file_name:
                Pelissä valittavien joukkueiden nimet sisältävän tiedoston nimi.
        """

        self._high_scores = []
        self._team_names = []

        self._score_file_path = Path(__file__).resolve(
        ).parents[2] / DATA_FOLDER / score_file_name

        self._name_file_path = Path(__file__).resolve(
        ).parents[2] / DATA_FOLDER / team_file_name

        self._load_team_name_list()
        self._load_high_score_list()

    def _load_high_score_list(self):
        try:
            with open(self._score_file_path, mode="r", encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    self._high_scores.append((int(row[0]), row[1]))
        except (FileNotFoundError, ValueError, StopIteration):
            self._high_scores = [(0, "N/A") for _ in range(10)]
            self.write_high_scores_to_file()

    def _load_team_name_list(self):
        try:
            with open(self._name_file_path, mode="r", encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    self._team_names.append(row[0])
        except FileNotFoundError:
            self._team_names = ['AFC', 'NFC']
            self._create_team_name_file()

    def get_high_score(self):
        """Palauttaa pelin korkeimman talletetun pistesuorituksen.

        Returns:
            Palauttaa korkeinta talletettua pistesuoritusta edustavan kokonaisluvun.
        """

        return max(self._high_scores)[0]

    def get_high_scores_list(self):
        """Palauttaa korkeimman talletettujen pistesuoritusten listan.

        Returns:
            Palauttaa korkeimmat talletetut pistesuoritukset listana tupleja.
        """

        return self._high_scores

    def get_lowest_high_score_on_list(self):
        """Palauttaa matalimman talletetun pistesuorituksen parhaiden pisteiden listalta.

        Returns:
            Palauttaa matalinta talletettua pistesuoritusta edustavan kokonaisluvun.
        """
        return min(self._high_scores)[0]

    def get_team_name_list(self):
        """Palauttaa pelissä valittavien joukkueiden nimien listan.

        Returns:
            Palauttaa pelissä valittavat joukkueet listana merkkijonoja.
        """

        return self._team_names

    def add_new_score_to_list(self, new_score, selected_team):
        """Lisää uuden tuloksen parhaiden pistesuoritusten listalle.

        Poistaa listalta samalla huonoimman tuloksen, jotta listan pituus ei muutu.

        Args:
            new_score: Lisättävän tuloksen pistemäärä kokonaislukuna.
            selected_team: Lisättävän tuloksen joukkue merkkijonona.
        """

        self._high_scores.sort(reverse=True)
        self._high_scores.pop()
        self._high_scores.append((new_score, selected_team))

    def _create_team_name_file(self):
        with open(self._name_file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            for team in self._team_names:
                writer.writerow(team)

    def write_high_scores_to_file(self):
        """Tallettaa parhaat pistesuoritukset (pistemäärä ja joukkue) csv-tiedostoon.

        Tiedosto talletetaan paikallisesti konstruktorin määrittelemään polkuun.
        """

        self._high_scores.sort(reverse=True)
        with open(self._score_file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            for score in self._high_scores:
                writer.writerow([score[0], score[1]])

    def reset_high_scores(self):
        """Nollaa parhaiden pistesuoritusten listan.
        """

        self._high_scores = [(0, "N/A") for _ in range(10)]
        self.write_high_scores_to_file()
