
import tkinter
from tkinter import ttk, constants

class MainMenuView:
    def __init__(self, root, new_game_view, quit_view, rules_view):
        self._root = root
        self._frame = None
        self._show_new_game_view = new_game_view
        self._show_quit_view = quit_view
        self._show_rules_view = rules_view
        
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = tkinter.Frame(
            self._root, bg='#013369', 
            width=800, height=800
            )

        self._initialize_labels()
        self._initialize_buttons()
        self._initialize_grid()

    def _initialize_labels(self):
        h1_label = tkinter.Label(
            self._frame, text="Gridiron Genius", 
            font=("Verdana", 40, "bold"), bg="#013369"
            )
        h2_label = tkinter.Label(
            self._frame, text="An NFL Trivia Game",
            font=("Verdana", 30), bg="#013369"
            )

        h1_label.grid(row=1, column=1)
        h2_label.grid(row=2, column=1)

    def _initialize_buttons(self):
        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.TButton', font=('Verdana', 20), 
            padding=10, background='#d50a0a', foreground='black'
            )

        self.new_game_button = ttk.Button(
            self._frame, text="NEW GAME", 
            style='custom.TButton',
            command=self._show_new_game_view
            )
        self.rules_button = ttk.Button(
            self._frame, text="VIEW RULES", 
            style='custom.TButton',
            command=self._show_rules_view
            )
        self.quit_button = ttk.Button(
            self._frame, text="QUIT GAME", 
            style='custom.TButton',
            command=self._show_quit_view
            )

        self.new_game_button.grid(row=4, column=0)
        self.rules_button.grid(row=4, column=1)
        self.quit_button.grid(row=4, column=2)

    def _initialize_grid(self):
        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(3, minsize=50)
        self._frame.grid_rowconfigure(5, minsize=300)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)