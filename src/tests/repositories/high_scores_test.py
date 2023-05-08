
import unittest
import os
from repositories.high_score_repository import HighScoreRepository


class TestHighScores(unittest.TestCase):

    def setUp(self):
        self._HS = HighScoreRepository()

    def test_high_score_file_exists(self):
        path = os.path.isfile(self._HS._score_file_path)
        self.assertEqual(path, True)

    def test_team_name_file_exists(self):
        path = os.path.isfile(self._HS._name_file_path)
        self.assertEqual(path, True)

    def test_high_score_is_not_None(self):
        self.assertIsNotNone(self._HS.get_high_score())
    
    def test_high_score_list_length_is_10(self):
        self.assertEqual(len(self._HS._high_scores), 10)

    def test_high_scores_are_not_negative(self):
        for x in self._HS._high_scores:
            self.assertGreaterEqual(x[0], 0)

    def test_team_name_list_is_not_empty(self):
        self.assertGreater(len(self._HS.get_team_name_list()), 0)

    def test_get_high_score_works(self):
        should_be_high_score = max(self._HS._high_scores)[0]
        self.assertEqual(self._HS.get_high_score(), should_be_high_score)

    def test_get_high_score_list_works(self):
        should_be_high_score_list = self._HS._high_scores
        self.assertEqual(self._HS.get_high_scores_list(), should_be_high_score_list)

    def test_add_score_to_list_works(self):
        minimum = min(self._HS._high_scores)[0]
        maximum = max(self._HS._high_scores)[0]
        add_to_list = None
        for i in range(minimum, maximum):
            if i not in self._HS._high_scores:
                add_to_list = i
                break
        self._HS.add_new_score_to_list(add_to_list, "Rob Lowe")
        is_in_list = self.score_is_in_list((add_to_list, "Rob Lowe"))
        self.assertEqual(is_in_list, True)
    
    def score_is_in_list(self, score):
        return score in self._HS._high_scores

    def test_load_high_score_exceptions_work(self):
        self._HS._score_file_path = 'NoFile.csv'
        self._HS._load_high_score_list()
        for score in self._HS._high_scores:
            self.assertEqual(score, (0, "N/A"))

    def test_load_team_name_exceptions_work(self):
        self._HS._name_file_path = 'NoFile.csv'
        self._HS._load_team_name_list()
        should_be_names = ["AFC", "NFC"]
        self.assertEqual(self._HS._team_names, should_be_names)

    def test_reset_high_score_works(self):
        self._HS.reset_high_scores()
        self.assertEqual(self._HS.get_high_score(), 0)
