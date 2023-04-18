
from random import choice, shuffle
import csv
from pathlib import Path


class QuestionService:
    def __init__(self):
        self._questions = None
        self._key_list = None
        self._number = None

        self._load_questions()

    def _load_questions(self):
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

    def _get_question(self):
        return self._questions[self._number]['Question']
    
    def _get_options(self):
        options = [
            self._questions[self._number]['A'],
            self._questions[self._number]['B'],
            self._questions[self._number]['C'],
            self._questions[self._number]['D']
        ]
        shuffle(options)

        return options

    def _next_question(self):
        if len(self._key_list) > 0:
            self._number = choice(self._key_list)
            self._key_list.remove(self._number)

    def _check_answer(self, user_answer):
        return self._questions[self._number]['Answer'] == user_answer
