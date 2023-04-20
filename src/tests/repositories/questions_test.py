
import unittest
import os
import csv
from repositories.questions import Questions

class TestQuestions(unittest.TestCase):
    
    def setUp(self):
        self.Qs = Questions()

    def test_question_file_exists(self):
        path = os.path.isfile(self.Qs._file_path)
        self.assertEqual(path, True)

    def test_dictionary_is_not_empty(self):
        self.assertGreater(len(self.Qs._questions_dictionary), 0)

    def test_compare_questions(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(
                    row[0],
                    self.Qs._questions_dictionary[num]['Question']
                )
                num += 1

    def test_compare_option_A(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(
                    row[1],
                    self.Qs._questions_dictionary[num]['A']
                )
                num += 1

    def test_compare_option_B(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(
                    row[2],
                    self.Qs._questions_dictionary[num]['B']
                )
                num += 1

    def test_compare_option_C(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(
                    row[3],
                    self.Qs._questions_dictionary[num]['C']
                )
                num += 1

    def test_compare_option_D(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(
                    row[4],
                    self.Qs._questions_dictionary[num]['D']
                )
                num += 1

    def test_compare_answers(self):
        with open(self.Qs._file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(
                    row[5],
                    self.Qs._questions_dictionary[num]['Answer']
                )
                num += 1
