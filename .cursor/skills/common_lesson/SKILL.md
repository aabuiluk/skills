---
name: common_lesson
description: >-
  Нормалізує пару курсу python_ai_step до вигляду еталонних пар 9 і 10:
  структура presentation.html, v2 простий шлях з підводками, компоненти,
  голос, teacher-нотатки на кожному блоці, «Де перечитати» в Checkpoint/Exit
  ticket, teacher.md, чистка CURSOR-ENRICHMENT / фантомного Support
  Intelligence. Material v2.0: intro-блоки + data-material-version; таймінг
  required/optional з перерахунком при приховуванні. Verify + deploy + commit.
---

# common_lesson

Еталон — **пара 9** (`m03/pair_01`, «Регресія з однією змінною») і **пара 10**
(`m03/pair_02`, «Метрики регресії та функція втрат`) курсу
[[active-course]] `python_ai_step`. Ця навичка описує, як довести будь-яку іншу
пару до того самого вигляду: **повний простий шлях v2 одразу** (не «скелет v2,
потім полірування»), з `<p class="lead">`-підводками перед кожним поясненням
і достатньою кількістю маленьких прикладів до абстракції.

Попередній структурний еталон (пари 7–8, `m02/pair_05`–`pair_06`, Matplotlib)
лишається корисним для скелета блоків ITSTEP / checkpoint / exit ticket, але
**голос, темп і v2-шар** — копіювати з пар 9–10.

Робочий каталог: `/Users/abuiluk/LessonPython/pet_projects/lesson_helper`
Пара: `backend/data/courses/python_ai_step/mNN/pair_NN/`
URL admin: `https://csctemplate.pythonanywhere.com/courses/python_ai_step/pairs/{global_index}/files/presentation.html`
URL студента: `https://csctemplate.pythonanywhere.com/course/python_ai_step/pairs/{global_index}/files/presentation.html`

Мова матеріалів — **українська**. Код та ідентифікатори — англійська.

---

## Поточний стан курсу (станом на 2026-09-01)

**Структура на диску:** `backend/data/courses/python_ai_step/` — `course.json`,
`catalog.json`, `hidden_blocks.json`, `overview/`, `tools/`, модулі `m01`…`m10`.
Розподіл пар: m01×2, m02×6, m03×6, m04×6, m05×5, m06×5, m07×6, m08×6, m09×6,
m10×2 = **50 пар + overview** (51 `presentation.html`). Пари 80 хв, група Python61.

**Назви модулів** (`course.json` → `modules[].title`) — офіційні ITSTEP, за
компетентністю, **не міняти**: 1 Вступ до ШІ та науки про дані · 2 Обробка та
аналіз даних · 3 Алгоритми навчання з учителем · 4 Основи нейронних мереж ·
5 Нейронні мережі в компʼютерному зорі · 6 Обробка природної мови · 7 Навчання
без учителя · 8 Generative AI у Google Cloud · 9 LLM-фреймворки та інженерія
генеративних систем · 10 Іспит.

**Що вже зроблено по всіх 50 парах** (див. [[step-web-lectures-workstream]]):
- 926 `CURSOR-ENRICHMENT` секцій + ~150 `data-ingest/gap/web` дампів вирізано;
- підписи нормалізовано (`Практика · X.1`, `Приклад · N`, без емодзі);
- кожен `#itstep-task-N` має X.1 solution + X.2 «складніший крок» + solution з
  `<p><b>Ключове.</b> …</p>`; TOC-підписи синхронізовані;
- усі 149+ `<details class="solution">` мають `<p><b>lead.</b> …</p>`, не лише код;
- `.lh-teacher-note` на кожному змістовному блоці; «Де перечитати» + відповіді в
  Checkpoint / Exit ticket;
- `teacher.md` переписані (без `CURSOR-ENRICHMENT`, без фантомного Support Intelligence);
- фронт: `pair-notebook.js` тримає solution-`<pre>` видимим у лекції + дзеркалить у консоль;
- `check_lectures.py` → **51 / 0 / 0**; усі `language-python` блоки `ast.parse` clean;
  Σ `data-minutes == 80` на кожній парі; усі `href="#…"` резолвляться.

**Гейт публікації:** студентам видно тільки пари, де користувач сам поставив
галочку (`public_plan.json`). Публічні зараз — пари 1–8. `public_plan.json` не
чіпати. Деплой не-`presentation` файлів — лише з `--force`, інакше лишаються старі.
Див. [[step-publish-gate]].

**Аудитний additive-шар застосований до всіх 50 пар** (2026-08-30, гілка
`claude/two-reports-93b8e8`, коміти `fd8c64da`…`c99bb75c`, задеплоєно): у
solution-демо `# ->` очікуваний вивід або інваріантний `assert`; демо «Приклад ·
N» марковані `RUNNABLE/EXCERPT`; checkpoint 4 питання + відповіді; 100-бальна
рубрика в кожному `#homework-stretch`; студентські «Джерела» з «— підтверджує:».
`check_lectures.py --audit` → 51 презентацій, 0 знахідок. Деталі — розділ 10.

**Відомий дефект (поза аудитом):** у частині пар блок «Відповіді» в Checkpoint
відповідає на питання в іншому порядку / про інші теми, ніж показаний `<ol>`
(артефакт keyword-substitution генератора). Q4 додано коректно, 1–3 не вирівняно.

**Material v2.0 + простий шлях (еталон — global_index 9 і 10,
`m03/pair_01`, `m03/pair_02`):** паралельні v2-блоки з життєвими прикладами
і `<p class="lead">`-підводками перед кожним поясненням; v1-теорія позаду;
`versions.json` → `active`, `student_active`, `overrides.2.0.pairs` =
**номери пар (global_index)**, не модулів. Admin: два селектори в toolbar —
«Студенти» (публічний URL) і «Версія» (перегляд у редакторі). Таймінг:
`data-timing="required|optional"`, перерахунок через `lesson_timing.py` +
editor mode. Деталі — розділ 12.

---

## 0. Порядок роботи

1. **Прочитати еталон:** `m03/pair_01/presentation.html` і/або `m03/pair_02/presentation.html`
   — темп v2, `<p class="lead">`, кількість прикладів до теорії.
2. Прочитати `presentation.html`, `teacher.md`, `plan.json`, запис пари в `catalog.json`.
3. Знайти офіційні завдання ITSTEP (розділ 6).
4. Прибрати сміття (розділ 5). **Структуру пари не міняти** — той самий набір блоків, ті самі `id`, якорі, `data-minutes`. Перейменування заголовка дозволене, лише якщо блок явно нелогічний; тоді синхронізувати `<li>` у `<ol class="toc">`.
5. Переписати «набір слів» на людський текст (розділ 3), заповнити тіла блоків реальним змістом теми — за принципами пояснення з розділу 11 і **голосом v2** з розділу 12.2.
6. Додати `.lh-teacher-note` на кожен змістовний блок (розділ 4).
7. Checkpoint і Exit ticket: студентський блок «Де перечитати» + teacher-нотатка з відповідями (розділ 4). **Checkpoint — після кластера теорія → завдання 1 → теорія → завдання 2 → workflow / міні-задачі**, не одразу після першого завдання (еталон пар 9–10 v4). Порядок у `<ol class="toc">` і в `.timing-strip` — точно як у DOM.
8. `#itstep-practical` — **опційно**; якщо `#itstep-task-N` уже повні — не ставити (як у парах 9–10). Не дублювати код.
8a. **`#itstep-homework`** — офіційне ДЗ перед `#homework-stretch` (розділ 6.1): умови з `data/faily/` або згенерувати; еталонний код лише в `.lh-teacher-note`.
9. Переписати `teacher.md` (розділ 7).
10. **Якщо v2.0 / простий шлях** — див. розділ 12: **одразу** повний маршрут з прикладами
    і підводками, не проміжний «скелет v2».
11. Verify (розділ 8) → deploy → commit у `main`.

Дій, не питай. Показуй результат готовим, не проміжними станами.

---

## 1. Файли пари

| Файл | Роль | Чіпаємо |
|---|---|---|
| `presentation.html` | веб-лекція, головний артефакт | так |
| `teacher.md` | методичка викладача | так |
| `homework.md` | домашнє / stretch | за потреби |
| `quiz.json` | самоперевірка | за потреби |
| `manifest.json` | білий список файлів пари | ні (крім нових файлів) |
| `pair-notebook.js`, `term-glossary.js`, `SLOVNYK_TERMINOLOGII.{md,html}` | рантайм зошита, глосарій | ні |

`presentation.html` для `python_ai_step` **не генерується** — правимо руками. `scripts/course_build/` таргетить `python_ai`, не `python_ai_step`.

---

## 2. Скелет presentation.html (послідовність блоків)

`<!DOCTYPE html>` → inline `<style>` (не чіпати) → `.mobile-bar` → `.rail` (меню/TOC) → `<main class="stage">`:

1. **`<header class="banner" id="agenda">`** — `.kicker`, `<h2>`, `.lead`, `.timing-strip` (пігулки хвилин), `.goals` (цілі), callout-и «Перед початком» / «Після пари ви можете», `.term-hint`.
2. **Теорія** `<article class="block" id="<topic>">` · `<span class="kind main">теорія</span>` · `.block-timer data-minutes`. Всередині: прозовий вступ → `.viz-grid` (діаграма SVG + `.cards` з поясненнями) → `<pre><code class="language-python">` → `.callout tip` «Зверніть увагу» → `<!-- theory-deeper:start:N:slug -->…<!-- theory-deeper:end -->` (глибший абзац + `.callout` «Коротко»).
3. **Deep-dive пара** (без таймера): `<!-- deep-dive:start:N:M -->` → `article.block.extra-deep-dive` (`kind deep` «додатковий матеріал», для сильніших студентів) → `article.block.teacher-deep-dive` (`data-project-feature="python-ai-modify-teacher-blocks"`, `hidden`, лише викладач) → `<!-- deep-dive:end -->`. У TOC — `<!-- deep-dive-toc:start -->` з `<li data-teacher-toc hidden>` для teacher-запису.
4. **Завдання** `id="itstep-task-N"` · `<span class="kind task">практика ITSTEP</span>` · таймер. Всередині: `.callout tip` з `data-task-level` (бейдж рівня) → **`.callout tip` «Звідки дані і навіщо»** (або «Що рахуємо…») — перед кодом: що за датасет, що означає `y`, чому ця колонка/рядок, що дасть результат (див. §11, п. 5) → `.callout example` `<span class="role-label">Приклад · N</span>` з офіційним завданням **і прямим лінком на LMS** (див. §6) + `<details class="callout solution">…` → `.callout your-task` … → крок N.2 + solution. У v2-парах розбір першого-двох завдань показуємо розгорнутим: `<details open class="callout solution">` (еталон пар 9–10 v4).
5. **`#checkpoint`** `kind main` «перевірка» · таймер 3 хв. 4 питання `<ol>` (§10.E) → **`.callout` «Де перечитати»** (студентські посилання, рядок на кожне питання) → `.callout tip` «Коротко» → **`.lh-teacher-note`** з відповідями. **Місце в потоці:** після теорії + завдань 1–2 + workflow / міні-задач, не одразу після першого завдання — тоді checkpoint і exit ticket стоять поруч наприкінці (еталон пар 9–10 v4).
6. …повтор теорія / завдання / теорія / завдання, і лише потім checkpoint…
7. **`#style-grid`** (або аналог) — теорія оформлення графіка.
8. **`#practice-N-<topic>`** `kind task` — мінізадача, що збирає попередній теоретичний блок; обовʼязкова частина + `<details class="solution">` + «крок далі» + `.callout tip` «Орієнтир».
9. **`#itstep-practical`** — **опційно**. Підсумок здачі практикуму (`.flow` + картки на `#itstep-task-N` + критерій), **без** дубля коду з робочих блоків. Якщо `#itstep-task-N` уже повні з лінками LMS — блок **можна не ставити** (еталон пар 9–10: немає). Не розмножувати розвʼязки сюди.
10. **`#extra-kb-*`, `#extra-*`** `kind deep` «додатковий матеріал» — необовʼязкове поглиблення теми.
11. **`#si-thread`** — «Відповідальна візуалізація …» — етика на матеріалі пари (обрізана вісь, підібрані bins, correlation≠causation тощо). Не «Support Intelligence».
12. **`#practice-levels`** — «Рівні практики»: **База / Практика / Stretch** на задачах саме цієї пари.
13. **`#repro-bar`** — «Відтворюваність графіка»: дані в коді, `seed`, явний `figsize`, `savefig` до `show`.
14. **`#practice-bar`** — «Самоперевірка перед здачею»: `.callout tip` «Що має вийти» + `.callout tip` «Часті помилки».
15. **`#itstep-homework`** `kind task` «домашнє», **без таймера**, **одразу перед** `#homework-stretch` — офіційне домашнє ITSTEP (див. §6.1). У TOC — окремий пункт перед «Домашнє / stretch».
16. **`#homework-stretch`** — додаткове take-home / stretch по темі пари (Тема / Що зробити `<ol>` / Що здати / Готово, коли / рубрика). Не плутати з `#itstep-homework`.
17. **`#exit-ticket`** `kind main` «перевірка» · таймер 4 хв. 1–2 питання → **`.callout` «Де перечитати»** → `.lh-teacher-note` з відповідями.

Далі — `<script>` блоки (TOC-toggle, таймери, Chart.js), `pair-notebook.js`, `term-glossary.js`. Не чіпати.

### Таймінг

Блоки з `<label class="block-timer" data-minutes="N" data-minutes-min="…" data-minutes-max="…">`
мають у сумі **required** давати **80** для кожного material-path (v1.0 і v2.0
окремо, якщо є `data-material-version`). Таймери — у теорії / завдань /
checkpoint / exit ticket.

- **Обовʼязкові:** `data-timing="required"` на `<article>` — входять у 80 хв.
- **Опційні:** `data-timing="optional"` на `extra-*`, `#si-thread`, `#homework-stretch`,
  `#itstep-practical`, `#itstep-homework` тощо — у strip з позначкою **(опц.)**, не входять у 80 хв.

На `<main class="stage" data-pair-minutes="80" data-pair-start="HH:MM">`.
Перерахунок `.timing-strip`, `.clock` і `.lh-timing-summary` — сервер
(`lesson_timing.apply_lesson_timing`) і editor mode (`presentation_chrome.js`).
Деталі — розділ 12.

Годинники для студента приховані сервером — не покладатися на них як на єдине
джерело хвилин.

---

## 3. Голос: студент читає сам

`presentation.html` викладач віддає студентам як є. Пиши до читача.

**Заборонено** (поза `.lh-teacher-note`): «студенти часто плутають», «типова помилка студентів», «поясніть / наголосіть / попросіть», «Ваше завдання …», мета-наратив («У цьому уроці ми розглянемо…», «Отже,», «Таким чином,», «як ми бачимо»), «з бази викладача», внутрішні id нотаток.

**Замість:** «Часто плутають A і B. Зверніть увагу: …».

**Санкціоновані підписи callout:** «Зверніть увагу», «Часта пастка», «Коротко», «Джерела», «Орієнтир», «Ваше рішення».

«Імітація логічного тексту» — набір термінів, що виглядає як абзац, але нічого не стверджує — вирізати повністю й писати реальний зміст теми. Джерело правди — [[teacher-materials-voice-rule]] + `AGENTS.md` §Hard constraints #6.

---

## 4. Teacher-only контент

### `.lh-teacher-note` — на кожному змістовному блоці

Останній елемент усередині `.block-body`:

```html
<div class="lh-teacher-note"><span class="lh-tn-label">Для викладача</span><p><b>Коротко.</b> одне речення «що сказати студенту першим» — простими словами.</p><p><b>Пояснення.</b> як подати, часта плутанина, що показати на дошці.</p><p><b>Рішення / відповідь.</b> відповідь на питання блоку / ключовий рядок коду / як виглядає коректний артефакт.</p></div>
```

- Теорія / завдання / checkpoint / exit ticket — повна нотатка (2 абзаци).
- `extra-*` — коротка (1 абзац, «Для сильніших. …»).
- **НЕ додавати** в `article.extra-deep-dive` і `article.teacher-deep-dive` (перший — і так extra, другий — і так лише для викладача).
- Тут teacher-directed мова **дозволена** («покажіть», «наголосіть») — `check_lectures.py` не сканує вміст `.lh-teacher-note`.
- Механізм: сервер (`backend/app/presentation_chrome.py`) віддає `.lh-teacher-note` лише з `?teacher=1`; студенту — `display:none`. Див. [[editor-mode-block-visibility]].

### Checkpoint / Exit ticket

- **Студенту** — `.callout` «Де перечитати» з прямими якорями на теоретичні блоки, що відповідають на кожне питання:
  ```html
  <div class="callout"><b>Де перечитати</b><ul><li>Тема питання — блок <a href="#figure-axes">Основні обʼєкти matplotlib</a></li>…</ul></div>
  ```
- **Викладачу** — `.lh-teacher-note`: `<b>Пояснення.</b>` (тайм, формат) + `<b>Відповіді.</b>` (модельні відповіді на всі питання).

### `teacher-deep-dive`

Один на deep-dive-пару. `data-project-feature="python-ai-modify-teacher-blocks"`, `hidden`, синя рамка. Технічний інваріант теми + `.teacher-sources` з 1–2 посиланнями на офіційну документацію. Прихований для студента сервером (`with_student_teacher_block_css`).

---

## 5. Що вирізати (сміття непричесаних пар)

| Маркер | Що це |
|---|---|
| `<!-- CURSOR-ENRICHMENT:*:START -->…<!-- CURSOR-ENRICHMENT:*:END -->` | шаблонний word-salad (~18 секцій/пара): «має точний навчальний контракт», фейкові `assert X_contract`, ті самі 3 «Перевірені джерела» |
| `<!-- data-ingest:start:N -->`, `data-gap`, `data-web` (+ `data-ingest-toc` у TOC) | дампи білдера: посилання на неіснуючий `materials_from_data/`, «Playwright MCP недоступний», сирі субтитри Udemy |
| **Фантомний Support Intelligence** | `tickets.csv`, `m02_eda.py`, `project/support_intelligence/`, «priority / subject length», data-dictionary з PII. **У `python_ai_step` такого проєкту немає** — практика тут це офіційні задачі ITSTEP. Часто протікає у `#si-thread`, `#practice-levels`, `#repro-bar`, `#practice-bar`, `#homework-stretch`, `#exit-ticket`, а також у питання `#checkpoint` («дисбаланс priority») і в `teacher.md` (секції «На дошці», «Live coding», хвіст) |
| `✍️ Ваше завдання · X.1`, `🧭 Приклад із розбором · N`, емодзі в `role-label` | старі підписи → `Практика · X.1`, `Приклад · N`, без емодзі |
| Порожні `<details class="solution">`, порожні `.callout`, порожні `X.1` intro | заповнити або прибрати |
| «Джерела» з піратськими книгами (`Build Your Own AI Investor…` тощо) | прибрати |
| Мертві `<div class="extra-more" data-kb="extra-more">` обгортки | прибрати (не мають ні CSS, ні JS) |

Регекс для CURSOR-ENRICHMENT: `\s*<!-- CURSOR-ENRICHMENT:[^>]*:START -->.*?<!-- CURSOR-ENRICHMENT:[^>]*:END -->` (DOTALL) — усі коментар-обгорнуті. `data-ingest/gap/web` так само.

---

## 6. Офіційні завдання ITSTEP — беруться з проєкту

**Не кидати загальний лінк.** Джерело — [[itstep-source-materials]]:

- Повний текст: `data/faily/w{NN}_{Практичне|Домашнє} завдання X.Y.html` (локально, `data/` в ігнорі).
- URL кожного аркуша: `data/all_links.txt` — рядок `Практичне завдання X.Y <tab> html_link <tab> https://materials.itstep.org/content/<uuid>/uk`.
- `beef810f-be75-4b3c-9c1b-a8124a1a4b01` = **програма курсу**, не практикум. Не використовувати як лінк на завдання.

**Посилання на практикум ITSTEP:**

1. **(Опційно) `#itstep-practical`** — короткий чеклист здачі + лінк на аркуш LMS. Не обовʼязковий, якщо задачі вже повні.
2. **Кожен `#itstep-task-N`** — у рядку `<b>N · офіційне завдання.</b>` (або «приклад з курсу» / «адаптоване завдання») **прямий лінк** на аркуш з підписом **`Практичне завдання X.Y · завдання N ↗`**. Окремих якорів на сторінці ITSTEP немає.

Шаблон:

```html
<p><b>3 · офіційне завдання.</b> …умова…
<a href="https://materials.itstep.org/content/<uuid>/uk" target="_blank" rel="noreferrer">Практичне завдання 3.1 · завдання 3 ↗</a></p>
```

**Порядок:** відкрити локальний `.html` → звірити формулювання дослівно → додати лінк у `#itstep-task-N`. Масово для всіх пар курсу:

```bash
python3 backend/data/courses/python_ai_step/tools/add_itstep_task_links.py
python3 backend/data/courses/python_ai_step/tools/add_itstep_task_links.py --check
```

Скрипт ідемпотентний: читає URL і назву аркуша з `#itstep-practical` або першого не-програмного LMS-лінка в `presentation.html`. Пари з **курованими** задачами без окремого аркуша ITSTEP (див. `teacher.md` → «Офіційне джерело практики») — без посилань; `--check` їх не вважає помилкою.

Відомі UUID (еталон):

- Практичне 2.3 (Matplotlib, пари 7–8): `9b44e3c1-146b-409e-a80b-a89ea82e693e`.
- Практичне 3.1 (регресія / метрики, пари 9–10): `96006df5-ea3c-49ff-8734-e319dc01a9d7`.
- Домашнє 3.1 (базова регресія, пари 9–10): `7d67d6ba-7cae-40bc-befe-129939bd1a3e`.
- Домашнє 3.2 (множинна регресія / preprocessing): `666c1cf0-526d-480c-881f-003556669211`.

### 6.1. `#itstep-homework` — офіційне домашнє перед stretch

**Правило для всіх пар `python_ai_step`.** Перед `#homework-stretch` обовʼязково є блок `#itstep-homework` (аналог `#itstep-practical`, але для ДЗ).

**Джерело умов (пріоритет):**

1. Якщо в `data/faily/` / `data/all_links.txt` є **Домашнє завдання X.Y** для модуля цієї пари — брати формулювання **дослівно** з локального HTML і лінк з `all_links.txt`.
2. Якщо аркуша немає (курована пара) — **згенерувати** 2–4 домашні задачі по темі пари (той самий стек, що на парі; California / diabetes / make_* за контекстом), без вигадування неіснуючого UUID LMS. У шапці блоку написати «Куроване домашнє · тема пари», без фейкового лінка ITSTEP.
3. Великий аркуш (4 задачі) можна **розрізати** між сусідніми парами модуля так само, як практикум (напр. пари 9–10: ДЗ 3.1 задачі 1–2 / 3–4).

**Структура блоку (еталон — пари 9 і 10):**

```html
<article class="block" id="itstep-homework" data-timing="optional">
  <div class="block-head"><h3>Домашнє · ITSTEP Завдання …</h3>
    <span class="kind task">домашнє</span></div>
  <div class="block-body">
    <div class="callout tip">…лінк на Домашнє завдання X.Y ↗…</div>
    <div class="callout tip"><b>Навіщо…</b>…</div>
    <!-- по одному .callout.example на задачу з умовою + лінком · завдання N -->
    <div class="flow">…здача…</div>
    <div class="callout task"><b>Критерій здачі.</b> …</div>
    <div class="lh-teacher-note">
      <span class="lh-tn-label">Для викладача · еталонні рішення (студент не бачить)</span>
      <!-- повний RUNNABLE-код на кожну задачу; видно лише з «Показувати блоки Для викладача» -->
    </div>
  </div>
</article>
```

**Еталонний код** — лише в `.lh-teacher-note` (студент не бачить). `#homework-stretch` лишається окремим додатковим stretch, не замінює офіційне ДЗ.

**Обовʼязковий патч `pair-notebook.js` при додаванні `#itstep-homework`.** Без нього
зошит дзеркалить `<pre>` з `.lh-teacher-note` у бічну панель — тобто студент
у student-режимі бачить еталонні рішення. Патч (є в `m03/pair_01`, `m03/pair_02`
з v4; решта пар — ні): у функції клонування `<pre>` додати

```js
var studentMode = Boolean(document.getElementById("lh-presentation-chrome-student"));
// …
if (studentMode && pre.closest && pre.closest(".lh-teacher-note")) continue;
```

`pair-notebook.js` тут — виняток із правила «не чіпати» (§1). Копіювати той
самий діф; деплой — з `--force` разом із `presentation.html` пари.

### 6.2. Наскрізний кейс на реальних даних — опційний варіант практики

**Статус: варіант, не обовʼязковий елемент скелета. Поки чернетка — далі
покращимо.** Дизайн для пар 9–10: `docs/superpowers/specs/2026-09-02-pairs-9-10-dou-salary-practice-design.md`
(дані зарплат DOU: досвід у роках → зарплата в доларах).

Коли пара виграє від одного наскрізного прикладу на «живих» даних — додати
**окремий опційний блок** практики **перед `#itstep-homework`**:

- Джерело даних назвати явно + дату зрізу; **вбудувати маленьку вручну
  перенесену таблицю** (2 колонки), без живого парсингу на занятті; у тексті
  зазначити, що це агрегований навчальний зріз, не індивідуальні дані.
- Один кейс тягнеться через сусідні пари модуля: пара 9 — побудувати
  `LinearRegression` + scatter з лінією + обережний висновок; пара 10 — на
  тих самих даних residuals, MAE/MSE/RMSE/R² і порівняння з
  `DummyRegressor(strategy="mean")`.
- `data-timing="optional"`, стабільний `id` + запис у TOC; `#itstep-task-1–4`,
  `#itstep-homework`, `#homework-stretch`, `public_plan.json` — не чіпати.
- Студентський текст — до читача; повний робочий код із перевірками форми й
  очікуваним результатом — лише в `.lh-teacher-note` (+ сценарій у `teacher.md`).
  Якщо код лягає в `.lh-teacher-note` — потрібен патч `pair-notebook.js` (§6.1).
- Verify як для `#itstep-homework`: `ast.parse` коду, `check_lectures.py --pair N`,
  незмінна сума `required`, TOC-якорі.

Не змішувати з `#itstep-task-N` (офіційний практикум) і з `#itstep-homework`
(офіційне ДЗ) — це додатковий тренувальний кейс поверх них.

---

## 7. teacher.md — структура

Викладацький файл, «студентський голос» тут не діє. Ніякого `<!-- CURSOR-ENRICHMENT -->`.

```
# Пара N. <Тема>
**Курс / Модуль / Тривалість / Практикум ITSTEP**

## Мета пари            — 3–4 конкретні вміння
## Головні акценти      — що наголосити, що плутають (тут «часто плутають» ОК)
## Хронометраж (80 хв)  — таблиця Хв | Блок | Тип
## Актуалізація         — 2–3 питання на розігрів
## Розбір на дошці      — що намалювати
## Живе кодування       — що набирати, у якому порядку, + навмисна помилка
## Контрольні точки     — Checkpoint + Exit ticket з модельними відповідями
## Типові помилки студентів
## Якщо часу мало (40–50 хв) / Якщо лишилось 15–20 хв
## Критерії оцінювання практики — База / Практика / Stretch
## Нотатки до окремих блоків    — 3–5 реальних нотаток, не шаблон
```

---

## 8. Verify

```bash
python3 backend/data/courses/python_ai_step/tools/check_lectures.py --pair N     # має бути 0 errors 0 warnings
```

Перевіряє: `viewport`, дрібний шрифт, teacher-voice / assistant-framing / ai-tone
у студентському тексті (вміст `.lh-teacher-note` і `teacher-deep-dive` пропускає),
порожні solution/callout/task. **Таймінг:** якщо є `data-material-version` —
окремо `required` sum для v1.0 і v2.0 (`lesson_timing.timing_sum_for_path`);
інакше одна сума required = 80.

```bash
python3 -m pytest backend/app/tests/test_lesson_timing.py -q   # після змін таймінгу
python3 -c "from backend.app.main import app"                  # перед deploy backend
```

Плюс вручну:
- **ITSTEP-лінки:** кожен `<b>N · офіційне завдання.</b>` (і «адаптоване завдання», якщо з того ж аркуша) має `materials.itstep.org/content/…` у тому ж `<p>` (не лише в `#itstep-practical`); перевірка — `add_itstep_task_links.py --check`;
- якорі TOC ↔ `id` збігаються (`href="#x"` → є `id="x"`);
- баланс тегів, немає залишків маркерів з розділу 5;
- рендер у браузері (force-reload; `file://` кешує).

---

## 9. Deploy + commit

```bash
# лише змінені файли пари
python3 scripts/push_files_to_pa.py --force \
  backend/data/courses/python_ai_step/mNN/pair_NN/presentation.html \
  backend/data/courses/python_ai_step/mNN/pair_NN/teacher.md
```
Далі перевірити live: `curl -s https://csctemplate.pythonanywhere.com/api/courses/python_ai_step/pairs/N/files/presentation.html` (студент) і `?teacher=1` (викладач).

Коміт — прямо в `main`, повідомлення в стилі `python_ai_step пара N: <що зроблено>`, з `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.

Якщо міняється `backend/app/*` або фронтенд — спершу `cd frontend && npm run build`, тоді
`push_files_to_pa.py --force backend/app backend/static`. **Перед push backend:**
`python3 -c "from backend.app.main import app"` — інакше весь сайт 500 (SyntaxError у
`presentation_chrome.py` тощо). Після reload: `curl -s -o /dev/null -w '%{http_code}' https://csctemplate.pythonanywhere.com/`
має бути `200`. `backend/static/` в ігнорі — білдити й пушити, не комітити.

---

## 10. Розширення з аудитів 2026-08-11

Два звіти в корені репо — `PROJECT_AUDIT_REPORT_2026-08-11.md` (платформа: секрети,
CI, тести, XSS, Git — **майже не про пари**, застосовне лише через розширення
`check_lectures.py`) і `EDUCATIONAL_PROGRAMS_AUDIT_SKILLS_2026-08-11.md`
(педагогіка — прямо про пари). Звіти писалися до `python_ai_step`, для курсів-предків
(`python_ai_codex/cursor`), але лінія генерації спільна, тож знахідки P0 (stub-рішення,
однакова практика, `X/y` для SVD) **вже закриті** в `python_ai_step`. Лишається
**лише additive** шар — нічого не ламає, structure/ids/anchors/timing не чіпає:

**A. Expected output + `assert` у кожному runnable-демо** (звіт §9.2, P1-EDU-6).
У `<pre><code class="language-python">` кожного `solution-body` і кожного теоретичного
демо, яке реально запускається, останніми рядками — детермінований доказ результату:
```python
# -> singular values: [5.46 3.16]
# -> reconstruction error: 2.98
assert x_rank_1.shape == x.shape
assert singular_values[0] >= singular_values[1] >= 0
```
Формат коментаря очікуваного виводу — `# -> …`. Random → фіксувати `seed` / `random_state`.

**B. Тип демо** (P1-EDU-6). На початку блоку коду або в підписі `.callout example`:
- `RUNNABLE` — копіюється й працює as-is (потрібні input + expected output + ≥1 check);
- `EXCERPT` — фрагмент більшого pipeline, залежності названі явно;
- `PSEUDOCODE` — пояснює дизайн, не видається за Python (тоді `ast.parse` не вимагається).
Мінімальна реалізація: `<span class="role-label">Приклад · N · RUNNABLE</span>`.

**C. 100-бальна рубрика в `#homework-stretch`** (P1-EDU-4). Після «Готово, коли» —
`<div class="callout"><b>Рубрика (100)</b><ul>` з 4–5 критеріями й вагами, специфічними
для теми (напр. PCA: центрування 20 · коваріація 20 · reconstruction 25 · тести 20 ·
інтерпретація 15). Загальний reproducibility-чекліст лишається.

**D. Джерела, привʼязані до тез** (P1-EDU-5). У студентському `.callout` «Джерела»
кожен пункт — конкретний розділ + `— підтверджує: <теза блоку>`. Загальний список
курсу лишається в меню. `teacher-sources` у `teacher-deep-dive` уже тематичні — там
додати назву розділу до кожного посилання.

**E. Retrieval-глибина** (P1-EDU-7, §10.1). Checkpoint — довести до 4 питань (зараз
3), Exit ticket — лишити 1–2. Кожне питання і далі має рядок у «Де перечитати».

**F. Розширити `check_lectures.py`** (звіт §11, COURSE-01/06) — нові перевірки:
`language-python` блок або `ast.parse`-валідний, або має тег `PSEUDOCODE`;
кожен `solution-body` `<pre>` містить `# ->` або `assert`; `#homework-stretch` містить
«Рубрика»; `#itstep-task-N` не порожній і згадує сутність завдання. Спершу — режим
report-only (`--audit`), не блокуючий, поки не пройдені всі 50 пар.

**Порядок застосування (виконано m01–m10):** модуль за модулем. Спочатку
`<scratchpad>/annotate_solutions.py <file>` — автоматично додає `# ->` (запускає
код у DS-пісочниці з numpy/pandas/sklearn/torch, для графіків описує `Axes`) і
теги `RUNNABLE/EXCERPT`. Далі вручну — інваріантні `assert` до блоків, що не
запускаються окремо (CSV / continuation / nltk-gensim). Тоді один
`<scratchpad>/content_mNN.py` (`str.replace`) на checkpoint Q4+відповідь+«Де
перечитати», рубрику `<div class="callout"><b>Рубрика (100)</b>`, привʼязку
«Джерела», чистку `Support Intelligence` / `SI-*` / фейкових проєктів, і
`Три→Чотири короткі питання`. Verify (`check_lectures.py --module N` 0/0 +
`--audit` 0 + `ast.parse` + `check_notebook_cells.py`) → `push_files_to_pa.py
--force` → commit `python_ai_step mNN: audit layer …`.

**Побічно виправлено:** `m03/pair_01` `x_test` undefined; `Path(__file__)` savefig
у ноутбуках m04–m07; `m07/pair_05` `title: [...]` placeholder; `m08/pair_05`
`cosine_similarity` 0-d; піратські книги в «Джерела»; `check_lectures.py`
`checkpoint_thin` пропускає теоретичні блоки з `id="checkpoint"`.

**Не робити:** cumulative-project checkpoints зі звіту §P1-EDU-7 через «Support
Intelligence» — цей проєкт у курсі відсутній (розділ 5); нову наскрізну лінію
проєкту заводити тільки за окремим рішенням користувача.

---

## 11. Принципи пояснення (адаптовано з `amosblomqvist/learn`)

Джерело — `github.com/amosblomqvist/learn`, skill `teach` (особистий `.pi`-конфіг,
не Claude Code). Повний механізм «probe → plan → teach» — для адаптивного 1:1
тьютора й сюди не переноситься. Переносяться чотири речі — застосовувати при
переписуванні тіл блоків (розділ 0, крок 4) і при написанні питань.

**1. Безумовні істини спершу.** Кожен теоретичний блок починати з факту без
застережень, який студент приймає as-is (справжнє означення, «усі X — це Y»,
атомарна одиниця «X завжди робиться через {____}»). У v2 — **перший абзац
блоку** часто `<p class="lead">`: місток від попереднього прикладу («До цього
моменту…», «На попередній парі…»). Нюанси, винятки й крайові випадки — після
того, як база стала «очевидно правдивою». Лягає на наявний формат: lead =
місток + безумовна істина → приклад/код → `.callout tip` «Зверніть увагу»
(нюанси) → `theory-deeper` (глибше). Еталон темпу — пари 9–10.

**2. «Як я міг би це відкрити сам?»** Прибирати відчуття довільності. Кожен новий
крок у поясненні й у коді має бути вмотивований: *чому пробуємо саме це? чому цей
рядок?* Не подавати готове рішення як факт з неба — вести коротким шляхом
відкриття. Це та сама вимога, що лікує «AI-tell tone» (див. [[teacher-materials-voice-rule]]):
замість «Отже, використаємо `groupby`» → «Нам потрібно число по кожній категорії
окремо — саме це робить `groupby`».

**3. Правила питань** (`#checkpoint`, `#exit-ticket`, `quiz.json`):
- кожен варіант — гола теза, **без** «тому що …»; усе пояснення — у відповіді
  викладача (`.lh-teacher-note`) / полі `explanation`;
- писати спочатку правильний варіант, тоді мутувати його в дистрактори в тому ж
  каркасі, тій же довжині й регістрі;
- дистрактори = реальні хибні уявлення студентів (спокусливі, не хитрі), не
  випадкові абсурди;
- жодного асиметричного форматування (правильний не довший, не жирніший);
- якщо правильну відповідь видно «на холодну», не читаючи умови — переписати.

**4. Перевірка DAG залежностей.** Перед впорядкуванням тем у парі (і при
перейменуванні заголовків, крок 3) — переконатися, що кожен «корінь» справді
безумовна істина, а не замаскована теорема, яка спирається на ще не пройдений
матеріал. Якщо блок потребує поняття з пізнішої пари — або винести залежність
уперед, або звести пояснення до безумовної форми.

**5. Контекст даних перед ITSTEP-кодом (еталон — пари 9–10).** Якщо завдання
бере датасет, індекс колонки або API «з повітря» — студент має знати **навіщо**,
ще до розбору рішення. Перед `.callout example` додати `.callout tip`:

- **Звідки дані** — що за набір (`load_diabetes`, `make_regression`…), що таке
  `X` і `y` (одиниці, що **не** є ціллю: не 0/1, не «цукор», якщо це прогресування).
- **Чому саме цей рядок** — напр. `X[:, 2]` = BMI; `reshape(-1, 1)` бо sklearn
  чекає 2D; `random_state=42` щоб поділ був відтворюваний.
- **Що дає результат** — що означають числа в таблиці метрик / перші 10 рядків
  порівняння; орієнтир порядку величини (MAE ≈ 52, R² ≈ 0.23 для BMI).
- **Місток v2** — блок типу `#v2-bridge-*` перед першим завданням на реальних
  даних: іграшковий приклад → той самий API → медичний/реальний датасет.

Не дублювати весь розбір у callout — лише мотивацію; формули й код лишаються в
solution. Responsible AI tip не замінює «Звідки дані».

---

## 12. Material v2.0 + простий шлях + таймінг

**Еталон усього skill:** global_index **9** і **10** (`m03/pair_01`, `m03/pair_02`).
Перед роботою над новою v2-парою — **прочитати їх цілком**, не лише розділ 12.
Також v2-шар мають пари **11–14** (`m03/pair_03`…`pair_06`: градієнтний спуск,
множинна регресія, валідація/CV, поліноми+дерева+класифікація) — приклади
«10–12 v2-блоків з ігор, чисел і життєвих аналогій» для абстрактних тем;
білд-скрипти в `<scratchpad>` тих сесій (`build_p11.py`…`build_p14.py`,
`v2common.py`) як зразок string-replace по якорях. `versions.json`
`overrides.2.0.pairs` = `[9…14]`.

**Коли:** матеріал «занадто заумний» — не переписувати v1 одразу, а додати **v2.0
шар** у той самий `presentation.html`. У `versions.json` → `overrides.2.0.pairs` —
це **global_index**, не номер модуля.

### 12.1. Версії матеріалів

Конфіг: `backend/data/courses/python_ai_step/versions.json`.

| Поле / атрибут | Сенс |
|----------------|------|
| `active` | версія перегляду в admin / `?material_version=` |
| `student_active` | версія на публічному `/course/…` для пар з overrides |
| `data-material-version="1.0"` | стара теорія (deep-dive, OLS, sklearn API) |
| `data-material-version="2.0"` | нові прості блоки |
| без мітки | спільні блоки (ITSTEP, checkpoint, exit ticket) |

Правила:
- v2-блоки — **нові** `<article id="v2-…">` **перед** відповідною v1-теорією.
- v1-теорію й `extra-deep-dive` позначити `data-material-version="1.0"`.
- Lead у banner: два `<div data-material-version="…"><p class="lead">` (не на `<p>` —
  фільтр працює лише на `article|section|div`).
- Admin toolbar (`python_ai_step`): **«Студенти vX»** (публікація) + **«Версія vX»**
  (перегляд у редакторі) — два незалежні селектори.
- Публічний URL `/course/python_ai_step/pairs/N/…` — без `?material_version=`; версія
  з `student_active` + `overrides`.

Код: `backend/app/material_version_blocks.py`, `course_versions.py`, `course_api.py`.

### 12.2. Простий шлях (голос v2) — пиши одразу повністю

**Заборонено:** «скелет v2» (3–4 блоки + v1-мітки) з обіцянкою «допишемо приклади
пізніше». **Одразу** — повний маршрут як у парах 9–10.

**Кожен v2-блок:**
1. `<p class="lead">` — місток від попереднього блоку / попередньої пари.
2. Життєвий приклад або runnable код **до 15 рядків**.
3. Коротке пояснення без заумних термінів; v1 лишається позаду.

**Пара 9** (`m03/pair_01`) — еталон регресії, блоки v2 (порядок у файлі, v4):
`v2-ml-idea` → `v2-example-hours` → `v2-example-price` → `v2-example-delivery` →
`v2-example-formula` → `v2-example-manual-predict` → `v2-regression-problem` →
`v2-bridge-diabetes` → `[itstep-task-1]` → `v2-regression-line` →
`v2-example-scatter` → `v2-residual-simple` → `v2-one-feature` →
`[itstep-task-2]` → `v2-workflow` → `[міні-задачі]` → `[checkpoint]`.

**Пара 10** (`m03/pair_02`) — еталон метрик, блоки v2:
`v2-metrics-start` → `v2-mae-by-hand` → `v2-example-grade-errors` →
`v2-mse-by-hand` → `v2-metrics-intro` → `v2-mae-mse` → `v2-r2-by-example` →
`v2-r2-simple` → `v2-loss-simple`.

**Не** починати v2 з `E[Y|X]`, `RegressorMixin`, `scoring='neg_mse'` — це v1 або
`theory-deeper`. Спочатку: ML у трьох кроках (дані → `fit()` → `predict()`),
години→оцінка, площа→ціна, MAE/MSE «на пальцях».

### 12.3. Таймінг required / optional

| Поле | Де | Сенс |
|------|-----|------|
| `data-pair-minutes="80"` | `<main class="stage">` | ціль пари |
| `data-pair-start="18:30"` | `<main class="stage">` | старт для годинників |
| `data-timing="required"` | `<article>` | входить у 80 хв |
| `data-timing="optional"` | `extra-*`, homework, SI… | поза 80 хв, **(опц.)** у strip |
| `data-minutes` | `.block-timer` | планові хвилини |
| `data-minutes-min` / `-max` | `.block-timer` | допустимий коридор |

**Сума `required` = 80** окремо для v1-path і v2-path (перевіряє `check_lectures.py`).

Приклад v2-path (пара 9): ~11 intro-блоків v2 + shared ITSTEP/checkpoint/practice/exit
= 80 (точна сума — у файлі; не вгадувати, прогнати `check_lectures.py --pair 9`).

Модулі:
- `backend/app/lesson_timing.py` — parse, schedule, `apply_lesson_timing`
- `course_api.py` — після material-version filter і перед `presentation_chrome.inject`
- `presentation_chrome.py` — `recalcTiming()` в editor mode при toggle «Показувати»

UI викладача: `.lh-timing-summary` («80 хв обовʼязково · +N хв опційно»),
`.pill.optional` — пунктир у timing-strip.

### 12.4. Порядок роботи v2-пари

1. **Прочитати цілком** `m03/pair_01` або `pair_02` — темп, lead, кількість прикладів.
2. Скопіювати структуру v2-блоків під тему нової пари; **одразу** lead + приклади +
   timers + `data-timing` (орієнтир: `tools/patch_pairs_9_10_v2.py`,
   `tools/patch_pairs_9_10_timing.py` — лише як шаблон, не заміна ручного тексту).
3. Оновити `versions.json` (`overrides.2.0.pairs`, за потреби `student_active`).
4. `check_lectures.py --pair N` (0/0) + `pytest test_lesson_timing.py`.
5. Deploy: `presentation.html` + при зміні backend — `lesson_timing.py`,
   `course_api.py`, `course_versions.py`, `presentation_chrome.py`, frontend static;
   **перевірити import app + HTTP 200**.

### 12.5. Типові помилки

- Плутати **пару 9** (global_index) з **модулем 9** (LLM, m09).
- **Скелет v2** замість повного маршруту — робити одразу як пари 9–10.
- Patch-скрипт без ручних `<p class="lead">` — текст сухий, без містків.
- `data-material-version` на `<p>` — не фільтрується; обгортати в `<div>`.
- Дублювати `data-material-version` двічі на одному `<article>`.
- Push `presentation_chrome.py` з незакритим `"""` у `_CSS` — **500 на всьому сайті**.
- Рахувати всі `data-minutes` разом для v1+v2 — має бути **два** required-path по 80.

### 12.6. Технічний чекліст після аналізу пар 9–12 (v4→v5, 2026-09-05)

Пари 9 і 10 будувались кілька заходів, 11 і 12 — з нуля цим скілом; повторні
скарги користувача на тих самих парах виявили системні прогалини, яких
розділи вище не покривали. Тепер це **обов'язкові кроки** для кожної нової
v2-пари, не «якщо згадаєте»:

**A. Тултіпи — `<code class="mv">`, інакше вони мовчать.** Рушій
`term-glossary.js` навмисне пропускає `<code>` (`SKIP_TAGS`), а майже кожен
математичний символ (`w`, `b`, `lr`) і скорочення API живуть саме в
`<code>`. Без винятку глосарій підсвічує лише слова в звичайному тексті.
Патч (одноразово на файл): у `shouldSkip()` додати виняток —

```js
if (tag === "CODE" && el.classList && el.classList.contains("mv")) {
  el = el.parentElement;
  continue;
}
```

Далі — позначити `class="mv"` **усі** інлайн `<code>…</code>` поза повними
`<pre><code class="language-python">` комірками (regex-заміна `<code>` →
`<code class="mv">` до/після кожного `<pre><code class="language-python">…
</code></pre>`, самі RUNNABLE-комірки не займати). Це виконати для кожної
пари, що отримує v2, а не лише коли хтось поскаржиться на конкретне слово.

**B. Аудит слів, яких немає в глосарії.** Після (A) пройтись по новому
v2-тексту й переконатись, що зареєстровані: односимвольні `w`, `b`,
скорочення (`lr`, `GD`, `seed`), назви датасетів (`diabetes`, `california
housing`), і — окремо — **відмінки українських слів**: рушій зіставляє
рівно ту стрічку, що в `keys` (case-insensitive, але не стемінг), тож
«епоха» не покриє «епохи»/«епох»/«епоху». Додавати кожну форму, що реально
трапляється в тексті пари, окремим ключем тієї самої tip-групи.

**C. `pyodide_http.patch_all()` — обов'язково, якщо пара використовує
мережеві датасети.** Будь-який `fetch_california_housing()` /
`fetch_openml()` тощо падає в браузерному Pyodide з `URLError: unknown url
type: https` — стандартний `urllib` там без реального HTTPS-хендлера.
Перевірити (і за потреби пропатчити) `pair-notebook.js` пари **до** того,
як додавати v2-контент з такими датасетами:

```js
await runtime.runPythonAsync(HELPERS);
try {
  await runtime.loadPackage("micropip");
  await runtime.runPythonAsync(
    "import micropip\n" +
    "await micropip.install('pyodide-http')\n" +
    "import pyodide_http\n" +
    "pyodide_http.patch_all()\n"
  );
} catch (error) { /* офлайн чи недоступний PyPI — решта сесії працює далі */ }
pyodide = runtime;
```

Якщо кілька пар мають побайтово ідентичний `pair-notebook.js` (звичайна
ситуація — перевірити `md5`), патчити один і розкопіювати на решту.

**D. Перевіряти код виконанням, не лише `ast.parse`.** `ast.parse`
ловить синтаксичні помилки, але не ловить **змістову** поламаність —
напр. дві конкатеновані чернетки в одному `<pre>`, де перша половина щось
визначає й ніколи не використовує, а друга тихо все перевизначає. Такий
код синтаксично чистий і пройде `check_lectures`, але це сміття. Перед
тим, як лишати legacy (v1) solution-код чужим, — виконати його
(`exec()` ізольовано мінімум, а для нового контенту — **реальним кліком
по кнопці «Запуск»** у відрендереній прев'ю-сторінці: знайти
`.lh-nb-source` textarea з потрібним фрагментом коду, її `.lh-nb-cell`,
натиснути `.lh-nb-run`, прочитати `.lh-nb-output`). Ізольований `exec()`
підтверджує, що код коректний; клік по кнопці підтверджує, що коректний
саме **цей харнес** (мережа, пакети, DOM-обвʼязка).

**E. Інтерактивні демо — коли текст самого поняття «крок» чи «напрям» не
відчувається на статичному графіку.** Патерн (Chart.js, уже підключений
CDN-скриптом на сторінці): `<canvas>` + кнопка «Запустити» + `<span>`
з живим текстом-підсумком, у `.viz` всередині блоку; JS — окремий
`<script>` перед `</body>` із власним `DOMContentLoaded`, повторно
використовує кольори сторінки (`--accent`, `--blue`, `--warm`, `--mute`,
`--ink`, `--line` з `:root`). Кожен клік стартує з нового випадкового
значення й анімує крок за кроком до того самого мінімуму — так студент
бачить «незалежно від старту результат один». `data-timing="optional"`,
без `<label class="block-timer">` — не займає бюджет 80 хв. Перед
деплоєм — обов'язково реальний клік у браузері (не лише `node --check`
на синтаксис): за потреби відкрити відрендерену сторінку в
Browser-інструменті, клікнути кнопку, прочитати результат.

**F. Lead — розгорнутий абзац, не одне речення.** І v1, і v2
`<p class="lead">` мають explicit пояснювати: звідки ми йдемо (звʼязок із
попередньою парою), що саме сьогодні робимо, навіщо. Одне сухе речення —
привід розширити, коли просять «розгорнутіше», а не привід сперечатись,
що воно вже є.

**G. Наскрізний приклад можна тягнути через кілька пар поспіль.**
Флагманський життєвий приклад (DOU-зарплати — досвід → зарплата) не
обов'язково зупиняти на 1–2 парах: пара 11 (градієнтний спуск) отримала
ручний GD на тих самих даних із порівнянням до `LinearRegression`; пара 12
(множинна регресія) — той самий зріз + похідна ознака (`level` із
`experience_years` через `pd.cut`), чесно позначена як похідна, не окреме
джерело. Продовжувати наскрізний приклад — коли тема пари природно на
нього лягає, не штучно.

**H. Що вже мало стати звичкою (не забувати при переносі скілу на нові
пари):** контекстний callout «Звідки дані і навіщо» перед кожним
`#itstep-task-N` (§11 п.5); перший solution першого завдання —
`<details open>`; checkpoint і exit ticket — в кінці пари, не одразу
після першого завдання (§0 крок 7); перевірка на «Stretch · поза вікном
80 хв» на завданнях, чиї хвилини насправді входять у суму 80 (пара 12
task-3/4 — такий кейс було знайдено й виправлено).

---

## Пов'язане

[[step-web-lectures-workstream]] · [[step-pair-polish-workflow]] · [[teacher-materials-voice-rule]] · [[editor-mode-block-visibility]] · [[itstep-source-materials]] · [[amos-learn-teaching-skill]] · `backend/app/lesson_timing.py` · `backend/app/material_version_blocks.py` · `AGENTS.md` · `.cursor/rules/course-content.mdc`
