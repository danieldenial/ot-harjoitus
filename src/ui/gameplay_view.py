
import tkinter
from tkinter import ttk
from ui.base_view import BaseView


class GameplayView(BaseView):
    def __init__(self, root):
        super().__init__(root)
        self._question = "Is this an example question?"
        self._optionA = "A"
        self._optionB = "B"
        self._optionC = "C"
        self._optionD = "D"

        self._initialize()

    def _initialize(self):
        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_elements()

    def _initialize_labels(self):
        question_label = tkinter.Label(
            self._frame, text=self._question,
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
            self._frame, text=self._optionA,
            style='custom.TButton',
            command=lambda: self._handle_player_answer("A")
        )

        self.B_button = ttk.Button(
            self._frame, text=self._optionB,
            style='custom.TButton',
            command=lambda: self._handle_player_answer("B")
        )

        self.C_button = ttk.Button(
            self._frame, text=self._optionC,
            style='custom.TButton',
            command=lambda: self._handle_player_answer("C")
        )

        self.D_button = ttk.Button(
            self._frame, text=self._optionD,
            style='custom.TButton',
            command=lambda: self._handle_player_answer("D")
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

    def _handle_player_answer(self, click):
        self._disable_buttons()
        if click == "A":
            self._change_button_green("A")
        elif click == "B":
            self._change_button_red("B")
        elif click == "C":
            self._change_button_red("C")
        elif click == "D":
            self._change_button_red("D")

    def _change_button_green(self, answer):
        if answer == "A":
            self.A_button.configure(style='custom.green.TButton')
        elif answer == "B":
            self.B_button.configure(style='custom.green.TButton')
        elif answer == "C":
            self.C_button.configure(style='custom.green.TButton')
        elif answer == "D":
            self.D_button.configure(style='custom.green.TButton')
        self._add_button()
        

    def _change_button_red(self, answer):
        if answer == "A":
            self.A_button.configure(style='custom.orange.TButton')
        elif answer == "B":
            self.B_button.configure(style='custom.orange.TButton')
        elif answer == "C":
            self.C_button.configure(style='custom.orange.TButton')
        elif answer == "D":
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
