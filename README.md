# skills

Project Cursor Agent Skills (`aabuiluk/skills`). Homemade / curated skills live under `.cursor/skills/`.

## Skills

| Skill | Role |
|-------|------|
| `teacher-materials-skill` | Python AI Materials: KB → web pair → student zip handout (work in `lesson_helper`) |
| `common_lesson` | Normalize a `python_ai_step` pair to the pair 9/10 reference style |
| `python-educator-senior` | Local persona: Python educator + senior (Core, AQA, Backend, DS, AI) |
| `knowledge-saver` | Immutable backup of hard-won knowledge under `knowledge_saver/`, then optional derived skills |

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
├── python-educator-senior/
└── knowledge-saver/
knowledge_saver/          # immutable deposits (not a skill folder)
└── deposits/
```
