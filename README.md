# skills

Project Cursor Agent Skills (`aabuiluk/skills`). Homemade / curated skills live under `.cursor/skills/`.

## Skills

| Skill | Role |
|-------|------|
| `teacher-materials-skill` | Python AI Materials: KB → web pair → student zip handout (work in `lesson_helper`) |
| `common_lesson` | Normalize a `python_ai_step` pair to the pair 9/10 reference style |
| `explaine_simple` | Numbered facts + diagram + tooltips; gold pairs 16–18 |
| `strategy_of_cource_building` | Split any syllabus into a pair menu (gold: `python_ai_step` 50×80 min) |
| `python-educator-senior` | Local persona: Python educator + senior (Core, AQA, Backend, DS, AI) |
| `knowledge-saver` | Immutable backup of hard-won knowledge under `knowledge_saver/`, then optional derived skills |
| `prompt-like-engineer` | Engineer-grade prompting: director principles, blocks, chaining, Align–Inspect–Refine |
| `ai-thematic-insights` | Modular LLM+spreadsheet thematic analysis (label → theme → sentiment → pivot → recommend) |
| `ai-private-workflow` | Privacy-first section-by-section AI pipelines (local/public hybrid, redaction) |

## Knowledge archive

Hard-won sources (investigate, scarce downloads, expensive-model / high-token
outputs) go first into [`knowledge_saver/`](knowledge_saver/) as immutable
`deposits/*/raw/`. Derived skills may use **copies**; originals are never deleted.
See [`.cursor/skills/knowledge-saver/SKILL.md`](.cursor/skills/knowledge-saver/SKILL.md).

## Layout

```text
.cursor/skills/
├── teacher-materials-skill/
├── common_lesson/
├── explaine_simple/
├── strategy_of_cource_building/
├── python-educator-senior/
├── knowledge-saver/
├── prompt-like-engineer/
├── ai-thematic-insights/
└── ai-private-workflow/
knowledge_saver/          # immutable deposits (not a skill folder)
└── deposits/
```

NetAcad / OD source dump on disk: `D:\knowledge_materials\` (see deposit `2026-09-13_netacad-apply-ai-od`).