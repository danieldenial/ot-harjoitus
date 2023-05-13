
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.widget_styles import WidgetStyles


class MainMenuView(BaseFrame):
    """Päävalikosta vastaava näkymä.

    Args:
        BaseView: 
            Luokka, joka luo kaikille näkymille pohjakehyksen.
    """

    def __init__(self, root, views):
        """Luokan konstruktori. Luo uuden päävalikon näkymän.

        Args:
            root: 
                Tkinter-pääikkuna, jonka sisään näkymä luodaan.
            views:
                Sanakirja kutsuttavia arvoja, joilla siirrytään eri näkymiin.
        """

        super().__init__(root)
        self._handle_show_new_game_view = views['show_new_game']
        self._handle_show_high_scores = views['show_high_scores']
        self._handle_show_rules = views['show_rules']
        self._handle_show_quit_view = views['show_quit']
        self._widget_creator = WidgetCreator(root)
        self._widget_styles = WidgetStyles(root)

        self._initialize()

    def _initialize(self):
        """Aloittaa päävalikon näkymän luomisen
        """

        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        h1_label = self._widget_creator.create_basic_label(
            self._frame, "Gridiron Genius", 16
            )
        
        h2_label = self._widget_creator.create_basic_label(
            self._frame, "An NFL Trivia Game", 20
            )

        h1_label.place(relx=0.5, rely=0.25, anchor='center')
        h2_label.place(relx=0.5, rely=0.35, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """
        
        self._widget_styles.config_basic_button()

        new_game_button = self._widget_creator.create_basic_button(
            self._frame, "NEW GAME", self._handle_show_new_game_view
            )

        high_scores_button = self._widget_creator.create_basic_button(
            self._frame, "SCORES", self._handle_show_high_scores
            )
        
        rules_button = self._widget_creator.create_basic_button(
            self._frame, "RULES", self._handle_show_rules
            )

        quit_button = self._widget_creator.create_basic_button(
            self._frame, "QUIT", self._handle_show_quit_view
            )

        new_game_button.place(relx=0.2, rely=0.5, anchor='center')
        high_scores_button.place(relx=0.4, rely=0.5, anchor='center')
        rules_button.place(relx=0.6, rely=0.5, anchor='center')
        quit_button.place(relx=0.8, rely=0.5, anchor='center')
