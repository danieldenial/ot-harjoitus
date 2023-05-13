
from random import shuffle
from repositories.question_repository import QuestionRepository


class QuestionService:
    """Pelin kysymysaineistoon liittyvästä sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, question_repo: QuestionRepository):
        """Luokan konstruktori. Tuo kysymysaineiston luokkaan.

        Konstruktori muodostaa myös kokonaislukujen listan, jonka
        avulla kysymysaineistoa pystyy käsittelemään tehokkaasti.

        Args:
            question_repo: Kysymysdatan talletuksesta vastaava luokkaolio
        """

        self._question_repo = question_repo
        self._question_list = self._question_repo.get_question_list()
        self._index_list = list(range(len(self._question_list)))
        shuffle(self._index_list)
        self._current_index = None

    def check_question_data_exists(self):
        """Tarkistaa onko kysymysaineisto tuotu sovellukseen onnistuneesti.

        Returns:
            Palauttaa kysymysaineiston sisältävän sanakirjojen listan pituuden.
        """

        return len(self._question_list) > 0

    def get_question_list(self):
        """Palauttaa kysymysaineiston.

        Returns:
            Palauttaa kysymysaineiston sisältävän listan sanakirjoja.
        """

        return self._question_list

    def get_question(self):
        """Palauttaa seuraavan kysymyksen indeksin perusteella.

        Returns:
            Palauttaa indeksin mukaisesta sanakirjasta haetun kysymyksen merkkijonona.
        """

        return self._question_list[self._current_index]['Question']

    def get_options(self):
        """Palauttaa vastausvaihtoehdot indeksin perusteella.

        Returns:
            Palauttaa vastausvaihtoehdot listana merkkijonoja satunnaisjärjestyksessä.
        """

        options = [
            self._question_list[self._current_index]['A'],
            self._question_list[self._current_index]['B'],
            self._question_list[self._current_index]['C'],
            self._question_list[self._current_index]['D']
        ]
        shuffle(options)

        return options

    def get_detail_text(self):
        """Palauttaa vastaukseen liittyvän lisätiedon indeksin perusteella.

        Returns:
            Palauttaa indeksin mukaisen lisätiedon merkkijonona.
        """

        return self._question_list[self._current_index]['Detail']

    def evaluate_user_answer(self, user_answer):
        """Arvioi onko käyttäjän vastaus oikein.

        Vertaa käyttäjän vastausta indeksin mukaiseen oikeaan vastaukseen.

        Args:
            user_answer: Käyttäjän valitsema vastaus merkkijonona.

        Returns:
            Palauttaa totuusarvona onko käyttäjän vastaus oikein.
        """

        return self._question_list[self._current_index]['Answer'] == user_answer

    def confirm_there_are_questions_left(self):
        """Varmistaa, että pelikerralla on kysymyksiä vielä jäljellä.

        Returns:
            Palauttaa totuusarvona onko kysymyksiä vielä jäljellä.
        """

        return len(self._index_list) > 0

    def set_next_question_index(self):
        """Asettaa indeksin seuraavaa kysymystä varten.

        Indeksilistalta poistetaan valittu kokonaisluku ja sitä käytetään haluttujen
        tietojen hakemiseen kysymysaineiston sisältävältä sanakirjojen listalta.
        """

        if len(self._index_list) > 0:
            self._current_index = self._index_list.pop()

    def reset_index_list(self):
        """Asettaa indeksilistan takaisin alkutilaansa uutta pelikertaa varten.
        """

        self._index_list = list(range(len(self._question_list)))
        shuffle(self._index_list)
