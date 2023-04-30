
from ui.main_menu_view import MainMenuView
from ui.new_game_view import NewGameView
from ui.quit_view import QuitView
from ui.rules_view import RulesView
from ui.gameplay_view import GameplayView


class UI:
    """Luokka, jonka avulla hallinnoidaan sovelluksen käyttöliittymän eri näkymiä.

    Attributes:
        _root: Luokan juuri-ikkuna
        _current_view: Sovelluksen ikkunan ja käyttöliittymän senhetkinen näkymä
    """

    def __init__(self, root):
        """Luokan konstruktori, joka alustaa uuden käyttöliittymän näkymän.

        Args:
            root: Luokan juuri-ikkuna
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää sovelluksen kutsumalla sen luomisesta vastaavaa metodia.
        """

        self._show_main_menu_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän, jotta sovellus voi luoda uuden näkymän.
        """

        if self._current_view:
            self._current_view.destroy()

        self.current_view = None

    def _show_main_menu_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia ja luo sitten päävalikon näkymän.
        """

        self._hide_current_view()

        self._current_view = MainMenuView(
            self._root,
            self._show_new_game_view,
            self._show_quit_view,
            self._show_rules_view
        )

        self._current_view.pack()

    def _show_new_game_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia ja luo sitten uutta peliä edeltävän näkymän.
        """

        self._hide_current_view()

        self._current_view = NewGameView(
            self._root,
            self._show_main_menu_view,
            self._show_gameplay_view
        )

        self._current_view.pack()

    def _show_gameplay_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia ja luo sitten itse pelinkulusta vastaavan näkymän.
        """

        self._hide_current_view()

        self._current_view = GameplayView(
            self._root,
            self._show_main_menu_view,
            self._show_new_game_view,
            self._show_quit_view
        )

        self._current_view.pack()

    def _show_rules_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia ja luo sitten pelin säännöt sisältävän näkymän.
        """

        self._hide_current_view()

        self._current_view = RulesView(
            self._root,
            self._show_main_menu_view
        )

        self._current_view.pack()

    def _show_quit_view(self):
        """Kutsuu nykyisen näkymän piilottamisesta vastaavaa metodia ja luo sitten sovelluksen sulkemista edeltävän näkymän. 
        """

        self._hide_current_view()

        self._current_view = QuitView(
            self._root, self._quit_game,
            self._show_main_menu_view
        )

        self._current_view.pack()

    def _quit_game(self):
        """Sulkee sovelluksen.
        """

        self._root.quit()
