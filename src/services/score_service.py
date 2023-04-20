
from repositories.high_scores import HighScores


class ScoreServices:
    def __init__(self):
        self._current_score = 0
        self._high_score = HighScores()._high_score

    def _get_current_score(self):
        return f"Score: {self._current_score}"

    def _get_high_score(self):
        return self._high_score

    def _increase_score(self):
        self._current_score += 1

    def _check_score(self):
        if self._current_score > self._high_score:
            HighScores().set_new_high_score(self._current_score)
