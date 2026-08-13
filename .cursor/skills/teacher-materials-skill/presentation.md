# Презентація

Оболонку (CSS, TOC, таймери, embed, wide stage) копіюй з готової веб-пари, напр. `m01/pair_02/presentation.html`. Не вигадуй тему. На широкому десктопі `.stage` до ~1360px (`widen_presentation_stage.py`).

## Порядок блоків

1. Banner `#agenda`: kicker, h2, lead, `.timing-strip` (сума pill = 80 хв), `.goals`, `.term-hint`.
2. Теорія `article.block` + `kind main`: `data-minutes` і `.clock` зі слотом.
3. **Extra з KB** після останньої теорії, **перед** практикою: `kind deep`, без HH:MM пари. Типовий id: `extra-kb-…`.
4. Практика `kind task` (ITSTEP або курована).
5. **`deep-study`** в кінці: take-home ~30 хв, без слоту вікна.
6. Усередині extra дозволений другий шар `<div class="extra-more" data-kb="extra-more">` — не чіпай timed-годинники.

## Тон і розмітка

- Код: `<pre><code class="language-python">` — мінімальний, запускається.
- `.callout.tip` — орієнтир / «Зверніть увагу»; `.callout.task` — критерій / «Ваше рішення». Текст **до студента**.
- Кожен extra: список «Джерела» (docs, підручник, OECD). Без sqlite-id.
- Візуал: SVG у `.viz.diagram`; Chart.js опційно (без мережі може зникнути). Тултіпи на вебі — з `term-glossary.js`.

## Практика ITSTEP

Блок X + X.1:

- X: умова + `.callout.tip` «Орієнтир» (фрагмент, не файл з `results/`).
- X.1: «зробіть за аналогією» + `.callout.task` «Ваше рішення». Без коду розвʼязку.

Повні розвʼязки X — лише в `lesson_materials/…/results/` після білдера.

## Словник

**Веб:** лишай `<script src="term-glossary.js" defer></script>`. Нові терміни — `assets/term-glossary.js`, формат tip: English name + рядок українською.

**Роздаток:** не запікай вручну. `build_lesson_materials_1_14.py` замінює тег на інлайн-скрипт (`/* baked term-glossary.js */` + `const ENTRIES`), прибирає посилання на `SLOVNYK_TERMINOLOGII.html`, ставить `.nav`, ріже `/course/` і `localhost`.

Перевірка білдера: немає зовнішнього glossary-тега, є `ENTRIES`, немає витоку журналу. Chart.js/шрифти з CDN можуть не завантажитись офлайн — це прийнятно; тултіпи мусять працювати з `file://`.

## Таймінг

`plan.json` і годинники HTML збігаються. Extra і `deep-study` не входять у суму 80 хв. Після правок вебу:

```bash
python3 backend/data/courses/python_ai_materials/tools/verify_pair_windows.py
```

(скрипт ще дивиться legacy `lessons/`; для нового zip орієнтир — вихід білдера.)

## Методичка

Тільки на вебі: `teacher.md` (курс, модуль, 80 хв, цілі, акценти, що extra стоїть перед практикою). `teacher.html` — опційно, як m01. У `lesson_materials/` не копіюй.
