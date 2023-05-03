
class ScoreService:
    def __init__(self, score_data):
        self._current_score = 0
        self._score_data = score_data

    def get_current_score(self):
        return f"Score: {self._current_score}"

    def get_high_score(self):
        return self._score_data.give_high_score()

    def increase_score(self):
        self._current_score += 1

    def check_score(self):
        if self._current_score > self.get_high_score():
            self._score_data.set_new_high_score(self._current_score)
