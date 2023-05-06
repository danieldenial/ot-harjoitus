import tkinter
from tkinter import ttk
from ui.base_view import BaseView
from ui.button_styles import ButtonStyles

class IntroView(BaseView):

    def __init__(self, root, context, view_manager):
        super().__init__(root)
        self._view_manager = view_manager
        self._score_service = context['score_service']
        self._button_style = ButtonStyles()

        self._initialize()

    def _initialize(self):
        self._initialize_labels()
        self._initialize_buttons()
        self._initialize_team_selection_menu()
        self._adjust_elements()

    def _initialize_labels(self):
        welcome_text = tkinter.Label(
                    self._frame, text="Welcome to Grididon Genius!",
                    font=("Arial", 35), fg='white', bg="#013369"
                )
        
        team_question_text = tkinter.Label(
            self._frame, text="Which team would you like to represent today?",
            font=("Arial", 30), fg='white', bg="#013369"
        )

        welcome_text.grid(row=1, column=1)
        team_question_text.grid(row=3, column=1)

    def _initialize_buttons(self):
        self._button_style.configure_basic_style()

        main_menu_button = ttk.Button(
            self._frame, text="SELECT",
            padding=10, style='custom.basic.TButton',
            command=self._view_manager.go_to_main_menu_view
        )

        main_menu_button.grid(row=7, column=1)

    def _initialize_team_selection_menu(self):
        team_options = self._score_service.get_team_names()

        selected_team = tkinter.StringVar(self._frame)
        selected_team.set(team_options[0])

        self._score_service.change_selected_team(team_options[0])

        selected_team.trace("w", lambda *args: self._score_service.change_selected_team(selected_team.get()))

        dropdown_menu = tkinter.OptionMenu(self._frame, selected_team, *team_options)

        dropdown_menu.config(font=('Arial', 20))

        dropdown_menu.grid(row=5, column=1, padx=0, pady=50)

    def _adjust_elements(self):
        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(2, minsize=25)
        self._frame.grid_rowconfigure(4, minsize=25)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
