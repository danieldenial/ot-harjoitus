
import tkinter
from tkinter import ttk, constants

class QuitView:
    def __init__(self, root, quit_game, main_menu_view):
        self._root = root
        self._frame = None
        self._quit_game = quit_game
        self._main_menu_view = main_menu_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tkinter.Frame(
            self._root, bg='#013369', 
            width=800, height=500
            )

        self._initialize_texts()
        self._initialize_buttons()
        self._initialize_grid()

    def _initialize_texts(self):
        quit_game_text_1 = tkinter.Label(
            self._frame, text="Quit game?", 
            font=("Arial", 30), fg='white', bg="#013369"
            )
        quit_game_text_2 = tkinter.Label(
            self._frame, text="Are you sure?",
            font=("Arial", 30), fg='white', bg="#013369"
            )
        
        quit_game_text_1.grid(row=1, column=1)
        quit_game_text_2.grid(row=3, column=1)

    def _initialize_buttons(self):
        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black'
            )

        quit_button = ttk.Button(
            self._frame, text="QUIT GAME",
            padding=10, style='custom.TButton',
            command=self._quit_game
            )
        
        back_button = ttk.Button(
            self._frame, text="BACK",
            padding=5, style='custom.TButton',
            command=self._main_menu_view
        )
        
        quit_button.grid(row=5, column=1)
        back_button.grid(row=7, column=1)

    def _initialize_grid(self):
        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(2, minsize=25)
        self._frame.grid_rowconfigure(4, minsize=50)
        self._frame.grid_rowconfigure(6, minsize=25)
        self._frame.grid_rowconfigure(8, minsize=200)

        self._frame.grid_columnconfigure(0,weight=1)
        self._frame.grid_columnconfigure(1,weight=1)
        self._frame.grid_columnconfigure(2,weight=1)