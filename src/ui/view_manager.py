
class ViewManager:

    def __init__(self, ui):
        self._ui = ui

    def go_to_main_menu_view(self):
        self._ui.show_main_menu_view()

    def go_to_new_game_view(self):
        self._ui.show_new_game_view()

    def go_to_gameplay_view(self):
        self._ui.show_gameplay_view()

    def go_to_high_score_view(self):
        self._ui.show_high_score_view()

    def go_to_rules_view(self):
        self._ui.show_rules_view()

    def go_to_quit_view(self):
        self._ui.show_quit_view()
