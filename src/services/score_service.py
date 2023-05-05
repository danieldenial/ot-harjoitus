
class ScoreService:
    def __init__(self, scores):
        self._current_score = 0
        self._score_repo = scores

    def get_current_score(self):
        return f"Score: {self._current_score}"

    def provide_high_score(self):
        return self._score_repo.get_high_score()
    
    def get_team_names(self):
        return self._score_repo.get_team_name_list()

    def increase_score(self):
        self._current_score += 1

    def check_score(self):
        if self._current_score > min(self._score_repo.get_high_scores_list()):
            self._score_repo.add_new_score_to_list(self._current_score)
    
    def store_high_scores(self):
        self._score_repo.write_high_scores_to_file()
