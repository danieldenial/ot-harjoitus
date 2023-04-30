
import tkinter
from tkinter import ttk
from ui.base_view import BaseView


class RulesView(BaseView):
    """Pelin säännöt näyttävä näkymä.

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
        self._main_menu_view = main_menu_view

        self._initialize()

    def _initialize(self):
        """Aloittaa pelin säännöt näyttävän näkymän luomisen kutsumalla ikkunaan eri elementtejä sijoittavia metodeja.
        """

        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_elements()

    def _initialize_labels(self):
        """Luo näkymään kuuluvat tekstit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        rules_text = tkinter.Label(
            self._frame, text="The rules will be added later.",
            font=("Arial", 35), fg='white', bg="#013369"
        )

        rules_text.grid(row=1, column=1)

    def _initialize_buttons(self):
        """Luo näkymään kuuluvat napit ja sijoittaa ne haluttuihin kohtiin ikkunaa.
        """

        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.rules_menu.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black'
        )

        back_button = ttk.Button(
            self._frame, text="BACK",
            padding=5, style='custom.rules_menu.TButton',
            command=self._main_menu_view
        )

        back_button.grid(row=3, column=1)

    def _adjust_elements(self):
        """Auttaa säätämään muiden elementtien sijainteja.
        (Tätä metodia ei lopulta varmaan tarvita, kunhan luokan muut metodit toteutetaan ensin vähän paremmin.)
        """

        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(2, minsize=100)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
