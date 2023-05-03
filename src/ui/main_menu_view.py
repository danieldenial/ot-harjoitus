
import tkinter
from tkinter import ttk
from ui.base_view import BaseView


class MainMenuView(BaseView):
    """Sovelluksen päävalikon näkymä.

    Args:
        BaseView: Sovelluksen perusnäkymästä vastaava luokka
    """

    def __init__(self, root, new_game_view, quit_view, rules_view):
        """Luokan konstruktori, joka alustaa päävalikon näkymän.

        Args:
            root: Luokan juuri-ikkuna
            new_game_view: Metodi, jolla siirrytään uutta peliä edeltävään näkymään
            quit_view: Metodi, jolla siirrytään sovelluksen sulkemista edeltävään näkymään
            rules_view: Metodi, jolla siirrytään pelin sääntöjä näyttävään näkymään
        """

        super().__init__(root)
        self._root = root
        self._show_new_game_view = new_game_view
        self._show_quit_view = quit_view
        self._show_rules_view = rules_view

        self._initialize()

    def _initialize(self):
        """Aloittaa päävalikon näkymän luomisen kutsumalla 
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_elements()

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

        h1_label.grid(row=1, column=1)
        h2_label.grid(row=2, column=1)

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.main_menu.TButton', font=('Verdana', 20),
            padding=10, background='#8a9095', foreground='black'
        )

        new_game_button = ttk.Button(
            self._frame, text="NEW GAME",
            style='custom.main_menu.TButton',
            command=self._show_new_game_view
        )
        rules_button = ttk.Button(
            self._frame, text="VIEW RULES",
            style='custom.main_menu.TButton',
            command=self._show_rules_view
        )
        quit_button = ttk.Button(
            self._frame, text="QUIT",
            style='custom.main_menu.TButton',
            command=self._show_quit_view
        )

        new_game_button.grid(row=4, column=0)
        rules_button.grid(row=4, column=1)
        quit_button.grid(row=4, column=2)

    def _adjust_elements(self):
        """Auttaa säätämään muiden elementtien sijainteja.
        (Tätä metodia ei lopulta varmaan tarvita, 
        kunhan luokan muut metodit toteutetaan ensin vähän paremmin.)
        """

        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(3, minsize=50)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
