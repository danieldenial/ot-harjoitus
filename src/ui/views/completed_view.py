
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.widget_styles import WidgetStyles

class CompletedView(BaseFrame):
    """Pelin läpäisyä koskevasta ilmoituksesta vastaava näkymä.

    Args:
        BaseFrame:
            Luokka, joka luo kaikille näkymille pohjakehyksen.
    """

    def __init__(self, root, views):
        """Luokan konstruktori. Luo uuden pelin läpäisystä kertovan näkymän.

        Args:
            root:
                Tkinter-pääikkuna, jonka sisään näkymä luodaan.
            views:
                Sanakirja kutsuttavia arvoja, joilla siirrytään eri näkymiin
        """

        super().__init__(root)
        self._widget_creator = WidgetCreator(root)
        self._widget_styles = WidgetStyles(root)

    def _initialize(self):
        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels():
        pass

    def _initialize_buttons():
        pass
