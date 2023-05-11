
from datetime import datetime
from pathlib import Path
import os
import pandas as pd
from config import QUESTION_FILE_NAME, QUESTION_FILE_TIMESTAMP_ID


class QuestionRepository:
    """Luokka, joka vastaa kysymysdatan talletuksesta.

    Attributes:
        question_list: Kysymysdataa varten luotava lista
        _file_path: Kysymysdatan sisältävän tiedoston polku
    """

    def __init__(self, question_file_id):
        self.question_list = []
        self._file_storage_path = Path(__file__).resolve(
        ).parents[2] / "data" / QUESTION_FILE_NAME
        self._question_file_url = (
            'https://docs.google.com/spreadsheets/d/' +
            f'{question_file_id}/export?format=tsv'
            )
        self._question_file_timestamp = (
            'https://docs.google.com/spreadsheets/d/' +
            f'{question_file_id}/export?format=tsv' +
            f'&gid={QUESTION_FILE_TIMESTAMP_ID}'
            )

        self._initialize()

    def _initialize(self):
        self._is_question_file_stored()

    def _is_question_file_stored(self):
        if os.path.exists(self._file_storage_path):
            self._check_for_updates(self._file_storage_path)
        else:
            self._import_question_data()

    def _check_for_updates(self, file_path):
        storage_file_modified = self._file_creation_time_format(file_path)

        timestamp_df = pd.read_csv(self._question_file_timestamp, header=None, nrows=1)
        online_file_updated = timestamp_df.iloc[0, 0]

        if online_file_updated > storage_file_modified:
            self._import_question_data()
        else:
            self._load_question_data_from_storage()

    def _file_creation_time_format(self, file_path):
        storage_file_created = os.path.getmtime(file_path)
        creation_datetime = datetime.fromtimestamp(storage_file_created)
        return creation_datetime.strftime("%d/%m/%Y %H:%M")

    def _import_question_data(self):
        question_data = pd.read_csv(self._question_file_url, delimiter='\t')

        self.question_list = question_data.to_dict('records')

        self._create_local_question_file(question_data)

    def _create_local_question_file(self, dataframe):
        dataframe.to_csv(self._file_storage_path, sep="\t", index=False)

    def _load_question_data_from_storage(self):
        dataframe = pd.read_csv(self._file_storage_path, delimiter="\t")
        self.question_list = dataframe.to_dict("records")

    def get_question_list(self):
        return self.question_list
