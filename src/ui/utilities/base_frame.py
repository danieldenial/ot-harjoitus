
from tkinter import Tk
from tkinter import constants
from ui.utilities.widget_creator import WidgetCreator


class BaseFrame:
    """Näkymien pohjakehysten asettamisesta/poistamisesta vastaava luokka.
    """

    def __init__(self, root: Tk):
        """Luokan konstruktori. Luo uuden kehyksen.

        Args:
            root:
                Tkinter-pääikkuna, jonka sisään uusi kehys asetetaan.
        """

        self._widget_creator = WidgetCreator(root)
        self._frame = self._widget_creator.create_base_frame(root)

    def pack(self):
        """Asettaa kehyksen Tkinter-pääikkunaan.
        """

        self._frame.pack(fill=constants.BOTH)

    def destroy(self):
        """Poistaa kehyksen Tkinter-pääikkunasta.
        """

        self._frame.destroy()
