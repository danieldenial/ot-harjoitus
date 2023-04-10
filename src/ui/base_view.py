
import tkinter
from tkinter import constants


class BaseView:
    w = 1000
    h = 400
    color = '#013369'

    def __init__(self, root):
        self._root = root
        self._frame = tkinter.Frame(
            self._root, bg=self.color,
            width=self.w, height=self.h
        )

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
