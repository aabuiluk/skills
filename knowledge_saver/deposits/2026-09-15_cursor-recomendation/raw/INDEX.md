# Індекс 50 пар

Програма: [ITSTEP 2.0.0](https://materials.itstep.org/content/beef810f-be75-4b3c-9c1b-a8124a1a4b01/uk).

| Пара | Шлях | Тема лекції | Унікальний акцент шару |
|---:|---|---|---|
| 1 | `m01/pair_01` | Вступ до ШІ, Data Science і Machine Learning | Три робочі визначення AI (OECD vs Turing vs Dartmouth) і NIST Map-реєстр. |
| 2 | `m01/pair_02` | Датасети, ознаки та середовище Jupyter | Datasheet набору + колонка-витік + контракт Restart Kernel. |
| 3 | `m02/pair_01` | NumPy: масиви, векторизація, Series / DataFrame та I/O | View проти copy: мутація, shares_memory і broadcasting. |
| 4 | `m02/pair_02` | Pandas: створення DataFrame та інформаційні методи | merge validate, вибух сум і anti-join як перевірка кардинальності. |
| 5 | `m02/pair_03` | Основи статистики: випадкова величина, середнє, мода, медіана, дисперсія та std | MCAR / MAR / MNAR, прапорці was_missing і Adult зі знаком «?». |
| 6 | `m02/pair_04` | Розподіли, коваріація та кореляція: рівномірний, нормальний і Пуассона | Квартет Енскомба + парадокс Сімпсона: Spearman проти Pearson. |
| 7 | `m02/pair_05` | Matplotlib: Figure, Axes, графіки функцій і гістограми | Гістограма: bins, обрізана вісь і n на графіку. |
| 8 | `m02/pair_06` | Matplotlib: pie, box-plot, scatter і bar | Спочатку питання — потім тип графіка: pie бреше, box ховає моди. |
| 9 | `m03/pair_01` | Регресія з однією змінною | Одиниці нахилу і заборона екстраполяції за межі train-діапазону. |
| 10 | `m03/pair_02` | Метрики регресії та функція втрат | DummyRegressor, викид у MAE/MSE, від'ємний R² і асиметрична ціна. |
| 11 | `m03/pair_03` | Градієнтний спуск і навчання регресії | Перевірка градієнта скінченною різницею і три learning rate. |
| 12 | `m03/pair_04` | Множинна регресія та Scikit-learn | Мультиколінеарність: стрибок коефіцієнтів, Ridge vs OLS, сенс після scaler. |
| 13 | `m03/pair_05` | Housing prices: препроцесинг і валідація | Географічний / group split проти random і scaler, що підглядає. |
| 14 | `m03/pair_06` | Поліноми, регуляризація, дерева й логістична регресія | PR-поріг за ціною помилки, log loss на впевненій помилці, early stopping лише на valid. |
| 15 | `m04/pair_01` | Персептрон і багатошарові мережі | XOR лінійно несепарабельний: перцептрон проти нелінійності hidden у MLP. |
| 16 | `m04/pair_02` | PyTorch: тензори, autograd, nn.Module | Autograd-пастки: leaf, in-place, grad is None, зайвий detach. |
| 17 | `m04/pair_03` | Dropout і регуляризація в нейромережах | Dropout: масштаб train vs eval; MC-dropout — не режим за замовчуванням. |
| 18 | `m04/pair_04` | Практика: MLP у PyTorch (digits / tabular) | Траєкторії SGD / momentum / Adam на спільному бюджеті кроків. |
| 19 | `m04/pair_05` | Функції активації та vanishing/exploding gradients | Зникаючі градієнти в стеку sigmoid, hooks на норми, ініціалізація Glorot. |
| 20 | `m04/pair_06` | Кейс: передбачення серцевих захворювань (NN) | UCI Heart Disease: поріг під recall і model card «це не діагноз». |
| 21 | `m05/pair_01` | Задачі класифікації зображень і CNN-ідея | Зсувова еквіваріантність згортки проти плоского MLP і receptive field. |
| 22 | `m05/pair_02` | Згортка, фільтри й згорткові шари | Формула розміру карти після conv і AdaptiveAvgPool замість hardcoded flatten. |
| 23 | `m05/pair_03` | Багатокласова класифікація і CNN на MNIST | Fashion-MNIST: галерея помилок і аугментація лише на train. |
| 24 | `m05/pair_04` | Batching, BatchNorm і глибокі мережі | BatchNorm: running stats, розрив train/eval і малий батч. |
| 25 | `m05/pair_05` | Архітектури CNN, прийоми навчання і кейс пневмонії | Пневмонія: patient-level split, межі Grad-CAM, ліцензії Kermany/NIH, не клініка. |
| 26 | `m06/pair_01` | NLP з NLTK: токенізація, лематизація, стоп-слова | Український апостроф і NFC/NFD ламають токени ще до NLTK. |
| 27 | `m06/pair_02` | Корпуси та embeddings: Word2Vec і GloVe | OOV і bias у векторі — це властивості корпусу, не «семантика світу». |
| 28 | `m06/pair_03` | Word2Vec / GloVe і практичні приклади | Аналогія king−man+woman крихка: інший домен — інші сусіди. |
| 29 | `m06/pair_04` | Мовні моделі: RNN, LSTM і Transformers | Нулі padding не ігноруються самі: вони псують hidden state. |
| 30 | `m06/pair_05` | Приклад seq2seq + transfer learning | Маска уваги на іграшковому перекладі б'є порожній HF-pipeline stub. |
| 31 | `m07/pair_01` | SVD і зниження розмірності | Rank-k — це бюджет пам'яті, не «дві компоненти завжди досить». |
| 32 | `m07/pair_02` | PCA 2D і порівняння з SVD | PCA, натягнута на всю таблицю, — це тихий leakage у CV. |
| 33 | `m07/pair_03` | Кластеризація K-Means | Силует високий, а кластер порожній на іншому seed — бізнес-k не доведений. |
| 34 | `m07/pair_04` | DBSCAN і сегментація клієнтів | eps без k-distance і масштабу — лотерея; −1 це шум, не «погані клієнти». |
| 35 | `m07/pair_05` | Content-based рекомендації книг | Топ-k клонів нудить: MMR, ваги TF-IDF і анкета cold-start. |
| 36 | `m07/pair_06` | Collaborative filtering на матриці оцінок | Випадковий split у рекомендаціях підглядає майбутнє; RMSE не рятує топ-N. |
| 37 | `m08/pair_01` | Вступ до Generative AI і хмарних платформ | Не «що таке LLM», а матриця родини моделей і профіль ризиків NIST. |
| 38 | `m08/pair_02` | Основи Prompt Engineering | Промпт без unit-тестів і schema pass rate — це чернетка, не компонент. |
| 39 | `m08/pair_03` | Патерни Prompt Engineering (CoT, ReAct, ToT…) | ToT дорогий; прихований CoT не просіть, якщо політика забороняє. |
| 40 | `m08/pair_04` | Контекстне вікно, галюцинації та Vertex AI / Gemini | Спочатку preflight (проєкт, регіон, ADC, модель, квота, бюджет), мок лишається дефолтом. |
| 41 | `m08/pair_05` | RAG і Vector Search | Chunking міняє recall; faithfulness міряють окремо, не одним «RAG score». |
| 42 | `m08/pair_06` | LLM-агенти, Agent Engine і GenAI-додаток | Інструмент без ідемпотентності — подвійне списання; rollback планують до deploy. |
| 43 | `m09/pair_01` | Екосистема LLM-фреймворків | ADR: коли LangChain, коли LangGraph, коли сирий SDK, коли взагалі без фреймворка. |
| 44 | `m09/pair_02` | LangChain: PromptTemplate, LCEL, Memory | LCEL — це Runnable з контрактом; memory має token budget, не безмежний список. |
| 45 | `m09/pair_03` | LangChain Tools і Function Calling | Не кожну помилку tool ретраїмо: malformed / business / transient / permanent. |
| 46 | `m09/pair_04` | Багатокрокові workflow і валідація | HITL — це серіалізований стан і interrupt approve/edit/reject, не кнопка «ок». |
| 47 | `m09/pair_05` | Спостережуваність: LangSmith і метрики | Червоний trace стає рядком eval; дві версії промпта — один experiment. |
| 48 | `m09/pair_06` | Інтеграційний практикум: GenAI-ланцюжок | Реліз = golden-set CI + секрети поза репо + критерії quality/latency/cost/risk. |
| 49 | `m10/pair_01` | Підготовка до іспиту: чеклист і пробні задачі | Іспит — це станції діагностики, не ще один чеклист тем модулів 1–9. |
| 50 | `m10/pair_02` | Іспит / захист проєкту | Захист = hashes артефактів, datasheet+model card і відповіді опоненту. |
