import csv
from pathlib import Path


class QuestionRepository:
    def __init__(self):
        self.question_list = []
        self._file_path = Path(__file__).resolve(
        ).parent.parent.parent / "files" / "questions.csv"

        self._load_questions()

    def _load_questions(self):
        with open(self._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                question = {
                    'Question': row[0],
                    'A': row[1], 'B': row[2],
                    'C': row[3], 'D': row[4],
                    'Answer': row[5],
                    'Detail': row[6]
                }
                self.question_list.append(question)

    def get_question_list(self):
        return self.question_list
