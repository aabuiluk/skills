# Why Materials 15–16 were garbage, and what the rewrite did

## What shipped before (anti-pattern)

Bulk generator:

- `generate_pairs_15_50.py` → `_pair_content_mNN.py` thin `pair_N()` → `pair_web_writer.py`
- Contract per theory block: **1 paragraph + 1 snippet + 1 callout**
- Catalog stamped `"status": "ready"`
- `teacher-materials-skill` only required the **journal skeleton** (theory → extra → ITSTEP → deep-study, timed sum 80). The generator satisfied the shell, not teaching.
- `common_lesson` (v2, leads, examples before abstraction) was applied to **python_ai_step pairs 9–14 only**, never to Materials 15–16.
- Pairs 1–14 had dedicated pack generators (still ~1 banner lead). Pairs 15–50 were one-shot cards (~33–40 KB, 1 lead).

Before rewrite, Materials 15/16 HTML was ~36 KB, ~10 articles, 1 banner lead, empty/short teacher.md, no checkpoint/exit, no SVG, theory bodies ~300–500 chars.

## Gold the owner accepted (2026-09-11 dialogue)

Pedagogy of **common_lesson pairs 9/10** inside the **Materials writer**, not step `data-material-version` blocks.

Source of truth: `backend/data/courses/python_ai_materials/tools/_rich_pairs_15_16.py`

Pair 15 (~18 articles, 80 min, ~14 leads). Pair 16 same density.

Writer upgrades that must stay:

- `kind_label` on theory (теорія / перевірка)
- task `why`/`context` → callout «Звідки дані і навіщо»
- spec `checks` after ITSTEP, timed, count toward 80; practice_min = 80 − theory − checks, still ≥ 20
- `teacher_md_full` passthrough
- Presentation tips self-contained (no leftover names, no `__file__` in notebook tips)
- Student voice: ви / зверніть увагу
- Hand calc must match autograd (`loss.item()`)

## Publish gate

- **Never** write `public_plan.json` checkboxes the owner did not tick.
- Student `/course/python_ai_step` shows Materials checkmarks via `student_visible_pairs`. That must **not** tick boxes on `/courses/python_ai_step`.

## Remaining work

Pairs 17–50 (and 1–14 if still 1-lead) rewrite to this gold via `_rich_pairs_*.py` imported from `specs()`, never by re-running `generate_pairs_15_50.py` as the teaching source.
