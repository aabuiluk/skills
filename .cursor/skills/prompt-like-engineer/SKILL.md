---
name: prompt-like-engineer
description: >-
  Applies engineer-grade prompting: director principles, prompt building
  blocks, chaining/few-shot/panel techniques, and Align–Inspect–Refine
  evaluation. Use when writing or reviewing prompts, designing multi-step LLM
  workflows, evaluating model output, or when the user mentions prompt
  engineering / prompt-like-engineer / NetAcad prompting.
---

# Prompt Like an Engineer

Source deposit: `knowledge_saver/deposits/2026-09-13_netacad-apply-ai-od/`  
Deep examples: `D:\knowledge_materials\netacad\prompt-like-an-engineer\lessons\`

You are the **director**. The LLM is one worker alongside spreadsheets, code, and humans. Never default to the model’s next-step suggestions.

## Five guiding principles

1. **Stay in the lead** — You own direction and quality. Reject “AI slop” (polished but unchecked output).
2. **Verify before trusting** — Every output is a draft: **Align → Inspect → Refine**. Only delegate what you can audit.
3. **Weigh the effort** — If prompt + verify + fix > doing it yourself, skip AI for that task.
4. **Adapt AI to you** — Fit tools to your goals; don’t contort the workflow to please the model.
5. **Manage risks** — Follow policy; don’t send confidential data to public chatbots; plan for outages.

## Prompt building blocks

Core = **instruction**. Add as needed:

| Block | Purpose |
|-------|---------|
| Input data | Content to process (paste or upload `.txt` / CSV) |
| Context | Project, audience, background |
| Role | Concise professional lens (long role play ≠ new skills) |
| Constraints | Correct default behavior (“only action items”, “use only provided sources”) |
| Output specs | Format, table layout, length, labels |

**Delimiters** (`###`, backticks, HTML/XML tags) separate instructions from data.

If paste truncates, **upload a `.txt` file** instead.

## Strategies

- Start simple; iterate with follow-ups; close the **instruction gap** as you learn what’s missing.
- **Meta-prompting**: ask the model what parameters matter for this task type.
- After a good multi-turn session, ask it to **consolidate into one reusable prompt**.
- Break work into steps with **checkpoints** (inspect before next step).
- Mix **LLM + spreadsheet/code**: use the model for judgment; use tools for counts, joins, deterministic transforms.

## Techniques

| Technique | When |
|-----------|------|
| **Few-shot** | Hard to describe in words — show input→output (+ why it is good) |
| **Chain-of-thought** | Need *prescribed* steps or verifiable intermediates (generic “think step by step” is weak on modern models) |
| **Prompt chaining** | Multi-step; each output feeds the next; catch errors early |
| **Multi-expert panel** | Separate specialist reviews — **prefer separate chats** per role to avoid cross-contamination |
| **Code over LLM math** | Prefer runnable code for bulk transforms / arithmetic |

## Evaluation (always)

Five questions for any response:

1. Is it **true**?
2. Does it **work**?
3. Is it **what you want**?
4. Is it **logical**?
5. Are **sources cited correctly**?

Also: ask for a **short draft first**, then expand; for edits use labeled tags (`<edit>`, `<explanation>`); for self-check use a **new chat / different model**.

Benchmarks: high accuracy can still mean high **hallucination** (aggressive guessing). Closed-book scores underestimate errors on private/domain work.

## Anti-patterns

- Accepting polished output without Align/Inspect/Refine
- One giant prompt for a whole corpus or long project
- Elaborate role essays instead of clear constraints + examples
- Letting the chatbot choose the next step by default
- Counting / pivoting in the LLM when Excel/code is reliable

## Related skills

- Thematic text pipelines → `ai-thematic-insights`
- Privacy / local↔public hybrid → `ai-private-workflow`
- Teaching these ideas in lessons → `python-educator-senior`
