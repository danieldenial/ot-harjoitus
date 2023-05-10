
from tkinter import ttk
from ui.widget_creator import WidgetCreator


class ButtonStyles(WidgetCreator):
    """Luokka, jonka avulla konfiguroidaan sovelluksen painikkeille eri tyylejä.

    Attributes:
        _style: ttk-moduulin objekti, jota konfiguroidaan
    """

    def __init__(self, root):
        """Luo konfiguroitavan ttk-moduulin objektin ja asettaa sille oletusteeman.
        """

        super().__init__(root)
        self._style = ttk.Style()
        self._style.theme_use('default')

    def configure_basic_style(self):
        """Konfiguroi sovelluksen peruspainikkeiden tyylin.
        """

        self._style.configure(
            'custom.basic.TButton', 
            font=('Verdana', round((self.window_height*0.03))),
            background='#8a9095', foreground='black'
        )

    def configure_option_style(self):
        self._style.configure(
            'custom.option.TButton', 
            font=('Verdana', round((self.window_height*0.03))),
            background='#8a9095', foreground='black',
            height=round(self.window_height*0.02), width=round(self.window_height*0.005)
        )

    def configure_right_answer_style(self):
        """Konfiguroi oikein menneen vastauksen painikkeen tyylin (väri vihreäksi).
        """
        self._style.configure(
            'custom.green.TButton', 
            font=('Verdana', round((self.window_height*0.03))),
            background='#3B9B00', foreground='black',
            height=round(self.window_height*0.02), width=round(self.window_height*0.005)
        )

        self._map_right_answer_style()

    def configure_wrong_answer_style(self):
        """Konfiguroi väärin menneen vastauksen painikkeen tyylin (väri punaiseksi).
        """

        self._style.configure(
            'custom.red.TButton', 
            font=('Verdana', round((self.window_height*0.03))),
            background='#d50a0a', foreground='black',
            height=round(self.window_height*0.02), width=round(self.window_height*0.005)
        )

        self._map_wrong_answer_style()

    def _map_right_answer_style(self):
        """Muuttaa jo painetun (nyt vihreän) napin asetuksia,
        jotta se ei enää reagoi käyttäjän uusiin painalluksiin tai hiiren liikkeeseen.
        """
        self._style.map(
            'custom.green.TButton',
            background=[('pressed', '#3B9B00')]
        )

    def _map_wrong_answer_style(self):
        """Muuttaa jo painetun (nyt punaisen) napin asetuksia,
        jotta se ei enää reagoi käyttäjän uusiin painalluksiin tai hiiren liikkeeseen.
        """

        self._style.map(
            'custom.red.TButton',
            background=[('pressed', '#d50a0a')]
        )
