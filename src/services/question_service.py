
from random import shuffle
from repositories.question_repository import QuestionRepository


class QuestionService:
    def __init__(self):
        self._questions = QuestionRepository()._questions_dictionary
        self._key_list = list(self._questions.keys())
        shuffle(self._key_list)
        self._number = None

    def get_question(self):
        return self._questions[self._number]['Question']

    def get_options(self):
        options = [
            self._questions[self._number]['A'],
            self._questions[self._number]['B'],
            self._questions[self._number]['C'],
            self._questions[self._number]['D']
        ]
        shuffle(options)

        return options

    def get_detail(self):
        return self._questions[self._number]['Detail']

    def check_answer(self, user_answer):
        return self._questions[self._number]['Answer'] == user_answer

    def get_next_question_key(self):
        if len(self._key_list) > 0:
            self._number = self._key_list.pop()
