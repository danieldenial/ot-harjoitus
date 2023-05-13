
from ui.views.main_menu_view import MainMenuView
from ui.views.new_game_view import NewGameView
from ui.views.gameplay_view import GameplayView
from ui.views.high_score_view import HighScoreView
from ui.views.rules_view import RulesView
from ui.views.error_view import ErrorView
from ui.views.completed_view import CompletedView
from ui.views.quit_view import QuitView


class UI:
    """Luokka, joka vastaa siirtymistä sovelluksen eri näkymien välillä.

    Attributes:
        _root: Tkinter-pääikkunan viite
        _question_service: Kysymysdatan käsittelyä hallinnoiva luokkaolio
        _score_service: Pisteiden käsittelyä hallinnoiva luokkaolio
        _current_view: Sovelluksen ikkunan ja käyttöliittymän senhetkinen näkymä
    """

    def __init__(self, root, instances):
        """Luokan konstruktori, joka luo eri näkymiä hallinnoivan luokkaolion.

        Args:
            root: Tkinter-pääikkuna, jonka sisään käyttöliittymä ja näkymät luodaan
            instances: Sanakirja, joka sisältää viitteet services-pakkauksen olioihin 
        """

        self._root = root
        self._question_service = instances['question_service']
        self._score_service = instances['score_service']
        self._current_view = None

    def start(self):
        """Käynnistää sovelluksen kutsumalla avausnäkymän luomisesta vastaavaa metodia.
        """

        self._show_main_menu_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän, jotta sovellus voi luoda uuden näkymän.
        """

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_main_menu_view(self):
        """Vastaa päävalikkoon siirtymisestä.
        """

        self._hide_current_view()

        views = {
            'show_new_game': self._show_new_game_view,
            'show_high_scores': self._show_high_score_view,
            'show_rules': self._show_rules_view,
            'show_quit': self._show_quit_view
        }

        self._current_view = MainMenuView(
            self._root,
            views
        )

        self._current_view.pack()

    def _show_new_game_view(self):
        """Vastaa peliä edeltävään näkymään siirtymisestä.
        """

        self._hide_current_view()

        views = {
            'show_gameplay_view': self._show_gameplay_view,
            'show_main_menu': self._show_main_menu_view
        }

        self._current_view = NewGameView(
            self._root,
            self._score_service,
            views
        )

        self._current_view.pack()

    def _show_gameplay_view(self):
        """Vastaa varsinaisen pelinkulun näkymään siirtymisestä.
        """

        self._hide_current_view()

        views = {
            'show_main_menu': self._show_main_menu_view,
            'show_new_game_view': self._show_new_game_view,
            'show_quit_view': self._show_quit_view,
            'show_error_view': self._show_error_view,
            'show_genius_view': self._show_completed_view
        }

        self._current_view = GameplayView(
            self._root,
            self._question_service,
            self._score_service,
            views
        )

        self._current_view.pack()

    def _show_high_score_view(self):
        """Vastaa parhaiden tulosten näkymään siirtymisestä.
        """

        self._hide_current_view()

        self._current_view = HighScoreView(
            self._root,
            self._score_service,
            self._show_main_menu_view
        )

        self._current_view.pack()

    def _show_rules_view(self):
        """Vastaa pelin säännöt näyttävään näkymään siirtymisestä.
        """

        self._hide_current_view()

        self._current_view = RulesView(
            self._root,
            self._show_main_menu_view
        )

        self._current_view.pack()

    def _show_error_view(self):
        """Vastaa virheilmoituksen antavaan näkymään siirtymisestä.
        """

        self._hide_current_view()

        self._current_view = ErrorView(
            self._root,
            self._quit_view_callback
        )

        self._current_view.pack()

    def _show_completed_view(self):
        """Vastaa pelin läpäisyä kuvaavaan näkymään siirtymisestä.
        """

        self._hide_current_view()

        self._current_view = CompletedView(
            self._root,
            self._show_main_menu_view,
            self._show_high_score_view,
            self._show_quit_view
        )

        self._current_view.pack()

    def _show_quit_view(self):
        """Vastaa sovelluksen sulkemista edeltävään näkymään siirtymisestä.
        """

        self._hide_current_view()

        self._current_view = QuitView(
            self._root,
            self._show_main_menu_view,
            self._quit_view_callback
        )

        self._current_view.pack()

    def _quit_view_callback(self):
        """Sulkee sovelluksen.
        """

        self._root.quit()
