
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles
from services.question_service import QuestionService
from services.score_service import ScoreService


class GameplayView(BaseView):
    """Pelinkulkua (eli kysymykset, vastausvaihtoehdot, jne.) kuvaava näkymä.

    Args:
        BaseView: Sovelluksen perusnäkymästä vastaava luokka
    """

    def __init__(self, root, main_menu, new_game, quit_game, question_data, score_data):
        """Luokan konstruktori, joka alustaa pelinkulkua kuvaavan näkymän.

        Args:
            root: Luokan juuri-ikkuna
            main_menu_view: Metodi, jolla siirrytään päävalikon näkymään
            new_game_view: Metodi, jolla siirrytään uutta peliä edeltävään näkymään
            quit_game_view: Metodi, jolla siirrytään sovelluksen sulkemisen näkymään
        """

        super().__init__(root)
        self._root = root
        self._main_menu_view = main_menu
        self._new_game_view = new_game
        self._quit_game_view = quit_game
        self._q = QuestionService(question_data)
        self._score = ScoreService(score_data)
        self._button_styles = ButtonStyles()

        self._initialize_subframes()

    def _initialize_subframes(self):
        """Luo näkymän selkeyttämistä varten tarvittavia alikehyksiä.
        """

        self._question_frame = tkinter.Frame(self._root, bg='#013369')
        self._question_frame.pack(padx=10, pady=10, anchor=tkinter.W)

        self._options_frame = tkinter.Frame(self._root, bg='#013369')
        self._options_frame.pack(padx=10, pady=10, anchor=tkinter.W)

        self._score_and_state_frame = tkinter.Frame(self._root, bg='#013369')
        self._score_and_state_frame.pack(padx=10, pady=10, anchor=tkinter.W)

        self._initialize()

    def _initialize(self):
        """Aloittaa pelinkulkua kuvaavan näkymän luomisen kutsumalla
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._q.set_next_question_key()

        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        q_text = self._q.get_question()
        self.options = self._q.get_options()

        self.question_label = tkinter.Label(
            self._question_frame, text=q_text,
            font=("Verdana", 25, "bold"), fg='white', bg='#013369',
            wraplength=1000, anchor=tkinter.W, justify=tkinter.LEFT
        )

        self.label_a = tkinter.Label(
            self._options_frame, text=self.options[0],
            font=("Verdana", 25), fg='white', bg='#013369'
        )

        self.label_b = tkinter.Label(
            self._options_frame, text=self.options[1],
            font=("Verdana", 25), fg='white', bg='#013369'
        )

        self.label_c = tkinter.Label(
            self._options_frame, text=self.options[2],
            font=("Verdana", 25), fg='white', bg='#013369'
        )

        self.label_d = tkinter.Label(
            self._options_frame, text=self.options[3],
            font=("Verdana", 25), fg='white', bg='#013369'
        )

        self.score_label = tkinter.Label(
            self._score_and_state_frame, text=self._score.get_current_score(),
            font=("Verdana", 16, "bold"), fg='white', bg='#013369'
        )

        self.question_label.grid(
            row=0, column=0, columnspan=2,
            padx=10, pady=10,sticky=tkinter.W+tkinter.E
        )

        self.label_a.grid(
            row=0, column=1, padx=10,
            pady=10, sticky=tkinter.W
        )

        self.label_b.grid(
            row=1, column=1, padx=10,
            pady=10, sticky=tkinter.W
        )

        self.label_c.grid(
            row=2, column=1, padx=10,
            pady=10, sticky=tkinter.W
        )

        self.label_d.grid(
            row=3, column=1, padx=10,
            pady=10, sticky=tkinter.W
        )

        self.score_label.grid(
            row=0, column=0, padx=10,
            pady=(0, 10), sticky=tkinter.W
        )

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._button_styles.configure_option_style()

        self.button_a = ttk.Button(
            self._options_frame, text='A',
            style='custom.option.TButton',
            command=lambda: self._handle_player_answer('A', self.options[0])
        )

        self.button_b = ttk.Button(
            self._options_frame, text='B',
            style='custom.option.TButton',
            command=lambda: self._handle_player_answer('B', self.options[1])
        )

        self.button_c = ttk.Button(
            self._options_frame, text='C',
            style='custom.option.TButton',
            command=lambda: self._handle_player_answer('C', self.options[2])
        )

        self.button_d = ttk.Button(
            self._options_frame, text='D',
            style='custom.option.TButton',
            command=lambda: self._handle_player_answer('D', self.options[3])
        )

        self.button_a.grid(row=0, column=0, padx=(20, 10), pady=10, sticky=tkinter.W)
        self.button_b.grid(row=1, column=0, padx=20, pady=10, sticky=tkinter.W)
        self.button_c.grid(row=2, column=0, padx=20, pady=10, sticky=tkinter.W)
        self.button_d.grid(row=3, column=0, padx=20, pady=10, sticky=tkinter.W)

    def _handle_player_answer(self, click, answer):
        """Käsittelee pelaajan tekemän napin painalluksen, 
        jotta selviää menikö kysymys oikein.

        Args:
            click: Painettu nappi (A-D)
            answer: Valittu vastausvaihtoehto (tekstimuodossa)
        """

        self._disable_buttons()

        if self._q.check_answer(answer):
            self._change_button_green(click)
            self._score.increase_score()
            self.score_label.config(text=self._score.get_current_score())
        else:
            self._change_button_red(click)
            self._score.check_score()

    def _change_button_green(self, click):
        """Muuttaa käyttäjän painaman napin vihreäksi
        vastauksen oltua oikein.

        Args:
            click: Käyttäjän painama nappi (A-D)
        """

        self._button_styles.configure_right_answer_style()

        if click == "A":
            self.button_a.configure(style='custom.green.TButton')
        elif click == "B":
            self.button_b.configure(style='custom.green.TButton')
        elif click == "C":
            self.button_c.configure(style='custom.green.TButton')
        elif click == "D":
            self.button_d.configure(style='custom.green.TButton')

        self._add_right_answer_widgets()

    def _change_button_red(self, click):
        """Muuttaa käyttäjän painaman napin punaiseksi
        vastauksen mentyä väärin.

        Args:
            click: Käyttäjän painama nappi
        """

        self._button_styles.configure_wrong_answer_style()

        if click == "A":
            self.button_a.configure(style='custom.red.TButton')
        elif click == "B":
            self.button_b.configure(style='custom.red.TButton')
        elif click == "C":
            self.button_c.configure(style='custom.red.TButton')
        elif click == "D":
            self.button_d.configure(style='custom.red.TButton')

        self._add_wrong_answer_widgets()

    def _disable_buttons(self):
        """Poistaa vastaamisen jälkeen napit käytöstä, 
        jotta pelaaja ei voi vastata kysymykseen uudestaan. 
        """

        self.button_a.configure(command=lambda: None)
        self.button_b.configure(command=lambda: None)
        self.button_c.configure(command=lambda: None)
        self.button_d.configure(command=lambda: None)

    def _add_right_answer_widgets(self):
        """Lisää oikean vastauksen jälkeen ikkunaan ilmaantuvat elementit. 
        """

        detail = self._q.get_detail_text()

        self.correct_label = tkinter.Label(
            self._score_and_state_frame, text='That is correct!',
            font=("Verdana", 20, 'bold'), fg='white', bg='#013369'
        )

        self.detail_label = tkinter.Label(
            self._score_and_state_frame, text=detail,
            font=("Verdana", 18), fg='white', bg='#013369',
            wraplength=1000, anchor=tkinter.W, justify=tkinter.LEFT
        )

        self.continue_button = ttk.Button(
            self._score_and_state_frame, text="CONTINUE",
            style='custom.basic.TButton',
            command=lambda: self._update_view()
        )

        self.correct_label.grid(row=1, column=0, padx=5, pady=10, sticky=tkinter.W)

        self.detail_label.grid(row=2, column=0, padx=10, pady=10, sticky=tkinter.W)

        self.continue_button.grid(row=3, column=0, padx=10, pady=10, sticky=tkinter.W)

    def _add_wrong_answer_widgets(self):
        """Lisää väärän vastauksen jälkeen ikkunaan ilmaantuvat elementit.
        """

        self.game_over_label = tkinter.Label(
            self._score_and_state_frame, text='Oops, game over!',
            font=("Verdana", 20, 'bold'), fg='white', bg='#013369'
        )

        self.main_menu_button = ttk.Button(
            self._score_and_state_frame, text="MAIN MENU",
            style='custom.basic.TButton',
            command=lambda: self._destroy_subframes(self._main_menu_view)
        )

        self.new_game_button = ttk.Button(
            self._score_and_state_frame, text="NEW GAME",
            style='custom.basic.TButton',
            command=lambda: self._destroy_subframes(self._new_game_view)
        )

        self.quit_game_button = ttk.Button(
            self._score_and_state_frame, text="QUIT",
            style='custom.basic.TButton',
            command=lambda: self._destroy_subframes(self._quit_game_view)
        )

        self.game_over_label.grid(
            row=1, column=0, padx=5, pady=10, 
            sticky=tkinter.W, columnspan=2
        )

        self.new_game_button.grid(row=2, column=0, padx=10, pady=10)
        self.main_menu_button.grid(row=2, column=1,padx=10, pady=10)
        self.quit_game_button.grid(row=2, column=2, padx=10, pady=10)

    def _update_view(self):
        """Päivittää näkymän seuraavaa kysymystä varten 
        poistamalla aiempaan kysymykseen liittyneet elementit.
        """

        for widget in self._question_frame.winfo_children():
            widget.destroy()

        for widget in self._options_frame.winfo_children():
            widget.destroy()

        for widget in self._score_and_state_frame.winfo_children():
            widget.destroy()

        self._initialize()

    def _destroy_subframes(self, move_to_view):
        """Poistaa näkymän alikehykset toisen luokan näkymään siirtymistä ennen.

        Args:
            move_to_view: Metodi, jolla siirrytään seuraavaan toivottuun näkymään.
        """

        self._question_frame.destroy()
        self._options_frame.destroy()
        self._score_and_state_frame.destroy()
        move_to_view()
