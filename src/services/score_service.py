
from repositories.high_score_repository import HighScoreRepository


class ScoreServices:
    def __init__(self):
        self._current_score = 0
        self._high_score = HighScoreRepository()._high_score

    def get_current_score(self):
        return f"Score: {self._current_score}"

    def get_high_score(self):
        return self._high_score

    def increase_score(self):
        self._current_score += 1

    def check_score(self):
        if self._current_score > self._high_score:
            HighScoreRepository().set_new_high_score(self._current_score)
