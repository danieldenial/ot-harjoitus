
from pathlib import Path
import csv
from config import DATA_FOLDER


class HighScoreRepository:
    """Luokka, joka vastaa parhaiden pistesuoritusten talletuksesta.

    Attributes:
        _high_scores: Parhaiden pistesuoritusten lista
        _team_names: Valittavien joukkueiden lista
        _score_file_path: Parhaat tulokset sisältävän tiedoston polku
        _name_file_path: Joukkueiden nimet sisältävän tiedoston polku
    """

    def __init__(self, score_file_name, team_file_name):
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
            print(self._team_names)
        except FileNotFoundError:
            self._team_names = ['AFC', 'NFC']
            self.create_team_name_file()

    def get_high_score(self):
        return max(self._high_scores)[0]

    def get_high_scores_list(self):
        return self._high_scores

    def get_lowest_high_score_on_list(self):
        return min(self._high_scores)[0]

    def get_team_name_list(self):
        return self._team_names

    def add_new_score_to_list(self, new_score, selected_team):
        self._high_scores.sort(reverse=True)
        self._high_scores.pop()
        self._high_scores.append((new_score, selected_team))

    def create_team_name_file(self):
        with open(self._name_file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            for team in self._team_names:
                writer.writerow(team)

    def write_high_scores_to_file(self):
        self._high_scores.sort(reverse=True)
        with open(self._score_file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            for score in self._high_scores:
                writer.writerow([score[0], score[1]])

    def reset_high_scores(self):
        self._high_scores = [(0, "N/A") for _ in range(10)]
        self.write_high_scores_to_file()
