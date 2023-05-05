
from pathlib import Path
import csv


class HighScoreRepository:
    def __init__(self):
        self._high_scores = []
        self._team_names = []
        self._score_file_path = Path(__file__).resolve(
        ).parent.parent.parent / "files" / "high_scores.csv"
        self._name_file_path = Path(__file__).resolve(
        ).parent.parent.parent / "files" / "team_names.csv"

        self._load_high_score_list()
        self._load_team_name_list()

    def _load_high_score_list(self):
        try:
            with open(self._score_file_path, mode="r", encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    self._high_scores.append(int(row[0]))
        except (FileNotFoundError, ValueError, StopIteration):
            for i in range(10):
                self._high_scores.append(0)

    def _load_team_name_list(self):
        try:
            with open(self._score_file_path, mode="r", encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    self._team_names.append(row[0])
        except:
            self._team_names.append("AFC")
            self._team_names.append("NFC")

    def get_high_score(self):
        return max(self._high_scores)

    def get_high_scores_list(self):
        return self._high_scores
    
    def get_team_name_list(self):
        return self._team_names

    def add_new_score_to_list(self, new_score):
        self._high_scores.sort(reverse=True)
        self._high_scores.pop()
        self._high_scores.append(new_score)

    def write_high_scores_to_file(self):
        self._high_scores.sort(reverse=True)
        with open(self._score_file_path, mode="w", encoding="utf-8") as file:
                writer = csv.writer(file)
                for score in self._high_scores:
                    writer.writerow([score])

    def _reset_high_scores(self):
        with open(self._score_file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            for i in range(10):
                writer.writerow([0])
        self._high_scores = []
