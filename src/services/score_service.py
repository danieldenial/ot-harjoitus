
from random import choice
from repositories.high_score_repository import HighScoreRepository


class ScoreService:
    """Luokka, jonka avulla hallinnoidaan pisteiden käsittelyä.

    Attributes:
        _current_score: Nykyinen pistemäärä
        _selected_team: Valittu joukkue
        _score_repo: Pistesuoritusten talletuksesta vastaava luokkaolio
    """

    def __init__(self, score_repo: HighScoreRepository):
        self._current_score = 0
        self._score_repo = score_repo
        self._selected_team = choice(self._score_repo.get_team_name_list())

    def get_current_score(self):
        """Palauttaa senhetkisen pistemäärän.

        Returns:
            _current_score: Pistemäärä sillä hetkellä
        """

        return self._current_score

    def get_current_score_text(self):
        return f"Score: {self._current_score}"

    def reset_current_score(self):
        self._current_score = 0

    def get_high_score(self):
        return self._score_repo.get_high_score()

    def get_high_scores_list(self):
        return self._score_repo.get_high_scores_list()

    def reset_high_scores_list(self):
        self._score_repo.reset_high_scores()

    def get_team_names(self):
        return self._score_repo.get_team_name_list()

    def get_selected_team(self):
        return self._selected_team

    def change_selected_team(self, new_team):
        self._selected_team = new_team

    def increase_score(self):
        self._current_score += 1

    def evaluate_score(self):
        if self._current_score > self._score_repo.get_lowest_high_score_on_list():
            self._score_repo.add_new_score_to_list(
                self._current_score, self._selected_team)

    def store_high_scores(self):
        self._score_repo.write_high_scores_to_file()
