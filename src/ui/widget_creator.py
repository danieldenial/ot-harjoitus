
import tkinter
from tkinter import Tk
from tkinter import constants


class WidgetCreator:

    def __init__(self, root: Tk):
        self._root = root
        self.window_width = round(root.winfo_screenwidth() * 0.7)
        self.window_height = round(root.winfo_screenheight() * 0.7)
        
    def create_frame(self):
        pass

    def create_basic_label(self, frame, label_txt, font_size):
        label = tkinter.Label(
            frame, text=label_txt, fg='white', bg='#013369',
            font=("Arial", round((self.window_height*font_size))),
            )
        
        return label

    def create_special_label(self, frame, label_txt, font_size):
        label = tkinter.Label(
            master=frame, text=label_txt, fg='white', bg='#013369',
            font=("Arial", round((self.window_height*font_size))),
            wraplength=(self.window_width*0.95), anchor=tkinter.W, justify=tkinter.LEFT
        )

        return label

    def create_button(self):
        pass

    def create_option_menu(self, frame, selected_team, *team_options):
        dropdown_menu = tkinter.OptionMenu(
            frame, selected_team, *team_options
        )

        return dropdown_menu
