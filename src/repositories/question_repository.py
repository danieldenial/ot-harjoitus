import csv
from pathlib import Path


class QuestionRepository:
    def __init__(self):
        self._questions_dictionary = {}
        self._file_path = Path(__file__).resolve(
        ).parent.parent.parent / "files" / "questions.csv"

        self._load_questions()

    def _load_questions(self):
        dict_number = 1

        with open(self._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self._questions_dictionary[dict_number] = {
                    'Question': row[0],
                    'A': row[1], 'B': row[2],
                    'C': row[3], 'D': row[4],
                    'Answer': row[5]
                }
                dict_number += 1
