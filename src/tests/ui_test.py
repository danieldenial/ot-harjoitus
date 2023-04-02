
import unittest
from unittest.mock import MagicMock
from tkinter import Tk
from index import UI
from ui.main_menu_view import MainMenuView

class TestButtons(unittest.TestCase):
    
    def setUp(self):
        self.window = Tk()
        self.ui = UI(self.window)
    
    def tearDown(self):
        self.window.destroy()

    def test_new_game_button(self):
        self.ui._show_new_game_view = MagicMock()
        self.ui.start()

        main_menu_view = self.ui._current_view

        if isinstance(main_menu_view, MainMenuView):
            main_menu_view.new_game_button.invoke()

        self.ui._show_new_game_view.assert_called_once()

    def test_rules_button(self):
        self.ui._show_rules_view = MagicMock()
        self.ui.start()

        main_menu_view = self.ui._current_view

        if isinstance(main_menu_view, MainMenuView):
            main_menu_view.rules_button.invoke()

        self.ui._show_rules_view.assert_called_once()

    def test_quit_button(self):
        self.ui._show_quit_view = MagicMock()
        self.ui.start()

        main_menu_view = self.ui._current_view

        if isinstance(main_menu_view, MainMenuView):
            main_menu_view.quit_button.invoke()

        self.ui._show_quit_view.assert_called_once()

if __name__ == "__main__":
    unittest.main()