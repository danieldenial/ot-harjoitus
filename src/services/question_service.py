
from random import shuffle
from repositories.questions import Questions


class QuestionService:
    def __init__(self):
        self._questions = Questions()._questions_dictionary
        self._key_list = list(self._questions.keys())
        shuffle(self._key_list)
        self._number = None

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

    def _check_answer(self, user_answer):
        return self._questions[self._number]['Answer'] == user_answer

    def _next_question(self):
        if len(self._key_list) > 0:
            self._number = self._key_list.pop()
