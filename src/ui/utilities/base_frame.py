
from tkinter import Tk
from tkinter import constants
from ui.utilities.widget_creator import WidgetCreator


class BaseFrame:
    """Luokka, jonka avulla luodaan pohjakehys sovelluksen muita näkymiä varten.
    """

    def __init__(self, root: Tk):
        """Luokan konstruktori, joka alustaa uuden perusnäkymän.

        Args:
            root: Luokan juuri-ikkuna
        """

        self._widget_creator = WidgetCreator(root)
        self._frame = self._widget_creator.create_view_frame(root)

    def pack(self):
        """Asettaa luokan kehyksen ikkunaan.
        """

        self._frame.pack(fill=constants.BOTH)

    def destroy(self):
        """Poistaa luokan kehyksen ikkunasta.
        """

        self._frame.destroy()
