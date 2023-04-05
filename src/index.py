
from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.title("Gridiron Genius: An NFL Trivia Game")
    window.geometry("800x500")

    view = UI(window)
    view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
