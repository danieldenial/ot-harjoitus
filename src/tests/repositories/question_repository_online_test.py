
import unittest
from pathlib import Path
import os
import shutil
import pandas as pd
from datetime import datetime
from repositories.question_repository import QuestionRepository
from config import QUESTION_FILE_URL, DATA_FOLDER


class TestQuestionRepositoryOnlineFile(unittest.TestCase):

    def setUp(self):
        self.test_dir_path = Path(__file__).resolve(
        ).parents[3] / DATA_FOLDER

        os.makedirs(self.test_dir_path, exist_ok=True)

        self.test_repo = QuestionRepository(QUESTION_FILE_URL)

    def tearDown(self):
        shutil.rmtree(self.test_dir_path)

    def test_question_list_is_not_empty(self):
        self.assertGreater(len(self.test_repo._question_data), 0)

    def test_compare_questions(self):
        df_test = pd.read_csv(self.test_repo._file_storage_path, delimiter="\t")
        for index, row in df_test.iterrows():
            self.assertEqual(
                row['Question'],
                self.test_repo._question_data.at[index, 'Question']
            )

    def test_compare_option_A(self):
        df_test = pd.read_csv(self.test_repo._file_storage_path, delimiter="\t")
        for index, row in df_test.iterrows():
            self.assertEqual(
                row['A'],
                self.test_repo._question_data.at[index, 'A']
            )

    def test_compare_option_B(self):
        df_test = pd.read_csv(self.test_repo._file_storage_path, delimiter="\t")
        for index, row in df_test.iterrows():
            self.assertEqual(
                row['B'],
                self.test_repo._question_data.at[index, 'B']
            )

    def test_compare_option_C(self):
        df_test = pd.read_csv(self.test_repo._file_storage_path, delimiter="\t")
        for index, row in df_test.iterrows():
            self.assertEqual(
                row['C'],
                self.test_repo._question_data.at[index, 'C']
            )

    def test_compare_option_D(self):
        df_test = pd.read_csv(self.test_repo._file_storage_path, delimiter="\t")
        for index, row in df_test.iterrows():
            self.assertEqual(
                row['D'],
                self.test_repo._question_data.at[index, 'D']
            )

    def test_compare_answers(self):
        df_test = pd.read_csv(self.test_repo._file_storage_path, delimiter="\t")
        for index, row in df_test.iterrows():
            self.assertEqual(
                row['Answer'],
                self.test_repo._question_data.at[index, 'Answer']
            )

    def test_compare_details(self):
        df_test = pd.read_csv(self.test_repo._file_storage_path, delimiter="\t")
        for index, row in df_test.iterrows():
            self.assertEqual(
                row['Detail'],
                self.test_repo._question_data.at[index, 'Detail']
            )

    def test_is_answer_in_options(self):
        for i in range(len(self.test_repo._question_data)):
            is_true = False
            answer = self.test_repo._question_data.at[i, 'Answer']
            options = [
                self.test_repo._question_data.at[i, 'A'],
                self.test_repo._question_data.at[i, 'B'],
                self.test_repo._question_data.at[i, 'C'],
                self.test_repo._question_data.at[i, 'D']
            ]
            if self.is_value_in_list(answer, options) == True:
                is_true = True

            self.assertEqual(is_true, True)
    
    def test_is_online_file_timestamp_correct(self):
        if self.test_repo._is_url_reachable(self.test_repo._qfile_timestamp_url):
            date_test = self.test_repo._get_question_file_timestamp()
            format = "%d/%m/%Y %H:%M"
            result = bool(datetime.strptime(date_test, format))
            self.assertEqual(result, True)
        else:
            self.skipTest("Request exception")

    def is_value_in_list(self, answer, options):
        return answer in options
