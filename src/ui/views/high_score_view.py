
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.button_styles import ButtonStyles
from services.score_service import ScoreService


class HighScoreView(BaseFrame):
    """Luokka, jonka avulla luodaan parhaat pistesuoritukset näyttävä näkymä.

    Args:
        BaseView: HighScoreView-luokan perimä pohjakehyksen näkymälle luova luokka.

    Attributes:
        _score_service: Näkymän painikkeiden tyyleistä vastaava luokkaolio
        _handle_show_main_menu: UI-luokan metodi päävalikon näkymän luomiseen
        _button_style: Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
    """

    def __init__(self, root, score_service: ScoreService, main_menu_view):
        """Luokan konstruktori, joka alustaa parhaiden pistesuoritusten näkymän.

        Args:
            root: Tkinter-pääikkunan viite
            score_service: Pisteytykseen liittyvästä sovelluslogiikasta vastaava luokkaolio
            main_menu_view: UI-luokan metodi päävalikon näkymän luomiseen
        """

        super().__init__(root)
        self._score_service = score_service
        self._handle_show_main_menu = main_menu_view
        self._widget_creator = WidgetCreator(root)
        self._button_style = ButtonStyles(root)

        self._initialize()

    def _initialize(self):
        self._initialize_labels()
        self._initialize_high_scores_table()
        self._initialize_buttons()

    def _initialize_labels(self):
        intro_text = self._widget_creator.create_basic_label(
            self._frame, "These are the high scores – so far.", 0.04
        )

        intro_text.place(relx=0.5, rely=0.2, anchor='center')

    def _initialize_high_scores_table(self):
        high_scores = self._score_service.get_high_scores_list()

        columns = ['Team', 'Score']
        headings = ['Team', 'Score']

        self._table = self._widget_creator.create_table(
            self._frame, columns, headings, "Position"
            )

        for i, score in enumerate(high_scores):
            i += 1
            self._table.insert(
                parent='', index='end', iid=i,text=i, values=(score[1], score[0])
                )
        
        self._table.place(relx=0.5, rely=0.5, anchor='center')

    def _initialize_buttons(self):
        self._button_style.configure_basic_style()

        reset_scores_button = self._widget_creator.create_basic_button(
            self._frame, "RESET", self._update_table
            )

        main_menu_button = self._widget_creator.create_basic_button(
            self._frame, "MAIN MENU", self._handle_show_main_menu
            )

        reset_scores_button.place(relx=0.4, rely=0.8, anchor='center')
        main_menu_button.place(relx=0.6, rely=0.8, anchor='center')

    def _update_table(self):
        self._score_service.reset_high_scores_list()
        for i in range(1, 11):
            self._table.item(i, values=('N/A', 0))
