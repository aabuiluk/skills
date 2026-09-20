# Локальний каталог методичних матеріалів і джерел

Зріз **усього, що доступно на цьому ПК** для викладання Python / AI / Data Science у кластері lesson_helper.

- **ПК:** `DESKTOP-GREEN`
- **Зібрано:** 2026-09-20 (живий scan дисків, не лише індекси)
- **Корінь:** `c:\Users\Green\PycharmProjects\pet_projects\lesson_helper`
- **Журнал:** http://127.0.0.1:3004 · прод: https://csctemplate.pythonanywhere.com

Це **методичний покажчик**: що є, навіщо, як брати, чого не відкривати першим. Повні таблиці пар і автолічильники лишаються в [`MATERIALS_INVENTORY.md`](MATERIALS_INVENTORY.md). Куди йти за задачею — [`MATERIALS_ROUTING.md`](MATERIALS_ROUTING.md). Кластер сусідів — [`CLUSTER.md`](CLUSTER.md).

Авторські PDF, повні витяги книжок і транскрипти **не публікувати**. У слайд студентам — факт / схема / один приклад / одна пастка, не розділ книжки.

---

## 0. Як обрати джерело за 10 секунд

| Потрібно | Брати звідси | Не брати звідси |
|----------|--------------|-----------------|
| Веб-лекція 80 хв для групи Python61 | `python_ai_step` (еталон структури 9–10, пояснень 16–18) | інші `python_ai_*`, доки власник не назвав курс |
| Методичка Materials + zip | `python_ai_materials` → KB → веб → `lesson_materials/` | Additional / Modify / step |
| Офіційна програма / практика / ДЗ ITSTEP | `knowledge_materials_prepared/courses/od/` | сирий `data/` і PDF з `D:\` |
| Факт / схема для слайда | `books_prepared/` (Грокаємо…) або один розділ з `knowledge_materials_prepared/books/` | увесь том, `books/*.pdf` |
| Пререквізит NetAcad | `knowledge_materials_prepared/courses/netacad/` | повторний скрейп LMS |
| Транскрипт відеоуроку | `knowledge_materials_prepared/videos/courses/` (лише уроки з субтитрами) | mp4 з `data/` чи `D:\` |
| Нотатка викладача / аркуш 1–N | `query_teacher_kb.py --note` / `--sheet` | цитувати sqlite-id студентам |
| Авторський курс 180 хв / тема | `astra/` (37 готових HTML) | копіювати з журналу в Astra і навпаки |
| Python Core / КОЛ | `python_kol` + OD `python-core-3680` | AI-пари step як заміна КОЛ |
| Інтернатура QAA | `intern_dmytro` / `intern_ofelya` | AI-курси |
| Кар’єра / roadmap.sh / патерни Guru | сусід `roadmap/kb/` (`python -m kb search …`) | glob `roadmap/data/` |
| Дороге вже добуте знання | `knowledge_saver/INDEX.md` | overwrite `deposits/*/raw/` |

Густина джерела: **не підставляти розділ книжки / годину відео замість лекції.**

---

## 1. Кластер на цьому ПК

Три репозиторії + диск оригіналів. Карта: `CLUSTER_CATALOG.json` (згенеровано 2026-09-20).

| Проєкт | Шлях | Роль | URL |
|--------|------|------|-----|
| **lesson_helper** | `C:\Users\Green\PycharmProjects\pet_projects\lesson_helper` | Журнал, веб-пари, текстовий корпус, роздатки, Astra | `:3004` |
| **bender** | `C:\Users\Green\PycharmProjects\pet_projects\bender` | Качає OD / NetAcad у `D:\knowledge_materials` | Django `:3003` |
| **roadmap** | `C:\Users\Green\PycharmProjects\pet_projects\roadmap` | Офлайн roadmap.sh / ProfDevMap / книги, FTS `kb/` | `:8000` |
| **диск** | `D:\knowledge_materials` | Сирі PDF / LMS / mp4 (власник: bender) | — |

Усі три проєкти **існують** локально. Fallback bender: `bender/knowledge_materials/` (`vertushka/`, `virt/`).

Обмін індексами: `python -m cluster publish`. Копія файла: `python -m cluster copy --from <proj> --src <rel> --to <proj>`.

У **roadmap** для фактів: `python -m kb search …` → `get`. Шість баз: `roadmap`, `profdev`, `academy`, `guru`, `gitbybit`, `books`. Не glob `data/`.

---

## 2. Курси журналу (готові веб-пари)

Шлях: `backend/data/courses/<slug>/`. Відкриття: `/course/<slug>`.

| Slug | Назва | Пар | presentation.html | Журнал |
|------|-------|----:|------------------:|--------|
| `python_ai_step` | Штучний інтелект із використанням Python (канон групи) | 50 | 51 | http://127.0.0.1:3004/course/python_ai_step |
| `python_ai_step_materials` | Робоча копія матеріалів до step | 50 | 51 | `/course/python_ai_step_materials` |
| `python_ai_materials` | Методичний шар Materials | 50 | 50 | `/course/python_ai_materials` |
| `python_ai_additional_materials` | Additional Materials | 50 | 50 | `/course/python_ai_additional_materials` |
| `python_ai_modify_materials` | Modify | 50 | 51 | `/course/python_ai_modify_materials` |
| `python_ai_codex_modify_materials` | Codex Modify | 50 | 50 | `/course/python_ai_codex_modify_materials` |
| `python_ai_cursor_modify_materials` | Cursor Modify (джерело step) | 50 | 51 | `/course/python_ai_cursor_modify_materials` |
| `python_ai` | Ранній шар | 50 | 50 | `/course/python_ai` |
| `python_ai_cursor` | Cursor-шар | 50 | 50 | `/course/python_ai_cursor` |
| `python_ai_codex` | Codex-шар (презентацій немає) | 50 | 0 | `/course/python_ai_codex` |
| `python_kol` | Основи програмування на Python (КОЛ) | 94 | 95 | `/course/python_kol` |
| `intern_dmytro` | Інтернатура QAA Python · Дмитро | 20 | 20 | `/course/intern_dmytro` |
| `intern_ofelya` | Інтернатура QAA Python · Офелія | 20 | 20 | `/course/intern_ofelya` |

Також є `_backups/` у тому ж каталозі курсів — не матеріал для пари.

**Правило ізоляції:** без явної назви курсу працюємо в `python_ai_step` (група) або `python_ai_materials` (методичка). Інші `python_ai_*` не чіпати як side effect.

Повний список 50 / 94 / 20 пар — у [`MATERIALS_INVENTORY.md`](MATERIALS_INVENTORY.md) §1.

### 2.1. `python_ai_step` — канон ITSTEP 2.0.0, 50 × 80 хв

Офіційна програма: https://materials.itstep.org/content/beef810f-be75-4b3c-9c1b-a8124a1a4b01/uk  
Пререквізити групи: Python Core + NetAcad (Modern AI, IBM SkillsBuild, Data Science Essentials with Python).

| Модуль | Пар | Тема |
|-------:|----:|------|
| 1 | 2 | Вступ до ШІ та науки про дані |
| 2 | 6 | Обробка та аналіз даних (NumPy, Pandas, статистика, Matplotlib) |
| 3 | 6 | Алгоритми навчання з учителем |
| 4 | 6 | Основи нейронних мереж / PyTorch |
| 5 | 5 | CNN і комп’ютерний зір |
| 6 | 5 | NLP |
| 7 | 6 | Навчання без учителя / рекомендації |
| 8 | 6 | Generative AI / Vertex AI |
| 9 | 6 | LLM-фреймворки (LangChain) |
| 10 | 2 | Іспит |

**Еталони якості всередині step:**

| Що | Де |
|----|----|
| Структура пари, v2-голос, teacher-нотатки | пари **9–10** (`m03/pair_01`, `m03/pair_02`) · скіл `common_lesson` |
| Густина інформації Materials | пари **11–16** · `gold-11-16.md` / `gold-15-16.md` |
| Пояснення фактами + схема + тултіпи | пари **16–18** (`m04/pair_02`–`pair_04`) · `explaine_simple` / `gold-16-18.md` |
| Унікальний акцент на кожну з 50 пар | `backend/data/courses/python_ai_step/CursorRecomendation/` (464 файли) і `CodexRecomendation/` (325 файли) |
| Прототип зон сторінки | `frontend/public/prototype-pair17-blocks.html` · скіл `tactic_of_cource_building` |

Файли типової пари: `presentation.html`, `teacher.md`, `plan.json`, `manifest.json`, `term-glossary.js`, словник. `public_plan.json` **не чіпати** (галочки лише власник).

Рекомендації Cursor: `CursorRecomendation/INDEX.md` + `SOURCES.md`. Це шар для викладача, не студентський слайд.

### 2.2. `python_kol` — 19 модулів, 94 пари

M1 змінні → M19 іспит: типи, розгалуження, цикли, рядки/списки, колекції, функції, типізація, винятки, файли, ООП (14 пар), unittest/pytest, concurrency, NumPy/Pandas/Matplotlib, патерни, SOLID, AI для програміста. Список пар — інвентар §1.

### 2.3. Інтернатури QAA

По 10 тижнів × 2 пари (теорія / практика+проєкт). Дмитро: pytest → API → UI → фреймворк → SQL → Git/CI → flaky. Офелія: додатково QA mindset і test design перед pytest.

---

## 3. Студентські роздатки (zip / пакети)

У git. Пакет `PythonAI61_LessonN_LessonM` = дві пари. Збирати **білдером** після веб-пари, не руками.

| Каталог | Курс | Пакетів | Zip | Примітка |
|---------|------|--------:|----:|----------|
| `lesson_materials/` | python_ai_materials | 25 | 0 | канонічний роздаток Materials |
| `additional_lesson_materials/` | additional | 25 | 0 | + `assessments/` |
| `modify_lesson_materials/` | modify | 25 | 0 | + `assessments/` |
| `modify_codex_lesson_materials/` | codex modify | 25 | 0 | + `assessments/` |
| `modify_cursor_lesson_materials/` | cursor modify | 25 | 0 | + `assessments/` |
| `step_lesson_materials/` | python_ai_step | 26 | 25 | є окремий `Lesson16_17_18`; + `assessments/` |
| `student_presentations/` | ранні HTML | — | — | пари 1–2 + словник |

У `student_presentations/`: `pair_01_vstup_do_shi.html`, `pair_02_datasety_jupyter.html`, `SLOVNYK_TERMINOLOGII.html` / `.md`, `term-glossary.js`, `build_slovnyk.py`.

`lessons/` — немає (legacy).

У zip **не** класти `teacher.md`, `plan.json`, окремий словник (словник запікається в HTML). У `results/` — офіційні 1–N, **без X.1**.

---

## 4. Офіційні сторінки ITSTEP (OD) — програма, практика, ДЗ

Текстовий корпус: `knowledge_materials_prepared/courses/od/`. Старт: [`knowledge_materials_prepared/INDEX.md`](knowledge_materials_prepared/INDEX.md) і [`courses/INDEX.md`](knowledge_materials_prepared/courses/INDEX.md).

Це **не** студентський слайд. Протокол: знайти тиждень `wNN` → **одна** сторінка в `pages/` → задачі X.1 на слайд без розв’язку.

| Програма | Папка OD | HTML | Роль |
|----------|----------|-----:|------|
| Штучний інтелект з Python 2.0.0 | `python-ai-3158` (`PYTHON AI_3158`) | 109 | **первинне** джерело сценаріїв / практики / ДЗ для AI-курсу |
| Те саме, додаткові матеріали OD | `ai-python-3161` (`AI PYTHON_3161`) | 41 | рекомендовані книжки, відео, ДЗ/практика OD |
| Python Core 2.0.2 | `python-core-3680` (`PythonCore_3680`) | 55 | сценарії КОЛ, практика, ДЗ |

Приклади з 3158 (неповний; повна таблиця в `COURSE.md`): ДЗ/практика 1.1–2.2 (вступ, змінні), 3.x розгалуження, 4.x цикли, 5.x рядки/списки, 6.x функції, Git 9.1–9.2, ООП 9.x, файли 8.x.

Приклади з 3161: програма курсу ШІ 2.0.0, практика/ДЗ модулів 1–10 (NumPy, Pandas, Matplotlib, статистика, supervised, NN, CV, …).

UUID програми курсу `beef810f-…` — **не** лінк на практикум.

Локальні HTML аркушів інколи ще лежать у gitignored `data/faily/` (якщо є). Для фактів спочатку prepared.

---

## 5. NetAcad (пререквізит групи)

Текст: `knowledge_materials_prepared/courses/netacad/`. Оригінал: `D:\knowledge_materials\netacad\`.

| Курс | Уроків | Навіщо в парі |
|------|-------:|---------------|
| Introduction to Modern AI | 86 | визначення ШІ, межі, етика — модуль 1 |
| AI Fundamentals with IBM SkillsBuild | 8 | короткий фундамент IBM |
| Data Science Essentials with Python | 61 | DS-пререквізит |
| Data Analytics Essentials | 322 | аналітика (брати один урок, не курс) |
| Find Insights with AI | 93 | інсайти / застосування |
| Prompt Like an Engineer | 78 | промпти (модулі 8–9) |
| Build your Resume with AI | 71 | кар’єрний AI, не ядро програми |

Також уроки NetAcad як «статті»: `knowledge_materials_prepared/articles/netacad/` (**156** md на диску).

---

## 6. Книжки

Два корпуси. PDF у git **не** їдуть. У контекст агента — **один розділ**, не том.

### 6.1. `books_prepared/` — чотири книжки для схем слайда

Старт: [`books_prepared/INDEX.md`](books_prepared/INDEX.md) + `topic-index.json`. Паспорти / карти в git; `chapters/` — gitignored, **є на цьому ПК**.

| Slug | Книжка | Розділів | PDF на диску | Коли брати |
|------|--------|---------:|--------------|------------|
| `grokking-algorithms` | Бхаргава, Грокаємо алгоритми | 11 | `books/Bhargava_….pdf` (14.6 МБ) | схеми explaine_simple: пошук, рекурсія, графи, DP, kNN |
| `grokking-deep-learning` | Траск | 19 | `books/Trask_….pdf` (15.9 МБ) | NN з нуля на NumPy: forward, GD, backprop, CNN, embeddings, RNN |
| `grokking-streaming` | Фішер / Ван | 12 | `books/Van_….pdf` (9.6 МБ) | потік, вікна, watermark; код у книжці Java — на слайд концепцію |
| `impractical-python` | Воган | 27 | `books/Vogan_….pdf` (60.4 МБ) | лабораторна 80 хв (проєкт як носій), не єдина теорія модуля |

Карта глава → тема пари вже в INDEX (бінарний пошук = ch.1, dropout = GDL ch.8, …).

### 6.2. `knowledge_materials_prepared/books/` — 17 книжок OD

Старт: [`books/INDEX.md`](knowledge_materials_prepared/books/INDEX.md).

| Slug | Назва | Розділів | Сторінок | Навіщо |
|------|-------|---------:|---------:|--------|
| `build-your-own-ai-investor` | Build Your Own AI Investor… | 7 | 281 | табличний ML-пайплайн, не DL |
| `essentials-of-python-for-ai-ml` | Essentials of Python for AI/ML | 11 | 524 | NumPy / Pandas / viz / MLOps |
| `generative-ai-with-langchain` | Generative AI with LangChain | 10 | 361 | промпт, ланцюг, RAG (модулі 8–9) |
| `generative-ai-with-python-and-tensorflow-2` | GenAI + TF2 (VAE/GAN) | 13 | 489 | концепції генерації; код застарілий |
| `learning-opencv-5` | Learning OpenCV 5 | 4 | 115 | кадр, фільтр, детектор |
| `opencv-dnn-computer-vision` | NN CV with OpenCV 5 | 11 | 309 | DNN-модуль OpenCV, міст до CV |
| `practical-explainable-ai` | Practical XAI | 14 | 356 | SHAP / LIME |
| `pro-deep-learning-tf2` | Pro Deep Learning TF2 | 6 | 667 | математика DL; на слайд — NumPy/PyTorch |
| `python-scientific-computing-ai` | Python for Scientific Computing | 21 | 334 | лінал як ґрунт ML |
| `python-beginners-guide-to-ai` | Beginner's Guide to AI | 24 | 662 | оглядний AI |
| `mastering-python-for-web` | Mastering Python for Web | 6 | 303 | веб/API, не AI-пари |
| `python-crash-course` | Python Crash Course, 3rd | 20 | 554 | еталон початкового Python |
| `python-complete-guide` | Python. Исчерпывающее руководство | 10 | 368 | довідник мови |
| `quick-python-3` | Quick Python 3 | 54 | 129 | мінімум синтаксису |
| `the-python-book` | The Python Book | 33 | 275 | мова → pandas/plot/API |
| `big-book-of-python-projects` | Большая книга проектов Python | 80 | 432 | 81 мініпроєкт на лабораторну |
| `znakomstvo-s-python` | Знакомство с Python | 21 | 509 | вступ (нарізано сторінками) |

Тема → файли: `knowledge_materials_prepared/topic-index.json`.

### 6.3. PDF-оригінали (gitignored)

`books/*.pdf` — 4 файли, див. §6.1. Не відкривати агенту як перший крок.

---

## 7. Статті та відео (підготовлені)

Старт: [`articles/INDEX.md`](knowledge_materials_prepared/articles/INDEX.md), [`videos/INDEX.md`](knowledge_materials_prepared/videos/INDEX.md).

### 7.1. Статті

| Полиця | На диску | Що це |
|--------|----------|--------|
| `articles/web/` | INDEX з **63 URL** (тіл сторінок немає) | посилання зі сторінок ITSTEP: NumPy, Pandas, Matplotlib, regression, NN, CV, NLP, GenAI, LangChain, Kaggle-датасети |
| `articles/geekforgeeks/` | **10** md | контур Python Foundation |
| `articles/netacad/` | **156** md | уроки NetAcad, придатні як стаття |

Типові хости web-полиці: numpy.org, datacamp, w3schools, GFG, Kaggle, PyTorch tutorials, McKinsey «What is AI», learnprompting.org, OpenAI prompt guide, TensorFlow Playground, chest-xray-pneumonia, Housing.csv.

Живе тіло зовнішньої статті: Playwright MCP → `data/kb_extracts/articles/` (каталогу зараз немає; текст уже в sqlite) або `fetch_articles_mcp.py`.

### 7.2. Відео

YouTube з OD: **47** роликів (ідентифікатор / назва, **без** транскриптів) — `videos/youtube/`.

Відеокурси Udemy/Packt/Pearson: **16** курсів. Транскрипт — лише де є субтитри; mp4 лишається на `D:\`.

| Курс | Уроків | Транскрипти | Тема |
|------|-------:|------------:|------|
| python-for-data-science-machine-learning-from-a-z | 140 | 140 | DS/ML огляд |
| complete-python-developer-in-2022-zero-to-mastery | 277 | 277 | Python developer |
| practical-ai-with-python-and-reinforcement-learning | 121 | 121 | RL / practical AI |
| python-for-absolute-beginners | 101 | 101 | абсолютний початок |
| natural-language-processing-nlp-in-python-with-8-projec | 88 | 88 | NLP + проєкти |
| python-programming-machine-learning-deep-learning-pytho | 59 | 59 | ML/DL |
| advanced-python-python-oop-with-10-real-world-programs | 31 | 31 | OOP |
| skill-up-with-python-data-science-and-machine-learning- | 21 | 21 | DS recipes |
| python-in-practice-15-projects-to-master-python | 98 | 24 | проєкти (частково) |
| computer-vision-projects-with-python-3 | 19 | 0 | лише ідентифікатор |
| learn-opencv-python-2022-computer-vision-course | 37 | 0 | лише ідентифікатор |
| python-3-deep-dive-part-1…4 | 156+134+80+162 | 0 | Deep Dive без субтитрів |
| python-course-learn-oop-by-doing-a-game-project | 18 | 0 | — |

Перезібрати корпус: `python knowledge_materials_prepared/_tools/prepare_knowledge_materials.py`.

---

## 8. База викладача (`teacher_kb`)

Локально на цьому ПК, gitignored. **Не видаляти.**

| Артефакт | Стан 2026-09-20 |
|----------|-----------------|
| `teacher_kb.sqlite` | **є**, 36.49 МБ |
| `teacher_kb.md` | дзеркало для людей (як питати) |
| `data/kb_extracts/` | каталогу немає; текст уже в sqlite |

Таблиці: `notes` 12 · `sheets` 40 · `tasks` 188 · `articles` 58 · `books` 10 · `chunks` 3018 · `videos` 808 · `related_sources` 32 · `pair_hints` 18.

**Нотатки (`--note`):** M1 вступ AI/DS/ML і Jupyter · M2 Matplotlib / NumPy / Pandas / статистика · M3 дерева й регресія · M4 персептрон і PyTorch · M5 CNN · M6 NLP · M7 unsupervised · M8–M10 GenAI/промпти.

**Книжки в KB** (перетин з §6.2): AI Investor, Essentials of Python for AI/ML, LangChain, TF2 GenAI, OpenCV 5, OpenCV DNN, XAI, Pro DL TF2, Scientific Computing, Beginner's Guide to AI.

Запит (зріз, не PDF):

```bash
python backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --info
python backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --note numpy
python backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --sheet practical_2.1
python backend/data/courses/python_ai_materials/tools/query_teacher_kb.py "numpy reshape"
```

Спочатку `--note`, потім `--sheet` для офіційних 1–N, потім короткий FTS.

---

## 9. Astra — авторський курс з першоджерел (180 хв / тема)

Незалежний курс за програмою ITSTEP (58 тем + іспит). Тексти написані заново. **Не** копіює журнал, `teacher_kb` і старі catalog. Навпаки теж: не переносити Astra HTML у журнал без запиту.

| Шлях | Роль |
|------|------|
| `astra/README.md`, `astra/PLAN.md` | правила й політика джерел |
| `astra/index.html` | каталог готових HTML (офлайн) |
| `astra/topic-XX-YY.html` | тема |
| `astra/examples/*.py` | самодостатні демо (stdlib) |
| `scripts/course_build/content/astra/original/` | єдине джерело авторського тексту (json) |
| `scripts/course_build/content/astra/web-syllabus.json` | структура з materials.itstep.org |
| `astra/verification.json` | що зібрано |
| `astra/pair_map.json` | номер пари → id теми (1–58) |

**Живий стан 2026-09-20:** `complete=false`. Готових HTML: **37** (пари 1–37, id `01-01` … `06-04`). Далі в роботі: 22 теми (`06-05` … `09-05` і `10-01`).

Готові зараз:

| Пари | Id | Модуль |
|------|----|--------|
| 1–4 | 01-01 … 01-04 | Вступ, алгоритми, датасети, Jupyter |
| 5–7 | 02-01 … 02-03 | NumPy/Pandas, статистика, Matplotlib |
| 8–19 | 03-01 … 03-12 | Supervised: регресія → бустинг → логістична → кейс авто |
| 20–25 | 04-01 … 04-06 | Нейромережі / PyTorch / Dropout / активації / вади серця |
| 26–33 | 05-01 … 05-08 | CNN / MNIST / batching / архітектури / пневмонія |
| 34–37 | 06-01 … 06-04 | NLP: NLTK, корпуси, TF–IDF/embeddings, Skip-gram/GloVe |

Не видавати missing-теми як готові. Генератор: `python scripts/course_build/astra_build.py --through N`.

---

## 10. `knowledge_saver/` — immutable депозити

Індекс: [`knowledge_saver/INDEX.md`](knowledge_saver/INDEX.md). Оригінали в `deposits/*/raw/` не правити й не видаляти.

На диску **21** депозит:

| id | Тема |
|----|------|
| `2026-09-06_python-kol-program` | Офіційна програма КОЛ |
| `2026-09-07_roadmap_sh_full_site_copy` | Повна локальна копія roadmap.sh |
| `2026-09-08_pair12-mobile-scroll-pa` | Баг мобільного скролу пари 12 |
| `2026-09-08_roadmap-ai-tutor-quiz-prompt` | Промпт AI-тьютора roadmap |
| `2026-09-09_roadmap-local-live-parity-audit` | Паритет live vs local |
| `2026-09-09_roadmap-sh-offline-business` | API-контракти offline |
| `2026-09-11_materials-pairs-15-16-gold` | Gold 15–16 vs тонкий генератор |
| `2026-09-13_step-pairs-17-18-v5-density` | v5 густина пар 17–18 |
| `2026-09-15_cursor-recomendation` | Унікальні пакети на 50 пар step |
| `2026-09-15_eval-mode-explanation` | Dropout / eval / no_grad |
| `2026-09-15_itstep-ai-course-primary-sources` | Матриця першоджерел на 50 пар |
| `2026-09-15_pairs-16-18-ten-steps` | 10 кроків пар 16–18 |
| `2026-09-15_step-v6-audit` | v6 audit completeness |
| `2026-09-16_strategy-of-cource-building` | Меню пар 50×80 як золото syllabus |
| `2026-09-16_tactic-of-cource-building` | Зони сторінки пари |
| `2026-09-16_growth-of-cource-building` | Additive / graft джерел |
| `2026-09-17_step-v14-pairs-1-20` | v14 explaine_simple на 1–20 |
| `2026-09-18_astra-web-syllabus` | Програма Astra з ITSTEP |
| `2026-09-18_books-prepared` | Чотири книжки для слайдів |
| `2026-09-18_knowledge-materials-prepared` | Корпус з `D:\` |
| `2026-09-18_step-v17-inventory-depth` | v17 глибина інвентаря на 17–20 |

Перед новим investigate — перевірити INDEX, щоб не добувати те саме з нуля.

---

## 11. Методичні скіли (локально в `.agents/skills/`)

Каталог: [`docs/ai/SKILLS.md`](docs/ai/SKILLS.md). **71** скіл. Homemade дзеркало: https://github.com/aabuiluk/skills.git.

**Always-on у цьому проєкті** (без запиту):

| Skill | Роль |
|-------|------|
| `python-educator-senior` | персона викладач + senior |
| `teacher-materials-skill` | Materials: KB → веб → zip |
| `common_lesson` | нормалізація step під пари 9/10 |
| `explaine_simple` | факти + схема + тултіпи (16–18) |
| `knowledge-saver` | immutable backup |

Інші teaching: `strategy_of_cource_building`, `tactic_of_cource_building`, `growth_of_cource_building`, `teach`, `scaffold-exercises`, `pptx`/`docx`/`pdf`/`xlsx`, `research`.

Gold-файли: `.agents/skills/teaching/teacher-materials-skill/gold-11-16.md`, `gold-15-16.md`; `explaine_simple/gold-16-18.md`; `strategy_of_cource_building/references/gold-python-ai-step.md`.

---

## 12. Локальні дампи (gitignored) — оригінали, не перший крок агента

### 12.1. `data/` у репозиторії — 158 файлів, ≈ 3.2 ГБ

| Дерево | Файлів | МБ | Зміст |
|--------|-------:|---:|-------|
| `data/AI PYTHON_3161/` | 2 | 274 | Udemy Customer Data Preprocessing (unsolved/solved mp4) |
| `data/faily/gdrive/` | 63 | 1398 | Packt CV, Pearson DS recipes, Udemy NLP/RL/ML, PDF LangChain/TF2/XAI/… |
| `data/Python College/` | 93 | 1541 | Udemy OOP 10 programs, Zero to Mastery 2022, Python 3 Deep Dive Part 2 |

Порожні дерева папок (`Python Core (КБ)…`, `Мова програмування Python…`) ще стоять — файлів 0.

### 12.2. `D:\knowledge_materials` — оригінали OD / NetAcad

Існує. Верх:

- `netacad/` — 7 курсів + `index.json` + `apply-ai-collection.json` (ті самі slug, що в prepared)
- `od/` — `AI PYTHON_3161`, `PYTHON AI_3158`, `PythonCore_3680`

Агент читає **prepared**, не цей диск.

---

## 13. Інше в проєкті, що є джерелом

| Шлях | Що |
|------|----|
| `scripts/course_build/content/` | джерела генераторів (`content_m01_m03.py` …) — для старих шарів, не для ручного step |
| `scripts/course_build/content/astra/` | syllabus + original json Astra |
| `docs/superpowers/specs/` і `plans/` | дизайн Additional / Modify / Codex / Cursor Modify, DOU-зарплати на парах 9–10, live notebook |
| `docs/ai/` | каталог скілів |
| `docs/domain/` | мова домену |
| `frontend/public/prototype-pair17-blocks.html` | прототип chrome / rail / stage / notebook |

---

## 14. Що локальне саме на цьому ПК (не для git / не для публікації)

| Шлях | Факт на 2026-09-20 |
|------|-------------------|
| `books/*.pdf` | 4 PDF, 100.5 МБ сумарно |
| `books_prepared/**/chapters/` | 11+19+12+27 розділів |
| `teacher_kb.sqlite` | 36.49 МБ, повні таблиці |
| `data/` | 3.2 ГБ, 158 файлів |
| `D:\knowledge_materials` | OD + NetAcad оригінали |
| `bender/` і `roadmap/` | сусіди існують |
| `roadmap/kb/` | 6 FTS-баз |

У git лишаються курси журналу, роздатки, паспорти книжок без тексту розділів, `knowledge_saver` (без секретів), Astra HTML.

---

## 15. Куди не варто (повтор маршруту)

- `python_ai` / `cursor` / `codex` як заміна step
- увесь `chapters/` книжки в контекст
- `books/*.pdf`, mp4, `D:\` як перший крок
- `knowledge_saver/deposits/*/raw/` як текст слайда
- внутрішні id KB і «студенти часто…» у HTML студентам
- галочки `public_plan.json`
- генераторні картки `generate_pairs_15_50.py` як матеріал
- змішувати Astra ↔ журнал

---

## 16. Команди обслуговування

```bash
python scripts/refresh_materials_index.py          # дата в ROUTING / INVENTORY
python knowledge_materials_prepared/_tools/prepare_knowledge_materials.py
python -m cluster status
python -m cluster publish
python backend/data/courses/python_ai_materials/tools/query_teacher_kb.py --info
python -m kb search roadmap "asyncio" --kind topic   # з каталогу roadmap
python3 scripts/aabuiluk_skills/sync.py status
```

Щоденна перевірка індексів уже в хуку sessionStart. Цей каталог — ручний зріз змісту; оновлювати, коли змінюється **склад** джерел (нова полиця, новий курс, великий шар Astra), не щодня заради лічильників.

---

## Пов’язане

[`MATERIALS_ROUTING.md`](MATERIALS_ROUTING.md) · [`MATERIALS_INVENTORY.md`](MATERIALS_INVENTORY.md) · [`CLUSTER.md`](CLUSTER.md) · [`knowledge_materials_prepared/INDEX.md`](knowledge_materials_prepared/INDEX.md) · [`books_prepared/INDEX.md`](books_prepared/INDEX.md) · [`knowledge_saver/INDEX.md`](knowledge_saver/INDEX.md) · [`astra/README.md`](astra/README.md) · [`docs/ai/SKILLS.md`](docs/ai/SKILLS.md)
