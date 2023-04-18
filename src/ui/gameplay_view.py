
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from services.questions_service import QuestionService


class GameplayView(BaseView):
    def __init__(self, root):
        super().__init__(root)
        self._root = root
        self.q = QuestionService()
        self._click = None
        self._initialize()

    def _initialize(self):
        self.q._next_question()
        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        q_text = self.q._get_question()
        self._options = self.q._get_options()

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

        self._question_label.place(x=50, y=30)

        self._A_label.place(x=150, y=150)

        self._B_label.place(x=150, y=225)

        self._C_label.place(x=150, y=300)

        self._D_label.place(x=150, y=375)

    def _initialize_buttons(self):
        style = ttk.Style()

        style.theme_use('default')

        style.configure(
            'custom.TButton', font=('Verdana', 20),
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
            style='custom.TButton',
            command=lambda: self._handle_player_answer('A', self._options[0])
        )

        self.B_button = ttk.Button(
            self._frame, text='B',
            style='custom.TButton',
            command=lambda: self._handle_player_answer('B', self._options[1])
        )

        self.C_button = ttk.Button(
            self._frame, text='C',
            style='custom.TButton',
            command=lambda: self._handle_player_answer('C', self._options[2])
        )

        self.D_button = ttk.Button(
            self._frame, text='D',
            style='custom.TButton',
            command=lambda: self._handle_player_answer('D', self._options[3])
        )

        self.A_button.place(x=50, y=150)

        self.B_button.place(x=50, y=225)

        self.C_button.place(x=50, y=300)

        self.D_button.place(x=50, y=375)

    def _handle_player_answer(self, click, answer):
        self._click = click

        self._disable_buttons()

        if self.q._check_answer(answer):
            self._change_button_green()
        else:
            self._change_button_red()

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
            'custom.cont.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black',
        )

        self.continue_button = ttk.Button(
            self._frame, text="CONTINUE",
            style='custom.cont.TButton',
            command=lambda: self._update_view()
        )

        self.continue_label.place(x=75, y=450)
        self.continue_button.place(x=75, y=500)

    def _add_wrong_answer_widgets(self):
        pass

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
        self._initialize()
