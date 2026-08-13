# Презентація і запікання тултіпів

Оболонку (CSS, TOC, таймери блоків, embed) копіюй з готової веб-пари, наприклад `m01/pair_02/presentation.html` або `tools/_presentation_shell_parts.py`. Не вигадуй нову тему.

## Структура сторінки

1. Banner `#agenda`: kicker, h2, lead, `.timing-strip` (сума pill = вікно пари), `.goals`, `.term-hint`.
2. Статті `article.block`:
   - `kind main` — теорія, `data-minutes` + `.clock` зі слотом
   - `kind task` — практика ITSTEP / курована
   - `kind deep` / extra — після вікна, без HH:MM пари
3. Код: `<pre><code class="language-python">` — мінімальний, запускається.
4. Підказки: `.callout.tip` (орієнтир), `.callout.task` (критерій здачі / «ваше рішення»).
5. Візуал: SVG у `.viz.diagram`, Chart.js canvas — опційно; без мережі графіки Chart.js можуть не зʼявитись, **тултіпи мусять**.

## Практика ITSTEP у слайдах

На блок X + X.1:

- X: умова списком + `.callout.tip` «Орієнтир» з коротким фрагментом (не весь файл з `results/`).
- X.1: «зробіть за аналогією», умова, `.callout.task` «Ваше рішення». **Без** готового коду розвʼязку.

Повні розвʼязки X — лише в `results/`.

## Запікання словника (обовʼязково для роздатку)

На вебі лишай `<script src="term-glossary.js" defer></script>`.

У `LessonN_00_presentation.html` **заміни** зовнішній скрипт на інлайн. Джерело: `backend/data/courses/python_ai_materials/assets/term-glossary.js` (або копія в парі).

Було (недостатньо для одного HTML-файла):

```html
<script src="Lesson1_ad_term_glossary.js" defer></script>
```

Має бути:

```html
<script>
/* повний вміст term-glossary.js: ENTRIES + walk + bindTips */
</script>
```

Вставляй **перед** скриптом Chart.js / перед `</body>`. Не лишай `src` на словник як єдине джерело.

Навіщо: студент відкриває HTML з папки або навіть один файл — пунктирні терміни (`.term`) показують English name + українське пояснення без журналу й без сусіднього JS.

`LessonN_ad_term_glossary.js` усе одно клади в папку: HTML-словник може підключати його. Презентація від цього файлу не залежить.

Перевірка: відкрий `LessonN_00_presentation.html` як `file://`, наведи на термін із пунктиром — тултіп є. Вимкни мережу — тултіп лишається (шрифти Google / Chart.js CDN можуть відпасти; це прийнятно).

## Локальні посилання роздатку

| Що | Значення |
|----|----------|
| Словник HTML | `LessonN_ae_slovnyk_terminologii.html` |
| Словник MD | `LessonN_af_slovnyk_terminologii.md` |
| Попередня / наступна пара | `Lesson{N-1}_00_presentation.html` / `Lesson{N+1}_00_presentation.html` |
| Журнал, localhost, `/course/` | заборонено |

У `LessonN_ae_slovnyk_terminologii.html` посилання на MD теж Lesson-імена.

## Таймінг

`plan.json` / `LessonN_ac_plan.json` і годинники в HTML мають збігатися. Непарна пара: старт 18:30; парна: 20:00. Extra-блоки не входять у суму вікна.

## Методичка

Короткий `teacher.md` / `LessonN_ab_teacher.md`: курс, модуль, тривалість, цілі, теми/акценти, посилання на презентацію й словник.

Повна `teacher.html` (як Lesson 1–2) — світла «паперова» тема, ті самі цілі й хід пари, що на вебі. Формуй з вебової методички, не з нуля.
