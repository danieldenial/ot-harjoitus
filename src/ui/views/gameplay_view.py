
import tkinter
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.button_styles import ButtonStyles
from services.question_service import QuestionService
from services.score_service import ScoreService


class GameplayView(BaseFrame):
    """Luokka, jonka avulla luodaan pelinkulkua kuvaavia näkymiä.

    Args:
        BaseView: GameplayView-luokan perimä pohjakehyksen näkymälle luova luokka

    Attributes:
        _question_service: Pelin kysymysten sovelluslogiikasta vastaava luokkaolio
        _score_service: Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
        _view_manager: Eri näkymien vaihtelusta vastaava luokkaolio
        _button_styles: Näkymän painikkeiden tyyleistä vastaava luokkaolio
    """

    def __init__(self, root,
                question_service: QuestionService,
                score_service: ScoreService,
                views):
        """Luokan konstruktori, joka alustaa pelinkulkua kuvaavan näkymän.

        Args:
            root: Tkinter-pääikkunan viite
            question_service: Kysymyksiin liittyvästä sovelluslogiikasta vastaava luokkaolio
            score_service: Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
            view_manager: Eri näkymien vaihtelusta vastaava luokkaolio
        """

        super().__init__(root)
        self._question_service = question_service
        self._score_service = score_service
        self._handle_show_main_menu = views['show_main_menu']
        self._handle_show_new_game_view = views['show_new_game_view']
        self._handle_show_quit_view = views['show_quit_view']
        self._widget_creator = WidgetCreator(root)
        self._button_styles = ButtonStyles(root)

        self._initialize()

    def _initialize(self):
        """Luo uuden pelin aloittavan näkymän.
        """

        self._set_up_new_game()
        self._initialize_subframes()
        self._initialize_question_view()

    def _set_up_new_game(self):
        """Alustaa uuden pelin pisteet ja kysymykset.

        Kutsuu sovellusluokkien metodeita, jotta pistemäärä on 
        pelin alussa aina 0 ja kaikki kysymykset mukana.
        """

        self._question_service.reset_index_list()
        self._score_service.reset_current_score()

    def _initialize_subframes(self):
        """Luo ja sijoittaa alikehyksiä näkymän selkeyttämistä varten.
        """

        self._question_frame = self._widget_creator.create_subframe(self._frame)
        self._options_frame = self._widget_creator.create_subframe(self._frame)
        self._score_and_state_frame = self._widget_creator.create_subframe(self._frame)

        self._question_frame.pack(padx=10, pady=10, anchor=tkinter.W)
        self._options_frame.pack(padx=10, pady=10, anchor=tkinter.W)
        self._score_and_state_frame.pack(padx=10, pady=10, anchor=tkinter.W)

    def _initialize_question_view(self):
        """Aloittaa kysymysten ja vastausvaihtoehtojen luomisen.

        Kutsuu ensin sovelluslogiikan luokan metodia seuraavan kysymyksen
        indeksin määrittelemiseksi ja kutsuu sen jälkeen oman luokan metodeita,
        jotka luovat kysymyksen ja vastausvaihtoehtojen näkymän.
        """

        self._question_service.set_next_question_index()

        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja määrittelee niiden sijainnit.

        Hakee ensin sovelluslogiikan luokan metodeilla tekstit kysymyksen
        ja vastausvaihtoehtojen luomista varten ja sijottaa ne sen jälkeen näkymään.
        """

        question_text = self._question_service.get_question()
        self.options = self._question_service.get_options()
        current_score_text = self._score_service.get_current_score_text()

        self.question_label = self._widget_creator.create_longer_label(
            self._question_frame, question_text, 0.035
            )

        option_labels = []

        for i in range(4):
            label = self._widget_creator.create_basic_label(
                self._options_frame, self.options[i], 0.035
                )
            
            option_labels.append(label)

        self.score_label = self._widget_creator.create_basic_label(
            self._score_and_state_frame, current_score_text, 0.025
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
        """Luo näkymään kuuluvat painikkeet ja määrittelee niiden sijainnit.
        """

        option_list = ['A', 'B', 'C', 'D']
        self.buttons = []

        self._button_styles.configure_option_style()

        for i, letter in enumerate(option_list):
            command = lambda letter=letter, i=i: self._handle_user_answer(
                i, self.options[i])

            button = self._widget_creator.create_option_button(
                self._options_frame, letter, command
                )

            self.buttons.append(button)

        for i, button in enumerate(self.buttons):
            button.grid(row=i, column=0, padx=20, pady=10, sticky=tkinter.W)

    def _handle_user_answer(self, clicked_button, user_answer):
        """Käsittelee pelaajan tekemän napin painalluksen.

        Kutsuu ensin painikkeet käytöstä poistavaa metodia ja selvittää
        sen jälkeen sovelluslogiikan luokkien metodeilla menikö vastaus oikein.

        Args:
            click: Painettu nappi ('A', 'B', 'C' tai 'D')
            answer: Valittu vastausvaihtoehto (tekstimuodossa)
        """

        self._disable_buttons()

        if self._question_service.evaluate_user_answer(user_answer):
            self._handle_right_answer(clicked_button)
        else:
            self._handle_wrong_answer(clicked_button)

    def _handle_right_answer(self, clicked_button):
        self._change_button_green(clicked_button)
        self._score_service.increase_score()  
        self.score_label.config(
            text=self._score_service.get_current_score_text())
        self._add_right_answer_widgets()

    def _handle_wrong_answer(self, clicked_button):
        self._change_button_red(clicked_button)
        new_high_score_boolean = (
            self._score_service.get_current_score() > self._score_service.get_high_score()
        )
        self._score_service.evaluate_score()
        self._add_wrong_answer_widgets(new_high_score_boolean)

    def _change_button_green(self, click):
        """Muuttaa käyttäjän painaman napin vihreäksi vastauksen oltua oikein.

        Args:
            click: Käyttäjän painama nappi ('A', 'B', 'C' tai 'D')
        """

        self._button_styles.configure_right_answer_style()

        self.buttons[click].configure(style='custom.green.TButton')

    def _change_button_red(self, click):
        """Muuttaa käyttäjän painaman napin punaiseksi vastauksen oltua väärin.

        Args:
            click: Käyttäjän painama nappi ('A', 'B', 'C' tai 'D')
        """

        self._button_styles.configure_wrong_answer_style()

        self.buttons[click].configure(style='custom.red.TButton')

    def _disable_buttons(self):
        """Poistaa vastaamisen jälkeen vaihtoehtojen painikkeet käytöstä.
        
        Koska käyttäjän halutaan vastaavan kysymykseen vain kerran,
        täytyy painikkeet poistaa käytöstä painalluksen jälkeen. 
        """

        for button in self.buttons:
            button.configure(command=lambda: None)

    def _add_right_answer_widgets(self):
        """Lisää oikean vastauksen jälkeen näkymään ilmaantuvat elementit. 
        """

        detail = self._question_service.get_detail_text()

        self.correct_label = self._widget_creator.create_basic_label(
            self._score_and_state_frame, 'That is correct!', 0.03
            )

        self.detail_label = self._widget_creator.create_longer_label(
            self._score_and_state_frame, detail, 0.0275
            )

        self.continue_button = self._widget_creator.create_basic_button(
            self._score_and_state_frame, "CONTINUE", self._update_view
            )

        self.correct_label.grid(row=1, column=0, padx=5,
                                pady=10, sticky=tkinter.W)
        self.detail_label.grid(row=2, column=0, padx=10,
                               pady=10, sticky=tkinter.W)
        self.continue_button.grid(row=3, column=0, padx=10,
                                  pady=10, sticky=tkinter.W)

    def _add_wrong_answer_widgets(self, new_high_score):
        """Lisää väärän vastauksen jälkeen näkymään ilmaantuvat elementit.

        Args:
            new_high_score: Totuusarvo, joka kertoo syntyikö uusi kärkitulos
        """

        self.game_over_label = self._widget_creator.create_basic_label(
            self._score_and_state_frame, 'Oops, game over!', 0.03
        )

        self.main_menu_button = self._widget_creator.create_basic_button(
            self._score_and_state_frame, "MAIN MENU",
            lambda: self._exit_view(self._handle_show_main_menu)
        )

        self.new_game_button = self._widget_creator.create_basic_button(
            self._score_and_state_frame, "NEW GAME",
            lambda: self._exit_view(self._handle_show_new_game_view)
        )

        self.quit_game_button = self._widget_creator.create_basic_button(
            self._score_and_state_frame, "QUIT",
            lambda: self._exit_view(self._handle_show_quit_view)
        )

        self.game_over_label.grid(
            row=1, column=0, padx=5, pady=10,
            sticky=tkinter.W, columnspan=2
        )

        self.new_game_button.grid(row=3, column=0, padx=10, pady=10)
        self.main_menu_button.grid(row=3, column=1, padx=10, pady=10)
        self.quit_game_button.grid(row=3, column=2, padx=10, pady=10)

        if new_high_score:
            self.high_score_label = self._widget_creator.create_basic_label(
                self._score_and_state_frame, 'But you set the new high score \o/', 0.03
                )

            self.high_score_label.grid(
                row=2, column=0, padx=5, pady=10,
                sticky=tkinter.W, columnspan=2
            )

    def _update_view(self):
        """Päivittää näkymän seuraavaa kysymystä varten.
        
        Poistaa kaikki aiempaan kysymykseen liittyneet elementit näkymästä ja 
        kutsuu kutsuu sen jälkeen seuraavan kysymyksen näkymän luovaa metodia.
        """

        for widget in self._question_frame.winfo_children():
            widget.destroy()

        for widget in self._options_frame.winfo_children():
            widget.destroy()

        for widget in self._score_and_state_frame.winfo_children():
            widget.destroy()

        self._initialize_question_view()

    def _destroy_subframes(self):
        """Poistaa tämän näkymän alikehykset ennen siirtymistä toisen luokan näkymään.
        """

        self._question_frame.destroy()
        self._options_frame.destroy()
        self._score_and_state_frame.destroy()

    def _exit_view(self, go_to_view):
        """Valmistelee siirtymisen toisen luokan näkymään.

        Kutsuu ensin sovelluslogiikan luokan metodia tulosten tallettamiseksi
        ja sen jälkeen oman luokan metodia, joka poistaa näkymän alikehykset.

        Args:
            go_to_view: ViewManager-luokan metodi, jolla siirrytään seuraavaan näkymään
        """

        self._score_service.store_high_scores()
        self._destroy_subframes()
        go_to_view()
