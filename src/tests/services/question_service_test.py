
import unittest
from pathlib import Path
import os
import shutil
from services.question_service import QuestionService
from repositories.question_repository import QuestionRepository
from config import QUESTION_FILE_URL, DATA_FOLDER


class TestQuestionService(unittest.TestCase):

    def setUp(self):
        self.test_dir_path = Path(__file__).resolve(
        ).parents[3] / DATA_FOLDER

        os.makedirs(self.test_dir_path, exist_ok=True)

        source_file_path = Path(__file__).resolve(
        ).parents[3] / 'data' / 'questions.tsv'

        shutil.copy(source_file_path, self.test_dir_path / 'test_questions.tsv')

        question_repo = QuestionRepository(QUESTION_FILE_URL)
        self.test_service = QuestionService(question_repo)

    def tearDown(self):
        shutil.rmtree(self.test_dir_path)

    def test_questions_dictionary_not_empty(self):
        self.assertGreater(len(self.test_service._question_data), 0)

    def test_key_list_and_number_of_keys_are_equal(self):
        self.assertEqual(len(self.test_service._question_data),
                         len(self.test_service._index_list))

    def test_key_list_is_shuffled(self):
        comparison = [x for x in range(1, len(self.test_service._index_list)+1)]
        self.assertNotEqual(self.test_service._index_list, comparison)

    def test_get_question(self):
        self.test_service.set_next_question_index()
        self.assertEqual(
            self.test_service.get_question(),
            self.test_service._question_data.at[self.test_service._current_index, 'Question']
        )

    def test_get_options(self):
        self.test_service.set_next_question_index()
        options1 = self.test_service.get_options()
        options2 = [
            self.test_service._question_data.at[self.test_service._current_index, 'A'],
            self.test_service._question_data.at[self.test_service._current_index, 'B'],
            self.test_service._question_data.at[self.test_service._current_index, 'C'],
            self.test_service._question_data.at[self.test_service._current_index, 'D'],
        ]
        options1.sort()
        options2.sort()
        self.assertEqual(options1, options2)

    def test_check_answer(self):
        self.test_service.set_next_question_index()
        answer = self.test_service._question_data.at[self.test_service._current_index, 'Answer']
        self.assertEqual(self.test_service.evaluate_user_answer(answer), True)

    def test_question_changes(self):
        self.test_service.set_next_question_index()
        q1 = self.test_service._question_data.at[self.test_service._current_index, 'Question']
        self.test_service.set_next_question_index()
        q2 = self.test_service._question_data.at[self.test_service._current_index, 'Question']
        self.assertNotEqual(q1, q2)
