
import unittest
from services.score_service import ScoreServices


class TestHighScoreService(unittest.TestCase):

    def setUp(self):
        self.HS = ScoreServices()

    def test_get_current_score(self):
        comparison = f"Score: {self.HS._current_score}"
        self.assertEqual(self.HS._get_current_score(), comparison)

    def test_get_high_score(self):
        self.assertEqual(self.HS._get_high_score(), self.HS._high_score)

    def test_increase_score(self):
        score = self.HS._current_score
        self.HS._increase_score()
        self.assertEqual(self.HS._current_score, score+1)
