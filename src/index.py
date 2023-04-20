
from tkinter import Tk
from ui.ui import UI
from repositories.questions import Questions
from repositories.high_scores import HighScores


def main():
    window = Tk()
    window.title("Gridiron Genius: An NFL Trivia Game")
    window.geometry('1000x600')
    window.configure(background='#013369')

    view = UI(window)
    Questions()
    HighScores()
    view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
