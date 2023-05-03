
from random import shuffle


class QuestionService:
    def __init__(self, question_data):
        self._question_dictionary = question_data.give_dictionary()
        self._key_list = list(self._question_dictionary.keys())
        shuffle(self._key_list)
        self._number = None

    def get_question(self):
        return self._question_dictionary[self._number]['Question']

    def get_options(self):
        options = [
            self._question_dictionary[self._number]['A'],
            self._question_dictionary[self._number]['B'],
            self._question_dictionary[self._number]['C'],
            self._question_dictionary[self._number]['D']
        ]
        shuffle(options)

        return options

    def get_detail_text(self):
        return self._question_dictionary[self._number]['Detail']

    def check_answer(self, user_answer):
        return self._question_dictionary[self._number]['Answer'] == user_answer

    def set_next_question_key(self):
        if len(self._key_list) > 0:
            self._number = self._key_list.pop()
