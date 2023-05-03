
import unittest
from services.score_service import ScoreService
from repositories.high_score_repository import HighScoreRepository


class TestHighScoreService(unittest.TestCase):

    def setUp(self):
        score_data = HighScoreRepository()
        self.HS = ScoreService(score_data)

    def test_get_current_score(self):
        comparison = f"Score: {self.HS._current_score}"
        self.assertEqual(self.HS.get_current_score(), comparison)

    def test_get_high_score(self):
        self.assertEqual(self.HS.get_high_score(), self.HS.get_high_score())

    def test_increase_score(self):
        score = self.HS._current_score
        self.HS.increase_score()
        self.assertEqual(self.HS._current_score, score+1)
