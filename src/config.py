
import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

QUESTION_FILE_ID=os.getenv("QUESTIONS_FILE_ID") or "1AEMvesLX_JNqHVdbM3hRqvEw4lxhhZWV2nAaA_2S6ik"
QUESTION_FILE_NAME=os.getenv("QUESTIONS_FILE_NAME") or "questions.tsv"
QUESTION_FILE_TIMESTAMP_ID=os.getenv("QUESTION_FILE_TIMESTAMP_ID") or "1339200912"
SCORE_FILE_NAME=os.getenv("HIGH_SCORES_FILENAME") or "high_scores.csv"
TEAM_FILE_NAME=os.getenv("TEAM_NAMES_FILENAME") or "team_names.csv"
BACKGROUND_COLOR=os.getenv("BACKGROUND_COLOR") or "#013369"
