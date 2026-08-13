# База джерел

Канон: **`teacher_kb.sqlite`** у корені `lesson_helper` (gitignored). Не видаляй.

Повні extracts книжок/HTML у контекст агента **не клади**. ZIP з LMS — не стартери.

JSON-дзеркало (швидкий grep, не джерело істини):

`lesson_helper/.agents/skills/teaching/teacher-materials-skill/kb/`

Перебудова (старий sqlite не чіпає, поки новий не готовий):

```bash
python3 backend/data/courses/python_ai_materials/tools/build_teacher_kb.py
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --info
```

## Запити (спочатку вузький зріз)

```bash
# дистилят теми
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --note numpy
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --note   # список id

# офіційний аркуш ITSTEP (задачі 1–N, не X.1)
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --sheet practical_2.1

# FTS: книжки / статті / відео-SRT / related docs — короткий snippet
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py "reshape broadcasting"
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py "pipeline leakage" -n 5
```

Порядок: `--note` → `--sheet` → FTS лише якщо не вистачає цитати.

На слайд винось формулювання для студента + публічне джерело (документація, підручник, OECD). Не винось: `note id`, `chunk id`, шлях sqlite, «з бази викладача».

## Що в базі (орієнтир)

| Таблиця | Навіщо |
|---------|--------|
| `notes` | дистилят на пару |
| `sheets` + `tasks` | умови ITSTEP |
| `chunks` + FTS | фрагменти книжок/статей/відео |
| `articles` / `related_sources` / `videos` | URL і супровід |

Якщо файлу немає: `Missing teacher_kb.sqlite. Rebuild: …/build_teacher_kb.py`.
