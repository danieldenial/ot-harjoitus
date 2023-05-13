
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.widget_styles import WidgetStyles


class QuitView(BaseFrame):
    """Sovelluksen sulkemista edeltävästä näkymästä vastaava luokka.

    Args:
        BaseView:
            Luokka, joka luo kaikille näkymille pohjakehyksen.
    """

    def __init__(self, root, main_menu_view, quit_view_callback):
        """Luokan konstruktori. Luo uuden sovelluksen sulkemista edeltävän näkymän.

        Args:
            root:
                Tkinter-pääikkuna, jonka sisään näkymä luodaan.
            main_menu_view:
                Kutsuttava arvo päävalikkoon siirtymiseksi.
            quit_view_callback: 
                Kutsuttava arvo sovelluksen sulkemiseksi.
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

        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        quit_game_label_1 = self._widget_creator.create_basic_label(
            self._frame, "Quit game?", 30
            )

        quit_game_label_1.place(relx=0.5, rely=0.4, anchor='center')

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
