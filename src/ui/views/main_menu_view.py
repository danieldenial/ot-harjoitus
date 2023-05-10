
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.button_styles import ButtonStyles


class MainMenuView(BaseFrame):
    """Luokka, jonka avulla luodaan sovelluksen päävalikon näkymä.

    Args:
        BaseView: MainMenuView-luokan perimä pohjakehyksen näkymälle luova luokka
    
    Attributes:
        _handle_show_new_game_view: UI-luokan metodi peliä edeltävän näkymän luomiseen
        _handle_show_high_scores: UI-luokan metodi parhaiden pisteiden näkymän luomiseen
        _handle_show_rules: UI-luokan metodi sääntönäkymän luomiseen
        _handle_show_quit_view: UI-luokan metodi sovelluksen lopetusnäkymän luomiseen
        _button_style: Näkymän painikkeiden tyyleistä vastaava luokkaolio
    """

    def __init__(self, root, views):
        """Luokan konstruktori, joka alustaa päävalikon näkymän.

        Args:
            root: Tkinter-pääikkunan viite
            views: Sanakirja UI-luokan metodeista, joilla siirrytään eri näkymiin
        """

        super().__init__(root)
        self._handle_show_new_game_view = views['show_new_game']
        self._handle_show_high_scores = views['show_high_scores']
        self._handle_show_rules = views['show_rules']
        self._handle_show_quit_view = views['show_quit']
        self._widget_creator = WidgetCreator(root)
        self._button_style = ButtonStyles(root)

        self._initialize()

    def _initialize(self):
        """Aloittaa päävalikon näkymän luomisen kutsumalla 
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        h1_label = self._widget_creator.create_basic_label(
            self._frame, "Gridiron Genius", 0.06
        )
        
        h2_label = self._widget_creator.create_basic_label(
            self._frame, "An NFL Trivia Game", 0.05
            )

        h1_label.place(relx=0.5, rely=0.25, anchor='center')
        h2_label.place(relx=0.5, rely=0.35, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """
        
        self._button_style.configure_basic_style()

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
