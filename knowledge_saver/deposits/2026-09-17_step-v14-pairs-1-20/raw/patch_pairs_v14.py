#!/usr/bin/env python3
"""Material v14.0: explaine_simple + tactic layout + growth for pairs 1–20."""

from __future__ import annotations

import html as html_lib
import json
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from v14_content import (  # noqa: E402
    AFTER_START,
    ALL_PAIRS,
    CHECKS,
    DETAILS,
    FACTS,
    GOLD_MAP,
    TARGET,
    THESIS,
    TITLES,
)

COURSE = Path(__file__).resolve().parents[1]

ACC = "#7dffb3"
BLU = "#7ec8ff"
WARM = "#ffb86b"
PINK = "#ff7d9a"
INK = "#e8f0e7"
MUTE = "#9aafa0"
PANEL = "#15221b"
STROKE = "#2f4137"

CSS = """
.lh-depth-bar{
  position:sticky;top:0;z-index:8;
  display:flex;flex-wrap:wrap;gap:.55rem .9rem;align-items:center;
  margin:0 0 1rem;padding:.65rem .8rem;
  background:rgba(15,20,18,.96);border:1px solid var(--line);border-radius:12px;
}
.lh-depth-label{margin:0;font-weight:800;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);}
.lh-depth-hint{margin:0;color:var(--mute);font-size:.82rem;flex:1 1 12rem;}
.lh-depth-switch{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;}
.lh-depth-btn{
  appearance:none;border:0;background:transparent;color:var(--ink);
  font:700 .85rem var(--font);padding:.4rem .9rem;cursor:pointer;
}
.lh-depth-btn[aria-pressed="true"]{background:var(--accent);color:var(--accent-ink);}
.lh-depth-bar.lh-depth-local{position:static;top:auto;z-index:1;background:rgba(15,20,18,.72);}
.lh-explain-detail{display:none;}
article.lh-is-detail .lh-explain-detail{display:block;}
article.lh-is-detail .lh-explain-short{display:none;}
.diagram svg text { paint-order: stroke fill; pointer-events: none; }
.diagram svg text.term, .diagram svg [data-tip] { pointer-events: auto; cursor: help; }
.diagram svg rect.term, .diagram svg circle.term { cursor: help; }
"""

JS = r"""
<script id="lh-v11-depth-js">
(function () {
  try { localStorage.removeItem("lh.explain.depth.v11"); } catch (e) {}
  document.querySelectorAll("[data-lh-depth-bar]").forEach(function (bar) {
    var root = bar.closest("article");
    if (!root) return;
    function apply(depth) {
      var detail = depth === "detail";
      root.classList.toggle("lh-is-detail", detail);
      bar.querySelectorAll(".lh-depth-btn").forEach(function (btn) {
        btn.setAttribute("aria-pressed", btn.getAttribute("data-depth") === depth ? "true" : "false");
      });
    }
    bar.querySelectorAll(".lh-depth-btn").forEach(function (btn) {
      btn.addEventListener("click", function () { apply(btn.getAttribute("data-depth")); });
    });
    apply("short");
  });
})();
</script>
"""

SWITCH = """
<div class="lh-depth-bar lh-depth-local" data-lh-depth-bar>
  <p class="lh-depth-label">Глибина пояснення</p>
  <div class="lh-depth-switch" role="group" aria-label="Глибина пояснення">
    <button type="button" class="lh-depth-btn" data-depth="short" aria-pressed="true">Коротко</button>
    <button type="button" class="lh-depth-btn" data-depth="detail" aria-pressed="false">Детально</button>
  </div>
  <p class="lh-depth-hint">За замовчуванням — коротко в цьому блоці. «Детально» відкриває лише його.</p>
</div>
"""


def esc(text: str) -> str:
    return html_lib.escape(text, quote=False)


def esc_attr(text: str) -> str:
    return html_lib.escape(text, quote=True)


def md_code(text: str) -> str:
    parts = re.split(r"`([^`]+)`", text)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2:
            out.append(f'<code class="mv">{esc(part)}</code>')
        else:
            out.append(esc(part))
    return "".join(out)


def t(
    x: float,
    y: float,
    text: str,
    tip: str,
    size: int = 12,
    fill: str = INK,
    weight: int = 700,
) -> str:
    return (
        f'<text class="term" data-tip="{esc_attr(tip)}" tabindex="0" role="button" '
        f'x="{x:.0f}" y="{y:.0f}" text-anchor="middle" fill="{fill}" '
        f'font-size="{size}" font-weight="{weight}" font-family="Manrope, system-ui, sans-serif" '
        f'style="pointer-events:auto">{esc(text)}</text>'
    )


def rect(x: float, y: float, w: float, h: float, tip: str, stroke: str = ACC) -> str:
    return (
        f'<rect class="term" data-tip="{esc_attr(tip)}" x="{x:.0f}" y="{y:.0f}" '
        f'width="{w:.0f}" height="{h:.0f}" rx="10" fill="{PANEL}" stroke="{stroke}" '
        f'stroke-width="1.6" style="pointer-events:auto;cursor:help"/>'
    )


def map_svg(rel: str) -> str:
    titles = TITLES[rel]
    facts = FACTS[rel]
    parts = [
        '<svg viewBox="0 0 640 220" role="img" aria-hidden="true" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    colors = (ACC, BLU, WARM, PINK, ACC)
    for i, (title, fact) in enumerate(zip(titles, facts)):
        col, row = i % 5, i // 5
        x, y = 12 + col * 126, 18 + row * 100
        tip = f"{i + 1}. {title}\n{fact}"
        parts.append(rect(x, y, 118, 84, tip, colors[col]))
        parts.append(t(x + 59, y + 32, f"{i + 1}", tip, 11, MUTE, 600))
        label = title if len(title) <= 14 else title[:13] + "…"
        parts.append(t(x + 59, y + 54, label, tip, 11, INK, 700))
    parts.append("</svg>")
    return "".join(parts)


def flow_svg(rel: str, n: int) -> str:
    titles = TITLES[rel]
    facts = FACTS[rel]
    fact = facts[n]
    title = titles[n]
    uid = f"v14{rel[-2:]}s{n+1}"
    left = title
    right = "далі в лекції"
    tip_l = f"{n + 1}. {title}\n{fact}"
    tip_r = "Той самий факт нижче в теоретичному блоці, не інший текст."
    inner = (
        f'<defs><marker id="{uid}-a" markerWidth="8" markerHeight="8" refX="7" refY="4" '
        f'orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{ACC}"/></marker></defs>'
        + rect(40, 55, 220, 90, tip_l, ACC)
        + t(150, 105, left if len(left) <= 18 else left[:17] + "…", tip_l)
        + f'<line x1="260" y1="100" x2="360" y2="100" stroke="{ACC}" stroke-width="2.2" '
        f'marker-end="url(#{uid}-a)"/>'
        + rect(360, 55, 240, 90, tip_r, BLU)
        + t(480, 105, right, tip_r)
    )
    return (
        f'<svg viewBox="0 0 640 200" role="img" aria-hidden="true" '
        f'xmlns="http://www.w3.org/2000/svg">{inner}</svg>'
    )


def catalog_title(rel: str) -> str:
    data = json.loads((COURSE / "catalog.json").read_text(encoding="utf-8"))
    for pair in data["pairs"]:
        if pair["path"].rstrip("/") == rel:
            return f"Пара {pair['global_index']}. {pair['title']}"
    return rel


def teacher_thesis(rel: str) -> str:
    return (
        '<article class="block teacher-deep-dive" id="v14-teacher-thesis" '
        'data-timing="optional" data-material-version-from="14.0" '
        'data-project-feature="python-ai-modify-teacher-blocks" hidden>'
        '<div class="block-head"><h3>Для викладача · що робимо сьогодні</h3>'
        '<span class="kind deep">для викладача</span>'
        '<span class="teacher-badge">лише викладач</span></div>'
        f'<div class="block-body">{THESIS[rel]}'
        "<p><b>Схема пари (tactic).</b> chrome / rail / stage / notebook. "
        "Карта 10 кроків і мікроперевірки — optional, required 80 хв не ріжемо. "
        "Дірка, якої немає в джерелі, лишається хуком growth, не вигаданою енциклопедією.</p>"
        "</div></article>"
    )


def pair_map(rel: str) -> str:
    facts = FACTS[rel]
    titles = TITLES[rel]
    items = []
    for i, (title, fact) in enumerate(zip(titles, facts), 1):
        items.append(
            f'<div class="card"><b>{i} · {esc(title)}</b><p>{md_code(fact)}</p>'
            f'<div class="viz diagram">{flow_svg(rel, i - 1)}</div></div>'
        )
    cards = "".join(items)
    return (
        '<article class="block extra-deep-dive" id="v14-pair-map" data-timing="optional" '
        'data-material-version-from="14.0"><div class="block-head">'
        "<h3>Карта пари · 10 кроків</h3>"
        '<div style="display:flex;gap:.35rem;flex-wrap:wrap;align-items:center">'
        '<span class="kind extra">додатково</span></div></div><div class="block-body">'
        '<p class="lead">Десять фактів на 80 хв. Кожен крок — одне речення і схема з підказкою на блоці. '
        "Далі лекція повторює той самий порядок, не інший текст.</p>"
        f'<div class="viz diagram">{map_svg(rel)}</div>'
        f'<div class="cards two">{cards}</div>'
        '<div class="callout tip"><b>Як читати</b><p>Йдіть по номерах. Наведіть на блок схеми — '
        "там той самий факт.</p></div>"
        '<div class="callout"><b>Часта пастка</b><p>Не зубріть абзац. Якщо факт не сказати за 10 секунд — '
        "верніться до номера на карті.</p></div>"
        "</div></article>"
    )


def pair_explain(rel: str) -> str:
    facts = FACTS[rel]
    titles = TITLES[rel]
    details = DETAILS[rel]
    short_bits = []
    detail_bits = []
    for i, (title, fact, detail) in enumerate(zip(titles, facts, details), 1):
        short_bits.append(
            f'<div class="card"><b>{i} · {esc(title)}</b><p>{md_code(fact)}</p></div>'
        )
        detail_bits.append(
            f"<h4>{i} · {esc(title)}</h4><p>{md_code(detail)}</p>"
            f'<div class="viz diagram">{flow_svg(rel, i - 1)}</div>'
        )
    return (
        '<article class="block extra-deep-dive" id="v14-explain" data-timing="optional" '
        'data-material-version-from="14.0"><div class="block-head">'
        "<h3>Пояснення · коротко / детально</h3>"
        '<div style="display:flex;gap:.35rem;flex-wrap:wrap;align-items:center">'
        '<span class="kind extra">додатково</span></div></div><div class="block-body">'
        + SWITCH
        + '<div class="lh-explain-short"><p class="lead">Коротко: ті самі 10 фактів і рахунок сенсу на схемі.</p>'
        f'<div class="cards two">{"".join(short_bits)}</div></div>'
        '<div class="lh-explain-detail"><p class="lead">Детально: навіщо крок саме сьогодні. '
        "Код рядок за рядком лишається в живих блоках лекції нижче.</p>"
        + "".join(detail_bits)
        + "</div>"
        '<div class="callout tip"><b>Коротко</b><p>Тогл діє лише на цей блок. Required 80 хв не змінено.</p></div>'
        "</div></article>"
    )


def gold_extras(rel: str) -> str:
    return (
        '<article class="block extra-deep-dive" id="v14-tactic-passport" data-timing="optional" '
        'data-material-version-from="14.0"><div class="block-head">'
        "<h3>Як іти по парі</h3>"
        '<div style="display:flex;gap:.35rem;flex-wrap:wrap;align-items:center">'
        '<span class="kind extra">додатково</span></div></div><div class="block-body">'
        '<p class="lead">Спочатку карта кроків, далі кожен факт у лекції, тоді практикум '
        "N / N.1 / N.2. Опційні блоки не входять у 80 хв.</p>"
        '<div class="cards two">'
        '<div class="card"><b>stage</b><p>Теорія, приклади, схеми, завдання. Це основна колонка пари.</p></div>'
        '<div class="card"><b>notebook</b><p>Комірки справа дзеркалять код зі stage. Запуск — тут, не в іншому вікні.</p></div>'
        '<div class="card"><b>rail</b><p>Зміст зліва. Якір веде на той самий <code class="mv">id</code> блоку.</p></div>'
        '<div class="card"><b>extra / викладач</b><p>Поглиблення і нотатки викладача поза 80 хв. Не замінюють практикум.</p></div>'
        "</div>"
        '<div class="callout tip"><b>Зверніть увагу</b><p>Нова версія матеріалів додає шар, а не ховає попередній повний текст.</p></div>'
        "</div></article>"
        '<article class="block teacher-deep-dive" id="v14-growth" data-timing="optional" '
        'data-material-version-from="14.0" data-project-feature="python-ai-modify-teacher-blocks" hidden>'
        '<div class="block-head"><h3>Для викладача · ріст пари</h3>'
        '<span class="kind deep">для викладача</span>'
        '<span class="teacher-badge">лише викладач</span></div><div class="block-body">'
        "<p><b>Freeze.</b> id core-слотів, required 80 хв, офіційний syllabus у банері, речення карти 10 кроків.</p>"
        "<p><b>Живі хуки.</b> Нова стаття / LMS / датасет graft в існуючий id того самого type. "
        "Overflow → extra кластера або deep-study, не пʼята зона і не урізання 80 хв.</p>"
        "<p><b>Не робити.</b> Не заліплювати дірку вигаданою енциклопедією «щоб виглядало готово». "
        "Не ставити until, який ховає повний шар.</p>"
        f"<p><b>Сьогодні вже товсто.</b> {esc(catalog_title(rel))} має карту 16–18. "
        "v14 лише підписує, куди ляже наступне джерело.</p>"
        "</div></article>"
    )


def check_article(item: tuple[str, int, str, str, str]) -> str:
    after, minutes, ask, code, key = item
    cid = f"v14-check-{minutes}"
    return (
        f'<article class="block" id="{cid}" data-timing="optional" data-minutes="3" '
        f'data-material-version-from="14.0"><div class="block-head">'
        f"<h3>Мікроперевірка · {minutes} хв пари</h3>"
        '<div style="display:flex;gap:.35rem;flex-wrap:wrap;align-items:center">'
        '<span class="kind task">2–3 хв</span></div></div>'
        '<div class="block-body"><p class="lead">'
        "Зупиніться на 2–3 хвилини. Відповідь — вголос, у чат або на папір."
        f"</p><div class=\"callout task\"><b>Перевірка</b><p>{md_code(ask)}</p></div>"
        f'<pre><code class="language-python">{esc(code)}\n# -&gt; відповідь своїми словами</code></pre>'
        '<div class="lh-teacher-note"><span class="lh-tn-label">Для викладача · v14</span>'
        f"<p><b>Приклад виконання.</b> {esc(key)}</p>"
        f'<pre><code class="language-python">{esc(code)}\n# -&gt; {esc(key)}</code></pre>'
        "<p><b>Час.</b> 2–3 хв. Не розгортайте в міні-лекцію.</p></div></div></article>"
    )


def insert_after_article(html: str, article_id: str, chunk: str) -> str:
    token = f'id="{article_id}"'
    start = html.find(token)
    if start < 0:
        print(f"  WARN: after #{article_id}")
        return html
    close = html.find("</article>", start)
    if close < 0:
        return html
    at = close + len("</article>")
    return html[:at] + chunk + html[at:]


def insert_toc_after(html: str, after_id: str, new_id: str, title: str, teacher: bool) -> str:
    if f'href="#{new_id}"' in html:
        return html
    cls = " data-teacher-toc hidden" if teacher else ""
    li = f'<li{cls}><a href="#{new_id}">{esc(title)}</a></li>'
    pattern = rf'(<li[^>]*>\s*<a href="#{re.escape(after_id)}"[^>]*>.*?</a>\s*</li>)'
    updated, n = re.subn(pattern, r"\1" + li, html, count=1, flags=re.S)
    if not n:
        print(f"  WARN: TOC after {after_id} -> {new_id}")
    return updated


def patch_css(html: str) -> str:
    if "svg text.term" in html and ".lh-depth-bar{" in html:
        if "article.lh-is-detail .lh-explain-detail" in html:
            return html
    needle = "</style>"
    idx = html.find(needle)
    if idx < 0:
        print("  WARN: no style")
        return html
    extra = CSS
    if "svg text.term" in html:
        extra = "\n".join(
            line
            for line in CSS.splitlines()
            if "diagram svg" not in line
        )
    if ".lh-depth-bar{" in html:
        extra = "\n".join(
            line
            for line in extra.splitlines()
            if "lh-depth" not in line and "lh-explain" not in line and "lh-is-detail" not in line
        )
    if not extra.strip():
        return html
    return html[:idx] + extra + "\n" + html[idx:]


def patch_js(html: str) -> str:
    if 'id="lh-v11-depth-js"' in html:
        return html
    marker = "<script>\n(function () {\n  const body = document.body;"
    if marker in html:
        return html.replace(marker, JS + marker, 1)
    return html.replace("</body>", JS + "\n</body>", 1)


def bump_versions() -> None:
    path = COURSE / "versions.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    ids = [item["id"] for item in data["versions"]]
    if "14.0" not in ids:
        data["versions"].append(
            {
                "id": "14.0",
                "label": "14.0",
                "note": (
                    "Пари 1–20: explaine_simple (10 кроків, тези викладача, Коротко/Детально, "
                    "мікроперевірки) + схема tactic/growth. Пари 16–18 без дубля карти. "
                    "Усі 50 в overrides, попередні шари не урізано."
                ),
            }
        )
    data["active"] = "14.0"
    data["student_active"] = "14.0"
    data["overrides"]["14.0"] = {
        "pairs": ALL_PAIRS,
        "note": "Усі 50 пар у v14. Новий шар — пари 1–20; решта успадковують v12.",
    }
    data["html"]["attrs"]["exact"] = (
        'data-material-version="1.0" | "2.0" | "3.0" | "4.0" | "5.0" | "6.0" | '
        '"7.0" | "8.0" | "9.0" | "10.0" | "11.0" | "12.0" | "14.0"'
    )
    data["html"]["attrs"]["from"] = (
        'data-material-version-from="2.0" | "4.0" | "5.0" | "6.0" | "7.0" | "8.0" | '
        '"9.0" | "10.0" | "11.0" | "12.0" | "14.0"'
    )
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("  versions.json -> 14.0")


def patch_teacher_md(rel: str, gold: bool) -> None:
    path = COURSE / rel / "teacher.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    if "## Версія 14.0" in text:
        return
    if gold:
        block = (
            "\n## Версія 14.0\n\n"
            "Additive шар tactic/growth (`from=14.0`). Карту 10 кроків не дублюємо — вона вже в v9–v11.\n\n"
            "- Студентам: `#v14-tactic-passport` — як іти по stage / notebook / rail.\n"
            "- Викладачу: `#v14-teacher-thesis` і `#v14-growth` — freeze id, хуки, не урізати 80 хв.\n"
            "- Required хвилини не змінено.\n"
        )
    else:
        block = (
            "\n## Версія 14.0\n\n"
            "Шар explaine_simple як у пар 16–18 (`from=14.0`). Required 80 хв не змінено.\n\n"
            "- Тези викладача: `#v14-teacher-thesis` (не слайд студентам).\n"
            "- Карта 10 кроків: `#v14-pair-map`. Коротко/Детально: `#v14-explain`.\n"
            "- Мікроперевірки `#v14-check-15/30/45/60` — optional, 2–3 хв, приклад виконання в нотатці.\n"
            "- Дірка без джерела лишається хуком growth, не вигаданим абзацом.\n"
        )
    path.write_text(text.rstrip() + "\n" + block, encoding="utf-8")
    print(f"  teacher.md  {rel}")


def patch_glossary(rel: str) -> None:
    path = COURSE / rel / "term-glossary.js"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    old = 'root.querySelectorAll(".term").forEach((el) => {'
    new = 'root.querySelectorAll(".term, svg [data-tip]").forEach((el) => {'
    if old in text:
        text = text.replace(old, new, 1)
    text = text.replace(
        'ev.target.closest(".term")',
        'ev.target.closest(".term, svg [data-tip]")',
        1,
    )
    path.write_text(text, encoding="utf-8")


def patch_pair(rel: str) -> None:
    path = COURSE / rel / "presentation.html"
    html = path.read_text(encoding="utf-8")
    gold = rel in GOLD_MAP
    if 'id="v14-teacher-thesis"' in html:
        print(f"  skip {rel} (already v14)")
        return
    html = patch_css(html)
    html = patch_js(html)
    start = AFTER_START[rel]
    html = insert_after_article(html, start, teacher_thesis(rel))
    html = insert_toc_after(html, start, "v14-teacher-thesis", "Для викладача · що робимо сьогодні", True)
    if gold:
        html = insert_after_article(html, "v14-teacher-thesis", gold_extras(rel))
        html = insert_toc_after(
            html, "v14-teacher-thesis", "v14-tactic-passport", "Як іти по парі", False
        )
        html = insert_toc_after(
            html, "v14-tactic-passport", "v14-growth", "Для викладача · ріст пари", True
        )
    else:
        chunk = pair_map(rel) + pair_explain(rel)
        html = insert_after_article(html, "v14-teacher-thesis", chunk)
        html = insert_toc_after(html, "v14-teacher-thesis", "v14-pair-map", "Карта пари · 10 кроків", False)
        html = insert_toc_after(html, "v14-pair-map", "v14-explain", "Пояснення · коротко / детально", False)
        for item in CHECKS[rel]:
            after = item[0]
            minutes = item[1]
            html = insert_after_article(html, after, check_article(item))
            html = insert_toc_after(
                html, after, f"v14-check-{minutes}", f"Мікроперевірка · {minutes} хв", False
            )
    path.write_text(html, encoding="utf-8")
    patch_teacher_md(rel, gold)
    patch_glossary(rel)
    print(f"  patched {rel} gold={gold}")


def catalog_paths() -> list[str]:
    data = json.loads((COURSE / "catalog.json").read_text(encoding="utf-8"))
    out = []
    for pair in data["pairs"]:
        if pair["global_index"] in TARGET:
            out.append(pair["path"].rstrip("/"))
    return out


def main() -> None:
    bump_versions()
    for rel in catalog_paths():
        patch_pair(rel)
    print("done")


if __name__ == "__main__":
    main()
