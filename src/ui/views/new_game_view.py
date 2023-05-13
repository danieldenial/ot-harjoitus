
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.widget_styles import WidgetStyles
from services.score_service import ScoreService


class NewGameView(BaseFrame):
    """Uutta peliä edeltävästä valikosta vastaava näkymä.

    Args:
        BaseView: 
            Luokka, joka luo kaikille näkymille pohjakehyksen.
    """

    def __init__(self, root, score_service: ScoreService, views):
        """Luokan konstruktori. Luo uuden peliä edeltävän valikon näkymän.

        Args:
            root:
                Tkinter-pääikkuna, jonka sisään näkymä luodaan
            score_service:
                Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
            views:
                Sanakirja kutsuttavia arvoja, joilla siirrytään eri näkymiin
        """

        super().__init__(root)
        self._score_service = score_service
        self._handle_show_gameplay_view = views['show_gameplay_view']
        self._handle_show_main_menu = views['show_main_menu']
        self._widget_creator = WidgetCreator(root)
        self._widget_styles = WidgetStyles(root)

        self._initialize()

    def _initialize(self):
        """Aloittaa uutta peliä edeltävän näkymän luomisen kutsumalla
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()
        self._initialize_team_selection_menu()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        font_scaler = 30
        
        new_game_text_1 = self._widget_creator.create_basic_label(
            self._frame,
            "It's game time! Which team will you represent?",
            font_scaler
            )

        new_game_text_2 = self._widget_creator.create_basic_label(
            self._frame,
            f"The current score to beat is {self._score_service.get_high_score()}.",
            font_scaler
            )
        
        new_game_text_1.place(relx=0.5, rely=0.3, anchor='center')
        new_game_text_2.place(relx=0.5, rely=0.5, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._widget_styles.config_basic_button()

        start_button = self._widget_creator.create_basic_button(
            self._frame, "START", self._handle_show_gameplay_view
            )

        back_button = self._widget_creator.create_basic_button(
            self._frame, "BACK", self._handle_show_main_menu
            )

        start_button.place(relx=0.5, rely=0.6, anchor='center')
        back_button.place(relx=0.5, rely=0.7, anchor='center')

    def _initialize_team_selection_menu(self):
        """Luo valikon, josta käyttäjä voi valita mieleisensä joukkueen.
        """

        selected_team = self._score_service.get_selected_team()

        dropdown_menu = self._widget_creator.create_team_selection_menu(
            self._frame, selected_team, self._score_service
        )

        font_size = self._widget_creator.set_relative_size(50)

        dropdown_menu.config(font=('Arial', font_size))

        dropdown_menu.place(relx=0.5, rely=0.4, anchor='center')
