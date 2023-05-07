
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles
from ui.view_manager import ViewManager
from services.score_service import ScoreService


class NewGameView(BaseView):
    """Uutta peliä edeltävä näkymä.

    Args:
        BaseView: Sovelluksen perusnäkymästä vastaava luokka
    """

    def __init__(self, root, score_service: ScoreService, view_manager: ViewManager):
        """Luokan konstruktori, joka alustaa uutta peliä edeltävän näkymän.

        Args:
            root: Luokan juuri-ikkuna
            main_menu_view: Metodi, jolla siirrytään päävalikon näkymään
            gameplay_view: Metodi, jolla siirrytään pelinkulkua kuvaavaan näkymään
        """

        super().__init__(root)
        self._view_manager = view_manager
        self._score_service = score_service
        self._button_style = ButtonStyles()

        self._initialize()

    def _initialize(self):
        """Aloittaa uutta peliä edeltävän näkymän luomisen kutsumalla
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_grid()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        new_game_text_1 = tkinter.Label(
            self._frame, text="Time for a new game!",
            font=("Arial", 35), fg='white', bg="#013369"
        )
        new_game_text_2 = tkinter.Label(
            self._frame,
            text=f"The current high score is {self._score_service.get_high_score()}.",
            font=("Arial", 30), fg='white', bg="#013369"
        )
        new_game_text_3 = tkinter.Label(
            self._frame, text="Can you beat it?",
            font=("Arial", 30), fg='white', bg="#013369"
        )

        new_game_text_1.grid(row=1, column=1)
        new_game_text_2.grid(row=3, column=1)
        new_game_text_3.grid(row=5, column=1)

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._button_style.configure_basic_style()

        start_button = ttk.Button(
            self._frame, text="START GAME",
            padding=10, style='custom.basic.TButton',
            command=self._view_manager.go_to_gameplay_view
        )

        back_button = ttk.Button(
            self._frame, text="BACK",
            padding=5, style='custom.basic.TButton',
            command=self._view_manager.go_to_main_menu_view
        )

        start_button.grid(row=7, column=1)
        back_button.grid(row=9, column=1)

    def _adjust_grid(self):
        """Auttaa säätämään muiden elementtien sijainteja.
        (Tätä metodia ei lopulta varmaan tarvita,
        kunhan luokan muut metodit toteutetaan ensin vähän paremmin.)
        """

        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(2, minsize=25)
        self._frame.grid_rowconfigure(4, minsize=25)
        self._frame.grid_rowconfigure(6, minsize=50)
        self._frame.grid_rowconfigure(8, minsize=25)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
