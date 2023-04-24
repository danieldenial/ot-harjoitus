
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from services.question_service import QuestionService
from services.score_service import ScoreServices


class GameplayView(BaseView):
    def __init__(self, root, main_menu_view, new_game_view):
        super().__init__(root)
        self._root = root
        self._main_menu_view = main_menu_view
        self._new_game_view = new_game_view
        self._q = QuestionService()
        self._score = ScoreServices()
        self._click = None
        self._initialize()

    def _initialize(self):
        self._q.next_question()
        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        q_text = self._q.get_question()
        self._options = self._q.get_options()

        self._question_label = tkinter.Label(
            self._frame, text=q_text,
            font=("Verdana", 25, "bold"), fg='white', bg='#013369'
        )

        self._A_label = tkinter.Label(
            self._frame, text=self._options[0],
            font=("Verdana", 25), fg='white', bg='#013369'
        )

        self._B_label = tkinter.Label(
            self._frame, text=self._options[1],
            font=("Verdana", 25), fg='white', bg='#013369'
        )

        self._C_label = tkinter.Label(
            self._frame, text=self._options[2],
            font=("Verdana", 25), fg='white', bg='#013369'
        )

        self._D_label = tkinter.Label(
            self._frame, text=self._options[3],
            font=("Verdana", 25), fg='white', bg='#013369'
        )

        self._score_label = tkinter.Label(
            self._frame, text=self._score.get_current_score(),
            font=("Verdana", 18), fg='white', bg='#013369'
        )

        self._question_label.grid(
            row=0, column=0, columnspan=2,
            padx=10, pady=10,
            sticky=tkinter.W+tkinter.E
        )

        self._A_label.grid(
            row=1, column=1,
            padx=(0, 10), pady=10,
            sticky=tkinter.W
        )

        self._B_label.grid(
            row=2, column=1,
            padx=(0, 10), pady=10,
            sticky=tkinter.W
        )

        self._C_label.grid(
            row=3, column=1,
            padx=(0, 10), pady=10,
            sticky=tkinter.W
        )

        self._D_label.grid(
            row=4, column=1,
            padx=(0, 10), pady=10,
            sticky=tkinter.W
        )

        self._score_label.grid(
            row=5, column=1,
            padx=10, pady=10,
            sticky=tkinter.E
        )

    def _initialize_buttons(self):
        style = ttk.Style()

        style.theme_use('default')

        style.configure(
            'custom.option.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black',
            height=10, width=3
        )

        style.configure(
            'custom.green.TButton', font=('Verdana', 20),
            background='#3B9B00', foreground='black',
            height=10, width=3
        )

        style.map(
            'custom.green.TButton',
            background=[('active', '#3B9B00')],
            foreground=[('active', 'black')],
        )

        style.configure(
            'custom.orange.TButton', font=('Verdana', 20),
            background='#F87B05', foreground='black',
            height=10, width=3
        )

        style.map(
            'custom.orange.TButton',
            background=[('active', '#F87B05')],
            foreground=[('active', 'black')]
        )

        self.A_button = ttk.Button(
            self._frame, text='A',
            style='custom.option.TButton',
            command=lambda: self._handle_player_answer('A', self._options[0])
        )

        self.B_button = ttk.Button(
            self._frame, text='B',
            style='custom.option.TButton',
            command=lambda: self._handle_player_answer('B', self._options[1])
        )

        self.C_button = ttk.Button(
            self._frame, text='C',
            style='custom.option.TButton',
            command=lambda: self._handle_player_answer('C', self._options[2])
        )

        self.D_button = ttk.Button(
            self._frame, text='D',
            style='custom.option.TButton',
            command=lambda: self._handle_player_answer('D', self._options[3])
        )

        self.A_button.grid(
            row=1, column=0,
            padx=(10, 0), pady=10,
            sticky=tkinter.W
        )

        self.B_button.grid(
            row=2, column=0,
            padx=(10, 0), pady=10,
            sticky=tkinter.W
        )

        self.C_button.grid(
            row=3, column=0,
            padx=(10, 0), pady=10,
            sticky=tkinter.W
        )

        self.D_button.grid(
            row=4, column=0,
            padx=(10, 0), pady=10,
            sticky=tkinter.W
        )

    def _handle_player_answer(self, click, answer):
        self._click = click

        self._disable_buttons()

        if self._q.check_answer(answer):
            self._change_button_green()
            self._score.increase_score()
            self._score_label.config(text=self._score.get_current_score())
        else:
            self._change_button_red()
            self._score.check_score()

    def _change_button_green(self):
        if self._click == "A":
            self.A_button.configure(style='custom.green.TButton')
        elif self._click == "B":
            self.B_button.configure(style='custom.green.TButton')
        elif self._click == "C":
            self.C_button.configure(style='custom.green.TButton')
        elif self._click == "D":
            self.D_button.configure(style='custom.green.TButton')
        self._add_right_answer_widgets()

    def _change_button_red(self):
        if self._click == "A":
            self.A_button.configure(style='custom.orange.TButton')
        elif self._click == "B":
            self.B_button.configure(style='custom.orange.TButton')
        elif self._click == "C":
            self.C_button.configure(style='custom.orange.TButton')
        elif self._click == "D":
            self.D_button.configure(style='custom.orange.TButton')
        self._add_wrong_answer_widgets()

    def _disable_buttons(self):
        self.A_button.configure(command=lambda: None)
        self.B_button.configure(command=lambda: None)
        self.C_button.configure(command=lambda: None)
        self.D_button.configure(command=lambda: None)

    def _add_right_answer_widgets(self):
        self.continue_label = tkinter.Label(
            self._frame, text='That is correct!',
            font=("Verdana", 20, 'bold'), fg='white', bg='#013369'
        )

        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.continue.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black',
        )

        self.continue_button = ttk.Button(
            self._frame, text="CONTINUE",
            style='custom.continue.TButton',
            command=lambda: self._update_view()
        )

        self.continue_label.grid(
            row=5, column=0,
            padx=10, pady=10
        )

        self.continue_button.grid(
            row=6, column=0,
            padx=10, pady=10
        )

    def _add_wrong_answer_widgets(self):
        self.game_over_label = tkinter.Label(
            self._frame, text='Oops, game over!',
            font=("Verdana", 20, 'bold'), fg='white', bg='#013369'
        )

        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.end.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black',
        )

        self.main_menu_button = ttk.Button(
            self._frame, text="MAIN MENU",
            style='custom.end.TButton',
            command=self._main_menu_view
        )

        self.new_game_button = ttk.Button(
            self._frame, text="NEW GAME",
            style='custom.end.TButton',
            command=self._new_game_view
        )

        self.game_over_label.grid(
            row=5, column=0,
            padx=10, pady=10
        )

        self.main_menu_button.grid(
            row=6, column=0,
            padx=10, pady=10
        )

        self.new_game_button.grid(
            row=7, column=0,
            padx=10, pady=10
        )

    def _update_view(self):
        self._question_label.destroy()
        self._A_label.destroy()
        self._B_label.destroy()
        self._C_label.destroy()
        self._D_label.destroy()
        self.A_button.destroy()
        self.B_button.destroy()
        self.C_button.destroy()
        self.D_button.destroy()
        self.continue_button.destroy()
        self.continue_label.destroy()
        self._score_label.destroy()
        self._initialize()
