# План матеріалів: Штучний інтелект з Python 2.0.0

Програма: [Штучний інтелект з використанням Python, версія 2.0.0](https://materials.itstep.org/content/beef810f-be75-4b3c-9c1b-a8124a1a4b01/uk)  
UUID: `beef810f-be75-4b3c-9c1b-a8124a1a4b01`  
Каталог джерел: [`MATERIALS_AND_BOOKS.md`](MATERIALS_AND_BOOKS.md)  
Дата плану: 2026-09-20

Це **план насичення**, не нова програма. Бюджет ITSTEP не змінювати: **10 модулів, 50 пар × 80 хв.** Кожен офіційний пункт має з’явитися. Зайвих модулів не додавати.

Мета: курс, який **закриває програму** і при цьому бере з локального корпусу схеми, лабораторні, пастки й глибину — без підміни лекції розділом книжки.

---

## Як насичувати (правило на весь курс)

Пріоритет джерела в слоті пари (зверху вниз):

1. **Формула програми** — нумерований пункт і підпункти зі сторінки ITSTEP. Не вигадувати тему.
2. **Офіційний аркуш** — `knowledge_materials_prepared/courses/od/ai-python-3161/` (практика/ДЗ ШІ) і `python-ai-3158/` (якщо аркуш саме цієї теми). На слайд — умова задачі, не розв’язок.
3. **Каркас 80 хв** — `python_ai_step` (пари нижче). Густина пояснень — як пари 16–18 (`explaine_simple`). Структура — як 9–10 (`common_lesson`).
4. **Нотатка / аркуш KB** — `teacher_kb` `--note` / `--sheet` цього модуля.
5. **Один розділ книжки** — факт + схема + одна пастка. Текст тому в слайд не класти.
6. **O’Reilly / Guru** — через `roadmap` `python -m kb search books "…"`, не glob HTML.
7. **Стаття / ролик з OD** — один URL або один урок з транскриптом.
8. **Astra** — коли офіційний пункт **упакований** у пару (особливо М3 п.7–12, М5, М6, М8): глибина 180 хв у `astra/topic-XX-YY.html` або `scripts/course_build/content/astra/original/`. Не копіювати журнал у Astra і навпаки; graft у слот step.

Нове джерело **вживляти в існуючу пару** (growth), не відкривати 51-шу пару.

Пререквізит групи (обов’язково з програми, **до** модуля 1):

| NetAcad | Де текст |
|---------|----------|
| Introduction to Modern AI | `courses/netacad/introduction-to-modern-ai/` (86 уроків) |
| AI Fundamentals with IBM SkillsBuild | `courses/netacad/ai-ibm-skillsbuild/` (8) |
| Data Science Essentials with Python | `courses/netacad/data-science-essentials-with-python/` (61) |

Додатково, не замість програми: Data Analytics Essentials, Find Insights with AI, Prompt Like an Engineer, Build your Resume with AI.

Немає на диску: Python Essentials 1 і 2. Пробіл Python Core закривати `python_kol` + OD `python-core-3680`, не парами ШІ.

Не тягнути в цей курс (немає в програмі): патерни Guru як окремий модуль, Grokking Streaming як ядро, інтернатури QAA, Python-B БД/Git.

---

## Огляд модулів → каркас

| М | Пар | Пари step | Офіційних тем у програмі | Хід | Astra HTML |
|--:|----:|-----------|--------------------------|-----|------------|
| 1 | 2 | 1–2 | 4 | join | 01-01…01-04 (готово) |
| 2 | 6 | 3–8 | 3 | split | 02-01…02-03 (готово) |
| 3 | 6 | 9–14 | 12 | 1:1 + lab + **pack** | 03-01…03-12 (готово) |
| 4 | 6 | 15–20 | 6 | split / lab | 04-01…04-06 (готово) |
| 5 | 5 | 21–25 | 8 | join + lab | 05-01…05-08 (готово) |
| 6 | 5 | 26–30 | 9 | join | 06-01…06-04 готово; 06-05…06-09 текст original |
| 7 | 6 | 31–36 | 3 | split | 07-01…07-03 original |
| 8 | 6 | 37–42 | 8 | 1:1 + join | 08-01…08-08 original |
| 9 | 6 | 43–48 | 5 | 1:1 + practicum | 09-01…09-05 original |
| 10 | 2 | 49–50 | іспит | exam | — |

Найтісніші місця (тут насичення = Astra + окремі книжкові розділи в *teacher-deep-dive*, не ще одна пара): **пара 14**, **пари 21–25**, **26–30**, **40–42**.

Роздаток після веб-пари: `step_lesson_materials/` (або шар, який назве власник). Assessments: `step_lesson_materials/assessments/`.

---

## Модуль 1. Вступ до штучного інтелекту та науки про дані

**2 пари.** Слухач має відрізняти ШІ / DS / ML і три сім’ї алгоритмів; побачити датасет, ознаку, ціль; відкрити Jupyter.

| Пара | Закриває пункти програми |
|-----:|--------------------------|
| 1 | 1. Вступ (історія, ШІ, DS, ML) + 2. Види алгоритмів (supervised / unsupervised / RL) |
| 2 | 3. Датасети та ознаки + 4. Jupyter notebook / JupyterLab |

### Обов’язково

- Програма: пункти 1–4 як є (RL у програмі є — не викидати).
- OD 3161: вступ / програма курсу; практика-ДЗ модуля 1.
- `python_ai_step` `m01/pair_01`, `m01/pair_02`.
- KB: нотатка *M1 · Вступ AI/DS/ML і Jupyter*.
- Astra: `01-01` … `01-04` (готовий HTML) — розпакувати 4 теми, які в журналі злиті в 2 пари.

### Книжки (по розділу)

- *Python: Beginner's Guide to AI* — Adaptive Thinker / When to Use AI (рамка «що таке ШІ»).
- *Essentials of Python for AI/ML* — Introduction.
- *Build Your Own AI Investor* — Introduction (датасет як таблиця прикладів, без фінансів на слайді).

O’Reilly: *AI Engineering* (що таке система, не код); *Hands-On Machine Learning* — вступні сторінки про типи задач.

### NetAcad / статті / відео

- **Спочатку** Modern AI + IBM SkillsBuild (пререквізит).
- Статті OD: TechTarget / [McKinsey What is AI](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-ai); Defined.ai datasets; 50 best free datasets; DataCamp Jupyter.
- Ролики: AI Tutorial for Beginners; Jupyter Complete Beginner Guide. 3Blue1Brown *Neural Network* — **не** в М1 (це М4).

### Не тягнути сюди

NumPy API, sklearn, нейромережі, промпти. Історія ШІ — один факт і лінія часу, не біографії.

---

## Модуль 2. Обробка та аналіз даних

**6 пар.** Три офіційні теми розрізані навпіл.

| Пара | Пункт програми |
|-----:|----------------|
| 3 | numpy/pandas: масиви vs list, Series, DataFrame, I/O |
| 4 | numpy/pandas: head / tail / sample / info / describe |
| 5 | статистика: випадкова величина, середнє, мода, медіана, дисперсія, std |
| 6 | статистика: рівномірний / нормальний / Пуассон, коваріація, кореляція |
| 7 | matplotlib: Figure, Axes, графік функції, гістограма |
| 8 | matplotlib: pie, box-plot, scatter, bar |

### Обов’язково

- OD 3161: практика/ДЗ 2.1 NumPy, 2.2 Pandas, 2.3 Matplotlib, 2.4 статистика; слайди `1.1 NumPy Basics`, `1.1 Pandas`, `1.2 Pandas Basics`, `2.1 Importing Python Data`, `3.1 Jupyter`.
- step `m02/pair_01` … `pair_06`.
- KB: *M2 · NumPy*, *Pandas*, *статистика*, *Matplotlib*.
- Astra `02-01` … `02-03`.

### Книжки

- *Essentials of Python for AI/ML* — NumPy, Pandas, Data Manipulation, Visualization, Statistical Methods.
- *Python for Scientific Computing and AI* — Anaconda/NumPy/Matplotlib, Statistics, Jupyter/Colab.
- *Python Crash Course* — Generating Data (графіки), не Django.
- Грокаємо алгоритми, розділ 2 (масив vs список) — **одна схема** на парі 3.

O’Reilly: *Python for Data Analysis* (3rd); *Python Data Science Handbook* (2nd); *Practical Statistics for Data Scientists* (2nd) — середні, розподіли, кореляція.

### Статті / відео

NumPy absolute beginners; W3Schools NumPy/pandas/statistics; DataCamp pandas / Matplotlib; Statistics as Foundation of DS.  
Ролики: NumPy Full Course / Tutorial; Learning Pandas; Pandas by Example; Matplotlib Crash Course; Statistics University Course — **один** урок на тему, не 10 годин.

### Насичення

На парі 3 обов’язково показати, чому `ndarray` ≠ `list` (векторизація). На парі 6 — що кореляція ≠ причинність. Графік функції vs графік вибірки — пастка matplotlib (голос до студента).

---

## Модуль 3. Алгоритми навчання з учителем

**6 пар, 12 пунктів програми.** Пари 9–13 закривають п.1–6 чесно. **Пара 14 пакує п.7–12** (поліноми, L1/L2, дерева/ліс, бустинг/XGBoost, логрег, задача покупки машини). Насичений курс **не викидає** ці пункти: глибина — Astra 03-07…03-12 + teacher-deep-dive, обов’язковий мінімум — на парі 14.

| Пара | Пункти |
|-----:|--------|
| 9 | 1. Регресія (одна змінна) |
| 10 | 2. Метрики (MAE, MSE, R², loss vs error) |
| 11 | 3. Навчання регресії (мін, градієнт, спуск) |
| 12 | 4–5. Кілька змінних + sklearn |
| 13 | 6. Housing prices (Factorize, OHE, MinMax/Standard, Imputer, split, over/underfit, CV, гіперпараметри) |
| 14 | 7–12. pack (див. вище) |

### Обов’язково

- OD 3161: ДЗ/практика 3.1–3.4; слайд `1.1 Supervised Learning`.
- Housing.csv з OD-статей (Rdatasets).
- step `m03/pair_01` … `pair_06` (еталон структури 9–10).
- KB: *M3 · Регресія*; *M3 · Дерева, ансамблі, класифікація*.
- Astra **усі** `03-01` … `03-12` (HTML готовий) — це головний важіль повноти модуля 3.

### Книжки

- Грокаємо глибоке навчання 2–6 (як машина вчиться, градієнт) — схема спуску на парі 11, не NumPy-CNN.
- *Essentials* — Machine Learning.
- *Beginner's Guide* — Optimize / NN Regression (лише ідея логрег).
- *Pro Deep Learning TF2* — Mathematical Foundations (похідна/градієнт), без Keras як основного стеку (програма далі — PyTorch).

O’Reilly: *Hands-On Machine Learning* (регресія, sklearn, housing, регуляризація, дерева, бустинг, логрег) — **головна** книжка модуля. *Feature Engineering for Machine Learning*; *Practical Statistics*; *Machine Learning Design Patterns* (один патерн на CV/гіперпараметри).

### Статті / відео

Basics of Regression; logistic regression real world; Top 10 ML algorithms; GFG/Javatpoint Supervised; Supervised learning 01/02 на YouTube; Scikit-Learn Full Course — фрагмент LinearRegression / train_test_split.  
Задача машини: sklearn + програма п.12. Не підміняти Housing на інший датасет без потреби.

### Ризик

Якщо пара 14 лишається «оглядом назв» — програма **не** виконана. Мінімум на 80 хв: поліном vs overfit, L2 одним графіком, дерево vs ліс одним реченням, XGBoost як «бустинг з бібліотеки», логрег + confusion/F1, 20 хв лабораторна «купити машину». Решта — Astra / домашка OD.

---

## Модуль 4. Основи нейронних мереж

**6 пар.** Стек програми: **PyTorch**, не Keras як ядро.

| Пара | Пункти |
|-----:|--------|
| 15 | Вступ: персептрон, MLP, forward, backprop, оптимізація *(частина)* |
| 16 | PyTorch: тензор, граф, `nn.Module`, оптимізатори, loss, train loop + решта «вступу» |
| 17 | Dropout |
| 18 | Приклад MLP у PyTorch |
| 19 | Активації (sigmoid/softmax вихід; sigmoid/tanh/ReLU/LeakyReLU/Swish приховані); vanishing/exploding |
| 20 | Кейс: вроджені вади серця |

Еталон пояснень курсу — пари **16–18**.

### Обов’язково

- OD 3161: 4.1–4.2 нейромережі / PyTorch.
- Kaggle heart disease (стаття OD).
- step `m04/pair_01` … `pair_06`.
- KB: *M4 · Персептрон і PyTorch*.
- Astra `04-01` … `04-06`.

### Книжки

- **Грокаємо глибоке навчання** — головна схема модуля: 3 forward, 4–5 градієнт, 6 backprop, 8 dropout, 9 softmax/ReLU, 13 autograd → міст до PyTorch.
- *Pro Deep Learning* — DL Concepts (поняття, не обов’язково TF-код на слайді).
- *Beginner's Guide* — Neurons, Biomimicking, DL Environments.

O’Reilly: *Deep Learning with PyTorch, Second Edition* — тензор, autograd, цикл навчання.

### Статті / відео

Activation functions guide; Simplilearn / PyImageSearch / DataCamp neural nets; PyTorch Full Course — **один** блок тензорів. 3Blue1Brown — після персептрона, як інтуїція, не як заміна лабораторної.

### Не тягнути

CNN, NLP, Vertex, LangChain. TensorFlow 2 GenAI book — лише якщо треба VAE/GAN пізніше (не цей модуль).

---

## Модуль 5. Нейронні мережі в комп’ютерному зорі

**5 пар, 8 пунктів.** Упаковка щільна: згортка, MNIST, batching, архітектури, пневмонія мають усі прозвучати.

| Пара | Пункти (орієнтир step) |
|-----:|-------------------------|
| 21 | 1. Класифікація зображень + 2. CNN (згортка, фільтри, шари) |
| 22 | 3. Багатокласова + 4. CNN на рукописних цифрах |
| 23 | 5. Batching, BatchNorm, проблеми глибоких мереж |
| 24 | 6. Архітектури (AlexNet, LeNet, ImageNet, ResNet) + 7. прийоми (clip, LayerNorm) |
| 25 | 8. Пневмонія за знімком |

Насичення: Astra `05-01` … `05-08` (готово) — по одній темі, якщо 80 хв не вміщає архітектури.

### Обов’язково

- OD 3161: 5.1–5.2 CV; Kaggle chest-xray-pneumonia.
- step `m05/pair_01` … `pair_05`.
- KB: *M5 · CNN і компʼютерний зір*.

### Книжки

- Грокаємо DL, розділ 10 (CNN з нуля — схема, далі PyTorch).
- *Neural Network Computer Vision with OpenCV 5* — DNN module, classification, detection (детекція — глибина, не обов’язкова лабораторна, якщо 80 хв на класифікацію).
- *Learning OpenCV 5* — витяг (обкладинка, faces, descriptors) — обережно: програма про CNN, не про класичний CV як ядро.
- *Pro Deep Learning* — CNN.
- *Beginner's Guide* — ConvNets digits, Object Detection, FaceNet.

O’Reilly: *Deep Learning with PyTorch* — розділ про зображення, якщо є в дзеркалі; інакше Hands-On ML CNN-розділ як порівняння, стек лишати PyTorch.

### Відео / курси

OpenCV Course; OpenCV Beginners; DL for CV TensorFlow (концепція, код — PyTorch). Packt *Computer Vision Projects* і Udemy OpenCV — транскриптів мало; не ставити mp4 у слайд.

### Не тягнути

Повний курс детекції/GAN/deepfake з *Generative AI TF2* — це не пункти М5.

---

## Модуль 6. Обробка природної мови

**5 пар, 9 пунктів.** Word2Vec/GloVe, RNN/LSTM/Transformer, seq2seq, transfer — не стискати до «NLTK tokenize».

| Пара | Пункти |
|-----:|--------|
| 26 | 1. NLTK: токени, лема, стем, стоп-слова |
| 27 | 2–3. Корпуси + embeddings як ідея |
| 28 | 4–5. Word2Vec, GloVe + приклад задач |
| 29 | 6–7. Мовні моделі; seq2seq: RNN, LSTM, Transformers |
| 30 | 8–9. Приклад seq2seq + transfer learning |

Astra `06-01`…`06-04` готові; **06-05…06-09** — брати `original/`, HTML ще немає. Це головний дефіцит глибини.

### Обов’язково

- OD 3161: 6.1–6.3 NLP.
- step `m06/pair_01` … `pair_05`.
- KB: *M6 · NLP*.
- Статті: DataCamp/freeCodeCamp/GFG NLP; Kaggle word2vec shortcut; PyTorch char-RNN tutorial.

### Книжки

- Грокаємо DL 11 embeddings, 12 RNN, 14 LSTM.
- *Beginner's Guide* — NLP Chatbots, Generative LM, DeepSpeech2 (один факт, не ASR-курс).
- *Practical Explainable AI* — NLP (пастка інтерпретації, не ядро).

O’Reilly: ***Natural Language Processing with Python* (Bird)** — канон NLTK для пар 26–27. ***NLP with Transformers*** — пари 29–30. *Hands-On Large Language Models* — місток до М8, не заміна seq2seq.

### Відео / Udemy

NLP Tutorial Python; spaCy course (spaCy **не** в програмі — згадати одним реченням). Транскрипт *NLP in Python with 8 projects* — одна лабораторна, узгоджена з Word2Vec, не вісім проєктів.

---

## Модуль 7. Навчання без учителя

**6 пар, 3 теми** — тут журнал уже розрізав добре; насичення = якісний приклад, не нові пункти.

| Пара | Пункт |
|-----:|-------|
| 31 | Зниження простору: задача, SVD |
| 32 | PCA + приклад для класифікації |
| 33 | Кластеризація, K-means |
| 34 | DBSCAN + сегментація клієнтів |
| 35 | Рекомендації: content-based, TF-IDF, cosine |
| 36 | Collaborative filtering + приклад фільмів |

### Обов’язково

- OD 3161: 7.1–7.3; слайд `1.1 Unsupervised Learning`.
- step `m07/pair_01` … `pair_06`.
- KB: *M7 · Навчання без учителя*.
- Статті: DataCamp/Javatpoint unsupervised; RFM K-Means retail; content-based recommender (Medium).
- Astra `07-01`…`07-03` (текст original).

### Книжки / O’Reilly

- *Essentials* — Machine Learning (unsupervised фрагмент).
- *Hands-On Machine Learning* — PCA, clustering.
- ***Applied Recommender Systems with Python*** — пари 35–36 (головна книжка рекомендацій).
- *Practical Statistics* — де потрібно відрізнити кореляцію від кластера.

Не підміняти «фільми» з програми іншим доменом без позначки в teacher.md.

---

## Модуль 8. Generative AI та GCP

**6 пар, 8 пунктів.** Пари 40 і 42 — join. Vertex, RAG, Agent Engine, Streamlit/Gradio — усі в програмі.

| Пара | Пункти |
|-----:|--------|
| 37 | 1. Вступ: GenAI vs класичне ML; LLM / Diffusion / Multimodal; Azure OpenAI, Bedrock, Vertex; етика |
| 38 | 2. Основи промпту (роль → контекст → задача → формат) |
| 39 | 3. Патерни: Zero/Few-shot, CoT, ReAct, ToT, Reflexion, Persona, Template, Output-Guidance |
| 40 | 4–5. Контекст / галюцинації + Vertex AI, Gemini, Vector Search, Model Garden, Express mode, SDK |
| 41 | 6. RAG, Vector Search 2.0, Knowledge Base, PDF/CSV |
| 42 | 7–8. Агенти / Agent Engine + застосунок GCP (frontend → Gemini → RAG → Agent Engine) |

### Обов’язково

- OD 3161: Generative AI, LLM (ДЗ/практика «7»).
- NetAcad: **Prompt Like an Engineer**; Find Insights with AI (пререквізит навички, не заміна Vertex).
- step `m08/pair_01` … `pair_06`.
- KB: *M8–M10 · GenAI / промпти*.
- Статті: Simplilearn GenAI; Microsoft generative-ai-for-beginners; learnprompting.org; OpenAI prompting + quickstart; DataCamp OpenAI API.
- Astra `08-01`…`08-08` (original) — розпакувати join пар 40 і 42.

### Книжки / O’Reilly

- *Generative AI with LangChain* (OD) — «що таке GenAI»; Tools лишити на М9.
- O’Reilly: ***GenAI on Google Cloud*** — головна книжка Vertex/Gemini. ***AI Engineering***; ***Hands-On Large Language Models***; ***RAG with Python Cookbook*** (пара 41). *Learning LangChain* — лише місток, ядро фреймворку в М9.

### Відео

Introduction to Generative AI; Generative AI in a Nutshell; Prompt Engineering Tutorial; LangChain Crash Course — на М9, якщо вже з’являється назва.

### Насичення без зриву 80 хв

Демо Vertex — один пайплайн на пару (ключ/квота в teacher.md, не в студентський HTML). Diffusion / картинки — визначення в п.1, лабораторна не обов’язкова. Порівняння Azure/AWS — таблиця на 5 хв, практика — GCP як у програмі.

---

## Модуль 9. LLM-фреймворки та інженерія генеративних систем

**6 пар, 5 тем + практикум.**

| Пара | Пункти |
|-----:|--------|
| 43 | 1. Екосистема: навіщо фреймворк; LLM → Chain → Retrieval → Agent; LangChain, LlamaIndex, Autogen, Semantic Kernel, Agent Framework, LangGraph, CrewAI; зв’язок із Vertex |
| 44 | 2. LangChain: PromptTemplate, LLMChain/LCEL, Memory, Tool; конектор Gemini |
| 45 | 3. Tools, Function Calling, CoT/ReAct vs Agent Engine |
| 46 | 4. Router / Sequential, валідація, Human-in-the-Loop |
| 47 | 5. LangSmith, faithfulness/relevance, vs Vertex Monitoring |
| 48 | practicum: зібрати ланцюжок програми (промпт → tool → RAG-або-пам’ять → лог) |

### Обов’язково

- OD 3161: ті самі GenAI-аркуші, якщо є завдання на фреймворк.
- step `m09/pair_01` … `pair_06`.
- Стаття: Nanonets Complete LangChain Guide.
- Astra `09-01`…`09-05`.

### Книжки / O’Reilly

- ***Generative AI with LangChain*** (OD) — головний том модуля (ланцюжки, chatbot, production).
- O’Reilly: *Learning LangChain*; *Hands-On LLM*; *AI Engineering*; *RAG Cookbook* (якщо RAG не закріпили в М8).

Не роздувати огляд 7 фреймворків у сім лабораторних: **один** огляд на парі 43, лабораторні — LangChain, як у пунктах 2–5.

Claude Academy / MCP (roadmap `academy`) — для викладача, не пункт програми студента Python AI.

---

## Модуль 10. Іспит

**2 пари.** У програмі немає нумерованих тем — це захист компетенцій з мети курсу.

| Пара | Зміст |
|-----:|-------|
| 49 | Чеклист усіх 9 модулів + пробні задачі з OD 3161 |
| 50 | Іспит / захист: дані → модель або GenAI-пайплайн (узгодити з офіційним форматом групи) |

Джерела: step `m10`; `step_lesson_materials/assessments/` (rubrics, quizzes, diagnostic); аркуші практики 1–N з KB; не нова теорія.

Карта навичок roadmap.sh (Python, ML, AI Engineer) — **самоперевірка викладача**, не білет студенту.

---

## Наскрізні шари (усі модулі)

| Шар | Навіщо |
|-----|--------|
| `python_ai_step` | Канонічна веб-лекція 50×80 |
| `python_ai_step_materials` | Робоча копія, якщо правите матеріали окремо |
| Роздаток `step_lesson_materials/` | Після пари, білдером |
| Bender `course_theory.py` | Помічник / та сама програма, не слайд журналу |
| `CursorRecomendation/` / `CodexRecomendation/` | Унікальний акцент на пару для викладача |
| `teacher_kb` articles + 808 video chunks | Пошук факту, не цитата id студентам |

Інші `python_ai_*` (materials / additional / modify) — **інші шари тієї ж програми**. Без явної назви курсу не змішувати zip і веб.

---

## Дефіцити корпусу (чесно)

| Пробіл | Що робити |
|--------|-----------|
| Astra HTML немає з 06-05 | Текст `scripts/course_build/content/astra/original/` + потім HTML |
| Learning OpenCV 5 — лише 4 частини | Не будувати М5 на повному OpenCV 5 |
| Python Essentials 1/2 немає | Core через `python_kol` / OD 3680 |
| Vertex / Gemini квоти | Лабораторна з демо-ключем викладача або скрін контракту API |
| *ML in Python with 5 Projects* без транскрипту | Не ставити в план як джерело факту |
| Пара 14 / М5 / М6 / М8 join | Обов’язковий graft Astra, інакше програма дірява |

---

## Порядок збірки насиченого курсу

1. Не чіпати меню 50 пар і назви модулів програми.
2. Для модуля: OD-аркуш → step-пара → KB-нотатка → **один** розділ книжки → **один** O’Reilly-hit → стаття з `articles/web`.
3. Якщо пункт програми не вміщається в 80 хв — слот *Детально* / teacher-deep-dive + Astra-тема з тією самою формулою syllabus.
4. Перевірка покриття: кожен нумерований пункт М1–М9 є в якійсь парі (колонка «Пункти» вище).
5. Густина слайда: факт → схема → тултіп; не том LangChain замість пари 44.

Джерело істини програми лишається [сторінка ITSTEP 2.0.0](https://materials.itstep.org/content/beef810f-be75-4b3c-9c1b-a8124a1a4b01/uk). Каталог «що є на ПК» — [`MATERIALS_AND_BOOKS.md`](MATERIALS_AND_BOOKS.md).
