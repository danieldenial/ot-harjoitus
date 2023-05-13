
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_styles import WidgetStyles
from ui.utilities.widget_creator import WidgetCreator


class ErrorView(BaseFrame):
    """Virhetilanteen ilmoituksesta vastaava näkymä.

    Args:
        BaseFrame:
            Luokka, joka luo kaikille näkymille pohjakehyksen.
    """

    def __init__(self, root, quit_view_callback):
        """Luokan konstruktori. Luo uuden virhetilanteen ilmoituksen näkymän.

        Args:
            root:
                Tkinter-pääikkuna, jonka sisään näkymä luodaan.
            quit_view_callback:
                Kutsuttava arvo sovelluksen sulkemiseksi.
        """
        super().__init__(root)
        self._widget_styles = WidgetStyles(root)
        self._widget_creator = WidgetCreator(root)
        self._quit_application = quit_view_callback

        self._initialize()

    def _initialize(self):
        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        font_scaler = 30
        error_text = self._widget_creator.create_basic_label(
            self._frame, 
            "Hmm, seems like the questions did not properly load.", 
            font_scaler
            )

        quit_game_text = self._widget_creator.create_basic_label(
            self._frame, "Please try again later.", font_scaler
            )

        error_text.place(relx=0.5, rely=0.4, anchor='center')
        quit_game_text.place(relx=0.5, rely=0.5, anchor='center')

    def _initialize_buttons(self):
        self._widget_styles.config_basic_button()

        main_menu_button = self._widget_creator.create_basic_button(
            self._frame, "QUIT", self._quit_application
            )

        main_menu_button.place(relx=0.5, rely=0.6, anchor='center')
