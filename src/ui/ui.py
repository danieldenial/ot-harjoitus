
from ui.utilities.base_frame import BaseFrame
from ui.views.intro_view import IntroView
from ui.views.main_menu_view import MainMenuView
from ui.views.new_game_view import NewGameView
from ui.views.gameplay_view import GameplayView
from ui.views.high_score_view import HighScoreView
from ui.views.rules_view import RulesView
from ui.views.quit_view import QuitView


class UI:
    """Luokka, jonka avulla siirrytään sovelluksen eri näkymien välillä.

    Attributes:
        _root: Tkinter-pääikkunan viite
        _question_service: Kysymysdatan käsittelyä hallinnoiva luokkaolio
        _score_service: Pisteiden käsittelyä hallinnoiva luokkaolio
        _current_view: Sovelluksen ikkunan ja käyttöliittymän senhetkinen näkymä
    """

    def __init__(self, root, service_instances):
        """Luokan konstruktori, joka luo eri näkymiä hallinnoivan luokkaolion.

        Args:
            root: Tkinter-pääikkunan viite
            context: Sanakirja, joka sisältää viitteet services-pakkauksen olioihin 
        """

        self._root = root
        self._question_service = service_instances['question_service']
        self._score_service = service_instances['score_service']
        self._pack_and_destroy = BaseFrame(self._root)
        self._current_view = None

    def start(self):
        """Käynnistää sovelluksen kutsumalla avausnäkymän luomisesta vastaavaa metodia.
        """

        self.show_intro_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän, jotta sovellus voi luoda uuden näkymän.
        """

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def show_intro_view(self):
        """Luo sovelluksen avausnäkymästä vastaavan luokkaolion.
        """

        self._hide_current_view()

        self._current_view = IntroView(
            self._root,
            self._score_service,
            self.show_main_menu_view
        )

        self._current_view.pack()

    def show_main_menu_view(self):
        """Luo päävalikon näkymästä vastaavan luokkaolion.
        """

        self._hide_current_view()

        views = {
            'show_new_game': self.show_new_game_view,
            'show_high_scores': self.show_high_score_view,
            'show_rules': self.show_rules_view,
            'show_quit': self.show_quit_view
        }

        self._current_view = MainMenuView(
            self._root,
            views
        )

        self._current_view.pack()

    def show_new_game_view(self):
        """Luo uutta peliä edeltävästä näkymästä vastaavan luokkaolion.
        """

        self._hide_current_view()

        views = {
            'show_gameplay_view': self.show_gameplay_view,
            'show_main_menu': self.show_main_menu_view
        }

        self._current_view = NewGameView(
            self._root,
            self._score_service,
            views
        )

        self._current_view.pack()

    def show_gameplay_view(self):
        """Luo varsinaisesta pelinkulun näkymästä vastaavan luokkaolion.
        """

        self._hide_current_view()

        views = {
            'show_main_menu': self.show_main_menu_view,
            'show_new_game_view': self.show_new_game_view,
            'show_quit_view': self.show_quit_view
        }

        self._current_view = GameplayView(
            self._root,
            self._question_service,
            self._score_service,
            views
        )

        self._current_view.pack()

    def show_high_score_view(self):
        """Luo parhaiden tulosten näkymästä vastaavan luokkaolion.
        """

        self._hide_current_view()

        self._current_view = HighScoreView(
            self._root,
            self._score_service,
            self.show_main_menu_view
        )

        self._current_view.pack()

    def show_rules_view(self):
        """Luo pelin säännöt näyttävästä näkymästä vastaavan luokkaolion.
        """

        self._hide_current_view()

        self._current_view = RulesView(
            self._root,
            self.show_main_menu_view
        )

        self._current_view.pack()

    def show_quit_view(self):
        """Luo sovelluksen sulkemista edeltävästä näkymästä vastaavan luokkaolion.
        """

        self._hide_current_view()

        self._current_view = QuitView(
            self._root,
            self.show_main_menu_view,
            self._quit_view_callback
        )

        self._current_view.pack()

    def _quit_view_callback(self):
        """Sulkee sovelluksen.
        """

        self._root.quit()
