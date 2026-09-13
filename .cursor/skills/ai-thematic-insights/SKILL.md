---
name: ai-thematic-insights
description: >-
  Runs modular LLM+spreadsheet thematic analysis: per-item topic labels,
  theme grouping, per-theme sentiment, pivots, sampled reviews, then
  recommendations with human checkpoints. Use for open-ended text (reviews,
  tickets, feedback), Find Insights with AI workflows, or when the user wants
  insights from many comments without dumping the whole corpus into one chat.
---

# AI Thematic Insights

Source deposit: `knowledge_saver/deposits/2026-09-13_netacad-apply-ai-od/`  
Deep examples: `D:\knowledge_materials\netacad\find-insights-with-ai\lessons\`

## Problem

Open-ended text (reviews, tickets, course feedback) resists keyword counts and one-shot chatbot summaries. LLMs have **context limits** and **soft degradation** on large pastes: answers look fine but miss detail or hallucinate, and you cannot verify how they got there.

**Never** dump the whole corpus into one chat for “themes + summary + recommendations.”

## Classic thematic analysis

1. Find key themes  
2. Label each comment (multi-label OK)  
3. Count mentions  
4. Summarize and recommend  

## LLM-safe modular pipeline

Adjust steps 1–2 so each LLM call is small and checkable:

```text
1. Per-comment topic labels (+ relevance 0–5)
2. Human review / clean / batch if needed
3. Flatten one-to-many topic rows (code or spreadsheet)
4. Group topics → themes (human + LLM assist)
5. Per-theme sentiment per row (−1 / 0 / 1)
6. Pivot counts (and optional Σ relevance) in spreadsheet — not in the LLM
7. Sample reviews by theme × sentiment
8. Row-wise analysis + recommendations (one theme’s evidence per row)
```

Human in the loop after labeling: fix false themes, merge overlaps, rename generic themes, catch relevance `0` that should be high (models fail more on huge tables than on single rows).

## Prompt rules for labeling

- State **goal**, **output columns**, **definitions**, **few-shot examples**.
- Prefer **relevance scores 0–5** over binary keep/drop.
- Sentiment: numeric **1 / 0 / −1** scoped to the **theme**, not the whole review.
- Instruct: process **row by row**, keep **input order** (models otherwise regroup and break joins).
- If quality drops: **batch** rows or send only needed columns.
- Prefer LM topic labels over brittle keyword rules; watch rate limits / partial runs.

## Spreadsheet / code jobs (not LLM)

| Job | Tool |
|-----|------|
| Flatten multi-topic rows | Code interpreter / script + few-shot (goal, columns, examples, “write and run code”, export CSV) |
| Counts by theme × sentiment | Pivot table |
| Weight by relevance | Sum relevance scores |
| Sample quotes | Filter by theme + sentiment (Excel formulas OK) |

Final recommend step: one spreadsheet row per theme with counts + condensed samples; prompt the model to weigh sentiment and propose actions **per row**.

## Anti-patterns

- One mega-prompt over the full dataset  
- Asking the LLM to count or pivot accurately without running code  
- Binary relevance with no human review  
- Sentiment on the whole review when analysis is per-theme  
- Skipping samples — recommendations without grounded quotes

## Related skills

- Prompt craft / evaluation → `prompt-like-engineer`
- Sensitive corpora / local models → `ai-private-workflow`
