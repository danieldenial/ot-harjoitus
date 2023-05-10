
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles
from services.score_service import ScoreService


class IntroView(BaseView):
    """Luokka, jonka avulla luodaan sovelluksen avausnäkymä.

    Args:
        BaseView: IntroView-luokan perimä pohjakehyksen näkymälle luova luokka

    Attributes:
        _score_service: Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
        _handle_show_main_menu = UI-luokan metodi päävalikon näkymän luomiseen
        _button_style: Näkymän painikkeiden tyyleistä vastaava luokkaolio
    """

    def __init__(self, root, score_service: ScoreService, main_menu_view):
        """Luokan konstruktori, joka alustaa sovelluksen avausnäkymän.

        Args:
            root: Tkinter-pääikkunan viite
            score_service: Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
            main_menu_view: UI-luokan metodi päävalikon näkymän luomiseen
        """

        super().__init__(root)
        self._score_service = score_service
        self._handle_show_main_menu = main_menu_view
        self._button_style = ButtonStyles(self.window_height)

        self._initialize()

    def _initialize(self):
        """Käynnistää sovelluksen avausnäkymän luomisen.
        """

        self._initialize_labels()
        self._initialize_buttons()
        self._initialize_team_selection_menu()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja määrittelee niiden sijainnit.
        """

        welcome_text = tkinter.Label(
            self._frame, text="Welcome to Grididon Genius!",
            font=('Arial', round((self.window_height*0.055))), fg='white', bg="#013369"
        )

        team_question_text = tkinter.Label(
            self._frame, text="Which team would you like to represent today?",
            font=('Arial', round((self.window_height*0.045))), fg='white', bg="#013369"
        )

        welcome_text.place(relx=0.5, rely=0.35, anchor='center')
        team_question_text.place(relx=0.5, rely=0.45, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat painikkeet ja määrittelee niiden sijainnit.
        """

        self._button_style.configure_basic_style()

        main_menu_button = ttk.Button(
            self._frame, text="SELECT",
            style='custom.basic.TButton',
            padding=round(self.window_height*0.015),
            command=self._handle_show_main_menu
        )

        main_menu_button.place(relx=0.5, rely=0.7, anchor='center')

    def _initialize_team_selection_menu(self):
        """Luo valikon, josta käyttäjä voi valita mieleisensä joukkueen.
        """

        team_options = self._score_service.get_team_names()

        selected_team = tkinter.StringVar(self._frame)
        selected_team.set(team_options[0])

        self._score_service.change_selected_team(team_options[0])

        selected_team.trace(
            "w", lambda *args: self._score_service.change_selected_team(selected_team.get()))

        dropdown_menu = tkinter.OptionMenu(
            self._frame, selected_team, *team_options)

        dropdown_menu.config(font=('Arial', round((self.window_height*0.03))))

        dropdown_menu.place(relx=0.5, rely=0.6, anchor='center')
