---
name: tactic_of_cource_building
description: >-
  Розкладає будь-яку навчальну програму на скелет сторінки кожної пари:
  чотири зони chrome / rail / stage / notebook і типи блоків як у прототипі
  пари 17. Еталон — prototype-pair17-blocks.html і live presentation пари 17.
  Застосовуй, коли треба скелет веб-лекції, блоки пари, tactic_of_cource_building,
  «як у пари 17», «як у prototype-pair17-blocks», внутрішня структура пари,
  порожні слоти «Потребує допрацювання». Не будує меню курсу — для меню
  спершу strategy_of_cource_building.
---

# tactic_of_cource_building

Одиниця роботи — **сторінка однієї пари**, не пункт меню.

Еталон схеми: [prototype-pair17-blocks.html](assets/prototype-pair17-blocks.html)  
(у журналі: `/prototype-pair17-blocks.html`).  
Жива пара: [пара 17 presentation](https://csctemplate.pythonanywhere.com/courses/python_ai_step/pairs/17/files/presentation.html).

Типи й зони: [block-types.md](references/block-types.md).  
Порядок слотів: [pair-layout.md](references/pair-layout.md).

Source deposit: `knowledge_saver/deposits/2026-09-16_tactic-of-cource-building/`.

## Коли

Користувач дає програму (або вже готове меню пар) і просить розкласти **всередину** пари: скелет `presentation.html`, блоки chrome/rail/stage/notebook, «як у 17». Не чекай назви скіла.

Немає списку пар — спочатку `strategy_of_cource_building`, потім ця схема на кожну пару.

Не пиши повну густину лекції (lead, SVG, walkthrough). Це скелет. Полірування — `explaine_simple` / `common_lesson` / `teacher-materials-skill`, коли попросять.

## Пайплайн

```
1. Intake     програма + URL, на які сказали спертись
2. Menu       список пар є? ні → strategy_of_cource_building, стоп до меню
3. Scheme     прочитай block-types.md + pair-layout.md
4. Skeleton   на кожну пару — знімок чотирьох зон у порядку схеми
5. Fill       з джерел; дірка → text «Потребує допрацювання»
6. Emit       pair-NN-structure.json (+ markdown-огляд); HTML лекції — лише якщо просили
```

### 1. Intake

Зібрати: назва курсу, N пар × хвилини (типово 80), модулі, пункти програми, лінки практик/ДЗ/статей, які назвав користувач.

Цитувати **ті** джерела, не вигадані. Немає аркуша завдання — слот `task` лишається порожнім.

**Готово:** дерево джерел `модуль → пара → URL/цитата`, без нових тем.

### 2. Menu

Потрібні `global_index`, `title`, `duration_min`, syllabus, objectives. Якщо користувач дав лише програму без розкладу — віддай меню стратегією й не малюй 50 порожніх презентацій навмання.

**Готово:** таблиця пар.

### 3. Scheme

Схема **одна** на всі пари курсу. Не вигадуй пʼяту зону. Не зливай `task` і `example`. Не став Checkpoint одразу після першого завдання.

**Готово:** відкриті `block-types.md` і `pair-layout.md`.

### 4. Skeleton

На пару скопіюй порядок `type` зі схеми. `title` — з теми цієї пари. `id` — стабільний kebab (`banner`, `theory-regularization`, …).

Чотири зони завжди. `toc` один у `rail`. `banner` перший у `stage`. `exit` перед `deep-study`. Teacher-близнюк після кластера, який веде.

**Готово:** повний список слотів, як у схемі.

### 5. Fill

Є факт/умова/лінк — впиши в `text` одне-два речення або цитату джерела. Немає — `Потребує допрацювання`. Слот не видаляй.

Голос студентських типів (`theory`, `example`, `callout`, `trap`, `task`, …) — до читача. `teacher` може говорити «покажіть».

**Готово:** жоден слот без `text`; дірки позначені явно.

### 6. Emit

Один JSON на пару (як `snapshot()` прототипу):

```json
{
  "pair": { "global_index": 17, "title": "", "duration_min": 80, "sources": [] },
  "zones": {
    "chrome": [{ "id": "", "type": "chrome", "kind": "chrome", "title": "", "text": "" }],
    "rail": [{ "id": "toc", "type": "toc", "kind": "nav", "title": "Зміст", "text": "" }],
    "stage": [],
    "notebook": []
  }
}
```

Поруч короткий `pair-NN-skeleton.md`: таблиця `type | title | хв | статус (заповнено / Потребує допрацювання)`.

Зупинись. Каталоги `mXX/pair_YY/presentation.html` створюй лише за явної просьби.

## Заборонена форма

Не: меню пар замість блоків сторінки.  
Не: одна картка «вся пара».  
Не: викинутий слот, бо «поки немає тексту».  
Не: учительський імператив у студентському `callout` / `trap`.  
Не: повна лекція замість скелета, доки не попросили полірування.

## Перевірка

- Є всі чотири зони.
- Порядок `stage` збігається зі схемою за `type` (заголовки можуть бути інші).
- Сума required ≈ 80, якщо хвилини вже розставлені; інакше пігулки банера зі схемою 45+4+24+3+4.
- Кожен порожній `text` = саме `Потребує допрацювання`.
- У `sources` лише ті URL, які дав користувач або які є в програмі пари.
