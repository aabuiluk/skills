# Розкладка файлів

Корінь: `/Users/abuiluk/LessonPython/pet_projects/lesson_helper`

```
backend/data/courses/python_ai_materials/   веб (журнал) — джерело істини
lesson_materials/PythonAI61_Lesson{odd}_Lesson{even}/   zip студентам
lessons/PythonAI61_Lesson{odd}_Lesson{even}/            legacy (вхід для білдера)
```

`global_index` N = Lesson N = `m{module}/pair_{index}` з `catalog.json`.
Пакети парні: 1+2, …, 13+14. Пише `tools/build_lesson_materials_1_14.py`.

## Веб-пара `mXX/pair_YY/`

```
presentation.html
plan.json
teacher.md
teacher.html              # опційно (m01)
term-glossary.js          # копія assets/; на вебі НЕ інлайн
SLOVNYK_TERMINOLOGII.html
SLOVNYK_TERMINOLOGII.md
manifest.json
```

Посилання: `term-glossary.js`, `SLOVNYK_TERMINOLOGII.html`.
Навігація між парами журналу: `../pair_ZZ/presentation.html`.
Словник канону: `assets/term-glossary.js` — після змін синхронізуй копії в парах (`sync_links.py` / enrich).

## Роздаток `lesson_materials/PythonAI61_Lesson{odd}_Lesson{even}/`

Еталон після білдера: `lesson_materials/PythonAI61_Lesson1_Lesson2/`.

```
LessonN_00_presentation.html     словник ЗАПЕЧЕНИЙ; без teacher/plan/slovnyk
LessonN_01_….py|.ipynb|.csv      стартери (легко / середнє / складніше)
LessonN_02_…
requirements.txt
results/
  README.txt
  task1_….py|.ipynb | pairN_taskk_solution.py
  … лише офіційні 1–N
  # НЕМАЄ task1.1, task2.1, …
```

Друга пара в тій самій папці — префікс `Lesson{N+1}_`.
Корінь `lesson_materials/README.txt` — як відкривати папки.

**У zip немає:** `teacher.md`, `teacher.html`, `plan.json`, `LessonN_ad_term_glossary.js`, окремий словник HTML/MD.

Навігація: та сама папка → `Lesson{N±1}_00_presentation.html`; інший пакет → `../PythonAI61_LessonX_LessonY/LessonZ_00_presentation.html`.

### `results/`

- Одна нумерація ITSTEP: `task1_solution.py`, …
- Дві пари з тими самими номерами: `pair{N}_task{k}_solution.py`
- Пара 1 (куровані задачі): `task1_ml_map.py`, `task2_classify_scenarios.py`, `task3_fp_fn_metric.py`
- Пара 2 (Jupyter Practical 1): `task1_intro_jupyter.ipynb` … `task4_students_grades.ipynb`
- CSV потрібні і в корені пакета, і в `results/` (movies, transactions, ratings, heights)
- Matplotlib: `plt.savefig(Path(__file__).with_suffix('.png'))` перед `show`

Білдер копіює з `lessons/…/results/`, пропускає імена з `\d+\.\d+` або `task\d+_\d+`.

### Стартери

Пише `write_handout_starters.py` (+ копія `LessonN_0k_` з `lessons/`, крім `_00_` HTML).

- Рівні в docstring / markdown: легко, середнє, складніше
- Дані: `Path(__file__).with_name("….csv")`
- Перевірка середовища (пари 1–2): `Lesson1_04_jupyter_check.ipynb`

## Відповідність веб → zip

| Веб | Zip |
|-----|-----|
| `presentation.html` | `LessonN_00_presentation.html` (інлайн словник, білдер) |
| `plan.json` / `teacher.md` | лишаються на вебі |
| `term-glossary.js` | запечений у HTML |
| практика / CSV | `LessonN_0k_` + `results/` |

Не збирай це вручну і не відновлюй схему `lessons/` (методичка + словник у пакеті).
