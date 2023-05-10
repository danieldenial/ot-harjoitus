
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles
from services.score_service import ScoreService


class NewGameView(BaseView):
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
        self._button_style = ButtonStyles(self.window_height)

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

        new_game_text_1 = tkinter.Label(
            self._frame, text="Time for a new game!",
            font=("Arial", round(self.window_height*0.05)), fg='white', bg="#013369"
        )
        new_game_text_2 = tkinter.Label(
            self._frame,
            text=f"The current high score is {self._score_service.get_high_score()}.",
            font=("Arial", round(self.window_height*0.05)), fg='white', bg="#013369"
        )
        new_game_text_3 = tkinter.Label(
            self._frame, text="Can you beat it?",
            font=("Arial", round(self.window_height*0.05)), fg='white', bg="#013369"
        )

        new_game_text_1.place(relx=0.5, rely=0.2, anchor='center')
        new_game_text_2.place(relx=0.5, rely=0.3, anchor='center')
        new_game_text_3.place(relx=0.5, rely=0.4, anchor='center')

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._button_style.configure_basic_style()

        start_button = ttk.Button(
            self._frame, text="START GAME",
            style='custom.basic.TButton',
            padding=round(self.window_height*0.015),
            command=self._handle_show_gameplay_view
        )

        back_button = ttk.Button(
            self._frame, text="BACK",
            style='custom.basic.TButton',
            padding=round(self.window_height*0.01),
            command=self._handle_show_main_menu
        )

        start_button.place(relx=0.5, rely=0.6, anchor='center')
        back_button.place(relx=0.5, rely=0.7, anchor='center')

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
