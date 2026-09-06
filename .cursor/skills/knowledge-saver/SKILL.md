---
name: knowledge-saver
description: >-
  Saves hard-won knowledge as immutable originals under knowledge_saver/, then
  optionally distills copies into internal skills without deleting sources. Use
  when backing up investigate findings, hard-to-reach downloads, expensive-model
  outputs, high-token research, or when the user names knowledge-saver /
  knowledge_saver.
disable-model-invocation: true
---

# knowledge-saver

Резервна копія знань, особливо добутих шляхом investigate, викачаних з
важкодоступних місць, або нагенерованих дорогими моделями / зі значною витратою
токенів.

**Правило:** будь-які такі знання спочатку зберігаємо в **незмінному** вигляді в
папці `knowledge_saver/` проєкту. На їх основі потім робимо внутрішні навички.
Оригінали **не видаляємо**, щоб вони не загубились. Копії можна використовувати
й змінювати; оригінали завжди мають лишатися.

Робочий корінь цього репо:

`/Users/abuiluk/LessonPython/pet_projects/skills`

Архів:

`knowledge_saver/`

## Коли застосовувати

- Результати investigate / deep research, які дорого або важко повторити
- Скрейп / викачка з важкодоступних місць (закриті доки, тимчасові URL, LMS)
- Великі відповіді дорогих моделей, довгі траси агента, витратні токени
- Користувач каже «збережи знання», «knowledge-saver», «knowledge_saver»
- Перед дистиляцією знайденого в новий `.cursor/skills/...` скіл

Не плутати з звичайними комітами коду: це **сховище джерел**, не заміна git.

## Пайплайн (не міняти місцями)

```
1. Deposit   → knowledge_saver/deposits/<id>/raw/   (оригінал, immutable)
2. Manifest  → ORIGIN.md + оновлення INDEX.md
3. (опційно) Derive → копія / дистилят у скіл або notes/
4. Ніколи    → rm / overwrite файлів у raw/
```

## Крок 1. Deposit (оригінал)

Створи каталог:

```text
knowledge_saver/deposits/YYYY-MM-DD_<short-slug>/
├── ORIGIN.md          # звідки, навіщо, вартість/контекст
├── raw/               # ТІЛЬКИ оригінали — не правити після запису
│   └── ...
└── notes/             # опційно: короткі нотатки агента (можна правити)
```

`<short-slug>` — латиниця, `kebab-case`, без пробілів (напр. `cursor-sdk-auth`,
`lms-zip-module3`).

У `raw/` клади файли **як є**: markdown, html, json, pdf, csv, логи, експорти
чату, скріншоти. Не переписуй «красивіше» перед збереженням — спочатку raw.

Якщо джерело вже файл на диску — **скопіюй** (`cp`), не `mv` з єдиної копії.

### ORIGIN.md (обовʼязково)

```markdown
# <title>

- **id:** YYYY-MM-DD_<short-slug>
- **saved:** ISO-8601 datetime
- **source:** URL / path / «chat session» / tool name
- **how_obtained:** investigate | download | expensive-model | high-token | other
- **cost_note:** model, ~tokens, time, access difficulty (якщо відомо)
- **why_keep:** одне речення
- **derived_skills:** (порожньо або список шляхів до скілів, зроблених пізніше)
- **license_warning:** якщо сторонній контент — personal archive only / не публікувати
```

## Крок 2. INDEX

Додай рядок у [`knowledge_saver/INDEX.md`](../../../knowledge_saver/INDEX.md)
(відносний шлях від скіла: `../../../knowledge_saver/INDEX.md`):

| id | date | topic | how | derived |
|----|------|-------|-----|---------|

Не дублюй повний текст джерел у INDEX — лише покажчик.

## Крок 3. Derive (скіл або робоча копія)

Після deposit можна:

1. **Скопіювати** потрібне з `raw/` у робочий каталог / новий скіл
2. Дистилювати структуру (як у `book-to-skill`: frameworks, rules, glossary — не
   сирий dump увесь у `SKILL.md`)
3. У `ORIGIN.md` дописати шлях derived-скіла в `derived_skills`
4. У новому скілі коротко вказати: `Source deposit: knowledge_saver/deposits/<id>/`

Працювати й змінювати **лише копії** (скіл, `notes/`, окремі working files).

## Заборонено

- Видаляти або overwrite файлів у `knowledge_saver/deposits/*/raw/`
- «Прибрати архів, бо вже є скіл»
- Замінювати raw відредагованою версією без нового deposit
- Класти секрети (API keys, паролі, `.env`) у архів — якщо трапились, редact у
  **копії** для скіла; у raw краще не класти взагалі, або окремий
  `raw/.private` + gitignore (узгодити з користувачем)

Якщо треба оновити знання з того самого джерела — новий deposit
`YYYY-MM-DD_<slug>-v2` (або нова дата), старий не чіпати.

## Чеклист

- [ ] Створено `deposits/<id>/raw/` з незмінними файлами
- [ ] Є `ORIGIN.md` з provenance
- [ ] Оновлено `knowledge_saver/INDEX.md`
- [ ] Derived-скіл (якщо є) посилається на deposit і не замінює raw
- [ ] Нічого з `raw/` не видалено й не перезаписано
