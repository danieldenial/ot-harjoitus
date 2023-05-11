
import tkinter
from random import choice
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_styles import WidgetStyles
from ui.utilities.widget_creator import WidgetCreator
from services.score_service import ScoreService


class IntroView(BaseFrame):
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
        self._widget_styles = WidgetStyles(root)
        self._widget_creator = WidgetCreator(root)

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

        welcome_text = self._widget_creator.create_basic_label(
            self._frame, "Welcome to Grididon Genius!", 25
            )

        team_question_text = self._widget_creator.create_basic_label(
            self._frame, "Which team would you like to represent today?", 30
            )

        welcome_text.place(relx=0.5, rely=0.35, anchor='center')
        team_question_text.place(relx=0.5, rely=0.45, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat painikkeet ja määrittelee niiden sijainnit.
        """

        self._widget_styles.config_basic_button()

        main_menu_button = self._widget_creator.create_basic_button(
            self._frame, "SELECT", self._handle_show_main_menu
            )

        main_menu_button.place(relx=0.5, rely=0.7, anchor='center')

    def _initialize_team_selection_menu(self):
        """Luo valikon, josta käyttäjä voi valita mieleisensä joukkueen.
        """

        team_options = self._score_service.get_team_names()

        selected_team = tkinter.StringVar(self._frame)

        default = choice(team_options)
        
        selected_team.set(default)
        self._score_service.change_selected_team(default)

        selected_team.trace(
            "w", lambda *args: self._score_service.change_selected_team(selected_team.get()))

        dropdown_menu = self._widget_creator.create_dropdown_menu(
            self._frame, selected_team, *team_options
        )

        dropdown_menu.place(relx=0.5, rely=0.6, anchor='center')
