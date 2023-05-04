from tkinter import ttk


class ButtonStyles:
    def __init__(self):
        self._style = ttk.Style()
        self._style.theme_use('default')

    def configure_basic_style(self):
        self._style.configure(
            'custom.basic.TButton', font=('Verdana', 20),
            padding=(10,10), background='#8a9095', foreground='black'
        )

    def configure_option_style(self):
        self._style.configure(
            'custom.option.TButton', font=('Verdana', 20),
            background='#8a9095', foreground='black',
            height=10, width=3
        )

    def configure_right_answer_style(self):
        self._style.configure(
            'custom.green.TButton', font=('Verdana', 20),
            background='#3B9B00', foreground='black',
            height=10, width=3
        )

        self._map_right_answer_style()

    def configure_wrong_answer_style(self):
        self._style.configure(
            'custom.red.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black',
            height=10, width=3
        )

        self._map_wrong_answer_style()

    def _map_right_answer_style(self):
        self._style.map(
            'custom.green.TButton',
            background=[('active', '#3B9B00')],
            foreground=[('active', 'black')],
        )

    def _map_wrong_answer_style(self):
        self._style.map(
            'custom.red.TButton',
            background=[('active', '#d50a0a')],
            foreground=[('active', 'black')]
        )
