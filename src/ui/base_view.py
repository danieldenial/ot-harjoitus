
import tkinter
from tkinter import Tk
from tkinter import constants


class BaseView:
    """Luokka, jonka avulla luodaan pohjakehys sovelluksen muita näkymiä varten.
    """

    BACKGROUND_COLOR = '#013369'

    def __init__(self, root: Tk):
        """Luokan konstruktori, joka alustaa uuden perusnäkymän.

        Args:
            root: Luokan juuri-ikkuna
        """

        self._root = root
        self.window_width = round(root.winfo_screenwidth() * 0.7)
        self.window_height = round(root.winfo_screenheight() * 0.7)
        self._frame = tkinter.Frame(
            self._root, bg=self.BACKGROUND_COLOR,
            width=self.window_width, height=self.window_height
        )

    def pack(self):
        """Asettaa luokan kehyksen ikkunaan.
        """

        self._frame.pack(fill=constants.BOTH)

    def destroy(self):
        """Poistaa luokan kehyksen ikkunasta.
        """

        self._frame.destroy()
