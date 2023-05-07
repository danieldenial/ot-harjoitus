
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles
from services.score_service import ScoreService


class HighScoreView(BaseView):
    """Luokka, jonka avulla luodaan parhaat tulokset näyttävä näkymä.

    Args:
        BaseView: Sovelluksen perusnäkymästä vastaava luokka, jonka HighScoreView perii.

    Attributes:
        _view_manager: Eri näkymien vaihtelusta vastaava luokkaolio
        _score_service: Näkymän painikkeiden tyyleistä vastaava luokkaolio
        _button_style: Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
    """

    def __init__(self, root, score_service: ScoreService, main_menu_view):
        """Luokan konstruktori, joka alustaa sovelluksen avausnäkymän.

        Args:
            root (_type_): _description_
            score_service (ScoreService): _description_
            view_manager (ViewManager): _description_
        """
        super().__init__(root)
        self._handle_show_main_menu = main_menu_view
        self._score_service = score_service
        self._button_style = ButtonStyles()

        self._initialize()

    def _initialize(self):
        self._initialize_labels()
        self._initialize_high_scores_table()
        self._initialize_buttons()
        self._adjust_grid()

    def _initialize_labels(self):
        intro_text = tkinter.Label(
            self._frame,
            text="These are the high scores – so far.",
            font=("Arial", 30), fg='white', bg="#013369"
        )

        intro_text.grid(row=0, column=1, pady=(100, 50))

    def _initialize_high_scores_table(self):
        high_scores = self._score_service.get_high_scores_list()

        self._table = ttk.Treeview(self._frame, columns=('Team', 'Score'))

        self._table.heading('#0', text='Pos')
        self._table.heading('Team', text='Team')
        self._table.heading('Score', text='Score')

        i = 1

        for score in high_scores:
            self._table.insert(parent='', index='end', iid=i,
                               text=i, values=(score[1], score[0]))
            i += 1

        self._table.grid(row=1, column=1)

    def _initialize_buttons(self):
        self._button_style.configure_basic_style()

        reset_scores_button = ttk.Button(
            self._frame, text="RESET SCORES",
            style='custom.basic.TButton',
            command=self._update_table
        )

        main_menu_button = ttk.Button(
            self._frame, text="MAIN MENU",
            style='custom.basic.TButton',
            command=self._handle_show_main_menu
        )

        reset_scores_button.grid(row=2, column=1, pady=(50, 25))
        main_menu_button.grid(row=3, column=1)

    def _adjust_grid(self):
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)

    def _update_table(self):
        self._score_service.reset_high_score_list()
        for i in range(1, 11):
            self._table.item(i, values=('N/A', 0))
