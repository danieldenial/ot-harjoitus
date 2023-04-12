
from ui.main_menu_view import MainMenuView
from ui.new_game_view import NewGameView
from ui.quit_view import QuitView
from ui.rules_view import RulesView
from ui.gameplay_view import GameplayView
from ui.game_end_view import GameEndView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_menu_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self.current_view = None

    def _show_main_menu_view(self):
        self._hide_current_view()

        self._current_view = MainMenuView(
            self._root,
            self._show_new_game_view,
            self._show_quit_view,
            self._show_rules_view
        )

        self._current_view.pack()

    def _show_new_game_view(self):
        self._hide_current_view()

        self._current_view = NewGameView(
            self._root,
            self._show_main_menu_view, 
            self._show_gameplay_view
        )

        self._current_view.pack()

    def _show_gameplay_view(self):
        self._hide_current_view()

        self._current_view = GameplayView(
            self._root,
            self._show_game_end_view
        )

        self._current_view.pack()

    def _show_game_end_view(self):
        self._hide_current_view()

        self._current_view = GameEndView(
            self._root,
            self._show_main_menu_view
        )

        self._current_view.pack()
        
    def _show_rules_view(self):
        self._hide_current_view()

        self._current_view = RulesView(
            self._root,
            self._show_main_menu_view
        )

        self._current_view.pack()

    def _show_quit_view(self):
        self._hide_current_view()

        self._current_view = QuitView(
            self._root, self._quit_game,
            self._show_main_menu_view
        )

        self._current_view.pack()

    def _quit_game(self):
        self._root.quit()
