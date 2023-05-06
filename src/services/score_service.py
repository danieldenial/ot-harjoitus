
class ScoreService:
    def __init__(self, score_repo):
        self._current_score = 0
        self._selected_team = None
        self._score_repo = score_repo

    def get_current_score(self):
        return f"Score: {self._current_score}"

    def reset_current_score(self):
        self._current_score = 0

    def reset_high_score_list(self):
        self._score_repo.reset_high_scores()

    def get_high_score(self):
        return self._score_repo.get_high_score()

    def get_high_scores_list(self):
        return self._score_repo.get_high_scores_list()

    def get_team_names(self):
        return self._score_repo.get_team_name_list()

    def get_selected_team(self):
        return self._selected_team

    def change_selected_team(self, team):
        self._selected_team = team

    def increase_score(self):
        self._current_score += 1

    def check_score(self):
        if self._current_score > min(self._score_repo.get_high_scores_list())[0]:
            self._score_repo.add_new_score_to_list(self._current_score, self._selected_team)

    def store_high_scores(self):
        self._score_repo.write_high_scores_to_file()
