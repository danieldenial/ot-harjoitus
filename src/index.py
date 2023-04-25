
from tkinter import Tk
from ui.ui import UI
from repositories.question_repository import QuestionRepository
from repositories.high_score_repository import HighScoreRepository


def main():
    window = Tk()
    window.title("Gridiron Genius: An NFL Trivia Game")
    window.geometry('1000x600')
    window.configure(background='#013369')

    view = UI(window)
    QuestionRepository()
    HighScoreRepository()
    view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
