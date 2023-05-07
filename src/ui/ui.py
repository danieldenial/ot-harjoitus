
from ui.intro_view import IntroView
from ui.main_menu_view import MainMenuView
from ui.new_game_view import NewGameView
from ui.gameplay_view import GameplayView
from ui.high_score_view import HighScoreView
from ui.rules_view import RulesView
from ui.quit_view import QuitView
from ui.view_manager import ViewManager


class UI:
    """Luokka, jonka avulla hallinnoidaan sovelluksen käyttöliittymän eri näkymiä.

    Attributes:
        _root: Luokan juuri-ikkuna
        _current_view: Sovelluksen ikkunan ja käyttöliittymän senhetkinen näkymä
    """

    def __init__(self, root, context):
        """Luokan konstruktori, joka alustaa uuden käyttöliittymän näkymän.

        Args:
            root: Luokan juuri-ikkuna
        """

        self._root = root
        self._question_service = context['question_service']
        self._score_service = context['score_service']
        self._view_manager = ViewManager(self)
        self._current_view = None

    def start(self):
        """Käynnistää sovelluksen kutsumalla sen luomisesta vastaavaa metodia.
        """

        self.show_intro_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän, jotta sovellus voi luoda uuden näkymän.
        """

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def show_intro_view(self):
        self._hide_current_view()

        self._current_view = IntroView(
            self._root,
            self._score_service,
            self._view_manager
        )

        self._current_view.pack()

    def show_main_menu_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia 
        ja luo sitten päävalikon näkymän.
        """

        self._hide_current_view()

        self._current_view = MainMenuView(
            self._root,
            self._view_manager
        )

        self._current_view.pack()

    def show_new_game_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia 
        ja luo sitten uutta peliä edeltävän näkymän.
        """

        self._hide_current_view()

        self._current_view = NewGameView(
            self._root,
            self._score_service,
            self._view_manager
        )

        self._current_view.pack()

    def show_gameplay_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia 
        ja luo sitten varsinaisesta pelinkulusta vastaavan näkymän.
        """

        self._hide_current_view()

        self._current_view = GameplayView(
            self._root,
            self._question_service,
            self._score_service,
            self._view_manager
        )

        self._current_view.pack()

    def show_high_score_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia
        ja luo sitten parhaiden tulosten listan näyttävän näkymän.
        """

        self._hide_current_view()

        self._current_view = HighScoreView(
            self._root,
            self._score_service,
            self._view_manager
        )

        self._current_view.pack()

    def show_rules_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia 
        ja luo sitten pelin säännöt sisältävän näkymän.
        """

        self._hide_current_view()

        self._current_view = RulesView(
            self._root,
            self._view_manager
        )

        self._current_view.pack()

    def show_quit_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia 
        ja luo sitten sovelluksen sulkemista edeltävän näkymän. 
        """

        self._hide_current_view()

        self._current_view = QuitView(
            self._root,
            self._view_manager,
            self._quit_view_callback
        )

        self._current_view.pack()

    def _quit_view_callback(self):
        """Sulkee sovelluksen.
        """

        self._root.quit()
