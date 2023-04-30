
import tkinter
from tkinter import constants


class BaseView:
    """Sovelluksen perusnäkymä, jonka kaikki käyttöliittymän näkymistä vastaavat luokat perivät.

    Attributes:
        w: Sovelluksen ikkunan oletusleveys
        h: Sovelluksen ikkunan oletuskorkeus
        color: Sovelluksen ikkunan oletustaustaväri
        _root: Luokan juuri-ikkuna
        _frame: Luokan luoman näkymän kehys
    """

    w = 1000
    h = 600
    color = '#013369'

    def __init__(self, root):
        """Luokan konstruktori, joka alustaa uuden perusnäkymän.

        Args:
            root: Luokan juuri-ikkuna
        """

        self._root = root
        self._frame = tkinter.Frame(
            self._root, bg=self.color,
            width=self.w, height=self.h
        )

    def pack(self):
        """Asettaa luokan kehyksen ikkunaan.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa luokan kehyksen ikkunasta.
        """

        self._frame.destroy()
