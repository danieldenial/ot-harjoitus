
from tkinter import Tk
from ui.ui import UI
from repositories.question_repository import QuestionRepository
from repositories.high_score_repository import HighScoreRepository


def main():
    window = Tk()
    window.title("Gridiron Genius: An NFL Trivia Game")
    window.geometry('1280x720')
    window.configure(background='#013369')

    questions = QuestionRepository()
    scores = HighScoreRepository()

    view = UI(window, questions, scores)
    view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
