
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles
from services.question_service import QuestionService
from services.score_service import ScoreService


class GameplayView(BaseView):
    """Pelinkulkua (eli kysymykset, vastausvaihtoehdot, jne.) kuvaava näkymä.

    Args:
        BaseView: Sovelluksen perusnäkymästä vastaava luokka, jonka GameplayView perii.

    Attributes:
        _root: Luokan juuri-ikkuna
        _main_menu_view: Metodi, jolla siirrytään päävalikon näkymään
        _new_game_view: Metodi, jolla siirrytään uutta peliä edeltävään näkymään
        _quit_game_view: Metodi, jolla siirrytään sovelluksen sulkemisen näkymään
        _question_service: Luokka-olio, joka tarjoaa kysymyksiin liittyviä palveluita
        _score_service: Luokka-olio, joka tarjoaa pelin pisteisiin liittyviä palveluita
        _button_styles: Luokka-olio, joka vastaa sovelluksen painikkeiden tyyleistä
    """

    def __init__(self, root, context, view_manager):
        """Luokan konstruktori, joka alustaa pelinkulkua kuvaavan näkymän.

        Args:
            root: Luokan juuri-ikkuna
            main_menu_view: Metodi, jolla siirrytään päävalikon näkymään
            new_game_view: Metodi, jolla siirrytään uutta peliä edeltävään näkymään
            quit_game_view: Metodi, jolla siirrytään sovelluksen sulkemisen näkymään
            question_data = QuestionRepository-luokan olio
            score_data = ScoreRepository-luokan olio
        """

        super().__init__(root)
        self._root = root
        self._view_manager = view_manager
        self._question_repo = context['question_repo']
        self._score_repo = context['score_repo']
        self._question_service = QuestionService(self._question_repo)
        self._score_service = ScoreService(self._score_repo)
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
        """Aloittaa pelinkulkua kuvaavan näkymän luomisen.
        """

        self._question_service.set_next_question_key()

        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        question_text = self._question_service.get_question()
        self.options = self._question_service.get_options()

        self.question_label = tkinter.Label(
            self._question_frame, text=question_text,
            font=("Verdana", 25, "bold"), fg='white', bg='#013369',
            wraplength=1000, anchor=tkinter.W, justify=tkinter.LEFT
        )

        option_labels = []

        for i in range(4):
            label = tkinter.Label(
                self._options_frame, text=self.options[i],
                font=("Verdana", 25), fg='white', bg='#013369'
            )
            option_labels.append(label)

        self.score_label = tkinter.Label(
            self._score_and_state_frame, text=self._score_service.get_current_score(),
            font=("Verdana", 16, "bold"), fg='white', bg='#013369'
        )

        self.question_label.grid(
            row=0, column=0, columnspan=2,
            padx=10, pady=10, sticky=tkinter.W+tkinter.E
        )

        for i, option in enumerate(option_labels):
            option.grid(
                row=i, column=1, padx=10,
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

        opt = ['A', 'B', 'C', 'D']
        self.buttons = []

        for i, letter in enumerate(opt):
            button = ttk.Button(
                self._options_frame, text=letter,
                style='custom.option.TButton',
                command=lambda letter=letter, i=i: self._handle_player_answer(
                    i, self.options[i])
            )

            self.buttons.append(button)

        for i, button in enumerate(self.buttons):
            button.grid(row=i, column=0, padx=20, pady=10, sticky=tkinter.W)

    def _handle_player_answer(self, click, answer):
        """Käsittelee pelaajan tekemän napin painalluksen, 
        jotta selviää menikö kysymys oikein.

        Args:
            click: Painettu nappi (A-D)
            answer: Valittu vastausvaihtoehto (tekstimuodossa)
        """

        self._disable_buttons()

        if self._question_service.check_answer(answer):
            self._change_button_green(click)
            self._score_service.increase_score()
            self.score_label.config(text=self._score_service.get_current_score())
            self._add_right_answer_widgets()
        else:
            self._change_button_red(click)
            self._score_service.check_score()
            self._score_service.store_high_scores()
            self._add_wrong_answer_widgets()

    def _change_button_green(self, click):
        """Muuttaa käyttäjän painaman napin vihreäksi
        vastauksen oltua oikein.

        Args:
            click: Käyttäjän painama nappi (A-D)
        """

        self._button_styles.configure_right_answer_style()

        self.buttons[click].configure(style='custom.green.TButton')


    def _change_button_red(self, click):
        """Muuttaa käyttäjän painaman napin punaiseksi
        vastauksen mentyä väärin.

        Args:
            click: Käyttäjän painama nappi
        """

        self._button_styles.configure_wrong_answer_style()

        self.buttons[click].configure(style='custom.red.TButton')

    def _disable_buttons(self):
        """Poistaa vastaamisen jälkeen napit käytöstä, 
        jotta pelaaja ei voi vastata kysymykseen uudestaan. 
        """

        for button in self.buttons:
            button.configure(command=lambda: None)

    def _add_right_answer_widgets(self):
        """Lisää oikean vastauksen jälkeen ikkunaan ilmaantuvat elementit. 
        """

        detail = self._question_service.get_detail_text()

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

        self.correct_label.grid(row=1, column=0, padx=5,
                                pady=10, sticky=tkinter.W)
        self.detail_label.grid(row=2, column=0, padx=10,
                               pady=10, sticky=tkinter.W)
        self.continue_button.grid(
            row=3, column=0, padx=10, pady=10, sticky=tkinter.W)


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
            command=lambda: self._destroy_subframes(self._view_manager.go_to_main_menu_view)
        )

        self.new_game_button = ttk.Button(
            self._score_and_state_frame, text="NEW GAME",
            style='custom.basic.TButton',
            command=lambda: self._destroy_subframes(self._view_manager.go_to_new_game_view)
        )

        self.quit_game_button = ttk.Button(
            self._score_and_state_frame, text="QUIT",
            style='custom.basic.TButton',
            command=lambda: self._destroy_subframes(self._view_manager.go_to_quit_view)
        )

        self.game_over_label.grid(
            row=1, column=0, padx=5, pady=10,
            sticky=tkinter.W, columnspan=2
        )

        self.new_game_button.grid(row=3, column=0, padx=10, pady=10)
        self.main_menu_button.grid(row=3, column=1, padx=10, pady=10)
        self.quit_game_button.grid(row=3, column=2, padx=10, pady=10)

        if self._score_service._current_score == self._score_service.provide_high_score():
            self.high_score_label = tkinter.Label(
            self._score_and_state_frame, text='But you set the new high score \o/',
            font=("Verdana", 20, 'bold'), fg='white', bg='#013369'
            )

            self.high_score_label.grid(
                row=2, column=0, padx=5, pady=10,
                sticky=tkinter.W, columnspan=2
            )

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

    def _destroy_subframes(self, go_to_view):
        """Poistaa näkymän alikehykset toisen luokan näkymään siirtymistä ennen.

        Args:
            move_to_view: Metodi, jolla siirrytään seuraavaan toivottuun näkymään.
        """

        self._question_frame.destroy()
        self._options_frame.destroy()
        self._score_and_state_frame.destroy()
        go_to_view()
