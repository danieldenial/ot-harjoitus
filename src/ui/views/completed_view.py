
from ui.utilities.base_frame import BaseFrame
from ui.utilities.widget_creator import WidgetCreator
from ui.utilities.widget_styles import WidgetStyles
from services.question_service import QuestionService

class CompletedView(BaseFrame):
    """Pelin läpäisyä koskevasta ilmoituksesta vastaava näkymä.

    Args:
        BaseFrame:
            Luokka, joka luo kaikille näkymille pohjakehyksen.
    """

    def __init__(self, root, question_service: QuestionService, show_high_scores):
        """Luokan konstruktori. Luo uuden pelin läpäisystä kertovan näkymän.

        Args:
            root:
                Tkinter-pääikkuna, jonka sisään näkymä luodaan.
            question_service:
                Kysymyksiin liittyvästä sovelluslogiikasta vastaava luokkaolio
            show_high_scores:
                Kutsuttava arvo, jolla siirrytään parhaiden pisteiden näkymään
        """

        super().__init__(root)
        self._question_service = question_service
        self._handle_show_high_scores = show_high_scores
        self._widget_creator = WidgetCreator(root)
        self._widget_styles = WidgetStyles(root)

    def _initialize(self):
        self._initialize_labels()
        self._initialize_buttons()

    def _initialize_labels(self):
        font_scaler = 30

        count = self._question_service.get_number_of_questions()

        no_more_questions_text = "That's all she wrote! There are no more questions left."
        question_number_text = f"You gave {count} correct answers. Pretty impressive!"
        go_see_scores_text = "Go see your score at the top of the table."

        no_more_questions_label = self._widget_creator.create_basic_label(
            self._frame, no_more_questions_text, font_scaler
        )

        question_number_label = self._widget_creator.create_basic_label(
            self._frame, question_number_text, font_scaler
        )

        go_see_scores_label = self._widget_creator.create_basic_label(
            self._frame, go_see_scores_text, font_scaler
        )

        no_more_questions_label.place(relx=0.5, rely=0.35, anchor='center')
        question_number_label.place(relx=0.5, rely=0.45, anchor='center')
        go_see_scores_label.place(relx=0.5, rely=0.55, anchor='center')

    def _initialize_buttons(self):
        self._widget_styles.config_basic_button()

        high_scores_button = self._widget_creator.create_basic_button(
            self._frame, "SCORES", self._handle_show_high_scores
            )

        high_scores_button.place(relx=0.5, rely=0.65, anchor='center')
