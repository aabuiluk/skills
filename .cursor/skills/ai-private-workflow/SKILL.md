---
name: ai-private-workflow
description: >-
  Designs privacy-first, section-by-section AI pipelines with local/public
  hybrid steps, redaction placeholders, and systematic review. Use when
  handling resumes or other sensitive documents, choosing local vs cloud LLMs,
  prototyping multi-step AI workflows, or when the user mentions privacy-first
  AI / build-your-resume-with-ai patterns.
---

# AI Private Workflow

Source deposit: `knowledge_saver/deposits/2026-09-13_netacad-apply-ai-od/`  
Worked example (resume): `D:\knowledge_materials\netacad\build-your-resume-with-ai\lessons\`

Resume is the **canonical lab**; the same pattern applies to any sensitive multi-section document (CV, performance notes, client briefs).

## Five guiding principles

1. **Privacy** — Protect sensitive data via local LLMs or de-identification.  
2. **Prototyping** — Experiment, critique, redesign, iterate.  
3. **Structured process** — Methodically section by section, line by line.  
4. **Focused context** — Keep accomplishments / sections distinct; avoid spillover.  
5. **Systematic review** — LLM self-checks + human evaluation + comparison tools / spreadsheets.

## Local vs public

| | Local LLM | Public chatbot |
|---|-----------|----------------|
| Privacy | Data stays on device | May train / retain prompts |
| Capability | Weaker on hard formatting | Stronger tools / larger models |
| Cost/use | Unlimited after download | Quotas / fees |
| Hardware | RAM limits model size + context; CPU/GPU → speed | N/A |

**Default local** for sensitive work. Use public only when capability requires it — **after redaction**.

## Sensitive-document workflow

```text
1. Flag sensitive fields (local LLM or manual)
2. Redact / replace with placeholders locally
3. Public (or strong) model does the hard non-sensitive subtask
4. Reinsert secrets locally (manual or local LLM)
5. Systematic review before shipping
```

Sensitive examples: contact info, confidential projects, coworker names, internal politics, layoffs/restructuring. Never paste confidential current/past work details into public tools for job apps.

### Hybrid patterns

1. **Anonymize → public format → restore locally**  
2. **Template method**: public creates HTML/CSS template → local fills with real content  

Objectives when designing any workflow: **privacy, quality, transparency** (what changed and why), **efficiency** (repeatable).

## Processing modes

| Mode | Idea | Use when |
|------|------|----------|
| Bulk | All sections in one go | Known-good prompt; low sensitivity spillover risk |
| Sequential (task-by-task) | Same task across all sections | Avoid mixing; clear per-task focus |
| **Section-by-section end-to-end** | Finish one section through all steps before the next | **Default while prototyping** — refine the process before scaling |

Each section may need: extract → synthesize bullets → edit/refine → (later) tailor to a job / format.

## Systematic review

- Combine model self-check with **human** read and diffs / spreadsheets.  
- Save intermediate artifacts (long bullets, skills lists) for later ATS tailoring.  
- Meta-prompt → reusable template prompts once a section workflow works.

## Anti-patterns

- Defaulting to public chat for “convenience” with PII still present  
- Bulk-processing a new workflow before one section is proven  
- Mixing projects/sections in one prompt (context bleed)  
- Skipping reinsertion / final human review after hybrid formatting  

## Related skills

- Prompt building / Align–Inspect–Refine → `prompt-like-engineer`  
- Large text corpora insights → `ai-thematic-insights`
