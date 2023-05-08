
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
    screen_width = round(window.winfo_screenwidth() * 0.7)
    screen_height = round(window.winfo_screenheight() * 0.7)
    window.geometry(f'{screen_width}x{screen_height}')
    window.eval('tk::PlaceWindow . center')
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
