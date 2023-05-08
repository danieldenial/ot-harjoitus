
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles


class RulesView(BaseView):
    """Luokka, jonka avulla luodaan pelin säännöt näyttävä näkymä.

    Args:
        BaseView: Sovelluksen perusnäkymästä vastaava luokka
    """

    def __init__(self, root, main_menu_view):
        """Luokan konstruktori, joka alustaa pelin säännöt näyttävän näkymän.

        Args:
            root: Luokan juuri-ikkuna
            main_menu_view: Metodi, jolla siirrytään päävalikon näkymään
        """

        super().__init__(root)
        self._handle_show_main_menu = main_menu_view
        self._button_style = ButtonStyles(self.screen_height)

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

        rules_text_1 = tkinter.Label(
            self._frame,
            text="Gridiron Genius is a multiple choice trivia game about the NFL.",
            font=("Arial", round(self.screen_height*0.035)), fg='white', bg="#013369"
        )

        rules_text_2 = tkinter.Label(
            self._frame,
            text="Once you start the game, you will see a question and four options.",
            font=("Arial", round(self.screen_height*0.035)), fg='white', bg="#013369"
        )

        rules_text_3 = tkinter.Label(
            self._frame,
            text="Click on A, B, C or D to select the answer you think is correct.",
            font=("Arial", round(self.screen_height*0.035)), fg='white', bg="#013369"
        )

        rules_text_4 = tkinter.Label(
            self._frame,
            text="You will get 1 point for each right answer.",
            font=("Arial", round(self.screen_height*0.035)), fg='white', bg="#013369"
        )

        rules_text_5 = tkinter.Label(
            self._frame,
            text="All questions and answers are valid as of May 2023.",
            font=("Arial", round(self.screen_height*0.035)), fg='white', bg="#013369"
        )

        rules_text_1.place(relx=0.5, rely=0.2, anchor='center')
        rules_text_2.place(relx=0.5, rely=0.3, anchor='center')
        rules_text_3.place(relx=0.5, rely=0.4, anchor='center')
        rules_text_4.place(relx=0.5, rely=0.5, anchor='center')
        rules_text_5.place(relx=0.5, rely=0.6, anchor='center')


    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        self._button_style.configure_basic_style()

        back_button = ttk.Button(
            self._frame, text="BACK",
            style='custom.basic.TButton',
            padding=round(self.screen_height*0.01),
            command=self._handle_show_main_menu
        )

        back_button.place(relx=0.5, rely=0.75, anchor='center')

    def _adjust_grid(self):
        """Auttaa säätämään muiden elementtien sijainteja.
        """

        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_rowconfigure(2, weight=1)
        self._frame.grid_rowconfigure(3, weight=1)
        self._frame.grid_rowconfigure(4, weight=1)
        self._frame.grid_rowconfigure(5, weight=2)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
