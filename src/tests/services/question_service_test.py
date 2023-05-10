
import unittest
from services.question_service import QuestionService
from repositories.question_repository import QuestionRepository


class TestQuestionService(unittest.TestCase):

    def setUp(self):
        question_data = QuestionRepository()
        self.Qs = QuestionService(question_data)

    def test_questions_dictionary_not_empty(self):
        self.assertGreater(len(self.Qs._question_list), 0)

    def test_key_list_and_number_of_keys_are_equal(self):
        self.assertEqual(len(self.Qs._question_list),
                         len(self.Qs._index_list))

    def test_key_list_is_shuffled(self):
        comparison = [x for x in range(1, len(self.Qs._index_list)+1)]
        self.assertNotEqual(self.Qs._index_list, comparison)

    def test_get_question(self):
        self.Qs.set_next_question_index()
        self.assertEqual(
            self.Qs.get_question(),
            self.Qs._question_list[self.Qs._index]['Question']
        )

    def test_get_options(self):
        self.Qs.set_next_question_index()
        options1 = self.Qs.get_options()
        options2 = [
            self.Qs._question_list[self.Qs._index]['A'],
            self.Qs._question_list[self.Qs._index]['B'],
            self.Qs._question_list[self.Qs._index]['C'],
            self.Qs._question_list[self.Qs._index]['D'],
        ]
        options1.sort()
        options2.sort()
        self.assertEqual(options1, options2)

    def test_check_answer(self):
        self.Qs.set_next_question_index()
        answer = self.Qs._question_list[self.Qs._index]['Answer']
        self.assertEqual(self.Qs.evaluate_user_answer(answer), True)

    def test_question_changes(self):
        self.Qs.set_next_question_index()
        question1 = self.Qs._question_list[self.Qs._index]['Question']
        self.Qs.set_next_question_index()
        question2 = self.Qs._question_list[self.Qs._index]['Question']
        self.assertNotEqual(question1, question2)
