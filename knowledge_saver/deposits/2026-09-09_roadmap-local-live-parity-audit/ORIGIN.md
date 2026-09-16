# roadmap.sh local vs live parity audit

- **id:** 2026-09-09_roadmap-local-live-parity-audit
- **saved:** 2026-09-09T18:15:00+00:00
- **source:** live https://roadmap.sh (auth session andrii.builuk8@gmail.com) + local http://127.0.0.1:3000/site
- **how_obtained:** investigate | playwright crawl | smoke_roadmap_sh
- **cost_note:** ~3–4 min smoke both targets + targeted deep probes; saved session `.tmp/roadmap_sh_storage.json`
- **why_keep:** baseline of broken parity before repair (HTML/asset hash skew, missing pages, auth gap)

## Method

1. `probe_session_headless()` → logged in as Andrii Builuk
2. `python -m scripts.smoke_roadmap_sh --target both --max-pages 60`
3. Targeted page probe of 27 routes + screenshots under `.tmp/parity_targeted/`
