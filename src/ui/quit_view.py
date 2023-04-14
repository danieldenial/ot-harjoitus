
import tkinter
from tkinter import ttk
from ui.base_view import BaseView


class QuitView(BaseView):
    def __init__(self, root, quit_game, main_menu_view):
        super().__init__(root)
        self._quit_game = quit_game
        self._main_menu_view = main_menu_view

        self._initialize()

    def _initialize(self):
        self._initialize_texts()
        self._initialize_buttons()
        self._adjust_elements()

    def _initialize_texts(self):
        quit_game_text_1 = tkinter.Label(
            self._frame, text="Quit game?",
            font=("Arial", 40), fg='white', bg="#013369"
        )

        quit_game_text_1.grid(row=1, column=1)

    def _initialize_buttons(self):
        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black'
        )

        quit_button = ttk.Button(
            self._frame, text="YES",
            padding=10, style='custom.TButton',
            command=self._quit_game
        )

        back_button = ttk.Button(
            self._frame, text="NO",
            padding=10, style='custom.TButton',
            command=self._main_menu_view
        )

        quit_button.grid(row=3, column=1)
        back_button.grid(row=5, column=1)

    def _adjust_elements(self):
        self._frame.grid_rowconfigure(0, minsize=200)
        self._frame.grid_rowconfigure(2, minsize=25)
        self._frame.grid_rowconfigure(4, minsize=25)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
