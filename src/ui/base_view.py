
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

    width = 1080
    height = 720
    BACKGROUND_COLOR = '#013369'

    def __init__(self, root):
        """Luokan konstruktori, joka alustaa uuden perusnäkymän.

        Args:
            root: Luokan juuri-ikkuna
        """

        self._root = root
        self._frame = tkinter.Frame(
            self._root, bg=self.BACKGROUND_COLOR,
            width=self.width, height=self.height
        )

    def pack(self):
        """Asettaa luokan kehyksen ikkunaan.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa luokan kehyksen ikkunasta.
        """

        self._frame.destroy()
