# Карта graft

Форма виводу скіла. Один файл на пару. Мова як у матеріалах пари (типово українська).

## pair-NN-growth.md

```markdown
# Пара {global_index}. {title}

Версія матеріалів: {material_version або «скелет»}  
Required: {сума} хв · хуків відкрито: {n}

## Freeze

| id | type | хв | факт (одне речення) |
|----|------|----|---------------------|
| … | theory | 5 | … |

## Hooks

| id | стан | прийме |
|----|------|--------|
| task-2 | hole | офіційний аркуш LMS |
| deep-study | stub | стаття / розділ книжки |

## Grafts

| джерело | клас | into | layer |
|---------|------|------|-------|
| {URL або файл} | приклад | example-dropout | extra |

## Лишилось

- …
```

Блок Freeze — щоб наступний агент не перейменував core. Hooks — куди класти наступне джерело. Grafts — що щойно вживили. Лишилось — hole/stub/unmatched після цієї сесії.

## graft.json

```json
{
  "pair": {
    "global_index": 17,
    "title": "",
    "duration_min": 80,
    "material_version": "12.0",
    "sources": []
  },
  "frozen": [
    {
      "id": "theory-regularization",
      "type": "theory",
      "minutes": 5,
      "fact": ""
    }
  ],
  "hooks": [
    {
      "id": "task-2",
      "type": "task",
      "state": "hole",
      "accepts": "official LMS sheet"
    }
  ],
  "grafts": [
    {
      "source": "",
      "class": "example",
      "into": "example-dropout",
      "layer": "extra",
      "note": ""
    }
  ]
}
```

`state`: `hole` | `stub` | `core` | `thick`.  
`layer`: `required` | `extra` | `teacher` | `take-home` | `version`.  
`class`: `fact` | `example` | `trap` | `task` | `homework` | `deeper` | `teacher` | `term`.

Порожній `grafts` нормальний, якщо користувач просив лише відкрити пару до росту (розставити хуки), без нового URL.

## Приклад рішення

Вхід: скелет пари 17, `task-2` = «Потребує допрацювання», користувач дав статтю про weight decay.

Вихід:

- `task-2` лишається hole (стаття — не аркуш LMS)
- graft статті → `extra` / deep-study `deep-study-weight-decay`, шар `take-home`
- required 80 не змінюється
- у Hooks з’являється той самий `task-2` плюс, якщо deep-study був stub, його стан стає thick або stub із цитатою

Вхід: густа пара 16 і прохання «зроби коротшу версію для слабкої групи».

Вихід:

- не різати існуючий шар
- якщо потрібен короткий шлях — тогл Коротко/Детально або окремий extra, не `until` що ховає повний текст
- grafts порожній або version-from з **додатковим** коротким маршрутом поруч
