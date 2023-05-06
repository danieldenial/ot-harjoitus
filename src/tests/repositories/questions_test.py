
import unittest
import os
import csv
from repositories.question_repository import QuestionRepository


class TestQuestions(unittest.TestCase):

    def setUp(self):
        self.Qs = QuestionRepository()

    def test_question_file_exists(self):
        path = os.path.isfile(self.Qs._file_path)
        self.assertEqual(path, True)

    def test_question_list_is_not_empty(self):
        self.assertGreater(len(self.Qs.question_list), 0)

    def test_compare_questions(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[0],
                    self.Qs.question_list[index]['Question']
                )
                index += 1

    def test_compare_option_A(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[1],
                    self.Qs.question_list[index]['A']
                )
                index += 1

    def test_compare_option_B(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[2],
                    self.Qs.question_list[index]['B']
                )
                index += 1

    def test_compare_option_C(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[3],
                    self.Qs.question_list[index]['C']
                )
                index += 1

    def test_compare_option_D(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[4],
                    self.Qs.question_list[index]['D']
                )
                index += 1

    def test_compare_answers(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[5],
                    self.Qs.question_list[index]['Answer']
                )
                index += 1

    def test_compare_details(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            for row in reader:
                self.assertEqual(
                    row[6],
                    self.Qs.question_list[index]['Detail']
                )
                index += 1
