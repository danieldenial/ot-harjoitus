
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.widget_styles import WidgetStyles


class RulesView(BaseFrame):
    """Luokka, jonka avulla luodaan pelin säännöt näyttävä näkymä.

    Args:
        BaseView: RulesView-luokan perimä pohjakehyksen näkymälle luova luokka

    Attributes:
        _handle_show_main_menu: UI-luokan metodi päävalikon näkymän luomiseen
        _button_style: Näkymän painikkeiden tyyleistä vastaava luokkaolio
    """

    def __init__(self, root, main_menu_view):
        """Luokan konstruktori, joka alustaa pelin säännöt näyttävän näkymän.

        Args:
            root: Tkinter-pääikkunan viite
            main_menu_view: UI-luokan metodi päävalikon näkymän luomiseen
        """

        super().__init__(root)
        self._handle_show_main_menu = main_menu_view
        self._widget_creator = WidgetCreator(root)
        self._widget_styles = WidgetStyles(root)

        self._initialize()

    def _initialize(self):
        """Aloittaa pelin säännöt näyttävän näkymän luomisen kutsumalla
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        font_size_factor = 30

        rules_text_1 = self._widget_creator.create_basic_label(
            self._frame, 
            "Gridiron Genius is a multiple choice trivia game about the NFL.",
            font_size_factor
            )

        rules_text_2 = self._widget_creator.create_basic_label(
            self._frame,
            "Once you start the game, you will see a question and four options.",
            font_size_factor
            )

        rules_text_3 = self._widget_creator.create_basic_label(
            self._frame,
            "Click on A, B, C or D to select the answer you think is correct.",
            font_size_factor
            )

        rules_text_4 = self._widget_creator.create_basic_label(
            self._frame, "You will get 1 point for each right answer.", font_size_factor
            )

        rules_text_5 = self._widget_creator.create_basic_label(
            self._frame, 
            "All questions and answers are valid as of May 2023.", font_size_factor
            )

        rules_text_1.place(relx=0.5, rely=0.2, anchor='center')
        rules_text_2.place(relx=0.5, rely=0.3, anchor='center')
        rules_text_3.place(relx=0.5, rely=0.4, anchor='center')
        rules_text_4.place(relx=0.5, rely=0.5, anchor='center')
        rules_text_5.place(relx=0.5, rely=0.6, anchor='center')


    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._widget_styles.config_basic_button()

        back_button = self._widget_creator.create_basic_button(
            self._frame, "BACK", self._handle_show_main_menu
            )

        back_button.place(relx=0.5, rely=0.75, anchor='center')
