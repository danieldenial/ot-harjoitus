
import tkinter
from tkinter import ttk
from ui.base_view import BaseView


class NewGameView(BaseView):
    def __init__(self, root, main_menu_view, gameplay_view):
        super().__init__(root)
        self._main_menu_view = main_menu_view
        self._gameplay_view = gameplay_view

        self._initialize()

    def _initialize(self):
        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_elements()

    def _initialize_labels(self):
        new_game_text_1 = tkinter.Label(
            self._frame, text="Time for a new game!",
            font=("Arial", 35), fg='white', bg="#013369"
        )
        new_game_text_2 = tkinter.Label(
            self._frame, text="Are you the true Gridiron Genius?",
            font=("Arial", 30), fg='white', bg="#013369"
        )

        new_game_text_1.grid(row=1, column=1)
        new_game_text_2.grid(row=3, column=1)

    def _initialize_buttons(self):
        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black'
        )

        start_button = ttk.Button(
            self._frame, text="START GAME",
            padding=10, style='custom.TButton',
            command=self._gameplay_view
        )

        back_button = ttk.Button(
            self._frame, text="BACK",
            padding=5, style='custom.TButton',
            command=self._main_menu_view
        )

        start_button.grid(row=5, column=1)
        back_button.grid(row=7, column=1)

    def _adjust_elements(self):
        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(2, minsize=25)
        self._frame.grid_rowconfigure(4, minsize=50)
        self._frame.grid_rowconfigure(6, minsize=25)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
