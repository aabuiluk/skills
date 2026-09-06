# Teacher KB · Python AI Materials

Канон: **`teacher_kb.sqlite`** у корені `lesson_helper` (gitignored). Ця папка — JSON-дзеркало для grep.

Як питати: див. [../kb.md](../kb.md) і `query_teacher_kb.py`.

| Що | Де | У контекст агента |
|----|----|-------------------|
| Дистилят / задачі / FTS | `teacher_kb.sqlite` | лише зріз `--note` / `--sheet` / FTS |
| Умови ITSTEP (дзеркало) | `assignments/*.json` | так, один аркуш |
| Індекс | `index.json` | коротко |
| Книжки (повний текст) | `data/kb_extracts/books/*.txt` | ні |
| Статті | `sources.json`, `articles_fetch.json` | дистилят або URL |

Не підвантажуй extracts цілком. На слайд не винось id нотаток.
