# План матеріалів: Основи програмування на Python (КОЛ)

- **Програма:** [ITSTEP, версія 1.0.0](https://materials.itstep.org/content/e844379c-9f58-4426-8702-a79a7ef80bfa/uk) · 188 год = **94 пари × 80 хв** · 19 модулів
- **Журнал (скелет):** `backend/data/courses/python_kol/` · `/course/python_kol`
- **Каталог полиць:** [`MATERIALS_AND_BOOKS.md`](../../../MATERIALS_AND_BOOKS.md)
- **Маршрут агента:** [`MATERIALS_ROUTING.md`](../../../MATERIALS_ROUTING.md)
- **Архів програми:** `knowledge_saver/deposits/2026-09-06_python-kol-program/`
- **Дата плану:** 2026-09-20

Мета: наситити вже існуючі 94 веб-пари так, щоб курс **повністю закривав офіційну програму** і був щільнішим за «огляд + snippet». Нових модулів і нових пар не вигадувати. Нове джерело **graft** в існуючу пару (`growth_of_cource_building`), не замінює 80 хв.

Слайд студенту — факт + схема + пастка. Книжку / годину відео на слайд не переказувати.

---

## Як читати таблиці

| Шар | Що це | Коли брати |
|-----|--------|------------|
| **Офіційне** | Пункт програми + аркуші OD (практика / ДЗ / сценарій) | Завжди. Без цього пара не «за програмою». |
| **Ядро** | 1–2 книжки, з яких береться пояснення | Обовʼязково для насичення. |
| **Насичення** | Друга книжка, відео-транскрипт, Guru / O’Reilly, NetAcad | Extra / teacher / нова material-версія. |
| **Лабораторна** | Мініпроєкт на 80 хв або take-home | Практикум модуля, не теорія. |
| **Не брати** | Джерело є на полиці, але ламає КОЛ | Щоб не змішати з Python AI / Astra. |

Протокол читання будь-якої книжки: `BOOK.md` → **один** `chapters/…`. Відео: **один** `lessons/…`. OD: **одна** сторінка `pages/…`.

---

## Пріоритет полиць (увесь курс)

1. **Офіційна програма КОЛ** — цей URL; пункти syllabus не переписувати.
2. **OD Python Core 3680** — практика/ДЗ/сценарії `knowledge_materials_prepared/courses/od/python-core-3680/`. Це **найближчий** ITSTEP-корпус до КОЛ (типи, умови, цикли, рядки, функції, винятки, файли).
3. **OD Python AI 3158** — те, чого немає в 3680: кортежі/множини/словники, Git, ООП 9.1–9.7, паралельне 16.x, GenAI 7. Шлях: `…/courses/od/python-ai-3158/`.
4. **Книжки Core з 3680** (витяги): *Python Crash Course* (Matthes) — хребет початківця; *Python. Исчерпывающее руководство* — щільний довідник; *The Python Book* — огляд до файлів/pandas; *Quick Python 3* — короткий мінімум + тести; *Большая книга проектов Python* — лабораторні; *Знакомство с Python* — запасний вступ.
5. **Відео з транскриптом:** *Python for Absolute Beginners* (101) · *Complete Python Developer 2022 / ZTM* (277) · *Advanced Python OOP with 10 programs* (31).
6. **Guru + O’Reilly (roadmap)** — патерни, SOLID, pytest, asyncio, typing. Текст сторінок не публікувати й не копіювати в HTML студентам; брати факт.
7. **NetAcad, що є на диску** — для модуля 18 (Modern AI, Prompt Like an Engineer). **PCAP: Programming Essentials in Python у програмі є як пререквізит — файлів на цьому ПК немає.**
8. **python_ai_step / Astra / 3161** — лише модулі 13–15 (NumPy/Pandas/Matplotlib) і обережно модуль 18 (що таке AI, не RAG/агенти). Не копіювати лекції AI-курсу в КОЛ.

**Не змішувати:** `python_ai_materials` і zip Materials; контент Astra як «заміна» КОЛ; сирі PDF з `D:\knowledge_materials` і mp4 як перший крок.

---

## Наскрізні діри програми (закрити graft, не новим модулем)

Офіційні **результати навчання** згадують те, чого **немає окремим модулем** у тематичному плані 1.0.0:

| Результат програми | Де закрити в 94 парах | Джерела |
|--------------------|------------------------|---------|
| Система контролю версій | Extra модулів 9 (файли), 11 (тести), 19 (іспит-проєкт) | OD 3158 сценарії 9.1–9.2 + ДЗ/практика Git; roadmap `gitbybit` (250 уроків); ZTM Git-блоки |
| Командна взаємодія | Пара 94 + Git-extra | gitbybit workflow; intern QAA «Git, CI» як зразок ритуалу, не як QA-курс |
| PCEP / PCAP | Deep-study модулів 1–9, 10 | Пререквізит Cisco PCAP **немає локально**. Поки немає дампу — не вигадувати сертифікаційні тести; позначити хук. Качати через **bender**, не glob `D:\`. |
| Функціональне програмування | Уже в модулі 6 (пари 16–17) | Crash Course 8 + Complete Guide 5–6 + Deep Dive Part 1 (слайди, без транскрипту) |

Bender **Python-B** (18 модулів, Помічник `:3003`) — паралельна теорія для M1–10 і Git. Брати формулювання/приклади через карту кластера, не сканувати `bender/` навмання.

---

## Зведена матриця

| М | Год | Пари `python_kol` | Ядро | Офіційна практика | Найкраще насичення |
|--:|----:|-------------------|------|-------------------|--------------------|
| 1 | 2 | 1 | Crash Course 1–2 | 3680 w01–w04 | GFG 01–04 · Absolute Beginners |
| 2 | 4 | 2–3 | Crash Course 5 · Complete Guide 2–3 | 3680 w05–w07 | GFG 05 · W3Schools conditions |
| 3 | 4 | 4–5 | Crash Course 4, 7 | 3680 w08–w10 | GFG 06 · Big Book Collatz / Life |
| 4 | 6 | 6–8 | Crash Course 2–4 | 3680 w11–w13 | GFG 08–09 · Impractical palindrome/anagram |
| 5 | 8 | 9–12 | Crash Course 6 · The Python Book 8–10 | 3158 кортежі/set/dict | Bhargava 5 (хеш) · Deep Dive 3 |
| 6 | 10 | 13–17 | Crash Course 8 · Complete Guide 5 | 3680 w14–w16 | Deep Dive 1 · Fluent/Effective |
| 7 | 8 | 18–21 | Robust Python · Effective Python | *немає аркуша 3680* | Fluent Python typing |
| 8 | 4 | 22–23 | Crash Course 10 · Complete Guide | 3680 w17 | Quick Python errors |
| 9 | 10 | 24–28 | Crash Course 10 · Complete Guide 9 | 3680 w18–w19 · 3158 files | The Python Book files/JSON/Excel |
| 10 | 28 | 29–42 | Crash Course 9 · Complete Guide 7 · OOP 10 programs | 3158 ДЗ/практика 9.1–9.7 | Deep Dive 4 (слайди) · Fluent |
| 11 | 8 | 43–46 | Crash Course 11 · *Python Testing with pytest* | *немає аркуша 3680* | intern pytest · Quick Python Testing |
| 12 | 16 | 47–54 | *Python Concurrency with asyncio* | 3158 16.1–16.2 | High Performance Python |
| 13 | 8 | 55–58 | Essentials NumPy · numpy.org beginners | слайди 3161 NumPy | Scientific Computing · python_ai_step п.3 |
| 14 | 8 | 59–62 | Essentials Pandas · *Python for Data Analysis* | слайди 3161 Pandas | DataCamp/W3 pandas · step п.4 |
| 15 | 8 | 63–66 | Essentials viz · Crash Course 15 | DataCamp Matplotlib | step п.7–8 · Astra 02-03 (факт, не HTML) |
| 16 | 30 | 67–81 | **Guru Dive Into Design Patterns (uk)** | *немає аркуша 3680* | Head First DP · Architecture Patterns |
| 17 | 12 | 82–87 | Clean Architecture / Clean Code · Guru refactoring | *немає аркуша 3680* | Architecture Patterns with Python |
| 18 | 12 | 88–93 | NetAcad Modern AI + Prompt Like an Engineer | 3158 GenAI ДЗ/практика 7 | learnprompting.org · Microsoft genai-for-beginners |
| 19 | 2 | 94 | Усі ядра + Big Book як банк ідей проєкту | критерії допуску з програми | PCEP/PCAP хук |

---

## Модуль 1. Вступ. Змінні та типи даних

**Бюджет:** 2 год → **пара 1** (`m01/pair_01`). Це найтовстіша пара курсу: історія, IDE, інтерпретатор, print/escape, типи, змінні, input, оператори, синтаксичні vs логічні помилки.

### Офіційне

- Програма: пункти 1–18 модуля 1 (історія → помилки) — усі мають з’явитись у цій одній парі (pack remainder; extra винести з 80 хв).
- OD 3680: сценарій уроку 1, урок 1, практика/ДЗ **1.1, 1.2, 2.1, 2.2** (`w01`–`w04`).
- Статті OD Core: PYPL, Programiz I/O, learnpython.org, W3Schools datatypes / operators / variables.

### Ядро

| Джерело | Що брати |
|---------|----------|
| *Python Crash Course* 1–2 | Встановлення, `print`, змінні, рядки, числа |
| *The Python Book* 2, 4, 5 | Старт, типи, оператори |
| *Quick Python 3* «Bare Minimum» | Мінімум синтаксису одним проходом |
| GFG 01–04 | Basics, Variables, I/O, Operators |

### Насичення

- *Знакомство с Python* (сторінками) — запасний російськомовний вступ.
- *Python. Исчерпывающее руководство* гл. 1–2 — пріоритет операторів, літерали.
- Відео: *Python for Absolute Beginners* (перші уроки середовища) · ZTM «Getting started».
- *Python for Scientific Computing* гл. 1 (IDLE) — лише якщо група сидить в IDLE, не як заміна VS Code/PyCharm з програми.

### Лабораторна

- Big Book: «Бейглз» або «Обратный отсчет» — після того, як є `input`/`print`/арифметика.
- Impractical Python гл. 1 (генератор імен, PEP 8) — іменування змінних.

### Не брати

- Astra / python_ai_step «Вступ до ШІ» — інша програма.
- *Fluent Python* — зарано.

---

## Модуль 2. Перетворення типів. Логіка. Розгалуження

**Бюджет:** 4 год → **пари 2–3**.

| Пара | Тема слота |
|-----:|------------|
| 2 | Перетворення типів і логічні оператори |
| 3 | `if` / `elif` / `else`, блок-схеми, тернарний, `match`/`case` |

### Офіційне

- OD 3680: практика/ДЗ **3.1–3.3**, сценарії 5–6, урок 2 (`w05`–`w07`).
- Статті: DigitalOcean type conversion · W3Schools conditions.

### Ядро

- Crash Course **5** (if).
- Complete Guide **2–3** (оператори, структура програми).
- *The Python Book* 11 (if/else; цикли тут не розгортати — модуль 3).
- GFG **05 Flow Control**.

### Насичення

- Absolute Beginners / ZTM — блоки conditionals.
- YouTube OD: Conditionals / Conditions_2 (лише назва/ідея; транскрипту немає).

### Лабораторна

- Big Book: «Чо-хан» або «Морковка в коробке» (гілки).
- Блок-схеми — зі сценаріїв 3680, не вигадувати нотацію.

### Не брати

- `match` з третіх книжок 2010-х, де його немає — офіційний синтаксис з програми + docs.

---

## Модуль 3. Цикли. Відлагоджувач

**Бюджет:** 4 год → **пари 4–5**.

| Пара | Тема |
|-----:|------|
| 4 | `while`, ітерація, `break`/`continue`, вічний цикл, блок-схеми |
| 5 | `for`, вкладені цикли, debugger (крок, breakpoint, вікно змінних) |

### Офіційне

- OD 3680: практика/ДЗ **4.1–4.5**, сценарії 8–9 (`w08`–`w10`).
- Статті: W3Schools while/for · GFG loops · learnpython.org Loops.

### Ядро

- Crash Course **4** (for по списках — узгодити з модулем 4: тут цикл, там методи list) і **7** (while + input).
- Complete Guide **3**.
- GFG **06 Loops**.

### Насичення

- Deep Dive Part 2 Iteration — **немає транскрипту**; слайди Udemy на `D:\` / 3680 PDF. Для викладача, не для слайда.
- ZTM / Absolute Beginners — цикли.
- Debugger: брати з сценарію 3680 + PyCharm/VS Code UI, не з книжки 2017.

### Лабораторна

- Big Book: гіпотеза Коллатца, «Жизнь», ромби, вкладені цикли.
- Impractical: паліндроми (цикл по рядку — місток до модуля 4).

---

## Модуль 4. Рядки, списки

**Бюджет:** 6 год → **пари 6–8**.

| Пара | Тема |
|-----:|------|
| 6 | Рядок як незмінна послідовність, методи, зрізи |
| 7 | f-string, модуль `string` |
| 8 | list vs «класичний масив», генератори, методи, `in`, клонування |

### Офіційне

- OD 3680: практика/ДЗ **5.1–5.3**, урок 3 (`w11`–`w13`).
- Статті: W3Schools strings · GFG 08 String, 09 List.

### Ядро

- Crash Course **2** (рядки), **3–4** (списки).
- *The Python Book* 7, 12.
- Complete Guide **1, 4** (послідовності, протоколи).
- Bhargava **2** (масив vs список) — одна схема, не весь розділ.

### Насичення

- Impractical Python **2–3** (паліндроми, анаграми) і **4–5** (шифр) — лабораторні на рядках.
- Big Book: Цезар, Віженер, «Виселица».
- Deep Dive Part 2 — генератори списків (викладач).

### Не брати

- Pandas Series як «кращий список».
- Regex з *The Python Book* 13 — немає в пункті модуля; extra максимум.

---

## Модуль 5. Кортежі, множини, словники

**Бюджет:** 8 год → **пари 9–12**.

| Пара | Тема |
|-----:|------|
| 9 | tuple |
| 10 | set / frozenset |
| 11 | dict, хеш-таблиці, вкладені словники |
| 12 | Практикум: яку колекцію вибрати |

### Офіційне

- У 3680 **немає** окремих аркушів «кортежі/множини/словники». Брати **3158**: ДЗ/практика кортежі-множини-словники (`w10`–`w11` у COURSE.md 3158).
- Програма КОЛ п.4 — «практичні приклади» = пара 12, не нова тема.

### Ядро

- Crash Course **6** (dict).
- *The Python Book* 8–10 (tuple, dict, set).
- *Quick Python 3* Better Tools (tuple/set).
- Bhargava **5** (хеш-таблиці) — інтуїція `dict`/`set`.

### Насичення

- Complete Guide **4**.
- Deep Dive Part 3 Hash maps — слайди, без транскрипту.
- ZTM — collections.

### Лабораторна

- Big Book: проєкти зі словником (інвентар, підрахунок).
- Пара 12 — таблиця вибору `list` / `tuple` / `set` / `dict` на 3 живих задачах з 3158.

---

## Модуль 6. Функції

**Бюджет:** 10 год → **пари 13–17**.

| Пара | Тема |
|-----:|------|
| 13 | `def`, аргументи, `return` |
| 14 | вбудовані, `math`, `random`, LEGB |
| 15 | `*args` / `**kwargs`, first-class, рекурсія |
| 16 | lambda, `map`/`filter`/`zip`/`reduce`, functools |
| 17 | замикання, каррінг, декоратори |

### Офіційне

- OD 3680: практика/ДЗ **6.1–6.3**, сценарій 14, урок 4 (`w14`–`w16`).
- GFG **07 Functions**.
- Рекурсія / декоратори в 3680 тонкі — добрати з ядра, не з AI-курсу.

### Ядро

- Crash Course **8**.
- Complete Guide **5–6** (функції, генератори — генератори не роздувати, якщо немає в пункті; декоратори — так).
- *The Python Book* Functions and Classes (лише функції).

### Насичення

- Deep Dive Part 1 Functional (156 уроків, **0 транскриптів**) — для викладача: LEGB, closures, decorators.
- O’Reilly *Fluent Python* (functions as objects, decorators) · *Effective Python* (args, closures).
- Impractical гл. 1 PEP 8 — сигнатури.
- Bhargava **3** (рекурсія) — одна схема стека викликів.

### Лабораторна

- Big Book: Фібоначчі, Ханойська башта (рекурсія).
- Не тягнути pygame з Impractical 13–14 сюди.

---

## Модуль 7. Типізація

**Бюджет:** 8 год → **пари 18–21**.

| Пара | Тема |
|-----:|------|
| 18 | динамічна vs статична |
| 19 | type hints |
| 20 | mypy: Optional, list, tuple, dict |
| 21 | кілька значень, функції вищого порядку, lambda |

### Офіційне

- **Аркушів 3680/3158 під typing/mypy немає.** Практика — власні мінізадачі на код з модулів 5–6 + `mypy`. Не вигадувати «офіційне X.1».
- Програма: пункти 1–3 модуля 7 — покрити буквально (`List`/`Tuple` у програмі; у слайді показати й `list[]` сучасний синтаксис як extra).

### Ядро

- O’Reilly **Robust Python** (типи як контракт).
- **Effective Python** (анотації).
- *Fluent Python* (hints) — факт, не глава в слайд.

### Насичення

- *Quick Python 3* не покриває mypy глибоко — лише контраст «без типів».
- Документація mypy — через одну коротку шпаргалку викладача, не dump.

### Не брати

- Pydantic / FastAPI як «типізація курсу» — немає в програмі КОЛ.
- ML-типи з Essentials.

---

## Модуль 8. Винятки

**Бюджет:** 4 год → **пари 22–23**.

| Пара | Тема |
|-----:|------|
| 22 | що таке виняток, `try`/`except`/`finally` |
| 23 | ієрархія, `raise` |

### Офіційне

- OD 3680: практика/ДЗ **7**, сценарій 17, урок 7 (`w17`).

### Ядро

- Crash Course **10** (exceptions-половина).
- Complete Guide (винятки в структурі / I/O).
- Ієрархія `BaseException` → `Exception` → `LookupError` / `ArithmeticError` — як у програмі, зі схемою.

### Насичення

- Effective Python (EAFP vs LBYL) — одна пастка.
- Не підміняти власні ієрархії з Django.

### Лабораторна

- Обгорнути `int(input())` і відкриття файлу (місток до модуля 9).

---

## Модуль 9. Файли

**Бюджет:** 10 год → **пари 24–28**.

| Пара | Тема |
|-----:|------|
| 24 | ФС, директорія, файл, формати, text vs binary |
| 25 | `open` / читання / запис |
| 26 | `with` |
| 27 | операції з директоріями |
| 28 | пошук за маскою, практикум I/O |

### Офіційне

- OD 3680: практика/ДЗ **8.1–8.2** (`w18`–`w19`).
- OD 3158: ті самі файлові аркуші (дубль; брати 3680 як канон).
- **Git (результат навчання):** extra пар 25–28 або 43 — сценарії 9.1–9.2 з 3158 + gitbybit. Не заміняти пару про `open`.

### Ядро

- Crash Course **10** (files).
- Complete Guide **9** (I/O).
- *The Python Book* 14 (files, Excel, JSON, XML) — JSON/Excel як extra, якщо встигаємо; програма каже «формати», тож 1 приклад JSON доречний.

### Насичення

- pathlib vs `os` — показати обидва; офіційні аркуші часто `os`.
- ZTM — files.

### Лабораторна

- Big Book: календар / лог-файл.
- Не Django з Crash Course 18–20.

---

## Модуль 10. ООП

**Бюджет:** 28 год → **пари 29–42** (найбільший модуль).

| Пари | Тема |
|------|------|
| 29 | Інкапсуляція, успадкування, поліморфізм, качина типізація |
| 30–32 | class / object / атрибути / методи / `self` |
| 33–34 | magic, `__init__`, `@staticmethod` / `@classmethod` |
| 35–37 | `__call__`, декоратори методів, `@property`, дескриптори |
| 38–40 | public / `_` / `__`, MRO, поліморфізм |
| 41 | перевантаження операторів |
| 42 | практикум: міні-модель предметної області |

### Офіційне

- OD **3158**: ДЗ/практика **9.1–9.7** (класи → декоратори). Це канон задач модуля.
- 3680 окремого ООП-аркуша немає.

### Ядро

- Crash Course **9** (перші пари 29–32).
- Complete Guide **7** (пари 33–41).
- Відео з транскриптом: **Advanced Python OOP with 10 Real-World Programs** (31 урок) — живий приклад класу, `self`, `__init__`.
- *Quick Python 3* Classes.

### Насичення

- Deep Dive Part 4 OOP (162 уроки, **0 транскриптів**, 235 PDF на диску) — викладач, дескриптори / MRO.
- *Fluent Python* / *Effective Python* — протоколи, magic.
- *python-course-learn-oop-by-doing-a-game* — немає транскрипту; mp4 на `D:\` лише якщо власник відкриває відео сам.
- Crash Course 12–14 (ship/aliens) — **лабораторна пари 42**, не теорія кожної magic-пари.

### Лабораторна

- Пара 42: одна предметна область (геометрія з OOP-10-programs **або** спрощений ship з Crash Course), покрити class + inheritance + один magic.
- Guru / патерни **не** починати тут — модуль 16.

### Не брати

- ML «моделі» sklearn як приклади класів.
- SOLID детально (модуль 17) — лише натяк у парі 29.

---

## Модуль 11. Модульне тестування

**Бюджет:** 8 год → **пари 43–46**.

| Пара | Тема |
|-----:|------|
| 43 | навіщо тести, огляд інструментів |
| 44 | `unittest` |
| 45 | `pytest` |
| 46 | практика на власний модуль (код з M10) |

### Офіційне

- **Аркушів 3680 немає.** Задачі — тести на класи з 3158 9.x і функції з 3680 6.x.
- Програма: огляд інструментів Python — `unittest` + `pytest` (як у меню пар), не Selenium.

### Ядро

- Crash Course **11**.
- O’Reilly **Python Testing with pytest**.
- *Quick Python 3* Testing.

### Насичення

- Інтернатури `intern_dmytro` / `intern_ofelya` — тиждень pytest / дизайн сценаріїв: **ритуал AAA, не QA-фреймворк**.
- Git extra: тест у CI як ідея, без Jenkins.

### Не брати

- Playwright / Selenium з AQA-скілів як зміст модуля.
- Coverage 100% як вимога КОЛ.

---

## Модуль 12. Паралельне та конкурентне програмування

**Бюджет:** 16 год → **пари 47–54**.

| Пари | Тема |
|------|------|
| 47 | concurrency vs parallelism, race, deadlock |
| 48–50 | `threading`, Lock/Event/Semaphore, спільні дані |
| 51–53 | `multiprocessing`, Queue/Pipe/shared memory, Pool |
| 54 | `asyncio`: корутини, gather, Queue; згадка aiohttp |

### Офіційне

- OD **3158**: практика/ДЗ **16.1–16.2** (`w19`–`w20`).
- Програма п.10 згадує **aiohttp** — один мініприклад, не курс по HTTP.

### Ядро

- O’Reilly **Python Concurrency with asyncio**.
- **High Performance Python** (коли threads не дають прискорення через GIL) — одна схема.

### Насичення

- Bender Python-B модуль 14 (паралельне/мережеве) — теорія Помічника.
- Effective Python (concurrency items).
- Не Deep Learning «batch parallelism».

### Лабораторна

- Сума чисел у потоках (як у програмі) + той самий код через ProcessPool — порівняти.
- `asyncio.Queue` — як у пункті 11 програми.

### Не брати

- Kafka / Spark зі *Грокаємо стримінг* — інший курс.
- Мережеві сокети Python-B, якщо їх немає в КОЛ (у КОЛ є aiohttp, не raw socket).

---

## Модуль 13. NumPy

**Бюджет:** 8 год → **пари 55–58**.

| Пара | Тема |
|-----:|------|
| 55 | ndarray vs list |
| 56 | індексація / slicing |
| 57 | векторизація і broadcasting |
| 58 | лінал + практикум |

### Офіційне

- У 3680 немає. Слайди OD **3161**: `1.1 NumPy Basics` (PDF на `D:\` / `data/`); текст — *Essentials* гл. NumPy.
- Статті: numpy.org absolute beginners · W3Schools NumPy.

### Ядро

- *Essentials of Python for AI/ML* **гл. 4 Introduction to NumPy**.
- *Python for Scientific Computing* **гл. 2** (NumPy/Matplotlib — тут лише NumPy).
- O’Reilly **Python Data Science Handbook** (NumPy).

### Насичення (обережно)

- Журнал **python_ai_step пара 3** і Astra `02-01` — **факт/схема/пастка**, не копіювати HTML.
- Відео: *Python for DS/ML from A–Z* (транскрипти є) · YouTube «NumPy Full Course» (без транскрипту — не перше джерело).
- `python_kol` уже має 4 пари — насичувати їх, не додавати ML.

### Не брати

- sklearn, датасети Housing, Jupyter як окремий курс (Jupyter можна 5 хв extra).
- OpenCV.

---

## Модуль 14. Pandas

**Бюджет:** 8 год → **пари 59–62**.

| Пара | Тема |
|-----:|------|
| 59 | Series / DataFrame |
| 60 | CSV, фільтри, сортування |
| 61 | очищення, пропуски, типи колонок |
| 62 | GroupBy, pivot, time series |

### Офіційне

- Слайди 3161 Pandas / Importing Data.
- Статті: DataCamp pandas · W3Schools pandas.
- Програма: CSV / Excel / SQL. **SQL** — один `read_sql` або навіть CSV-заміна, якщо немає навчальної БД; не модуль «Вступ до БД» з 3158 (це інша програма Python-B).

### Ядро

- *Essentials* гл. **5–6** (Pandas + manipulation).
- O’Reilly **Python for Data Analysis, 3rd**.
- *The Python Book* Pandas.

### Насичення

- python_ai_step пара 4 — graft фактів.
- *Build Your Own AI Investor* «Python Crash Course / pandas» — лише I/O таблиць, не трейдинг.
- Feature Engineering book — зарано / extra.

### Лабораторна

- Один CSV з OD-статей (не обовʼязково Housing — це AI-модуль). Навчальний маленький CSV у репо пари, не 28 ГБ 3161.

---

## Модуль 15. Matplotlib

**Бюджет:** 8 год → **пари 63–66**.

| Пара | Тема |
|-----:|------|
| 63 | типи діаграм |
| 64 | Figure / Axes |
| 65 | Pandas/NumPy + plot |
| 66 | стиль, best practices, export |

### Офіційне

- Статті: DataCamp Matplotlib.
- Слайдів 3680 немає.

### Ядро

- *Essentials* гл. **7 Data Visualization**.
- Crash Course **15** Generating Data (matplotlib-частина).
- *The Python Book* Plotting.
- Scientific Computing гл. 2 — Figure.

### Насичення

- python_ai_step пари 7–8 · Astra `02-03` — типи графіків (pie/box/scatter) як extra до КОЛ, якщо програма каже «типи діаграм».
- Скіл `matplotlib-best-practices` — для викладача, не цитувати студенту як «скіл».

### Не брати

- Seaborn як основна бібліотека (можна 1 extra).
- TensorBoard / CNN-картинки з модуля 5 AI.

---

## Модуль 16. Патерни проєктування

**Бюджет:** 30 год → **пари 67–81**.

| Пари | Тема |
|------|------|
| 67–68 | що таке патерн, категорії, UML (класи / обʼєкти / взаємодія) |
| 69–74 | твірні: огляд, Abstract Factory, Builder, Factory Method, Prototype, Singleton |
| 75–78 | структурні: огляд, Adapter, Composite, Facade & Proxy |
| 79–81 | поведінка: огляд, Command & Iterator, Observer & Strategy |

Програма каже «інші структурні / інші поведінкові» — **extra**, не роздувати 15 пар новими обовʼязковими GoF.

### Офіційне

- Аркушів 3680/3158 **немає**. Практика — переписати код модуля 10 під патерн (як у програмі: мета, причина, структура, результат, приклад).

### Ядро

- **Refactoring Guru *Dive Into Design Patterns*** — є **uk** PDF/EPUB у `roadmap/data_guru/books/`. Це найкраще ядро модуля. Не комітити PDF; читати локально, на слайд — 1 схема + 1 Python-приклад.
- Сайт Guru в `roadmap/kb` (`python -m kb search guru …`).

### Насичення

- O’Reilly **Head First Design Patterns, 2nd**.
- **Architecture Patterns with Python** — не GoF-довідник; extra для «застосунок», не замість Factory.
- Bender `course_refactoring.py` (Guru для модуля 11 Python-B) — узгодити приклади.
- *Machine Learning Design Patterns* — **не цей модуль**.

### Не брати

- 202 бінарники Guru в git / HTML студентам.
- Усі 23 GoF за 30 год — програма фіксує конкретний список.

---

## Модуль 17. SOLID

**Бюджет:** 12 год → **пари 82–87**.

| Пара | Тема |
|-----:|------|
| 82 | SRP |
| 83 | OCP |
| 84 | LSP |
| 85 | ISP |
| 86 | DIP |
| 87 | практикум: рефакторинг навчального коду |

### Офіційне

- Аркушів немає. Вхід — класи з модуля 10 + патерни 16 (Strategy/Factory добре сідають на OCP/DIP).

### Ядро

- O’Reilly **Clean Code, 2nd** · **Clean Architecture**.
- Guru **Refactoring** (uk) — smells, що SOLID лікує.
- Architecture Patterns with Python — DIP на протоколах.

### Насичення

- Не «пʼять слайдів визначень». Кожна пара: зламаний навчальний клас → виправлення.
- intern QAA не потрібен.

---

## Модуль 18. AI, Generative AI, LLM і ефективність програміста

**Бюджет:** 12 год → **пари 88–93**.

| Пара | Тема |
|-----:|------|
| 88 | що таке AI і Generative AI, цілі |
| 89 | LLM: можливості, межі, як працює |
| 90 | Prompt engineering |
| 91 | GPT, Gemini, Claude, Mistral |
| 92 | ChatGPT, Copilot, Amazon CodeWhisperer / Q, Google Duet |
| 93 | практика: AI як напарник, не як автор |

### Офіційне

- OD **3158**: ДЗ/практика **Generative AI, LLM 7** (`w20`).
- Статті OD: McKinsey/TechTarget What is AI · Simplilearn Generative AI · Microsoft `generative-ai-for-beginners` · learnprompting.org · OpenAI prompt engineering.
- **Це КОЛ, не курс ШІ.** Не тягнути RAG, Vertex Agent Engine, LangChain LCEL як обовʼязкові пункти — їх немає в цій програмі.

### Ядро

- NetAcad **Introduction to Modern AI** (визначення, chatbot, hallucinations, prompts).
- NetAcad **Prompt Like an Engineer** (принципи, building blocks, CoT, перевірка відповіді).
- NetAcad **AI Fundamentals with IBM SkillsBuild** — короткий огляд, не 86 карток.
- python_kol пари 88–93 уже розкладені під програму — насичувати **їх**.

### Насичення

- Claude Academy (`roadmap` kb academy) — для викладача про інструменти; студенту — принципи з програми.
- O’Reilly *Hands-On Large Language Models* / *AI Engineering* — **extra вчителя**, не 80 хв студенту.
- python_ai_step модулі 8–9 (пари 37–48) — **не копіювати**. Можна 1 факт про галюцинації / контекстне вікно в пару 89–90.
- *Generative AI with LangChain* — поза програмою КОЛ.
- YouTube OD: «Generative AI in a Nutshell», «Prompt Engineering Tutorial».

### Практика пари 93

- Написати prompt до власного коду з модуля 10/11; перевірити відповідь (NetAcad 6.x «is it true / does it work»).
- Заборона: здавати згенерований код без розуміння (узгодити з голосом слайда: «зверніть увагу», не методичка викладачу).

### Не брати

- Astra теми 08–09.
- OpenCV, GAN, TF2 GenAI book як ядро КОЛ.
- teacher_kb нотатки M8–M10 AI-курсу як студентський текст.

---

## Модуль 19. Іспит

**Бюджет:** 2 год → **пара 94**.

Програма: практичне завдання (максимум розділів) + теоретичний іспит; допуск — усі ДЗ і практики.

### Офіційне

- Критерії з тексту програми (не вигадувати рубрики «як у Materials», якщо власник не просив).
- Не ставити галочки `public_plan.json`.

### Ядро збірки проєкту

- Колекції + файли + функції + 1–2 класи + тести + (бажано) Git.
- Банк ідей: **Большая книга проектов** (один проєкт, не 80).
- NumPy/Pandas/Matplotlib — опційно, якщо група дійшла; не блокувати допуск.

### Насичення

- PCEP/PCAP — хук, доки немає Cisco PCAP на диску.
- Командна взаємодія — короткий Git-ритуал здачі.

---

## Порядок насичення (коли робити пари «товстими»)

Існуючий веб уже **готовий як скелет**. Щоб курс став «максимально повним», не переписувати 94 HTML з нуля. Порядок за впливом на програму й наявністю джерел:

1. **Модулі 1–6, 8–9** — найкраща полиця (3680 + Crash Course + GFG). Закриває PCEP-подібну базу.
2. **Модуль 10** — 3158 9.x + OOP video + Complete Guide 7.
3. **Модуль 16–17** — Guru uk; інакше пари залишаться визначеннями.
4. **Модуль 12** — 3158 16.x + Concurrency book.
5. **Модулі 13–15** — Essentials + статті; AI-курс лише як graft.
6. **Модуль 11 і 7** — O’Reilly; офіційних аркушів немає — зробити власні практикуми.
7. **Модуль 18** — NetAcad + 3158 GenAI 7, без LangChain.
8. **Модуль 19** — коли 1–18 мають практику 1–N.

Роздатковий zip для КОЛ **свідомо не збирається** (див. README курсу). Цей план — про веб-пари й джерела викладача.

---

## Що свідомо не входить (щоб курс лишився КОЛ)

| Полиця | Чому ні як ядро КОЛ |
|--------|---------------------|
| `python_ai_step` / Materials / Astra повні лекції | Інша програма (ШІ 2.0 / авторський 180 хв) |
| 10 книжок 3161 про DL, OpenCV, LangChain, XAI | Немає в тематичному плані КОЛ |
| *Грокаємо глибоке навчання / стримінг* | Інший предмет |
| NetAcad Data Analytics 322 уроки | Роздуває M13–15 |
| Python-B модулі БД 16–18 | Немає в КОЛ 1.0.0 |
| PCAP Essentials 1–2 | **Немає файлів**; пререквізит — хук на bender |

---

## Файли, з яких починати агенту

```
MATERIALS_AND_BOOKS.md
MATERIALS_ROUTING.md
backend/data/courses/python_kol/README.md
backend/data/courses/python_kol/catalog.json
knowledge_materials_prepared/courses/od/python-core-3680/COURSE.md
knowledge_materials_prepared/courses/od/python-ai-3158/COURSE.md
knowledge_materials_prepared/books/python-crash-course/BOOK.md
knowledge_materials_prepared/articles/geekforgeeks/INDEX.md
knowledge_saver/deposits/2026-09-06_python-kol-program/raw/program-uk.md
```

Оригінали книжок і mp4: `D:\knowledge_materials` (bender). Текст для лекції — лише `knowledge_materials_prepared/` і `books_prepared/`.
