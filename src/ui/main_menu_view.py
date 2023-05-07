
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles


class MainMenuView(BaseView):
    """Luokka, jonka avulla luodaan sovelluksen päävalikon näkymä.

    Args:
        BaseView: Sovelluksen perusnäkymästä vastaava luokka
    """

    def __init__(self, root, views):
        """Luokan konstruktori, joka alustaa päävalikon näkymän.

        Args:
            root: Luokan juuri-ikkuna
        """

        super().__init__(root)
        self._handle_show_new_game_view = views['show_new_game']
        self._handle_show_high_scores = views['show_high_scores']
        self._handle_show_rules = views['show_rules']
        self._handle_show_quit_view = views['show_quit']
        self._button_style = ButtonStyles()

        self._initialize()

    def _initialize(self):
        """Aloittaa päävalikon näkymän luomisen kutsumalla 
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_grid()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        h1_label = tkinter.Label(
            self._frame, text="Gridiron Genius",
            font=("Verdana", 40, "bold"), fg='white', bg="#013369"
        )
        h2_label = tkinter.Label(
            self._frame, text="An NFL Trivia Game",
            font=("Verdana", 30), fg='white', bg="#013369"
        )

        h1_label.grid(row=1, column=1, columnspan=2)
        h2_label.grid(row=2, column=1, columnspan=2)

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._button_style.configure_basic_style()

        new_game_button = ttk.Button(
            self._frame, text="NEW GAME",
            style='custom.basic.TButton',
            command=self._handle_show_new_game_view
        )

        high_scores_button = ttk.Button(
            self._frame, text="HIGH SCORES",
            style='custom.basic.TButton',
            command=self._handle_show_high_scores
        )
        rules_button = ttk.Button(
            self._frame, text="RULES",
            style='custom.basic.TButton',
            command=self._handle_show_rules
        )
        quit_button = ttk.Button(
            self._frame, text="QUIT",
            style='custom.basic.TButton',
            command=self._handle_show_quit_view
        )

        new_game_button.grid(row=4, column=0)
        high_scores_button.grid(row=4, column=1)
        rules_button.grid(row=4, column=2)
        quit_button.grid(row=4, column=3)

    def _adjust_grid(self):
        """Auttaa säätämään muiden elementtien sijainteja.
        (Tätä metodia ei lopulta varmaan tarvita, 
        kunhan luokan muut metodit toteutetaan ensin vähän paremmin.)
        """

        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(3, minsize=50)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
        self._frame.grid_columnconfigure(3, weight=1)
