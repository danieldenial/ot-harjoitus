
import unittest
from services.questions_service import QuestionService
from pathlib import Path
import csv


class TestQuestions(unittest.TestCase):

    def setUp(self):
        self.Qs = QuestionService()
        self.file_path = Path(__file__).resolve(
        ).parent.parent.parent.parent / "files" / "questions.csv"

    def test_questions_dictionary_not_empty(self):
        self.assertGreater(len(self.Qs._questions), 0,
                           "The dictionary is empty")

    def test_key_list_and_number_of_keys_are_equal(self):
        self.assertEqual(len(self.Qs._questions), len(self.Qs._key_list))

    def test_compare_questions(self):
        with open(self.file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(row[0], self.Qs._questions[num]['Question'])
                num += 1

    def test_compare_option_A(self):
        with open(self.file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(row[1], self.Qs._questions[num]['A'])
                num += 1

    def test_compare_option_B(self):
        with open(self.file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(row[2], self.Qs._questions[num]['B'])
                num += 1

    def test_compare_option_C(self):
        with open(self.file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(row[3], self.Qs._questions[num]['C'])
                num += 1

    def test_compare_option_D(self):
        with open(self.file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(row[4], self.Qs._questions[num]['D'])
                num += 1

    def test_compare_answers(self):
        with open(self.file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            num = 1
            for row in reader:
                self.assertEqual(row[5], self.Qs._questions[num]['Answer'])
                num += 1

    def test_question_changes(self):
        self.Qs._next_question()
        question1 = self.Qs._questions[self.Qs._number]['Question']
        self.Qs._next_question()
        question2 = self.Qs._questions[self.Qs._number]['Question']
        self.assertNotEqual(question1, question2)
