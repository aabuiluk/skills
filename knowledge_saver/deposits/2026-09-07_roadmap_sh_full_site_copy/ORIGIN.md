# ORIGIN

- id: `2026-09-07_roadmap_sh_full_site_copy`
- source: https://roadmap.sh (Google SSO session)
- account: andrii.builuk8@gmail.com
- purpose: full independent local site copy under `data_site/` + left nav `/site`
- how_obtained: Playwright Google OAuth → JWT cookie; `python -m roadmap_sh.site_copy` HTML/API/assets download; auth re-fetch unlocked lesson `content`
- local_copy: `/Users/abuiluk/LessonPython/pet_projects/roadmap/data_site` (~551MB, 470 HTML, 70 unlocked lessons)
- note: `raw/` holds compact auth-sensitive JSON originals; bulk HTML/assets stay in `data_site/` (too large to duplicate)
