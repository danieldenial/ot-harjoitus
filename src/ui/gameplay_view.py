
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from services.questions_service import QuestionService


class GameplayView(BaseView):
    def __init__(self, root):
        super().__init__(root)
        self._root = root
        self._initialize()

    def _initialize(self):
        self._next = QuestionService._next_question(self._root)
        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_elements()

    def _initialize_labels(self):
        question_label = tkinter.Label(
            self._frame, text=self._next['Question'],
            font=("Verdana", 25, "bold"), fg='white', bg="#013369"
        )

        question_label.grid(
            row=1, column=0, columnspan=3,
            padx=30, pady=20, sticky='w')

    def _initialize_buttons(self):
        style = ttk.Style()

        style.theme_use('default')

        style.configure(
            'custom.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black',
            height=10, width=10
        )

        style.configure(
            'custom.green.TButton', font=('Verdana', 20),
            background='#3B9B00', foreground='black',
            height=10, width=10
        )

        style.map(
            'custom.green.TButton',
            background=[('active', '#3B9B00')],
            foreground=[('active', 'black')]
        )

        style.configure(
            'custom.orange.TButton', font=('Verdana', 20),
            background='#F87B05', foreground='black',
            height=10, width=10
        )

        style.map(
            'custom.orange.TButton',
            background=[('active', '#F87B05')],
            foreground=[('active', 'black')]
        )

        self.A_button = ttk.Button(
            self._frame, text=self._next['A'],
            style='custom.TButton',
            command=lambda: self._handle_player_answer('A', self._next['A'])
        )

        self.B_button = ttk.Button(
            self._frame, text=self._next['B'],
            style='custom.TButton',
            command=lambda: self._handle_player_answer('B', self._next['B'])
        )

        self.C_button = ttk.Button(
            self._frame, text=self._next['C'],
            style='custom.TButton',
            command=lambda: self._handle_player_answer('C', self._next['C'])
        )

        self.D_button = ttk.Button(
            self._frame, text=self._next['D'],
            style='custom.TButton',
            command=lambda: self._handle_player_answer('D', self._next['D'])
        )

        self.A_button.grid(
            row=3, column=0,
            padx=30, pady=20, 
            sticky="w"
            )
        self.B_button.grid(
            row=4, column=0,
            padx=30, pady=20,
            sticky="w"
            )
        self.C_button.grid(
            row=5, column=0,
            padx=30, pady=20,
            sticky="w"
            )
        self.D_button.grid(
            row=6, column=0,
            padx=30, pady=20,
            sticky="w"
            )

    def _adjust_elements(self):
        self._frame.grid_rowconfigure(0, minsize=50)
        self._frame.grid_rowconfigure(2, minsize=50)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)

    def _handle_player_answer(self, click, answer):
        self._disable_buttons()
        if self._next['Answer'] == answer:
            self._change_button_green(click)
        else:
            self._change_button_red(click)


    def _change_button_green(self, click):
        if click == "A":
            self.A_button.configure(style='custom.green.TButton')
        elif click == "B":
            self.B_button.configure(style='custom.green.TButton')
        elif click == "C":
            self.C_button.configure(style='custom.green.TButton')
        elif click == "D":
            self.D_button.configure(style='custom.green.TButton')
        self._add_button()
        

    def _change_button_red(self, click):
        if click == "A":
            self.A_button.configure(style='custom.orange.TButton')
        elif click == "B":
            self.B_button.configure(style='custom.orange.TButton')
        elif click == "C":
            self.C_button.configure(style='custom.orange.TButton')
        elif click == "D":
            self.D_button.configure(style='custom.orange.TButton')
        self._add_button()

    def _disable_buttons(self):
        self.A_button.configure(command=lambda: None)
        self.B_button.configure(command=lambda: None)
        self.C_button.configure(command=lambda: None)
        self.D_button.configure(command=lambda: None)

    def _add_button(self):
        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.cont.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black',
        )

        self.continue_button = ttk.Button(
            self._frame, text="CONTINUE",
            style='custom.cont.TButton',
            command=lambda: None
        )

        self.continue_button.grid(row=8, column=1, sticky='w')
