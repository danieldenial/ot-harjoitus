
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles


class RulesView(BaseView):
    """Pelin säännöt näyttävä näkymä.

    Args:
        BaseView: Sovelluksen perusnäkymästä vastaava luokka
    """

    def __init__(self, root, view_manager):
        """Luokan konstruktori, joka alustaa pelin säännöt näyttävän näkymän.

        Args:
            root: Luokan juuri-ikkuna
            main_menu_view: Metodi, jolla siirrytään päävalikon näkymään
        """

        super().__init__(root)
        self._root = root
        self._view_manager = view_manager
        self._button_style = ButtonStyles()

        self._initialize()

    def _initialize(self):
        """Aloittaa pelin säännöt näyttävän näkymän luomisen kutsumalla
        ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_elements()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        rules_text_1 = tkinter.Label(
            self._frame,
            text="Gridiron Genius is a multiple choice trivia game about the NFL.",
            font=("Arial", 25), fg='white', bg="#013369",
            padx=10, pady=10
        )

        rules_text_2 = tkinter.Label(
            self._frame,
            text="Once you start the game, you will see a question and four options.",
            font=("Arial", 25), fg='white', bg="#013369",
            padx=10, pady=10
        )

        rules_text_3 = tkinter.Label(
            self._frame,
            text="Click on A, B, C or D to select the answer you think is correct.",
            font=("Arial", 25), fg='white', bg="#013369",
            padx=10, pady=10
        )

        rules_text_4 = tkinter.Label(
            self._frame,
            text="You will get 1 point for each right answer.",
            font=("Arial", 25), fg='white', bg="#013369",
            padx=10, pady=10
        )

        rules_text_5 = tkinter.Label(
            self._frame,
            text="All questions and answers are valid as of May 2023.",
            font=("Arial", 25), fg='white', bg="#013369",
            padx=10, pady=10
        )

        rules_text_1.grid(row=1, column=1, sticky="nsew")
        rules_text_2.grid(row=2, column=1)
        rules_text_3.grid(row=3, column=1)
        rules_text_4.grid(row=4, column=1)
        rules_text_5.grid(row=5, column=1)

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._button_style.configure_basic_style()

        back_button = ttk.Button(
            self._frame, text="BACK",
            padding=5, style='custom.basic.TButton',
            command=self._view_manager.go_to_main_menu_view()
        )

        back_button.grid(row=6, column=1, padx=30, pady=30)

    def _adjust_elements(self):
        """Auttaa säätämään muiden elementtien sijainteja.
        (Tätä metodia ei lopulta varmaan tarvita, 
        kunhan luokan muut metodit toteutetaan ensin vähän paremmin.)
        """

        self._frame.grid_rowconfigure(0, minsize=100)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
