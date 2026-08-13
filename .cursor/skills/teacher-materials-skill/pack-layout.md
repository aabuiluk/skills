# Розкладка файлів

Корінь курсу в `lesson_helper`:

```
backend/data/courses/python_ai_materials/     веб (журнал)
lessons/PythonAI61_Lesson{odd}_Lesson{even}/  роздаток студентам
```

Нумерація: `global_index` N = Lesson N = `m{module}/pair_{index}` з `catalog.json`.
Пакети завжди парні: 1+2, 3+4, …, 13+14.

## Веб-пара `mXX/pair_YY/`

```
presentation.html
plan.json
teacher.md
teacher.html              # опційно (є в m01)
term-glossary.js
SLOVNYK_TERMINOLOGII.html
SLOVNYK_TERMINOLOGII.md
manifest.json
```

Посилання в презентації: `term-glossary.js`, `SLOVNYK_TERMINOLOGII.html`.
Навігація між парами: `../pair_ZZ/presentation.html`.

## Роздаток `lessons/PythonAI61_Lesson{odd}_Lesson{even}/`

Еталон: `lessons/PythonAI61_Lesson1_Lesson2/`. Пізніші пакети (3–14) — та сама схема, інколи без `*_aa_teacher.html`.

```
LessonN_00_presentation.html      # автономна презентація (словник ЗАПЕЧЕНИЙ)
LessonN_aa_teacher.html           # повна методичка (якщо є)
LessonN_ab_teacher.md             # короткі нотатки викладача
LessonN_ac_plan.json              # копія вебового plan.json
LessonN_ad_term_glossary.js       # копія словника (для HTML-словника; презентація не залежить від нього)
LessonN_ae_slovnyk_terminologii.html
LessonN_af_slovnyk_terminologii.md
LessonN_01_….ipynb | .py | .csv   # стартери / дані до розбору
LessonN_02_….ipynb | .py
…
requirements.txt
results/
  README.txt
  task1_….ipynb | task1_solution.py | pairN_task1_solution.py
  task2_…
  task3_…
  task4_…
  # НЕМАЄ task1.1, task2.1, …
```

Друга пара в тій самій папці — ті самі префікси `Lesson{N+1}_`.

### Імена `results/`

- Одна пара в пакеті або спільна нумерація ITSTEP: `task1_solution.py`, `task2_solution.py`, …
- Дві пари з однаковими номерами задач: префікс `pair{N}_task{k}_solution.py` (як у Lesson3–4, 11–12, 13–14).
- Jupyter (як Lesson 1–2): `task1_intro_jupyter.ipynb`, `task2_calculations_report.ipynb`, … — без `2.1` у назві.

### Що класти студентам vs перевірка

| Місце | Зміст |
|--------|--------|
| Корінь пакета | Презентація, словник, стартери, дані, `requirements.txt`, методичка |
| Стартери `LessonN_0k_` | Робочий мінімум для розбору X на парі (можна з коментарями) |
| `results/` | Повні розвʼязки офіційних X. Студент може звірити 1–N. Аналоги X.1 — ніколи |

## Відповідність веб → роздаток

| Веб | Роздаток |
|-----|----------|
| `presentation.html` | `LessonN_00_presentation.html` + інлайн словник |
| `plan.json` | `LessonN_ac_plan.json` |
| `teacher.md` | `LessonN_ab_teacher.md` (шляхи Lesson*) |
| `teacher.html` | `LessonN_aa_teacher.html` |
| `term-glossary.js` | інлайн у презентації **і** `LessonN_ad_term_glossary.js` |
| `SLOVNYK_TERMINOLOGII.html` | `LessonN_ae_slovnyk_terminologii.html` |
| `SLOVNYK_TERMINOLOGII.md` | `LessonN_af_slovnyk_terminologii.md` |

У роздатковій презентації:

- `href` словника → `LessonN_ae_slovnyk_terminologii.html`
- навряд «Далі / Назад» → `Lesson{N±1}_00_presentation.html`
- meta: «відкривається локально з папки», без «пара N/50 · журнал»
