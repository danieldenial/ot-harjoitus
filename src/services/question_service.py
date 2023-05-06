
from random import shuffle


class QuestionService:
    def __init__(self, question_repo):
        self._question_repo = question_repo
        self._question_list = self._question_repo.get_question_list()
        self._index_list = list(range(len(self._question_list)))
        shuffle(self._index_list)
        self._index = None

    def get_question_list(self):
        return self._question_list

    def get_question(self):
        return self._question_list[self._index]['Question']

    def get_options(self):
        options = [
            self._question_list[self._index]['A'],
            self._question_list[self._index]['B'],
            self._question_list[self._index]['C'],
            self._question_list[self._index]['D']
        ]
        shuffle(options)

        return options

    def get_detail_text(self):
        return self._question_list[self._index]['Detail']

    def check_answer(self, user_answer):
        return self._question_list[self._index]['Answer'] == user_answer

    def set_next_question_index(self):
        if len(self._index_list) > 0:
            self._index = self._index_list.pop()

    def reset_index_list(self):
        self._index_list = list(range(len(self._question_list)))
        shuffle(self._index_list)
