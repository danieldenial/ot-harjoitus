
from datetime import datetime
from pathlib import Path
import os
import requests
import pandas as pd
from config import DATA_FOLDER, QUESTION_FILE_NAME, QUESTION_FILE_TIMESTAMP_ID


class QuestionRepository:
    """Pelin kysymysaineiston käsittelystä vastaava luokka.
    """

    def __init__(self, question_file_url):
        """Luokan konstruktori. Luo pohjan kysymysaineiston käsittelylle.

        Args:
            question_file_id: Verkko-osoite (merkkijonona), jossa kysymysaineisto on.
        """

        self._question_data = pd.DataFrame()

        self._file_storage_path = Path(__file__).resolve(
        ).parents[2] / DATA_FOLDER / QUESTION_FILE_NAME

        self._question_file_url = question_file_url

        self._qfile_timestamp_url = (
            self._question_file_url +
            f'&gid={QUESTION_FILE_TIMESTAMP_ID}'
            )

        self._initialize()

    def _initialize(self):
        if self._is_question_file_stored():
            if self._is_url_reachable(self._question_file_url):
                self._check_for_updates(self._file_storage_path)
            else:
                self._load_question_data_from_storage_file()
        else:
            if self._is_url_reachable(self._question_file_url):
                self._import_question_data()
            else:
                pass

    def _is_question_file_stored(self):
        return os.path.exists(self._file_storage_path)

    def _is_url_reachable(self, url):
        try:
            response = requests.get(url, timeout=5.0, stream=True)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def _check_for_updates(self, file_path):
        storage_file_modified = self._get_formatted_last_modified_date(file_path)

        online_file_last_updated = self._get_question_file_timestamp()

        if online_file_last_updated > storage_file_modified:
            self._import_question_data()
        else:
            self._load_question_data_from_storage_file()

    def _get_formatted_last_modified_date(self, file_path):
        storage_file_created = os.path.getmtime(file_path)
        creation_datetime = datetime.fromtimestamp(storage_file_created)
        return creation_datetime.strftime("%d/%m/%Y %H:%M")

    def _get_question_file_timestamp(self):
        timestamp_df = pd.read_csv(self._qfile_timestamp_url, header=None, nrows=1)
        return timestamp_df.iloc[0, 0]

    def _import_question_data(self):
        self._question_data = pd.read_csv(self._question_file_url, delimiter='\t')

        self._create_local_question_file(self._question_data)

    def _create_local_question_file(self, dataframe: pd.DataFrame):
        dataframe.to_csv(self._file_storage_path, sep="\t", index=False)

    def _load_question_data_from_storage_file(self):
        self._question_data = pd.read_csv(self._file_storage_path, delimiter="\t")

    def get_question_list(self):
        """Palauttaa sovellukseen ladatun pelin kysymysaineiston.

        Returns:
            Palauttaa pelin kysymysaineiston datataulukon (DataFrame) muodossa.
        """
        return self._question_data
