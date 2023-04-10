
from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Gridiron Genius: An NFL Trivia Game")
    window.minsize(1000, 400)
    window.resizable(False, False)

    view = UI(window)
    view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
