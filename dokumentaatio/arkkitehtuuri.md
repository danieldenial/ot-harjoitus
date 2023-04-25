# Arkkitehtuurikuvaus

## Rakenne

Ohjelman koodin pakkausrakenne on seuraavanlainen:

![Pakkausrakenne](./kuvat/pakkausrakenne.png)

Käyttöliittymästä vastaava koodi sijaitsee pakkauksessa _ui_.

Sovelluslogiikasta vastaava koodi sijaitsee pakkauksessa _services_.

Tietojen pysyväistalletuksesta vastaava koodi sijaitsee pakkauksessa _repositories_.

## Päätoiminnallisuudet

### Uuden pelin aloittaminen

```mermaid
sequenceDiagram
    participant User
    participant UI
    participant QuestionService
    participant ScoreService
    User->>UI: click "START GAME" button
    UI->>QuestionService: next_question()
    UI->>QuestionService: get_question()
    UI->>QuestionService: get_options()
    UI->>ScoreService: get_current_score()
```
