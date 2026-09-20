# Матеріали і книжки (локально)

Зріз **книжок і методичних матеріалів**, які лежать на цьому ПК у `lesson_helper`, сусідах `bender` і `roadmap`, і на диску `D:\knowledge_materials`.

- **Дата:** 2026-09-20
- **ПК:** DESKTOP-GREEN
- Повний текст книжок сюди **не** скопійовано (авторське право). Тут — назви, розділи й де файл.

Маршрут «куди йти агенту» лишається в `MATERIALS_ROUTING.md`. Цей файл — лише **що є**.

Перевірка 2026-09-20: **полиці всі названі; частина раніше була згорнута.** Нижче — що є повним списком, що лишається покажчиком (сотні уроків), чого на диску немає.

| Полиця | У цьому файлі | Не розгортати тут |
|--------|---------------|-------------------|
| 4 «Грокаємо» / Impractical | розділи | текст розділів |
| 17 книжок OD | TOC | 80 проєктів Big Book повністю |
| O’Reilly 29 назв | список назв | HTML сторінок |
| Guru (патерни + Refactoring) | назви видань, мови | 202 бінарники |
| 13 курсів журналу | таблиця slug + 50/94/20 назв пар | HTML кожної пари |
| Роздатки / assessments | каталоги | zip-вміст |
| Astra 58 тем | усі назви | текст HTML |
| Bender Python-B / AI | 18 + 10 модулів | HTML Помічника |
| OD 3158 / 3161 / 3680 | програма + типи аркушів | 205 HTML сторінок дослівно |
| NetAcad 7 курсів | назви + кількість уроків | 719 уроків по одному |
| Відеокурси 16 | назви | 862 транскрипти |
| Статті OD + GFG + YouTube | повні списки | тіла сторінок |
| teacher_kb | книжки, 12 нотаток, лічильники | sqlite-текст |
| `data/` і `D:\` | що лежить | mp4 / 235 слайдів Deep Dive |
| roadmap (карти, Git, Academy, ProfDev) | назви колекцій | 11k+ сторінок kb |

**Немає локально** (згадано як пререквізит Python-B, файлів немає): NetAcad *Python Essentials 1* і *Python Essentials 2*. На `D:\knowledge_materials\netacad\` лише 7 AI/DS курсів.

---

# A. Книжки

## A1. Чотири книжки в `lesson_helper/books/` + витяги `books_prepared/`

PDF gitignored. Розділи на диску в `books_prepared/<slug>/chapters/`.

### 1. Грокаємо алгоритми — Aditya Bhargava (2017)

PDF: `books/Bhargava_Grokaem-algoritmy.581423.pdf` (14.6 МБ, 290 с.)

| # | Розділ |
|---|--------|
| 1 | Знакомство с алгоритмами (бінарний пошук, O(log n)) |
| 2 | Сортировка выбором (масив vs список) |
| 3 | Рекурсия |
| 4 | Быстрая сортировка |
| 5 | Хеш-таблицы |
| 6 | Поиск в ширину |
| 7 | Алгоритм Дейкстры |
| 8 | Жадные алгоритмы |
| 9 | Динамическое программирование |
| 10 | k ближайших соседей |
| 11 | Что дальше? |

### 2. Грокаємо глибоке навчання — Andrew Trask (2019)

PDF: `books/Trask_Grokaem-glubokoe-obuchenie.581982.pdf` (15.9 МБ, 354 с.)

| # | Розділ |
|---|--------|
| 1 | Введение в глубокое обучение |
| 2 | Как машины учатся |
| 3 | Прямое распространение |
| 4–5 | Градиентный спуск / кілька ваг |
| 6 | Обратное распространение |
| 7 | Как изобразить сеть |
| 8 | Регуляризация и пакеты (dropout) |
| 9 | Активации (softmax, ReLU) |
| 10 | Сверточные сети |
| 11 | Word embeddings |
| 12 | RNN |
| 13 | Автоград |
| 14 | LSTM |
| 15 | Федеративное обучение |
| 16 | Куда идти дальше |

### 3. Грокаємо стримінг — Fischer, Wang (2023)

PDF: `books/Van_Grokaem-striming.738373.pdf` (9.6 МБ, 288 с.). Код у книжці Java.

| # | Розділ |
|---|--------|
| 1 | Знакомство со стриминговыми системами |
| 2 | Первая джоба |
| 3 | Параллелизация |
| 4 | Граф потока (DAG) |
| 5 | Семантика доставки |
| 6 | Обзор систем (Spark, Flink, Kafka) |
| 7 | Окна, watermark |
| 8 | Join |
| 9 | Обратное давление |
| 10 | Вычисления с состоянием |
| 11 | Продвинутые концепции |

### 4. «Непрактичний» Python — Lee Vaughan (2021)

PDF: `books/Vogan_-Nepraktichnyy-Python-….pdf` (60.4 МБ, 466 с.)

| # | Розділ |
|---|--------|
| 1 | Генератор дурацких имен (PEP 8) |
| 2 | Палиндромы |
| 3 | Анаграммы |
| 4–5 | Шифры гражданской войны |
| 6 | Невидимые чернила |
| 7 | Генетические алгоритмы |
| 8–9 | Хокку / цепи Маркова |
| 10 | Парадокс Ферми |
| 11 | Монти Холл |
| 12 | Монте-Карло |
| 13–14 | pygame (вулкан, Марс) |
| 15 | Астрофото / pillow |
| 16 | Закон Бенфорда |

---

## A2. Сімнадцять книжок OD (`knowledge_materials_prepared/books/`)

Оригінали: `D:\knowledge_materials\od\`. Текст розділів — у `chapters/` кожної книжки.

### З `AI PYTHON_3161` (10 книжок)

**Build Your Own AI Investor** (7 розд.): Introduction · Python Crash Course · ML with Scikit-learn · Making the AI Investor · AI Backtesting · Statistical Likelihood of Returns · Stock Picks 2021.

**Essentials of Python for AI/ML** (11): Introduction · Statistical Methods · Python Basics · NumPy · Pandas · Data Manipulation · Visualization · Machine Learning · Data Pipelines · MLOps.

**Generative AI with LangChain** (10): What Is Generative AI? · LangChain for LLM Apps · Getting Started · Capable Assistants · Chatbot like ChatGPT · Developing Software with GenAI · LLMs for Data Science · Customizing LLMs · Production · Future of Generative Models.

**Generative AI with Python and TensorFlow 2** (13): Drawing Data from Models · TensorFlow Lab · DNN Building Blocks · Generate Digits · VAEs · GANs · Style Transfer · Deepfakes · Text Generation · Transformers · Music · GAIL / games · Emerging Applications.

**Learning OpenCV 5** (витяг 4 частини): обкладинка · Detecting Faces · Image Descriptors · Custom Object Detectors.

**Neural Network Computer Vision with OpenCV 5** (11): Intro to CV · Basics of Imaging · Challenges · Classical Solutions · DL and CNNs · OpenCV DNN Module · Image Classification · Object Detection · Faces and Text · Running the Code · End-to-end Demo.

**Practical Explainable AI** (14): Explainability · Ethics/Bias · Linear · Non-Linear · Ensemble · Time Series · NLP · What-If Fairness · Deep Learning · Counterfactual · Contrastive · Prediction Invariance · Rule-Based · Computer Vision.

**Pro Deep Learning with TensorFlow 2.0** (6): Mathematical Foundations · DL Concepts and TF · CNN · NLP · RBM/Autoencoders · Advanced NN.

**Python for Scientific Computing and AI** (21): IDLE · Anaconda/NumPy/Matplotlib/SymPy · Jupyter/Colab · AS/A-Level math · Biology · Chemistry · Data Science · Economics · Engineering · Fractals · Image Processing · ODE/PDE · Physics · Statistics · Brain Inspired Computing · NN · TensorFlow/Keras · RNN · CNN/TensorBoard · Answers.

**Python: Beginner's Guide to AI** (24): Adaptive Thinker · Think Like a Machine · Human Problem · Unconventional Innovator · Manage ML/DL · Optimize · When to Use AI · Disruptive Innovations · Neurons · Biomimicking · Conceptual Representation · Blockchains · NLP Chatbots · Emotional IQ · DL Environments · NN Regression · Generative LM · DeepSpeech2 · ConvNets digits · Object Detection · FaceNet · GAN · AI Hardware · TensorFlow Serving.

Ті самі PDF/EPUB також у `lesson_helper/data/faily/gdrive/` (LangChain, TF2 GenAI, OpenCV DNN epub, XAI, Pro DL, Beginner's Guide) і в `D:\knowledge_materials\od\AI PYTHON_3161\` (**10 книжок** + **10 аркушів**, разом 18 PDF + 2 EPUB).

Додаткові PDF у тій самій папці 3161 (не книжки):

- слайди: `1.1 NumPy Basics`, `1.1 Pandas`, `1.2 Pandas Basics`, `2.1 Importing Python Data`, `2.2 Python Basics`, `3.1 Jupyter Notebook`, `1.1 Supervised Learning`, `1.1 Unsupervised Learning`
- `110 DQNNaturePaper.pdf` (стаття DQN, Nature)
- `25154140-sample.pdf` (зразок)

### З `PythonCore_3680` (7 книжок)

Оригінали: `D:\knowledge_materials\od\PythonCore_3680\` (235 окремих PDF — переважно слайди Udemy *Python 3 Deep Dive* Parts 1–4: змінні, типи, функції, декоратори, named tuples, пакети, sequences; це **не** ще 235 книжок).

**Python Crash Course, 3rd (Matthes)** — 20 розд.: Getting Started · Variables · Lists · Working with Lists · if · Dictionaries · while · Functions · Classes · Files/Exceptions · Testing · Ship · Aliens · Scoring · Generating Data · Downloading Data · APIs · Django · User Accounts · Styling/Deploy.

**Python. Исчерпывающее руководство** — 10: Основы · Операторы · Структура программы · Объекты/типы · Функции · Генераторы · Классы · Модули · I/O · Stdlib.

**Quick Python 3** — 6 блоків: Bare Minimum · Better Tools · Classes · Getting Fancy · Testing · Tkinter GUI.

**The Python Book** — Introduction · Getting Started · Packages · Data Types · Operators · Dates · Lists · Tuples · Dictionaries · Sets · Loops · Strings · Regex · Files/Excel/JSON/XML · Functions and Classes · Pandas · Plotting (Matplotlib/Seaborn) · APIs · Scraping · Conclusion.

**Mastering Python for Web** — Introduction · Data Type · Comments · Programs/Algorithms/Functions · Execution Model · Web Development.

**Большая книга проектов Python** — 80 мініпроєктів: Бейглз, парадокс днів народження, Цезар, «Жизнь», Фібоначчі, Виселица, Монти Холл, судоку, Ханойська башта, 2048, Віженер, … (повний список у `big-book-of-python-projects/BOOK.md`).

**Знакомство с Python** — 21 файл по 25 сторінок (1–509), без TOC у PDF.

---

## A3. Книжки O’Reilly / локальне дзеркало `roadmap/data_books/`

Особиста копія сторінок (1134 сторінки в `kb/books`). Не публікувати.

1. A Byte of Python  
2. AI Engineering  
3. Applied Recommender Systems with Python  
4. Architecture Patterns with Python  
5. Building Machine Learning Powered Applications  
6. Clean Architecture  
7. Clean Code, 2nd Edition  
8. Deep Learning with PyTorch, Second Edition  
9. Effective Python: 125 Specific Ways, 3rd  
10. Feature Engineering for Machine Learning  
11. Fluent Python, 2nd Edition  
12. Fundamentals of Data Engineering  
13. GenAI on Google Cloud  
14. Hands-On Large Language Models  
15. Hands-On Machine Learning with Scikit-Learn and PyTorch  
16. Head First Design Patterns, 2nd  
17. High Performance Python, 3rd  
18. Learning LangChain  
19. Machine Learning Design Patterns  
20. Natural Language Processing with Python (Bird et al.)  
21. Natural Language Processing with Transformers  
22. Practical Statistics for Data Scientists, 2nd  
23. Python Concurrency with asyncio  
24. Python Cookbook, 3rd  
25. Python Data Science Handbook, 2nd  
26. Python for Data Analysis, 3rd  
27. Python Testing with pytest  
28. RAG with Python Cookbook  
29. Robust Python  

Шлях сайту: `roadmap/data_books/site/<slug>/`.

---

## A4. Книжки Refactoring Guru (`roadmap/data_guru/books/`, 202 файли)

- Dive Into Design Patterns / `patterns-*` — PDF, EPUB, MOBI, KFX: en, ru, uk, es, fr, ja, ko, pl, pt-br, **zh**; плюс demo-файли
- Refactoring — C# / Java / PHP × en, ru, uk (PDF/EPUB/MOBI)

---

## A5. Книжки в `teacher_kb.sqlite`

Ті самі 10 томів, що в A2 з програми 3161 (AI Investor, Essentials, LangChain, TF2 GenAI, OpenCV 5, OpenCV DNN, XAI, Pro DL TF2, Scientific Computing, Beginner's Guide). Індекс, не окремі видання.

---

# B. Методичні матеріали

## B0. Усі курси журналу (13 slug)

Шлях: `backend/data/courses/<slug>/`. URL: `/course/<slug>`.

| Slug | Назва | Пар | `presentation.html` |
|------|-------|----:|--------------------:|
| `python_ai_step` | Штучний інтелект із використанням Python | 50 | 51 |
| `python_ai_step_materials` | Робоча копія матеріалів до step | 50 | 51 |
| `python_ai_materials` | Python AI Materials | 50 | 50 |
| `python_ai_additional_materials` | Additional Materials | 50 | 50 |
| `python_ai_modify_materials` | Modify | 50 | 51 |
| `python_ai_codex_modify_materials` | Codex Modify | 50 | 50 |
| `python_ai_cursor_modify_materials` | Cursor Modify | 50 | 51 |
| `python_ai` | Ранній шар | 50 | 50 |
| `python_ai_cursor` | Cursor-шар | 50 | 50 |
| `python_ai_codex` | Codex-шар (презентацій немає) | 50 | 0 |
| `python_kol` | Основи програмування на Python (КОЛ) | 94 | 95 |
| `intern_dmytro` | Інтернатура QAA Python · Дмитро | 20 | 20 |
| `intern_ofelya` | Інтернатура QAA Python · Офелія | 20 | 20 |

У `python_ai_step` також: `CursorRecomendation/` (464 файли) і `CodexRecomendation/` (325) — пакети для викладача, не слайд студенту. `_backups/` у каталозі курсів — не матеріал пари.

## B1. Журнал `python_ai_step` — 50 пар × 80 хв

Шлях: `backend/data/courses/python_ai_step/`. URL: `/course/python_ai_step`.

| № | Модуль | Назва |
|--:|--------|--------|
| 1 | 1 | Вступ до ШІ, Data Science і Machine Learning |
| 2 | 1 | Датасети, ознаки та середовище Jupyter |
| 3 | 2 | NumPy: масиви, векторизація, Series / DataFrame та I/O |
| 4 | 2 | Pandas: створення DataFrame та інформаційні методи |
| 5 | 2 | Основи статистики: випадкова величина, середнє, мода, медіана, дисперсія та std |
| 6 | 2 | Розподіли, коваріація та кореляція |
| 7 | 2 | Matplotlib: Figure, Axes, графіки функцій і гістограми |
| 8 | 2 | Matplotlib: pie, box-plot, scatter і bar |
| 9 | 3 | Регресія з однією змінною |
| 10 | 3 | Метрики регресії та функція втрат |
| 11 | 3 | Градієнтний спуск і навчання регресії |
| 12 | 3 | Множинна регресія та Scikit-learn |
| 13 | 3 | Housing prices: препроцесинг і валідація |
| 14 | 3 | Поліноми, регуляризація, дерева й логістична регресія |
| 15 | 4 | Персептрон і багатошарові мережі |
| 16 | 4 | PyTorch: тензори, autograd, nn.Module |
| 17 | 4 | Dropout і регуляризація в нейромережах |
| 18 | 4 | Практика: MLP у PyTorch |
| 19 | 4 | Функції активації та vanishing/exploding gradients |
| 20 | 4 | Кейс: передбачення серцевих захворювань (NN) |
| 21 | 5 | Задачі класифікації зображень і CNN-ідея |
| 22 | 5 | Згортка, фільтри й згорткові шари |
| 23 | 5 | Багатокласова класифікація і CNN на MNIST |
| 24 | 5 | Batching, BatchNorm і глибокі мережі |
| 25 | 5 | Архітектури CNN і кейс пневмонії |
| 26 | 6 | NLP з NLTK |
| 27 | 6 | Корпуси та embeddings: Word2Vec і GloVe |
| 28 | 6 | Word2Vec / GloVe на практиці |
| 29 | 6 | Мовні моделі: RNN, LSTM і Transformers |
| 30 | 6 | seq2seq + transfer learning |
| 31 | 7 | SVD і зниження розмірності |
| 32 | 7 | PCA 2D і порівняння з SVD |
| 33 | 7 | Кластеризація K-Means |
| 34 | 7 | DBSCAN і сегментація клієнтів |
| 35 | 7 | Content-based рекомендації книг |
| 36 | 7 | Collaborative filtering |
| 37 | 8 | Вступ до Generative AI і хмарних платформ |
| 38 | 8 | Основи Prompt Engineering |
| 39 | 8 | Патерни Prompt Engineering |
| 40 | 8 | Контекстне вікно, галюцинації, Vertex AI / Gemini |
| 41 | 8 | RAG і Vector Search |
| 42 | 8 | LLM-агенти, Agent Engine |
| 43 | 9 | Екосистема LLM-фреймворків |
| 44 | 9 | LangChain: PromptTemplate, LCEL, Memory |
| 45 | 9 | LangChain Tools і Function Calling |
| 46 | 9 | Багатокрокові workflow і валідація |
| 47 | 9 | LangSmith і метрики |
| 48 | 9 | Інтеграційний практикум |
| 49 | 10 | Підготовка до іспиту |
| 50 | 10 | Іспит / захист проєкту |

Та сама програма (інші шари журналу, ті самі 50 пар): `python_ai_materials`, `python_ai_additional_materials`, `python_ai_modify_materials`, `python_ai_codex_modify_materials`, `python_ai_cursor_modify_materials`, `python_ai_step_materials`, `python_ai`, `python_ai_cursor`. У `python_ai_codex` каталог пар є, презентацій 0.

У кожній парі step зазвичай: `presentation.html`, `teacher.md`, `plan.json`.

---

## B2. `python_kol` — 94 пари

`/course/python_kol`

| № | Модуль | Назва |
|--:|--------|--------|
| 1 | 1 | Вступ до Python: змінні, типи, введення-виведення |
| 2 | 2 | Перетворення типів і логічні оператори |
| 3 | 2 | Розгалуження: if, elif, else і match |
| 4 | 3 | Цикл while, break і continue |
| 5 | 3 | Цикл for, вкладені цикли та відлагоджувач |
| 6 | 4 | Рядки: створення, методи, зрізи |
| 7 | 4 | Форматоване виведення і модуль string |
| 8 | 4 | Списки: методи, генератори, клонування |
| 9 | 5 | Кортежі |
| 10 | 5 | Множини і frozenset |
| 11 | 5 | Словники |
| 12 | 5 | Колекції на практиці: вибір структури |
| 13 | 6 | Функції: def, return, аргументи |
| 14 | 6 | Вбудовані функції, math, random, область видимості LEGB |
| 15 | 6 | *args, **kwargs, first-class і рекурсія |
| 16 | 6 | lambda, map, filter, zip і functools |
| 17 | 6 | Замикання, каррінг і декоратори |
| 18 | 7 | Динамічна і статична типізація |
| 19 | 7 | Анотації типів (type hints) |
| 20 | 7 | mypy: Optional, list, tuple, dict |
| 21 | 7 | Складні підписи: кілька значень і функції вищого порядку |
| 22 | 8 | try / except / finally |
| 23 | 8 | raise і ієрархія винятків |
| 24 | 9 | Файлова система: файл, директорія, формати |
| 25 | 9 | Відкриття, читання і запис файлів |
| 26 | 9 | Менеджер контексту with |
| 27 | 9 | Операції з директоріями |
| 28 | 9 | Пошук файлів за маскою і практика I/O |
| 29 | 10 | ООП: інкапсуляція, успадкування, поліморфізм |
| 30 | 10 | Класи, об'єкти, атрибути |
| 31 | 10 | Методи і self |
| 32 | 10 | Magic-методи та `__init__` |
| 33 | 10 | @staticmethod і @classmethod |
| 34 | 10 | Функтори: `__call__` |
| 35 | 10 | Декоратори методів |
| 36 | 10 | @property: керовані атрибути |
| 37 | 10 | Дескриптори |
| 38 | 10 | Інкапсуляція: public, _internal, __private |
| 39 | 10 | Успадкування і MRO |
| 40 | 10 | Поліморфізм і качина типізація |
| 41 | 10 | Перевантаження операторів |
| 42 | 10 | Практика ООП: міні-модель предметної області |
| 43 | 11 | Навіщо модульні тести |
| 44 | 11 | unittest |
| 45 | 11 | pytest |
| 46 | 11 | Практика тестів на власний модуль |
| 47 | 12 | Конкурентність, паралелізм, гонитва, deadlock |
| 48 | 12 | threading.Thread: start, join, daemon |
| 49 | 12 | Lock, Event, Semaphore |
| 50 | 12 | Спільні дані в потоках |
| 51 | 12 | multiprocessing.Process |
| 52 | 12 | Міжпроцесна взаємодія: Queue, Pipe, shared memory |
| 53 | 12 | Пул процесів: map, apply, apply_async |
| 54 | 12 | asyncio: корутини, gather, Queue |
| 55 | 13 | NumPy: ndarray проти list |
| 56 | 13 | NumPy: індексація і slicing |
| 57 | 13 | Векторизація і broadcasting |
| 58 | 13 | Лінійна алгебра в NumPy і практика |
| 59 | 14 | Pandas: Series і DataFrame |
| 60 | 14 | Pandas: CSV, фільтри, сортування |
| 61 | 14 | Очищення даних і пропуски |
| 62 | 14 | GroupBy, pivot і time series |
| 63 | 15 | Matplotlib: типи діаграм |
| 64 | 15 | Figure і Axes |
| 65 | 15 | Pandas/NumPy + Matplotlib |
| 66 | 15 | Стиль графіка, best practices, export |
| 67 | 16 | Що таке патерн і навіщо категорії |
| 68 | 16 | UML: класи, об'єкти, взаємодія |
| 69 | 16 | Твірні патерни: огляд |
| 70 | 16 | Abstract Factory |
| 71 | 16 | Builder |
| 72 | 16 | Factory Method |
| 73 | 16 | Prototype |
| 74 | 16 | Singleton |
| 75 | 16 | Структурні патерни: огляд |
| 76 | 16 | Adapter |
| 77 | 16 | Composite |
| 78 | 16 | Facade і Proxy |
| 79 | 16 | Патерни поведінки: огляд |
| 80 | 16 | Command і Iterator |
| 81 | 16 | Observer і Strategy |
| 82 | 17 | SRP |
| 83 | 17 | OCP |
| 84 | 17 | LSP |
| 85 | 17 | ISP |
| 86 | 17 | DIP |
| 87 | 17 | SOLID разом: рефакторинг навчального коду |
| 88 | 18 | AI і Generative AI: що це для програміста |
| 89 | 18 | LLM: як працює, можливості і межі |
| 90 | 18 | Prompt engineering |
| 91 | 18 | Огляд LLM: GPT, Gemini, Claude, Mistral |
| 92 | 18 | Copilot, ChatGPT і інші інструменти в IDE |
| 93 | 18 | Практика: AI як напарник, не як автор |
| 94 | 19 | Іспит: інтеграція курсу |

---

## B3. Інтернатури QAA (по 20 пар)

Кожен тиждень: пара теорії + пара практики/проєкту.

**`intern_dmytro`**

| Тиждень | Теми |
|--------:|------|
| 1 | Python syntax і локальне середовище |
| 2 | Колекції, файли, JSON і exceptions |
| 3 | Основи pytest |
| 4 | API testing |
| 5 | UI automation |
| 6 | Структура фреймворку |
| 7 | SQL for QAA |
| 8 | Git workflow і CI |
| 9 | Debugging і flaky tests |
| 10 | Фінальне самостійне завдання |

**`intern_ofelya`**

| Тиждень | Теми |
|--------:|------|
| 1 | Python syntax і локальне середовище |
| 2 | Колекції, файли, JSON і exceptions |
| 3 | QA mindset і дизайн сценаріїв |
| 4 | Основи pytest |
| 5 | API testing |
| 6 | UI automation |
| 7 | Test design + automation design |
| 8 | SQL for QAA |
| 9 | Структура фреймворку |
| 10 | Git, CI і фінальне завдання |

---

## B4. Роздатки студентам (`PythonAI61_LessonN_LessonM`)

| Каталог | Курс | Пакетів |
|---------|------|--------:|
| `lesson_materials/` | materials | 25 |
| `additional_lesson_materials/` | additional | 25 |
| `modify_lesson_materials/` | modify | 25 |
| `modify_codex_lesson_materials/` | codex modify | 25 |
| `modify_cursor_lesson_materials/` | cursor modify | 25 |
| `step_lesson_materials/` | step | 26 (+ окремий Lesson16_17_18, 25 zip) |

`student_presentations/`: `pair_01_vstup_do_shi.html`, `pair_02_datasety_jupyter.html`, `SLOVNYK_TERMINOLOGII.html` / `.md`, `term-glossary.js`.

Оцінювання в zip-шарах: `assessments/` у additional / modify / codex modify / cursor modify / step — `module_rubrics.md`, `module_quizzes.json`, `diagnostic.json`.

`lessons/` — немає (legacy).

---

## B5. Astra — авторський курс 180 хв / тема

`astra/topic-XX-YY.html`. Готово **37** (пари 1–37). Далі — у програмі, HTML ще немає.

| Пара | Id | Готово | Тема |
|-----:|------|:------:|------|
| 1 | 01-01 | так | Вступ до ШІ, DS, ML |
| 2 | 01-02 | так | Види алгоритмів |
| 3 | 01-03 | так | Датасети та ознаки |
| 4 | 01-04 | так | Jupyter |
| 5 | 02-01 | так | NumPy, pandas |
| 6 | 02-02 | так | Основи статистики |
| 7 | 02-03 | так | Matplotlib |
| 8 | 03-01 | так | Регресія |
| 9 | 03-02 | так | Метрики |
| 10 | 03-03 | так | Навчання регресії |
| 11 | 03-04 | так | Кілька змінних |
| 12 | 03-05 | так | Scikit-learn |
| 13 | 03-06 | так | Housing prices |
| 14 | 03-07 | так | Поліноміальна регресія |
| 15 | 03-08 | так | Регуляризація |
| 16 | 03-09 | так | Дерева і випадковий ліс |
| 17 | 03-10 | так | Градієнтний бустинг |
| 18 | 03-11 | так | Логістична регресія |
| 19 | 03-12 | так | Покупка машини, sklearn |
| 20 | 04-01 | так | Вступ до нейромереж |
| 21 | 04-02 | так | PyTorch |
| 22 | 04-03 | так | Dropout |
| 23 | 04-04 | так | MLP у PyTorch |
| 24 | 04-05 | так | Активації, градієнти |
| 25 | 04-06 | так | Вади серця |
| 26 | 05-01 | так | Класифікація зображень |
| 27 | 05-02 | так | CNN |
| 28 | 05-03 | так | Багатокласова класифікація |
| 29 | 05-04 | так | CNN на MNIST |
| 30 | 05-05 | так | Batching |
| 31 | 05-06 | так | Архітектури CNN |
| 32 | 05-07 | так | Прийоми навчання |
| 33 | 05-08 | так | Пневмонія |
| 34 | 06-01 | так | NLP / NLTK |
| 35 | 06-02 | так | Корпуси |
| 36 | 06-03 | так | Embeddings / TF–IDF |
| 37 | 06-04 | так | Skip-gram, GloVe / алгоритми embeddings |
| 38 | 06-05 | ні | Приклад розв’язання задач цими алгоритмами |
| 39 | 06-06 | ні | Мовні моделі |
| 40 | 06-07 | ні | Seq-to-seq алгоритми |
| 41 | 06-08 | ні | Приклад задачі Seq-to-seq |
| 42 | 06-09 | ні | Transfer learning |
| 43 | 07-01 | ні | Зниження простору |
| 44 | 07-02 | ні | Кластеризація |
| 45 | 07-03 | ні | Рекомендаційні системи |
| 46 | 08-01 | ні | Вступ до Generative AI |
| 47 | 08-02 | ні | Основи Prompt Engineering |
| 48 | 08-03 | ні | Патерни Prompt Engineering |
| 49 | 08-04 | ні | Оптимізація та управління контекстом |
| 50 | 08-05 | ні | GCP Vertex AI |
| 51 | 08-06 | ні | Дані та RAG у Vertex AI |
| 52 | 08-07 | ні | LLM-агенти та оркестрація |
| 53 | 08-08 | ні | AI-застосунок у GCP |
| 54 | 09-01 | ні | Екосистема LLM-фреймворків |
| 55 | 09-02 | ні | LangChain — основи оркестрації |
| 56 | 09-03 | ні | LangChain Tools і Function Calling |
| 57 | 09-04 | ні | Багатокрокові workflow і валідація |
| 58 | 09-05 | ні | Спостережуваність і LangSmith |

Текст тем: `scripts/course_build/content/astra/original/`.

---

## B6. Bender — теорія Помічника (`homework/course_*.py`)

UI: http://127.0.0.1:3003/pomichnyk/

**Python-B / 100 пар / ITSTEP v1.3.5** (18 модулів): 1 програмування й Python (2) · 2 типи (2) · 3 розгалуження (6) · 4 цикли (8) · 5 списки/рядки (8) · 6 функції (8) · 7 сортування/пошук (8) · 8 кортежі/множини/словники (5) · 9 файли (5) · 10 Git (6) · 11 ООП (10) · 12 структури даних (8) · 13 пакування даних (2) · 14 паралельне/мережеве (4) · 15 Generative AI/LLM (4) · 16 вступ до БД (10) · 17 БД у Python (6) · 18 іспит (2). Пререквізит у програмі: NetAcad Python Essentials 1 і 2 — **на цьому диску їх немає**.

**Python AI** у `homework/course_theory.py` — ті самі 10 модулів, що в B1. Додатково: `course_expansion.py`, `course_ai_solutions.py`, `course_m6_*`, `course_refactoring.py` (Guru для модуля 11), `course_assistant.py`.

Сирий дамп, який bender качає: `D:\knowledge_materials` (NetAcad 957 файлів; OD 3158 = 109 HTML / 495 файлів; 3161 = 1504 файли / 28 ГБ; Core 3680 = 2876 файли / 135 ГБ, з них 1057 mp4 і 235 pdf).

Fallback у репо `bender/knowledge_materials/`: `vertushka/` (знайдені `id_spec`), `virt/` — 582 файли **не ITSTEP** (Academind JS, Pluralsight C# Design Patterns). Не джерело пари Python.

---

## B7. Офіційні сторінки ITSTEP (текст у `knowledge_materials_prepared/courses/od/`)

### Програма ШІ 2.0.0 — `ai-python-3161` (41 HTML)

Практичне + домашнє: М1 вступ · 2.1 NumPy · 2.2 Pandas · 2.3 Matplotlib · 2.4 статистика · 3.1–3.4 supervised · 4.1–4.2 нейромережі/PyTorch · 5.1–5.2 CV · 6.1–6.3 NLP · 7.1–7.3 unsupervised · 7 GenAI/LLM. Плюс файл програми курсу.

### `python-ai-3158` (109 HTML)

Змішані аркуші Python-B і ШІ: алгоритми 1.1–1.2, змінні 2.x, розгалуження 3.x, цикли 4.x, рядки/списки 5.x, функції 6.x, сортування, кортежі, файли 8.x, Git 9.1–9.2, ООП 9.2–9.7, структури 10.x, стиснення 11.x, паралельне 16.x, GenAI 7, БД 17.x–18.x. Повна таблиця: `courses/od/python-ai-3158/COURSE.md`.

### Python Core 2.0.2 — `python-core-3680` (55 HTML)

Сценарії уроків 1, 5, 6, 8, 9, 14, 17 + практика/ДЗ 1.1–8.2 (алгоритми, типи, умови, цикли, рядки/списки, функції, винятки, файли).

---

## B8. NetAcad (пререквізит)

`knowledge_materials_prepared/courses/netacad/` · оригінал `D:\knowledge_materials\netacad\`.

| Курс | Уроків |
|------|-------:|
| Introduction to Modern AI | 86 |
| AI Fundamentals with IBM SkillsBuild | 8 |
| Data Science Essentials with Python | 61 |
| Data Analytics Essentials | 322 |
| Find Insights with AI | 93 |
| Prompt Like an Engineer | 78 |
| Build your Resume with AI | 71 |

Додатково 156 уроків як статті: `articles/netacad/`.

---

## B9. Відеокурси (транскрипт у prepared; mp4 на `D:\`)

| Курс | Уроків | Транскрипт |
|------|-------:|-----------:|
| Complete Python Developer 2022 (ZTM) | 277 | 277 |
| Python for DS/ML from A–Z | 140 | 140 |
| Practical AI + Reinforcement Learning | 121 | 121 |
| Python for Absolute Beginners | 101 | 101 |
| NLP in Python with 8 projects | 88 | 88 |
| Python in practice (15 projects) | 98 | 24 |
| Python programming / ML / DL | 59 | 59 |
| Advanced Python OOP (10 programs) | 31 | 31 |
| Skill Up with Python (Pearson) | 21 | 21 |
| Learn OpenCV Python 2022 | 37 | 0 |
| Computer Vision Projects with Python 3 | 19 | 0 |
| Python 3 Deep Dive Part 1 Functional | 156 | 0 |
| Deep Dive Part 2 Iteration | 134 | 0 |
| Deep Dive Part 3 Hash maps | 80 | 0 |
| Deep Dive Part 4 OOP | 162 | 0 |
| OOP by doing a game | 18 | 0 |

YouTube з OD: 47 роликів (назви/id, без транскриптів) — `videos/youtube/INDEX.md`: 10 BEST ML PROJECTS · 10 Free Dataset Resources · AI Tutorial for Beginners · 3Blue1Brown Neural Network · GitHub Copilot · NLP Tutorial Python · Conditionals / Conditions_2 / For / While / Loops (Core) · LLM from Scratch · DL for CV TensorFlow · Generative AI Full Course · Generative AI in a Nutshell · How is data prepared · Introduction to Generative AI · Jupyter Complete Beginner · LangChain Crash Course · Amazon Q Developer · Learn Python Full Course · Learning Pandas · ML for Everybody · ML 10 Hours · ML 2024 Beginner · ML Scikit-Learn Full Course · Matplotlib Crash Course · NLP 2023 Simplilearn · NLP spaCy · Neural Network Full Course · Neural Networks TensorFlow Crash · NumPy Full Course · OpenCV Full Tutorial · Pandas by Example · Prompt Engineering Tutorial · Python Crash Course · NumPy Tutorial · OpenCV Beginners · Python Tutorial for Beginners · PyTorch Full Course · Statistics University Course · Supervised 01/02 · Supervised vs Unsupervised · Data Types 10 min · Unsupervised 01/02.

---

## B10. Статті й зовнішні посилання OD

### Веб (63 URL, `articles/web/INDEX.md`)

Housing.csv (Rdatasets) · logistic regression real world · TensorFlow Playground · activation functions · Kaggle heart disease · chest-xray-pneumonia · word2vec shortcut · PyTorch char-RNN · RFM K-Means retail · content-based recommender · TechTarget What is AI · McKinsey What is AI · Defined.ai datasets · 50 best free datasets · DataCamp Jupyter · DataCamp pandas · W3Schools pandas/NumPy/statistics · NumPy absolute beginners · Statistics as Foundation of DS · DataCamp Matplotlib · Basics of Regression · Top 10 ML algorithms · GFG/Javatpoint Supervised ML · Simplilearn Neural Networks · PyImageSearch NN · GFG neural networks · DataCamp Deep NN · GFG/MLM/RealPython/ActiveState Computer Vision · DataCamp/freeCodeCamp/GFG/Simplilearn NLP · Simplilearn Generative AI · Microsoft generative-ai-for-beginners · learnprompting.org · OpenAI prompt engineering / quickstart · DataCamp OpenAI API · Nanonets LangChain · DataCamp/Javatpoint/Thamm/Guru99 Unsupervised · PYPL · Programiz I/O · learnpython.org · W3Schools datatypes/operators/variables/conditions/while/for/strings · DigitalOcean type conversion · GFG loops.

### GeekForGeeks Python Foundation (9 контурів)

01 Basics · 02 Variables and Data Types · 03 Input/Output · 04 Operators · 05 Flow Control · 06 Loops · 07 Functions · 08 String · 09 List. Файли: `articles/geekforgeeks/`.

### NetAcad як статті

155 уроків у `articles/netacad/` — ті самі 7 курсів, що в B8, інший зріз (стаття, не COURSE.md).

---

## B11. `teacher_kb.sqlite` (не лише книжки)

36.49 МБ, gitignored. Дзеркало для людей: `teacher_kb.md`.

| Таблиця | Записів | Що це |
|---------|--------:|-------|
| books | 10 | індекс 10 томів OD ШІ (A5) |
| notes | 12 | нотатки модулів (нижче) |
| sheets | 40 | аркуші практики 1–N |
| tasks | 188 | задачі |
| articles | 58 | статті в індексі |
| videos | 808 | шматки відео (шляхи ще вказують на порожній `data/kb_extracts/`) |
| chunks | 3018 | пошукові шматки |
| related_sources | 32 | суміжні доки |

Нотатки: M1 Вступ AI/DS/ML і Jupyter · M2 Matplotlib · M2 NumPy · M2 Pandas · M2 Основи статистики · M3 Дерева, ансамблі, класифікація · M3 Регресія з учителем · M4 Персептрон і PyTorch · M5 CNN і компʼютерний зір · M6 NLP · M7 Навчання без учителя · M8–M10 GenAI / промпти (аркуш w10).

---

## B12. Дамп `lesson_helper/data/` (gitignored, ≈ 3.2 ГБ, 158 файлів)

Окремо від `D:\`. Після дедупа лишились відео/книжки з Drive.

| Шлях | Що |
|------|----|
| `data/AI PYTHON_3161/` | 2 mp4 *Complete Python Pro Bootcamp for Data Science and AI* (Customer Data Preprocessing unsolved/solved) |
| `data/faily/gdrive/` | Packt CV Projects (6) · Pearson Skill Up Python (16) · Udemy ML in Python with 5 Projects (3) · Udemy NLP 8 Projects (14) · Udemy Practical AI + RL (18) · 5 PDF + 1 EPUB книжок OD |
| `data/Python College/PYTHON AI_3158/faily/gdrive/` | Udemy OOP 10 programs (60) · ZTM Complete Python Developer 2022 (29) · Deep Dive Part 2 (4) |
| `data/Python College/…3680/` і `Мова програмування Python…3158/` | дерева папок, файлів 0 |

У prepared **немає** окремого транскрипту для *ML in Python with 5 Projects* і для двох mp4 Pro Bootcamp.

---

## B13. Матеріали `roadmap` (не книжки A3–A4)

Шість баз `kb/` (готовий індекс 2026-09-20):

| База | Записів | Зміст |
|------|--------:|-------|
| roadmap | 11 137 | 93 карти навичок, теми, 177 гайдів, 113 проєктів, питання, best practices |
| profdev | 4 640 | ProfDevMap (позиції, capabilities, грейди Trainee→Principal). **Не публікувати.** |
| academy | 766 | Claude Academy: Claude 101, Claude Code, MCP, agent skills, subagents, Claude API, Vertex/Bedrock, AI Fluency, Teaching AI Fluency, AI-Native SDLC |
| guru | 5 773 | патерни, рефакторинги, smells (сайт, крім PDF A4) |
| gitbybit | 666 | курс Git: 250 уроків + 330 термінів Gitopedia |
| books | 1 134 | сторінки O’Reilly (A3) |

Найближчі карти roadmap.sh для викладання: Python Developer, Python for Data Analysis, Machine Learning, AI Engineer, AI and Data Scientist, Data Analyst, Data Engineer, Computer Science, SQL, QA, System Design, Claude Code, AI Agents.

---

## B14. Архіви `knowledge_saver/` (уже добуті матеріали)

Депозити з програмами/еталонами пар (не сирі книжки): python-kol-program · pairs 15–18 gold · ITSTEP AI primary sources · Cursor/Codex рекомендації · astra web-syllabus · books-prepared · knowledge-materials-prepared · цей каталог `2026-09-20_materials-and-books`. Індекс: `knowledge_saver/INDEX.md`.

Прототип зон пари: `frontend/public/prototype-pair17-blocks.html`.

---

Кінець файлу. Авторські PDF і HTML O’Reilly / Guru / Academy не комітити й не публікувати.
