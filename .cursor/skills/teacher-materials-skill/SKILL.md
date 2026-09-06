---
name: teacher-materials-skill
description: >-
  Пише методичні матеріали Python AI Materials: зріз teacher_kb → веб-пара
  журналу → автономний роздаток у lesson_materials/ (тултіпи запечені в HTML).
  Рішення 1–N у results/, без X.1. Лише коли користувач явно назвав
  teacher-materials-skill.
disable-model-invocation: true
---

# teacher-materials-skill

Працюй у `lesson_helper`:

`/Users/abuiluk/LessonPython/pet_projects/lesson_helper`

Канон у `lesson_helper`: `.agents/skills/teaching/teacher-materials-skill/`.
Опубліковане дзеркало — цей каталог (`skills` / aabuiluk/skills). Мова матеріалів — **українська**.

Не збирай роздаток руками. Після веб-пари запускай білдер.

Деталі: [kb.md](kb.md), [pack-layout.md](pack-layout.md), [presentation.md](presentation.md).

## Голос: студент читає сам

`presentation.html` і `lesson_materials/` викладач віддає студентам як є. Пиши до читача.

Заборонено в цих файлах: «типова помилка студентів», «студенти часто плутають», «поясніть / наголосіть / попросіть», «з бази викладача», внутрішні id нотаток KB.

Так: «Часто плутають A і B. Зверніть увагу: …».  
Не так: «Студенти часто плутають A і B. Поясніть: …».

Callout: «Зверніть увагу», «Часта пастка», «Коротко», «Джерела», «Орієнтир», «Ваше рішення». Асисти викладачу — лише в `teacher.md` на вебі.

## Пайплайн (не міняти місцями)

```
1. query_teacher_kb          зріз, не PDF
2. веб-пара                  mXX/pair_YY/
3. verify_pair_windows       вікно 80 хв
4. build_lesson_materials_1_14.py
```

```
1. Веб  → backend/data/courses/python_ai_materials/mXX/pair_YY/
2. Zip  → lesson_materials/PythonAI61_Lesson{odd}_Lesson{even}/
```

`lessons/` — **legacy**. Звідти білдер копіює старі стартери/CSV/results. Новий zip туди не пиши. Методичку студентам не клади.

## Окремий курс: Python AI Additional Materials

Лише якщо користувач **явно** назвав Additional Materials. Не підміняй пайплайн вище.

- Веб: `backend/data/courses/python_ai_additional_materials/`
- Zip: `additional_lesson_materials/`
- Журнал: `/course/python_ai_additional_materials`
- Інструменти: `…/python_ai_additional_materials/tools/` (`complete_all_modules.py`, `build_lesson_materials_1_14.py`, `verify_pair_windows.py`)
- Не чіпати `python_ai_materials/` і `lesson_materials/`
- Не запускати скопійований `build_teacher_kb.py` з additional-курсу (спільна KB — read-only)

## Окремий курс: Python AI Modify Materials

Лише якщо користувач **явно** назвав Modify Materials. Не підміняй пайплайн Materials і не чіпай Additional.

- Веб: `backend/data/courses/python_ai_modify_materials/`
- Zip: `modify_lesson_materials/` (після підтвердження веб-пар; білдер `tools/build_lesson_materials_1_14.py`)
- Журнал: `/course/python_ai_modify_materials`
- Цикл слайда: теорія (таймінг) → extra студента (без таймінгу) → блок викладача (без таймінгу, унікальний, лише по темі) → практика (таймінг, ITSTEP після блоку)
- Інструменти: `…/python_ai_modify_materials/tools/` (`reshape_modify_pairs.py`, `verify_pair_windows.py`)
- Не чіпати `python_ai_materials/`, `python_ai_additional_materials/`, `lesson_materials/`, `additional_lesson_materials/`

## Окремий курс: Python AI Codex Modify Materials

Лише якщо користувач **явно** назвав Codex Modify Materials. Не підміняй пайплайн Materials / Additional / Modify.

- Веб: `backend/data/courses/python_ai_codex_modify_materials/`
- Zip: `modify_codex_lesson_materials/` (білдер `tools/build_lesson_materials_1_14.py`; starters з `handout_src/`)
- Журнал: `/course/python_ai_codex_modify_materials`
- Цикл слайда: як у Modify — теорія → extra → блок викладача → практика
- Інструменти: `…/python_ai_codex_modify_materials/tools/` (`reshape_modify_pairs.py`, `verify_pair_windows.py`, `validate_codex_course.py`)
- Не чіпати `python_ai_modify_materials/`, `modify_lesson_materials/`, `python_ai_materials/`, `lesson_materials/`

## Крок 0. База

Канон: `teacher_kb.sqlite` у корені `lesson_helper` (gitignored). Як питати — [kb.md](kb.md).

```bash
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --note numpy
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --sheet practical_2.1
python3 backend/data/courses/python_ai_materials/tools/query_teacher_kb.py "numpy reshape"
```

Спочатку `--note`, потім `--sheet` для офіційних 1–N, потім короткий FTS. Повні extracts книжок у контекст не клади.

## Крок 1. Веб-пара

Шлях: `m{module:02d}/pair_{pair_index:02d}/`. `global_index` N = Lesson N.

| Файл | Роль |
|------|------|
| `presentation.html` | Студентська презентація |
| `plan.json` | Цілі, теми, таймінг = годинники HTML |
| `teacher.md` | Нотатки викладача (не в zip) |
| `term-glossary.js` | Словник; на вебі окремий файл |
| `SLOVNYK_TERMINOLOGII.html` / `.md` | Повний словник |
| `manifest.json` | Для журналу |

Правила (див. [presentation.md](presentation.md)):

- Непарна пара: **18:30–19:50**. Парна: **20:00–21:20**. Сума timed = `duration_min` (зазвичай 80).
- Порядок: теорія (`main`) → extra з KB **перед** практикою (без HH:MM) → ITSTEP (`task`) → `deep-study` в кінці (take-home).
- ITSTEP: умова + орієнтир. X.1 — «за аналогією», без розвʼязку.
- Extra: «Джерела» без sqlite-id. Нові терміни — в `assets/term-glossary.js`, далі копії в пари.
- Оболонка як у готових пар (wide stage). Після правок HTML:

```bash
python3 backend/data/courses/python_ai_materials/tools/verify_pair_windows.py
```

Не пиши `lesson_materials/`, поки веб-пара не зібрана.

## Крок 2. Роздаток — лише білдер

```bash
python3 backend/data/courses/python_ai_materials/tools/build_lesson_materials_1_14.py
```

Білдер: запікає словник у HTML, ставить відносну навігацію (і між пакетами), пише `requirements.txt`, стартери (`write_handout_starters.py`), `results/` без X.1. Не редагуй згенерований HTML вручну — виправ веб і перезапусти.

Стартери `LessonN_01_…`: робочі приклади (легко / середнє / складніше), не розвʼязки X.1. CSV через `Path(__file__).with_name(...)`. Matplotlib у `results/` — `savefig` поруч зі скриптом.

Нова пара поза 1–14: додай її в `PACKS` / `PAIR_WEB` білдера, не збирай zip руками.

## `results/`

Так: офіційні **1–N** (і 5–6, якщо є в аркуші).  
Ні: **1.1 / 2.1 / 3.1 / 4.1** і будь-яке `X.1`.

Немає файлів на кшталт `task2.1.ipynb`. У `results/README.txt` — що є і що навмисно відсутнє.

## Що не робити

- Не починати з zip, минаючи веб і KB.
- Не класти в zip `teacher.md`, `plan.json`, окремий словник.
- Не лишати в роздатковій презентації `<script src="term-glossary.js">`.
- Не вставляти розвʼязки X.1.
- Не тягнути PDF/ZIP LMS у контекст і не цитувати внутрішні id KB на слайді.

## Чеклист

- [ ] Взято `--note` / `--sheet`, не весь extract
- [ ] Веб: таймінг HTML = `plan.json`; extra перед практикою; deep-study в кінці
- [ ] `verify_pair_windows.py` для курсу — OK
- [ ] Запущено `build_lesson_materials_1_14.py` без помилок
- [ ] У HTML роздатку є `const ENTRIES` і коментар `baked term-glossary.js`
- [ ] Немає `/course/`, `localhost`, посилання на `SLOVNYK_TERMINOLOGII.html`
- [ ] Стартери запускаються; у `results/` є 1–N і немає X.1
- [ ] Голос слайда — до студента
