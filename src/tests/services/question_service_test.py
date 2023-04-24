
import unittest
from services.question_service import QuestionService


class TestQuestionService(unittest.TestCase):

    def setUp(self):
        self.Qs = QuestionService()

    def test_questions_dictionary_not_empty(self):
        self.assertGreater(len(self.Qs._questions), 0)

    def test_key_list_and_number_of_keys_are_equal(self):
        self.assertEqual(len(self.Qs._questions), len(self.Qs._key_list))

    def test_key_list_is_shuffled(self):
        comparison = [x for x in range(1, len(self.Qs._key_list)+1)]
        self.assertNotEqual(self.Qs._key_list, comparison)

    def test_get_question(self):
        self.Qs.next_question()
        self.assertEqual(
            self.Qs.get_question(),
            self.Qs._questions[self.Qs._number]['Question']
        )

    def test_get_options(self):
        self.Qs.next_question()
        options1 = self.Qs.get_options()
        options2 = [
            self.Qs._questions[self.Qs._number]['A'],
            self.Qs._questions[self.Qs._number]['B'],
            self.Qs._questions[self.Qs._number]['C'],
            self.Qs._questions[self.Qs._number]['D'],
        ]
        options1.sort()
        options2.sort()
        self.assertEqual(options1, options2)

    def test_check_answer(self):
        self.Qs.next_question()
        answer = self.Qs._questions[self.Qs._number]['Answer']
        self.assertEqual(self.Qs.check_answer(answer), True)

    def test_question_changes(self):
        self.Qs.next_question()
        question1 = self.Qs._questions[self.Qs._number]['Question']
        self.Qs.next_question()
        question2 = self.Qs._questions[self.Qs._number]['Question']
        self.assertNotEqual(question1, question2)
