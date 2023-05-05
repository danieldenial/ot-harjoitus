
import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles
from services.score_service import ScoreService

class HighScoreView(BaseView):

    def __init__(self, root, context, view_manager):
        super().__init__(root)
        self._view_manager = view_manager
        self._score_repo = context['score_repo']
        self._score_service = ScoreService(self._score_repo)
        self._button_style = ButtonStyles()

        self._initialize()

    def _initialize(self):
        self._initialize_labels()
        self._initialize_buttons()
        self._adjust_elements()

    def _initialize_labels(self):
        intro_text = tkinter.Label(
            self._frame,
            text="These are the high scores – so far.",
            font=("Arial", 25), fg='white', bg="#013369",
            padx=10, pady=10
        )

    def _initialize_buttons(self):
        pass

    def _adjust_elements(self):
        pass