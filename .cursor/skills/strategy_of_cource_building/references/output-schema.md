# Вивід

Два файли. Мова як у програмі.

## thematic-plan.md

```markdown
# {title}

{N} пар · по {duration_min} хв · {M} модулів

{subtitle}

{goal}

Пререквізити: …

## Тематичний план

### Модуль {k}. {офіційна назва}

{n} пари · пари {start}–{end}

{overview}

**Результати навчання**

- …

#### Пара {global_index}. {title}

1. {офіційний пункт програми}.
   - {офіційний підпункт}
2. …

**Цілі пари:** …

## Покриття

| Пункт програми | Пара |
|----------------|------|
| … | {global_index} |
```

Блок «Покриття» — для викладача, який перевіряє скіл; у студентському меню журналу його немає.

## catalog.json

Мінімальні поля, з якими може жити меню на кшталт `python_ai_step`:

```json
{
  "title": "",
  "duration": "N пар · по 80 хв",
  "total_pairs": 50,
  "pair_duration_min": 80,
  "goal": "",
  "prerequisites": [],
  "plan_by_module": { "1": 2 },
  "modules": [
    {
      "order_index": 1,
      "title": "",
      "overview": "",
      "pairs_count": 2,
      "learning_outcomes": []
    }
  ],
  "pairs": [
    {
      "module": 1,
      "module_title": "",
      "pair_index": 1,
      "global_index": 1,
      "title": "",
      "duration_min": 80,
      "objectives": [],
      "topics": [],
      "syllabus": [
        { "title": "", "items": [] }
      ]
    }
  ]
}
```

- `pair_index` — номер у модулі, з 1.
- `global_index` — наскрізний номер пари курсу, з 1.
- `syllabus[].title` / `items` — verbatim з програми.
- `topics` — плоский список тих самих рядків (заголовок + items), для запасного рендеру меню без вкладеності.
- Не обовʼязкові для цього скіла: `path`, `file`, `status`, кольори модулів, `public_plan`.

## Що не емітити

`presentation.html`, `plan.json` слайдів, `teacher.md`, zip роздатку, галочки публікації.
