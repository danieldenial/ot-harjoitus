
from random import shuffle
from repositories.question_repository import QuestionRepository


class QuestionService:
    """Luokka, jonka avulla hallinnoidaan sovelluksen kysymysdatan käsittelyä.

    Attributes:
        _question_repo: Kysymysdatan talletuksesta vastaava luokkaolio
        _question_list: Kysymysdata listana sanakirjoja
        _index_list: Kysymysdatan sanakirjalistan mahdolliset indeksit
        _index: Kysymyksen valintaa varten määriteltävä indeksi
    """

    def __init__(self, question_repo: QuestionRepository):
        """Luokan konstruktori, joka 

        Args:
            question_repo: Kysymysdatan talletuksesta vastaava luokkaolio
        """

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

    def evaluate_user_answer(self, user_answer):
        return self._question_list[self._index]['Answer'] == user_answer

    def set_next_question_index(self):
        if len(self._index_list) > 0:
            self._index = self._index_list.pop()

    def reset_index_list(self):
        self._index_list = list(range(len(self._question_list)))
        shuffle(self._index_list)
