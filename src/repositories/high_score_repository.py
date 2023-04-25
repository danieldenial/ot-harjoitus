
from pathlib import Path
import csv


class HighScoreRepository:
    def __init__(self):
        self._high_score = None
        self._file_path = Path(__file__).resolve(
        ).parent.parent.parent / "files" / "high_scores.csv"

        self._load_high_score()

    def _load_high_score(self):
        try:
            with open(self._file_path, mode="r", encoding='utf-8') as file:
                reader = csv.reader(file)
                row = next(reader)
                self._high_score = int(row[0])
        except (FileNotFoundError, ValueError, StopIteration):
            self._high_score = 0

    def set_new_high_score(self, new_score):
        with open(self._file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([new_score])
        self._high_score = new_score

    def _reset_high_score(self):
        with open(self._file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([0])
        self._high_score = 0
