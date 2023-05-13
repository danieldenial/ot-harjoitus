
import unittest
from pathlib import Path
import os
import shutil
import csv
from datetime import datetime
from repositories.question_repository import QuestionRepository
from config import QUESTION_FILE_URL, DATA_FOLDER


class TestQuestions(unittest.TestCase):

    def setUp(self):
        self.test_dir_path = Path(__file__).resolve(
        ).parents[3] / DATA_FOLDER

        os.makedirs(self.test_dir_path, exist_ok=True)
        self.test_repo = QuestionRepository(QUESTION_FILE_URL)

    def tearDown(self):
        shutil.rmtree(self.test_dir_path)

    def test_question_file_exists(self):
        path = os.path.isfile(self.test_repo._file_storage_path)
        self.assertEqual(path, True)

    def test_does_question_data_load_from_storage(self):
        with open(self.test_repo._file_storage_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            entries = sum(1 for row in reader)
        if entries > 0:
            entries -= 1
        self.test_repo._question_list = []
        self.test_repo._load_question_data_from_storage_file()
        self.assertEqual(len(self.test_repo._question_list), entries)

    def test_question_list_is_not_empty(self):
        self.assertGreater(len(self.test_repo._question_list), 0)

    def test_compare_questions(self):
        with open(self.test_repo._file_storage_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            index = 0
            next(reader)
            for row in reader:
                self.assertEqual(
                    row[0],
                    self.test_repo._question_list[index]['Question']
                )
                index += 1

    def test_compare_option_A(self):
        with open(self.test_repo._file_storage_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            index = 0
            next(reader)
            for row in reader:
                self.assertEqual(
                    row[1],
                    self.test_repo._question_list[index]['A']
                )
                index += 1

    def test_compare_option_B(self):
        with open(self.test_repo._file_storage_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            index = 0
            next(reader)
            for row in reader:
                self.assertEqual(
                    row[2],
                    self.test_repo._question_list[index]['B']
                )
                index += 1

    def test_compare_option_C(self):
        with open(self.test_repo._file_storage_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            next(reader)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[3],
                    self.test_repo._question_list[index]['C']
                )
                index += 1

    def test_compare_option_D(self):
        with open(self.test_repo._file_storage_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            next(reader)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[4],
                    self.test_repo._question_list[index]['D']
                )
                index += 1

    def test_compare_answers(self):
        with open(self.test_repo._file_storage_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            next(reader)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[5],
                    self.test_repo._question_list[index]['Answer']
                )
                index += 1

    def test_compare_details(self):
        with open(self.test_repo._file_storage_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            next(reader)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[6],
                    self.test_repo._question_list[index]['Detail']
                )
                index += 1

    def test_is_answer_in_options(self):
        for i in range(len(self.test_repo._question_list)):
            is_true = False
            answer = self.test_repo._question_list[i]['Answer']
            options = [
                self.test_repo._question_list[i]['A'],
                self.test_repo._question_list[i]['B'],
                self.test_repo._question_list[i]['C'],
                self.test_repo._question_list[i]['D']
            ]
            if self.is_value_in_list(answer, options) == True:
                is_true = True

            self.assertEqual(is_true, True)

    def test_is_date_format_correct(self):
        date_test = self.test_repo._get_formatted_last_modified_date(
            self.test_repo._file_storage_path
            )
        format = "%d/%m/%Y %H:%M"
        result = bool(datetime.strptime(date_test, format))
        self.assertEqual(result, True)

    def test_is_file_timestamp_correct(self):
        date_test = self.test_repo._get_question_file_timestamp()
        format = "%d/%m/%Y %H:%M"
        result = bool(datetime.strptime(date_test, format))
        self.assertEqual(result, True)

    def is_value_in_list(self, answer, options):
        return answer in options
