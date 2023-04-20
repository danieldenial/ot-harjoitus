
import unittest
import os
from repositories.high_scores import HighScores

class TestHighScores(unittest.TestCase):

    def setUp(self):
        self._HS = HighScores()

    def test_high_score_file_exists(self):
        path = os.path.isfile(self._HS._file_path)
        self.assertEqual(path, True)

    def test_high_score_is_not_None(self):
        self.assertIsNotNone(self._HS._high_score)

    def test_new_high_score_works(self):
        self._HS._set_new_high_score(20)
        self.assertEqual(self._HS._high_score, 20)

    def test_reset_high_score_works(self):
        self._HS._reset_high_score()
        self.assertEqual(self._HS._high_score, 0)
