
from tkinter import Tk
from ui.ui import UI
from services.question_service import QuestionService
from services.score_service import ScoreService
from repositories.question_repository import QuestionRepository
from repositories.high_score_repository import HighScoreRepository

BACKGROUND_COLOR = '#013369'

def main():
    window = Tk()
    window.title("Gridiron Genius: An NFL Trivia Game")
    window.geometry('1080x720')
    window.configure(background=BACKGROUND_COLOR)

    question_repo = QuestionRepository()
    score_repo = HighScoreRepository()

    question_service = QuestionService(question_repo)
    score_service = ScoreService(score_repo)

    context = {
        'question_service': question_service,
        'score_service': score_service
        }

    view = UI(window, context)
    view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
