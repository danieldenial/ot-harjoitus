
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.button_styles import ButtonStyles
from services.score_service import ScoreService


class NewGameView(BaseFrame):
    """Luokka, jonka avulla luodaan uutta peliä edeltävä näkymä.

    Args:
        BaseView: NewGameView-luokan perimä pohjakehyksen näkymälle luova luokka

    Attributes:
        _score_service: Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
        _handle_show_gameplay_view: UI-luokan metodi pelinkulun näkymän luomiseen
        _handle_show_main_menu: UI-luokan metodi päävalikon näkymän luomiseen
        _button_style: Näkymän painikkeiden tyyleistä vastaava luokkaolio
    """

    def __init__(self, root, score_service: ScoreService, views):
        """Luokan konstruktori, joka alustaa uutta peliä edeltävän näkymän.

        Args:
            root: Tkinter-pääikkunan viite
            main_menu_view: Metodi, jolla siirrytään päävalikon näkymään
            gameplay_view: Metodi, jolla siirrytään pelinkulkua kuvaavaan näkymään
        """

        super().__init__(root)
        self._score_service = score_service
        self._handle_show_gameplay_view = views['show_gameplay_view']
        self._handle_show_main_menu = views['show_main_menu']
        self._widget_creator = WidgetCreator(root)
        self._button_style = ButtonStyles(root)

        self._initialize()

    def _initialize(self):
        """Aloittaa uutta peliä edeltävän näkymän luomisen kutsumalla
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        new_game_text_1 = self._widget_creator.create_basic_label(
            self._frame, "Time for a new game!", 0.05
            )
        
        new_game_text_2 = self._widget_creator.create_basic_label(
            self._frame,
            f"The current high score is {self._score_service.get_high_score()}.",
            0.05
            )
        
        new_game_text_3 = self._widget_creator.create_basic_label(
            self._frame, "Can you beat it?", 0.05
            )
        
        new_game_text_1.place(relx=0.5, rely=0.2, anchor='center')
        new_game_text_2.place(relx=0.5, rely=0.3, anchor='center')
        new_game_text_3.place(relx=0.5, rely=0.4, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._button_style.configure_basic_style()

        start_button = self._widget_creator.create_basic_button(
            self._frame, "START", self._handle_show_gameplay_view
            )

        back_button = self._widget_creator.create_basic_button(
            self._frame, "BACK", self._handle_show_main_menu
            )

        start_button.place(relx=0.5, rely=0.6, anchor='center')
        back_button.place(relx=0.5, rely=0.7, anchor='center')
