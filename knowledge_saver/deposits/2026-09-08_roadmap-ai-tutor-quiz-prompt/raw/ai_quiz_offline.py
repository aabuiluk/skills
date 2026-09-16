"""Offline AI quiz generation (stream format matching live /api/v1-generate-ai-quiz).

Live roadmap.sh streams quiz markdown; locally we:
1. Prefer a previously cached live quiz (data_site/api/api__v1-get-ai-quiz__*.json)
2. Else call OpenAI with the same output contract as the live AI Tutor (if OPENAI_API_KEY)
3. Else fall back to a grounded markdown template from local topic notes
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator
from uuid import uuid4

from shared.paths import DATA, DATA_SITE, ROOT

from roadmap_sh.site_api import load_api
from roadmap_sh.site_copy import api_out_path, write_json

# Reverse-engineered from live /api/v1-generate-ai-quiz streams (2026-09).
# Keep this in sync with real tutor output: MCQ + explanations + open questions.
TUTOR_QUIZ_SYSTEM_PROMPT = """
You are the roadmap.sh AI Tutor quiz generator.

Write a quiz about the learner's keyword for a developer roadmap. Output ONLY the quiz
markdown body — no title line, no JSON, no preamble.

Output format (strict):
- Multiple-choice questions start with a line: `# <question>`
- Exactly four options, each on its own line
- Incorrect options MUST start with exactly: `- ` (dash + space)
- The single correct option MUST start with exactly: `-* ` (dash + asterisk + space)
  Example correct line: `-* display: flex`
  Example wrong line: `- display: grid`
  NEVER put the asterisk inside the option text (bad: `- display: flex-*`, `- It-* allows…`)
- Immediately after the options, one explanation line: `## <why the correct option is right>`
  Prefer "Option N is correct because …" or "<correct answer> is correct because …"
- Open-ended questions (mixed format only) are a single line: `### <prompt>`
- Separate blocks with a blank line
- No markdown headings other than `#`, `##`, `###`
- No code fences unless the question itself is about a short code snippet (then keep the
  snippet inside the `#` question text or as an option)

Content rules:
- Questions must be domain-specific and factually correct for the keyword
- Distractors must be plausible misconceptions, not absurd jokes
- Prefer fundamentals that appear on developer roadmaps (definitions, when to use,
  common pitfalls, complexity, related tools)
- Use the optional context notes when provided; do not invent APIs that contradict them
- Keep language clear for intermediate learners

Format modes:
- mixed: about 4 multiple-choice questions interleaved with 3–4 `###` open questions
- mcq: about 8–10 multiple-choice questions only (no `###` lines)
- open: about 6–8 `###` open questions only (no `#` MCQ blocks)
""".strip()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def slugify_keyword(keyword: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", (keyword or "topic").lower()).strip("-") or "topic"
    return f"{base}-quiz-generation"


def _load_topic_context(keyword: str, roadmap_slug: str = "", node_id: str = "") -> str:
    """Pull local topic markdown so offline generation stays grounded."""
    chunks: list[str] = []
    needle = (keyword or "").strip().lower()
    if not needle:
        return ""

    search_dirs: list[Path] = []
    if roadmap_slug:
        search_dirs.append(DATA / "roadmaps" / roadmap_slug / "topics")
    else:
        search_dirs.extend(sorted((DATA / "roadmaps").glob("*/topics")))

    for topics_dir in search_dirs:
        if not topics_dir.is_dir():
            continue
        for path in sorted(topics_dir.glob("*.md")):
            stem = path.stem.lower()
            if node_id and f"@{node_id.lower()}" in stem:
                text = path.read_text(encoding="utf-8", errors="replace")
                chunks.append(f"### file:{path.name}\n{text[:4000]}")
                break
            label = stem.split("@", 1)[0].replace("-", " ")
            if needle in label or any(tok in label for tok in needle.split() if len(tok) > 2):
                text = path.read_text(encoding="utf-8", errors="replace")
                chunks.append(f"### file:{path.name}\n{text[:2500]}")
                if len(chunks) >= 3:
                    break
        if chunks:
            break
    return "\n\n".join(chunks)[:7000]


def _template_content(
    keyword: str,
    *,
    roadmap_slug: str = "",
    node_id: str = "",
    fmt: str = "mixed",
    context: str = "",
) -> str:
    """Deterministic fallback when cache + OpenAI are unavailable."""
    topic = keyword.strip() or "this topic"
    ctx_note = ""
    if roadmap_slug:
        ctx_note = f" on the {roadmap_slug} roadmap"
    if node_id:
        ctx_note += f" (node {node_id})"

    facts: list[str] = []
    for line in context.splitlines():
        line = line.strip().lstrip("-* ").strip()
        if 40 <= len(line) <= 180 and not line.startswith("#") and "http" not in line.lower():
            facts.append(line)
        if len(facts) >= 4:
            break
    while len(facts) < 4:
        facts.append(f"{topic} is a concept you should be able to explain and apply{ctx_note}.")

    mcq_blocks = [
        (
            f"# What is the primary purpose of {topic}{ctx_note}?",
            [
                f"A deprecated marketing term unrelated to {topic}",
                f"An implementation detail that never affects real systems",
                facts[0][:120],
                f"Only a syntax sugar feature with no practical trade-offs",
            ],
            2,
            f"Option 3 is correct because it reflects a core idea of {topic}: {facts[0][:160]}",
        ),
        (
            f"# Which statement about {topic} is most accurate for a practitioner?",
            [
                f"It replaces the need to learn fundamentals around {topic}",
                facts[1][:120],
                f"It is identical to every neighboring topic and needs no separate study",
                f"It only matters in academic papers, never in production",
            ],
            1,
            f"Option 2 is correct because practical use of {topic} centers on: {facts[1][:160]}",
        ),
        (
            f"# When applying {topic}, what should you do after reading a definition?",
            [
                "Memorize only the name and stop",
                "Skip related prerequisites entirely",
                "Apply it on a small example and check edge cases",
                "Avoid comparing it to similar concepts",
            ],
            2,
            f"Option 3 is correct because applying {topic} on a small example cements understanding better than rote recall.",
        ),
        (
            f"# Which learning habit helps most when studying {topic}?",
            [
                "Only watching videos without notes or practice",
                "Alternating short theory with hands-on checks and feedback",
                "Ignoring error messages and copying answers",
                "Avoiding documentation until an interview",
            ],
            1,
            f"Option 2 is correct because active practice with feedback is the strongest loop for mastering {topic}.",
        ),
    ]

    open_qs = [
        f"### In your own words, explain what {topic} is and why it matters{ctx_note}.",
        f"### Describe one concrete scenario where choosing {topic} (or applying it) is clearly the right call.",
        f"### What is a common misconception about {topic}, and how would you correct it?",
        f"### Outline the first small exercise you would give a junior to practice {topic}.",
    ]

    def render_mcq(q: str, options: list[str], correct_idx: int, expl: str) -> str:
        lines = [q]
        for i, opt in enumerate(options):
            prefix = "-* " if i == correct_idx else "- "
            lines.append(f"{prefix}{opt}")
        lines.append(f"## {expl}")
        return "\n".join(lines)

    fmt = (fmt or "mixed").lower()
    if fmt == "open":
        return "\n\n".join(open_qs[:6]) + "\n"
    if fmt == "mcq":
        # Expand to ~8 MCQs by repeating with slight focus shifts.
        extra = [
            (
                f"# Which risk should you watch for when working with {topic}?",
                [
                    "Assuming it has no trade-offs or failure modes",
                    "Documenting assumptions and measuring results",
                    "Reading official docs before changing production",
                    "Writing a small regression check after changes",
                ],
                0,
                f"Option 1 is correct because treating {topic} as risk-free is a common and costly mistake.",
            ),
            (
                f"# How does {topic} typically relate to neighboring fundamentals?",
                [
                    "It replaces networking, data structures, and testing entirely",
                    "It builds on fundamentals and should be learned with them, not instead of them",
                    "It is only useful after abandoning prior skills",
                    "It has no relationship to other roadmap topics",
                ],
                1,
                f"Option 2 is correct because {topic} sits on top of fundamentals rather than replacing them.",
            ),
            (
                f"# What is a good first validation that you understand {topic}?",
                [
                    "Being able to recite the name only",
                    "Explaining it and solving one tiny concrete example correctly",
                    "Waiting until a senior confirms without trying yourself",
                    "Skipping feedback loops",
                ],
                1,
                f"Option 2 is correct because explaining {topic} plus a tiny worked example is a strong early check.",
            ),
            (
                f"# Which resource habit helps most when going deeper into {topic}?",
                [
                    "Copying answers without reading explanations",
                    "Mixing short theory, docs, and deliberate practice",
                    "Only collecting bookmarks and never opening them",
                    "Avoiding error messages",
                ],
                1,
                f"Option 2 is correct because mixing theory, docs, and practice is how {topic} sticks.",
            ),
        ]
        blocks = [render_mcq(*b) for b in (mcq_blocks + extra)]
        return "\n\n".join(blocks) + "\n"

    # mixed: interleave MCQ + open
    parts: list[str] = []
    for i, block in enumerate(mcq_blocks):
        parts.append(render_mcq(*block))
        if i < len(open_qs):
            parts.append(open_qs[i])
    return "\n\n".join(parts) + "\n"


def _normalize_quiz_markdown(content: str) -> str:
    """Repair common model mistakes around the `-* ` correct-option marker."""
    lines: list[str] = []
    option_buf: list[str] = []

    def flush_options() -> None:
        nonlocal option_buf
        if not option_buf:
            return
        fixed: list[str] = []
        correct_idx = -1
        for i, raw in enumerate(option_buf):
            text = raw.lstrip()
            # Already correct marker
            if text.startswith("-* "):
                correct_idx = i
                fixed.append("-* " + text[3:].strip())
                continue
            # Asterisk stuck to the dash without space: -*-foo / -*foo
            if text.startswith("-*") and not text.startswith("-* "):
                correct_idx = i
                fixed.append("-* " + text[2:].lstrip(" :").strip())
                continue
            # Asterisk embedded in option text: "- foo-* bar" or "- foo-*"
            m = re.match(r"^-\s+(?P<body>.*)$", text)
            body = m.group("body") if m else text
            if "-*" in body or body.rstrip().endswith("*"):
                correct_idx = i
                body = body.replace("-*", " ").replace("*", " ")
                body = re.sub(r"\s+", " ", body).strip()
                fixed.append("-* " + body)
            else:
                fixed.append("- " + body.strip())
        if correct_idx < 0 and fixed:
            # Last resort: mark first option correct so the quiz stays parseable.
            fixed[0] = "-* " + fixed[0][2:].lstrip()
        lines.extend(fixed)
        option_buf = []

    for line in content.splitlines():
        if re.match(r"^-\*?\s?", line) or (line.startswith("-") and not line.startswith("---")):
            # Option-like line
            if line.startswith("#"):
                flush_options()
                lines.append(line)
            elif line.startswith("##") or line.startswith("###"):
                flush_options()
                lines.append(line)
            else:
                option_buf.append(line)
        else:
            flush_options()
            lines.append(line)
    flush_options()
    text = "\n".join(lines).strip() + "\n"
    # Collapse accidental double markers
    text = re.sub(r"^-\*\s+-\*\s+", "-* ", text, flags=re.M)
    return text


def _openai_generate(
    keyword: str,
    *,
    fmt: str,
    roadmap_slug: str,
    node_id: str,
    context: str,
) -> str | None:
    api_key = (os.environ.get("OPENAI_API_KEY") or "").strip().strip("'\"")
    if not api_key:
        return None
    model = (os.environ.get("OPENAI_MODEL") or "gpt-4o-mini").strip()
    user = {
        "keyword": keyword,
        "format": fmt or "mixed",
        "roadmapSlug": roadmap_slug or None,
        "nodeId": node_id or None,
        "contextNotes": context or None,
    }
    try:
        import httpx

        with httpx.Client(timeout=90.0) as client:
            r = client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "temperature": 0.4,
                    "messages": [
                        {"role": "system", "content": TUTOR_QUIZ_SYSTEM_PROMPT},
                        {
                            "role": "user",
                            "content": (
                                "Generate the quiz markdown for this request as JSON fields imply:\n"
                                + json.dumps(user, ensure_ascii=False, indent=2)
                            ),
                        },
                    ],
                },
            )
        if r.status_code >= 400:
            return None
        data = r.json()
        content = (
            ((data.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
        ).strip()
        if not content.startswith("#") and "###" not in content[:80]:
            # Sometimes models wrap in fences — strip once.
            content = re.sub(r"^```(?:markdown|md)?\s*", "", content)
            content = re.sub(r"\s*```$", "", content).strip()
        if content.count("\n# ") + (1 if content.startswith("#") else 0) < 1 and "###" not in content:
            return None
        return _normalize_quiz_markdown(content)
    except Exception:
        return None


def _find_cached_by_keyword(keyword: str) -> dict[str, Any] | None:
    needle = (keyword or "").strip().lower()
    if not needle:
        return None
    api_dir = DATA_SITE / "api"
    if not api_dir.is_dir():
        return None
    needle_slug = needle.replace(" ", "-")
    best: tuple[int, dict[str, Any]] | None = None
    for path in sorted(api_dir.glob("api__v1-get-ai-quiz__*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not isinstance(data, dict) or not data.get("content"):
            continue
        kw = str(data.get("keyword") or "").lower()
        title = str(data.get("title") or "").lower()
        slug = str(data.get("slug") or "").lower()
        score = 0
        if needle == kw:
            score = 100
        elif needle_slug == slug or needle_slug in slug:
            score = 80
        elif needle in kw or needle in title:
            score = 60
        elif all(tok in (kw + " " + title + " " + slug) for tok in needle.split() if len(tok) > 2):
            score = 40
        if score and (best is None or score > best[0]):
            best = (score, data)
    return best[1] if best else None


def build_quiz_payload(body: dict[str, Any]) -> dict[str, Any]:
    keyword = str(body.get("keyword") or "topic").strip() or "topic"
    fmt = str(body.get("format") or "mixed")
    roadmap_slug = str(body.get("roadmapSlug") or "")
    node_id = str(body.get("nodeId") or "")
    ai_roadmap_id = str(body.get("aiRoadmapId") or "")

    cached = _find_cached_by_keyword(keyword)
    if cached and cached.get("content"):
        payload = dict(cached)
        payload.setdefault("format", fmt)
        meta = dict(payload.get("metadata") or {})
        if roadmap_slug:
            meta["roadmapSlug"] = roadmap_slug
        if node_id:
            meta["nodeId"] = node_id
        if ai_roadmap_id:
            meta["aiRoadmapId"] = ai_roadmap_id
        payload["metadata"] = meta
        return payload

    context = _load_topic_context(keyword, roadmap_slug=roadmap_slug, node_id=node_id)
    content = _openai_generate(
        keyword,
        fmt=fmt,
        roadmap_slug=roadmap_slug,
        node_id=node_id,
        context=context,
    )
    source = "openai" if content else "template"
    if not content:
        content = _template_content(
            keyword,
            roadmap_slug=roadmap_slug,
            node_id=node_id,
            fmt=fmt,
            context=context,
        )

    slug = slugify_keyword(keyword)
    now = _utc_now()
    me = load_api("/api/v1-me")
    user_id = ""
    if isinstance(me, dict):
        user_id = str(me.get("_id") or "")
    payload = {
        "_id": uuid4().hex[:24],
        "userId": user_id,
        "keyword": keyword.lower(),
        "title": f"{keyword.title()} Quiz Generation",
        "slug": slug,
        "format": fmt,
        "content": content,
        "viewCount": 1,
        "lastVisitedAt": now,
        "metadata": {
            **({"roadmapSlug": roadmap_slug} if roadmap_slug else {}),
            **({"nodeId": node_id} if node_id else {}),
            **({"aiRoadmapId": ai_roadmap_id} if ai_roadmap_id else {}),
            "offline": True,
            "generator": source,
        },
        "createdAt": now,
        "updatedAt": now,
    }
    return payload


def persist_quiz(payload: dict[str, Any]) -> Path:
    slug = str(payload.get("slug") or "offline-quiz")
    path = api_out_path(f"/api/v1-get-ai-quiz/{slug}")
    write_json(path, payload)
    return path


def stream_generate_ai_quiz(payload: dict[str, Any], *, chunk_size: int = 48) -> Iterator[bytes]:
    """Yield Vercel AI-style stream: ``0:"…"`` chunks then ``d:{…details}``."""
    content = str(payload.get("content") or "")
    for i in range(0, max(len(content), 1), chunk_size):
        piece = content[i : i + chunk_size]
        yield f"0:{json.dumps(piece, ensure_ascii=False)}\n".encode("utf-8")
    # Client onData expects type=details from the `d:` stream part.
    yield f"d:{json.dumps(payload, ensure_ascii=False)}\n".encode("utf-8")
