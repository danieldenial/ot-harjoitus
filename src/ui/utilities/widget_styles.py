
from tkinter import ttk
from ui.utilities.widget_creator import WidgetCreator


class WidgetStyles(WidgetCreator):
    """Näkymien komponenttien tyylien konfiguroimisesta vastaava luokka.

    Args:
        WidgetCreator: Näkymien komponenttien luomisesta vastaava luokkaolio.
    """

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden tyyliolion ja asettaa sille oletusteeman.
        """

        super().__init__(root)
        self._style = ttk.Style()
        self._style.theme_use('default')

    def config_basic_button(self):
        """Konfiguroi sovelluksen peruspainikkeiden tyylin.
        """

        self._style.configure(
            'custom.basic.TButton', 
            font=('Verdana', round((self.window_height*0.03))),
            background='#8a9095', foreground='black'
        )

    def config_option_button(self):
        """Konfiguroi pelin vastausvaihtoehtopainikkeiden tyylin.
        """

        self._style.configure(
            'custom.option.TButton', 
            font=('Verdana', round((self.window_height*0.03))),
            background='#8a9095', foreground='black',
            height=round(self.window_height*0.02), width=round(self.window_height*0.005)
        )

    def config_right_answer_button(self):
        """Konfiguroi oikein menneen vastauksen painikkeen tyylin (väri vihreäksi).
        """

        style = 'custom.green.TButton'
        bg_color = '#3B9B00'

        self._style.configure(
            style, font=('Verdana', round((self.window_height*0.03))),
            background=bg_color, foreground='black',
            height=round(self.window_height*0.02),
            width=round(self.window_height*0.005)
        )

        self._map_answer_button(style, bg_color)

    def configure_wrong_answer_button(self):
        """Konfiguroi väärin menneen vastauksen painikkeen tyylin (väri punaiseksi).
        """

        style = 'custom.red.TButton'
        bg_color = '#d50a0a'

        self._style.configure(
            style, font=('Verdana', round((self.window_height*0.03))),
            background=bg_color, foreground='black',
            height=round(self.window_height*0.02), 
            width=round(self.window_height*0.005)
        )

        self._map_answer_button(style, bg_color)

    def _map_answer_button(self, selected_style, bg_color):
        self._style.map(
            selected_style,
            background=[('pressed', bg_color)]
        )

    def config_table(self):
        """Konfiguroi Treeview-taulukon fontin tyyliä.
        """

        font_size = self.set_relative_size(50)
        self._style.configure('Treeview', font=('Verdana', font_size))
