
import tkinter
from tkinter import Tk
from tkinter import ttk


class WidgetCreator:

    def __init__(self, root: Tk):
        self._root = root
        self.window_width = round(root.winfo_screenwidth() * 0.7)
        self.window_height = round(root.winfo_screenheight() * 0.7)
        self.fg_color = 'white'
        self.bg_color = '#013369'

    def create_view_frame(self, _master):
        frame = tkinter.Frame(_master, bg=self.bg_color,
                              width=self.window_width,
                              height=self.window_height
                              )
        return frame

    def create_subframe(self, _master):
        subframe = tkinter.Frame(_master, bg=self.bg_color)

        return subframe

    def create_basic_label(self, frame, label_txt, font_scaler):
        font_size = self.set_relative_size(font_scaler)

        label = tkinter.Label(
            frame, text=label_txt, fg=self.fg_color, bg=self.bg_color,
            font=("Arial", font_size)
            )

        return label

    def create_longer_label(self, frame, label_txt, font_scaler):
        font_size = self.set_relative_size(font_scaler)


        label = tkinter.Label(
            frame, text=label_txt, fg=self.fg_color, bg=self.bg_color,
            font=("Arial", font_size),
            wraplength=round(self.window_width*0.95), anchor=tkinter.W, justify=tkinter.LEFT
            )

        return label

    def create_basic_button(self, _frame, _text, _command):
        padding_size = self.set_relative_size(100)

        button = ttk.Button(
            _frame, text=_text, 
            style='custom.basic.TButton',
            padding=padding_size,
            command=_command
            )

        return button

    def create_option_button(self, frame, _text, _command):
        padding_size = self.set_relative_size(100)
        button = ttk.Button(
            frame, text=_text, style='custom.option.TButton',
            padding=padding_size,
            command=_command
            )

        return button

    def create_dropdown_menu(self, frame, selected_team, *team_options):
        font_size = self.set_relative_size(70)

        dropdown_menu = tkinter.OptionMenu(
            frame, selected_team, *team_options
            )

        dropdown_menu.config(font=('Arial', font_size))

        return dropdown_menu

    def create_table(self, _frame, _columns, _headings, first_header):
        table = ttk.Treeview(_frame, columns=_columns)

        table.heading('#0', text=first_header)

        for col, head in zip(_columns, _headings):
            table.heading(col, text=head)

        return table
    
    def set_relative_size(self, font_scaler):
        dpi = self._root.winfo_fpixels('1i')
        dpi_scaling = dpi / 96

        return round((self.window_width / font_scaler) * dpi_scaling)
