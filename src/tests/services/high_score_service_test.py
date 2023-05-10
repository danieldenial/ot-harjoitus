
import unittest
from services.score_service import ScoreService
from repositories.high_score_repository import HighScoreRepository
from random import choice

class TestHighScoreService(unittest.TestCase):

    def setUp(self):
        self._score_data = HighScoreRepository()
        self.HS = ScoreService(self._score_data)

    def test_get_current_score(self):
        comparison = self.HS._current_score
        self.assertEqual(self.HS.get_current_score(), comparison)

    def test_reset_current_score(self):
        self.HS._current_score = 10
        self.HS.reset_current_score()
        self.assertEqual(self.HS._current_score, 0)

    def test_get_high_score(self):
        comparison_score = self._score_data.get_high_score()
        self.assertEqual(self.HS.get_high_score(), comparison_score)
        
    def test_get_high_scores_list(self):
        comparison_score_list = self._score_data.get_high_scores_list()
        self.assertEqual(self.HS.get_high_scores_list(), comparison_score_list)

    def test_reset_high_scores_list(self):
        self.HS.reset_high_scores_list()
        for score in self._score_data._high_scores:
            self.assertEqual(score, (0, "N/A"))

    def test_get_team_names(self):
        self.assertEqual(self.HS.get_team_names(), self._score_data._team_names)

    def test_get_selected_team(self):
        self.assertEqual(self.HS.get_selected_team(), self.HS._selected_team)

    def test_change_selected_team(self):
        team = choice(self._score_data.get_team_name_list())
        if team != self.HS._selected_team:
            self.HS.change_selected_team(team)
            self.assertEqual(self.HS._selected_team, team)
        else:
            self.test_change_selected_team()

    def test_check_score(self):
        self.HS._selected_team = "Rob Lowe"
        self.HS._current_score = max(self._score_data._high_scores)[0]+1
        self.HS.evaluate_score()
        is_true = self.is_value_in_list((self.HS._current_score, "Rob Lowe"))
        self.assertEqual(is_true, True)

    def test_increase_score(self):
        score = self.HS._current_score
        self.HS.increase_score()
        self.assertEqual(self.HS._current_score, score+1)

    def is_value_in_list(self, score):
        return score in self._score_data._high_scores
