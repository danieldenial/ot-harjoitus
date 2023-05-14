
import unittest
from pathlib import Path
import os
import shutil
from services.score_service import ScoreService
from repositories.high_score_repository import HighScoreRepository
from random import choice
from config import SCORE_FILE_NAME, TEAM_FILE_NAME, DATA_FOLDER

class TestScoreService(unittest.TestCase):

    def setUp(self):
        self.test_dir_path = Path(__file__).resolve(
        ).parents[3] / DATA_FOLDER
        os.makedirs(self.test_dir_path, exist_ok=True)
        self.score_data = HighScoreRepository(SCORE_FILE_NAME, TEAM_FILE_NAME)
        self.test_service = ScoreService(self.score_data)

    def tearDown(self):
        shutil.rmtree(self.test_dir_path)

    def test_get_current_score(self):
        comparison = self.test_service._current_score
        self.assertEqual(self.test_service.get_current_score(), comparison)

    def test_reset_current_score(self):
        self.test_service._current_score = 10
        self.test_service.reset_current_score()
        self.assertEqual(self.test_service._current_score, 0)

    def test_get_high_score(self):
        comparison_score = self.score_data.get_high_score()
        self.assertEqual(self.test_service.get_high_score(), comparison_score)
        
    def test_get_high_scores_list(self):
        comparison_score_list = self.score_data.get_high_scores_list()
        self.assertEqual(self.test_service.get_high_scores_list(), comparison_score_list)

    def test_reset_high_scores_list(self):
        self.test_service.reset_high_scores_list()
        for score in self.score_data._high_scores:
            self.assertEqual(score, (0, "N/A"))

    def test_get_team_names(self):
        self.assertEqual(self.test_service.get_team_names(), self.score_data._team_names)

    def test_get_selected_team(self):
        self.assertEqual(self.test_service.get_selected_team(), self.test_service._selected_team)

    def test_change_selected_team(self):
        team = choice(self.score_data.get_team_name_list())
        if team != self.test_service._selected_team:
            self.test_service.change_selected_team(team)
            self.assertEqual(self.test_service._selected_team, team)
        else:
            self.test_change_selected_team()

    def test_check_score(self):
        self.test_service._selected_team = "Rob Lowe"
        self.test_service._current_score = max(self.score_data._high_scores)[0]+1
        self.test_service.evaluate_score()
        is_true = self.is_value_in_list((self.test_service._current_score, "Rob Lowe"))
        self.assertEqual(is_true, True)

    def test_increase_score(self):
        score = self.test_service._current_score
        self.test_service.increase_score()
        self.assertEqual(self.test_service._current_score, score+1)

    def is_value_in_list(self, score):
        return score in self.score_data._high_scores
