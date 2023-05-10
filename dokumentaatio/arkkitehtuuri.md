# Arkkitehtuurikuvaus

## Rakenne

Ohjelman koodin pakkausrakenne on seuraavanlainen:

![Pakkausrakenne](./kuvat/pakkausrakenne.png)

Käyttöliittymästä vastaava koodi sijaitsee pakkauksessa _ui_.

Sovelluslogiikasta vastaava koodi sijaitsee pakkauksessa _services_.

Tietojen pysyväistalletuksesta vastaava koodi sijaitsee pakkauksessa _repositories_.

## Käyttöliittymä

Käyttöliittymä sisältää seitsemän erilaista näkymää:

- Aloitus
- Päävalikko
- Uusi peli
- Pelinkulku
- Parhaat tulokset
- Säännöt
- Lopetus

Näistä näkymistä pelinkulku on dynaaminen näkymä, jonka sisältö vaihtuu kysymysten mukana.

Kaikki näkymät on toteutettu omana luokkanaan ja niistä vain yksi näkyy kerrallaan. Ulkoasun 
yhtenäistämiseksi ja koodin toiston välttämiseksi kaikki yllä olevat näkymäluokat perivat 
luokan _BaseView_, jonka luoman pohjakehyksen päälle näkymät rakentuvat. Näkymien 
näyttämisestä ja hallinnoinnista vastaa luokka _UI_. Käyttöliittymä on pyritty eristämään 
sovelluslogiikasta, josta vastaa puolestaan sovelluksen _services_-luokat.

## Sovelluslogiikka

Sovelluslogiikasta vastaavat luokat _QuestionService_ ja _ScoreService_.

_QuestionService_-luokka tarjoaa käyttöliittymän pelinkulkunäkymästä vastaavalle 
_GameplayView_-luokalle erinäisiä pelin kysymysaineistoon liittyviä metodeja, joita ovat 
esimerkiksi:

- `set_next_question_index`
- `get_question()`
- `get_options()`
- `get_detail_text()`
- `evaluate_user_answer(user_answer)`

Näitä metodeja hyödyntämällä käyttöliittymän luokka saa tarvittavat pelin kysymyksiin 
liittyvät tiedot esitettäviksi, voi tarkistaa käyttäjän antaman vastauksen 
oikeellisuuden, ja pystyy siirtymään seuraavaan kysymykseen.

_ScoreService_ on toinen sovelluslogiikasta vastaavista luokista. Se tarjoaa käyttöliittymän eri 
luokille muun muassa seuraavia metodeja:

- `get_current_score()`
- `reset_current_score()`
- `get_high_score()`
- `get_high_scores_list()`
- `get_selected_team()`
- `change_selected_team(new_team)`
- `increase_score()`
- `check_score()`
- `store_high_scores()`

Metodit tarjoavat käyttöliittymälle tietoa sekä sillä hetkellä käynnissä olevan pelin tuloksesta 
että parhaasta kokonaisuutena siihen asti saavutetusta tuloksesta. Parhaan tuloksen varsinaisesta
tallentamisesta vastaa kuitenkin pakkauksen _repositories_ luokka _HighScoreRepository_.

## Tietojen hallinnointi ja tallennus

Pakkauksen _repositories_ luokat _QuestionRepository_ ja _HighScoreRepository_ 
vastaavat kysymysaineiston tuomisesta peliin sekä tulosten tallettamisesta. 

_QuestionRepository_-luokka lataa sovelluksen käynnistyessä pelin kysymysaineiston (eli 
kysymykset, vastausvaihtoehdot, oikeat vastaukset ja kysymyksiin liittyvät lisätiedot) sovellukseen 
lukemalla csv-tiedostoa. Kysymysaineisto talletetaan sovelluksessa listana sanakirjoja.

_HighScoreRepository_-luokka tallettaa 10 parasta pelistä saavutettua tulosta csv-tiedostoon. Mikäli 
tiedostoa ei löydy, luo luokka sen automaattisesti sovelluksen käynnistymisen yhteydessä.

## Päätoiminnallisuudet

### Pelinkulun alku

```mermaid
sequenceDiagram
    participant GameplayView
    participant QuestionService
    participant ScoreService
    GameplayView->>GameplayView: initialize()
    GameplayView->>GameplayView: set_up_new_game()
    GameplayView->>QuestionService: reset_index_list()
    GameplayView->>ScoreService: reset_current_score()
    GameplayView->>GameplayView: initialize_subframes()
    GameplayView->>GameplayView: initialize_question_view()
    GameplayView->>QuestionService: set_next_question_index()
    GameplayView->>GameplayView: initialize_labels()
    GameplayView->>QuestionService: get_questions()
    QuestionService->>GameplayView: question
    GameplayView->>QuestionService: get_options()
    QuestionService->>GameplayView: options_list
    GameplayView->>GameplayView: initialize_buttons()
    GameplayView->>ScoreService: get_current_score_text()
    ScoreService->>GameplayView: f"Score: {current_score}"
```

### Käyttäjä vastaa oikein

```mermaid
sequenceDiagram
    participant User
    participant GameplayView
    participant QuestionService
    participant ScoreService
    User->>GameplayView: click button "A"
    GameplayView->>GameplayView: handle_user_answer("A", "John Madden")
    GameplayView->>GameplayView: disable_buttons()
    GameplayView->>QuestionService: evaluate_user_answer("John Madden")
    QuestionService->>GameplayView: True
    GameplayView->>GameplayView: change_button_green("A")
    GameplayView->>ScoreService: increase_score()
    GameplayView->>ScoreService: get_current_score_text()
    ScoreService->>GameplayView: f"Score: {current_score}"
    GameplayView->>GameplayView: add_right_answer_widgets()
    Gameplayview->>QuestionService: get_detail_text()
    QuestionService->>GameplayView: detail_text
    User->>GameplayView: click "CONTINUE"
    GameplayView->>GameplayView: update_view()

```

## Käyttäjä vastaa väärin

```mermaid
sequenceDiagram
    participant User
    participant GameplayView
    participant QuestionService
    participant ScoreService
    User->>GameplayView: click button "B"
    GameplayView->>GameplayView: handle_user_answer("B", "Tom Brady")
    GameplayView->>GameplayView: disable_buttons()
    GameplayView->>QuestionService: evaluate_user_answer("Tom Brady")
    QuestionService->>GameplayView: False
    GameplayView->>GameplayView: change_button_red("B")
    GameplayView->>ScoreService: check_score()
    GameplayView->>GameplayView: add_wrong_answer_widgets(False)
```
