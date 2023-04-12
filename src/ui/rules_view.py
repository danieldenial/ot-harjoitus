
import tkinter
from tkinter import ttk
from ui.base_view import BaseView


class RulesView(BaseView):
    def __init__(self, root, main_menu_view):
        super().__init__(root)
        self._main_menu_view = main_menu_view

        self._initialize()

    def _initialize(self):
        self._initialize_labels()
        self._initialize_buttons()
        self._initialize_grid()

    def _initialize_labels(self):
        rules_text = tkinter.Label(
            self._frame, text="The rules will be added later.",
            font=("Arial", 35), fg='white', bg="#013369"
        )

        rules_text.grid(row=1, column=1)

    def _initialize_buttons(self):
        style = ttk.Style()

        style.theme_use('default')
        style.configure(
            'custom.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black'
        )

        back_button = ttk.Button(
            self._frame, text="BACK",
            padding=5, style='custom.TButton',
            command=self._main_menu_view
        )

        back_button.grid(row=3, column=1)

    def _initialize_grid(self):
        self._frame.grid_rowconfigure(0, minsize=100)
        self._frame.grid_rowconfigure(2, minsize=100)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
