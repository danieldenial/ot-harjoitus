
import tkinter
from tkinter import Tk
from tkinter import ttk
from services.score_service import ScoreService
from config import FOREGROUND_COLOR, BACKGROUND_COLOR


class WidgetCreator:
    """Näkymien komponenttien luomisesta vastaava luokka.
    """

    def __init__(self, root: Tk):
        """Luokan konstruktori. Asettaa oletusarvot.

        Args:
            root:
                Tkinter-pääikkuna.

        Attributes:
            window_width = Käyttäjän koneen ruutuun suhteutettu leveys
            window_height = Käyttäjän koneen ruutuun suhteutettu korkeus
            fg_color = Luotavien komponenttien teksteille annettava väri
            bg_color = Luotaville komponenttien annettava taustaväri
        """

        self._root = root
        self.window_width = round(root.winfo_screenwidth() * 0.7)
        self.window_height = round(root.winfo_screenheight() * 0.7)
        self.fg_color = FOREGROUND_COLOR
        self.bg_color = BACKGROUND_COLOR

    def create_base_frame(self, master):
        """Luo BaseFrame-luokalle kehyksen, jonka sisään tulee näkymien komponentit.

        Args:
            master: Komponentti, jonka sisään kehys luodaan ja sijoitetaan.

        Returns:
            Luotu kehys
        """

        frame = tkinter.Frame(master, bg=self.bg_color,
                              width=self.window_width,
                              height=self.window_height
                              )
        return frame

    def create_subframe(self, master):
        """Luo näkymän pohjakehyksen sisälle kehyksen.

        Args:
            master: Komponentti, jonka sisään kehys luodaan ja sijoitetaan.

        Returns:
            Luotu kehys.
        """

        subframe = tkinter.Frame(master, bg=self.bg_color)

        return subframe

    def create_basic_label(self, master, label_txt, font_scaler):
        """Luo uuden (sovelluksen kontekstissa) perusversion Label-komponentista.

        Args:
            frame: Komponentti, jonka sisään Label luodaan ja sijoitetaan.
            label_txt: Labelin tekstiksi asetettava merkkijono.
            font_scaler: Kokonaisluku, jota käytetään fontin koon määrittelyyn.

        Returns:
            Luotu Label-komponentti. 
        """

        font_size = self.set_relative_size(font_scaler)

        basic_label = tkinter.Label(
            master, text=label_txt, fg=self.fg_color, bg=self.bg_color,
            font=("Arial", font_size)
            )

        return basic_label

    def create_extended_label(self, master, label_txt, font_scaler):
        """Luo uuden (sovelluksen kontekstissa) kattavamman Label-komponentin.

        Args:
            frame: Komponentti, jonka sisään Label luodaan ja sijoitetaan.
            label_txt: Labelin tekstiksi asetettava merkkijono.
            font_scaler: Kokonaisluku, jota käytetään fontin koon määrittelyyn.

        Returns:
            Luotu Label-komponentti.
        """

        font_size = self.set_relative_size(font_scaler)


        extended_label = tkinter.Label(
            master, text=label_txt, fg=self.fg_color, bg=self.bg_color,
            font=("Arial", font_size),
            wraplength=round(self.window_width*0.95), anchor=tkinter.W, justify=tkinter.LEFT
            )

        return extended_label

    def create_basic_button(self, master, text, command):
        """Luo uuden (sovelluksen kontekstissa) peruspainikkeen.

        Args:
            master: Komponentti, jonka sisään painike luodaan ja sijoitetaan.
            text: Painikkeen tekstiksi asetettava merkkijono.
            command: Painikkeen klikkaukselle asetettava komento.

        Returns:
            Luotu peruspainike.
        """

        padding_size = self.set_relative_size(100)

        basic_button = ttk.Button(
            master, text=text, 
            style='custom.basic.TButton',
            padding=padding_size,
            command=command
            )

        return basic_button

    def create_option_button(self, master, text, command):
        """Luo uuden pelin vastausvaihtoehdoille tarkoitetun painikkeen.
t
        Args:
            master: Komponentti, jonka sisään painike luodaan ja sijoitetaan.
            text: Painikkeen tekstiksi asetettava merkkijono.
            command: Painikkeen klikkaukselle asetettava komento.

        Returns:
            Luotu painike.
        """

        padding_size = self.set_relative_size(100)
        
        option_button = ttk.Button(
            master, text=text, style='custom.option.TButton',
            padding=padding_size,
            command=command
            )

        return option_button

    def create_team_selection_menu(self, master, selection, score_service: ScoreService):
        """Luo uuden OptionMenu-valikon.

        Args:
            master: Komponentti, jonka sisään valikko luodaan ja sijoitetaan.
            selection: Merkkijono, jonka perusteella asetetaan valikon oletusvalinta.
            score_service: Pisteytyksen sovelluslogiikasta vastaava luokkaolio. 

        Returns:
            Luotu OptionMenu-valikko.
        """

        team_options = score_service.get_team_names()

        selected_team = tkinter.StringVar(master)

        selected_team.set(selection)

        selected_team.trace(
            "w", lambda *args: score_service.change_selected_team(selected_team.get()))

        dropdown_menu = tkinter.OptionMenu(
            master, selected_team, *team_options
            )

        return dropdown_menu

    def create_high_score_table(self, master, columns, headings, first_header):
        """Luo uuden Treeview-taulukon parhaiden pistesuoritusten näyttämistä varten.

        Args:
            master: Komponentti, jonka sisään taulukko luodaan ja sijoitetaan.
            columns: Lista merkkijonoja, joka asetetaan taulukon kolumnien tunnisteiksi.
            headings: Lista merkkijonoja, jotka asetetaan taulukon kolumnien otsikoiksi.
            first_header: Merkkijono, joka asetetaan ensimmäisen kolumnin otsikoksi.

        Returns:
            Luotu Treeview-taulukko.
        """

        table = ttk.Treeview(master, columns=columns)

        table.heading('#0', text=first_header)

        for col, head in zip(columns, headings):
            table.heading(col, text=head)

        return table

    def set_relative_size(self, scaler):
        """Laskee käyttäjän koneen näytön pikseleihin ja leveyteen suhteutetun koon.

        Metodia käytetään määrittelemään sopiva ja skaalautuva koko sovelluksen 
        käyttöliittymän fonteille sekä painikkeille.

        Args:
            scaler: Kokonaisluku, jota käytetään suhteellisen koon laskemisessa.

        Returns:
            Kokonaisluvuksi pyöristetty suhteellinen koko.
        """

        dpi = self._root.winfo_fpixels('1i')
        dpi_scaling = dpi / 96

        return round((self.window_width / scaler) * dpi_scaling)
