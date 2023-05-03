from tkinter import ttk


class ButtonStyles:
    def __init__(self):
        self._style = ttk.Style()

    def configure_styles(self):
        self._style.theme_use('default')

        self._style.configure(
            'custom.option.TButton', font=('Verdana', 20),
            background='#8a9095', foreground='black',
            height=10, width=3
        )

        self._style.configure(
            'custom.green.TButton', font=('Verdana', 20),
            background='#3B9B00', foreground='black',
            height=10, width=3
        )

        self._style.configure(
            'custom.red.TButton', font=('Verdana', 20),
            background='#d50a0a', foreground='black',
            height=10, width=3
        )

        self._style.configure(
            'custom.continue.TButton', font=('Verdana', 20),
            background='#8a9095', foreground='black',
        )

        self._style.configure(
            'custom.end.TButton', font=('Verdana', 20),
            background='#8a9095', foreground='black',
        )

        self._map_styles()

    def _map_styles(self):
        self._style.map(
            'custom.green.TButton',
            background=[('active', '#3B9B00')],
            foreground=[('active', 'black')],
        )

        self._style.map(
            'custom.red.TButton',
            background=[('active', '#d50a0a')],
            foreground=[('active', 'black')]
        )
