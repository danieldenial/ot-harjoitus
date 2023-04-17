
from random import choice
import csv
from pathlib import Path


class QuestionService:
    def __init__(self):
        self._questions = None
        self._key_list = None
        self._number = None

        self.load_questions()

    def load_questions(self):
        file_path = Path(__file__).resolve(
        ).parent.parent.parent / "files" / "questions.csv"

        dict_number = 1
        self._questions = {}

        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self._questions[dict_number] = {
                    'Question': row[0],
                    'A': row[1], 'B': row[2],
                    'C': row[3], 'D': row[4],
                    'Answer': row[5]
                }
                dict_number += 1

        self._key_list = list(self._questions.keys())

    def _next_question(self):
        if len(self._key_list) > 0:
            self._number = choice(self._key_list)
            self._key_list.remove(self._number)
            return self._questions[self._number]
        else:
            pass

    def _check_question(self, user_answer):
        return self._questions['answer'] == user_answer
