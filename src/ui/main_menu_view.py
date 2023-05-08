
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
        self._button_style = ButtonStyles(self.screen_height)

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

        h1_label = tkinter.Label(
            self._frame, text="Gridiron Genius",
            font=("Verdana", round(self.screen_height*0.06), "bold"), fg='white', bg="#013369"
        )
        h2_label = tkinter.Label(
            self._frame, text="An NFL Trivia Game",
            font=("Verdana", round(self.screen_height*0.05)), fg='white', bg="#013369"
        )

        h1_label.place(relx=0.5, rely=0.25, anchor='center')
        h2_label.place(relx=0.5, rely=0.35, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._button_style.configure_basic_style()

        new_game_button = ttk.Button(
            self._frame, text="NEW GAME",
            style='custom.basic.TButton',
            padding=round(self.screen_height*0.015),
            command=self._handle_show_new_game_view
        )

        high_scores_button = ttk.Button(
            self._frame, text="SCORES",
            style='custom.basic.TButton',
            padding=round(self.screen_height*0.015),
            command=self._handle_show_high_scores
        )
        rules_button = ttk.Button(
            self._frame, text="RULES",
            style='custom.basic.TButton',
            padding=round(self.screen_height*0.015),
            command=self._handle_show_rules
        )
        quit_button = ttk.Button(
            self._frame, text="QUIT",
            style='custom.basic.TButton',
            padding=round(self.screen_height*0.015),
            command=self._handle_show_quit_view
        )

        new_game_button.place(relx=0.2, rely=0.5, anchor='center')
        high_scores_button.place(relx=0.4, rely=0.5, anchor='center')
        rules_button.place(relx=0.6, rely=0.5, anchor='center')
        quit_button.place(relx=0.8, rely=0.5, anchor='center')
