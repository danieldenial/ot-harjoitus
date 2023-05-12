
import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DEFAULT_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1AEMvesLX_JNqHVdbM3hRqvEw4lxhhZWV2nAaA_2S6ik/export?format=tsv"
    )

DATA_FOLDER=os.getenv("DATA_FOLDER") or "data"
QUESTION_FILE_URL=os.getenv("QUESTION_FILE_URL") or DEFAULT_URL
QUESTION_FILE_NAME=os.getenv("QUESTION_FILE_NAME") or "questions.tsv"
QUESTION_FILE_TIMESTAMP_ID=os.getenv("QUESTION_FILE_TIMESTAMP_ID") or "1339200912"
SCORE_FILE_NAME=os.getenv("SCORE_FILE_NAME") or "high_scores.csv"
TEAM_FILE_NAME=os.getenv("TEAM_FILE_NAME") or "team_names.csv"
BACKGROUND_COLOR=os.getenv("BACKGROUND_COLOR") or "#013369"
