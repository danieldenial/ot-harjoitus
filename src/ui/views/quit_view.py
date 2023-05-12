
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.widget_styles import WidgetStyles


class QuitView(BaseFrame):
    """Luokka, jonka avulla luodaan sovelluksen sulkemista edeltävä näkymä.

    Args:
        BaseView: QuitView-luokan perimä pohjakehyksen näkymälle luova luokka

    Attributes:
        _handle_show_main_menu: UI-luokan metodi päävalikon näkymän luomiseen
        _quit_game: UI-luokan metodi sovelluksen sulkemiseen
        _button_style: Näkymän painikkeiden tyyleistä vastaava luokkaolio
    """

    def __init__(self, root, main_menu_view, quit_view_callback):
        """Luokan konstruktori, joka alustaa sovelluksen sulkemista edeltävän näkymän.

        Args:
            root: Luokan juuri-ikkuna
            quit_game: Metodi, jolla siirrytään sovelluksen sulkemista edeltävään näkymään
            main_menu_view: Metodi, jolla siirrytään päävalikon näkymään
        """

        super().__init__(root)
        self._handle_show_main_menu = main_menu_view
        self._quit_application = quit_view_callback
        self._widget_creator = WidgetCreator(root)
        self._widget_styles = WidgetStyles(root)

        self._initialize()

    def _initialize(self):
        """Aloittaa uutta peliä edeltävän näkymän luomisen kutsumalla
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_texts()
        self._initialize_buttons()

    def _initialize_texts(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        quit_game_text_1 = self._widget_creator.create_basic_label(
            self._frame, "Quit game?", 30
            )

        quit_game_text_1.place(relx=0.5, rely=0.4, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._widget_styles.config_basic_button()

        quit_button = self._widget_creator.create_basic_button(
            self._frame, "YES", self._quit_application
            )

        back_button = self._widget_creator.create_basic_button(
            self._frame, "NO", self._handle_show_main_menu
            )

        quit_button.place(relx=0.5, rely=0.5, anchor='center')
        back_button.place(relx=0.5, rely=0.6, anchor='center')