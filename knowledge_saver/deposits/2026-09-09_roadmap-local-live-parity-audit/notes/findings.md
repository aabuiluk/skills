# Findings (2026-09-09) — continued parity

## Pages
- **960/960** OK (final_health.json)

## Live account sync
- Script: `python -m scripts.sync_live_account`
- Local user: **andrii / andrii** (also mirrored onto admin)
- Synced: profile name/email/avatar, billing, AI limits, 13 favorites, 20 roadmap progress buckets, lesson packs, projects, persona/resume

## Actions crawl (35 key surfaces)
- Pages: 35/35 OK
- Clicks: 66, errors: 0
- Mutations seen: favorites, resource progress, pulse/visit
- Forced checks: project start/stop, lesson-pack progress, newsletter subscribe, pack “Already Know that”, AI chat persona/resume **200**
- API smoke: **16/16** ok

## How to use
1. `python -m scripts.sync_live_account` (needs Google session)
2. Open http://127.0.0.1:3000/login → `andrii` / `andrii`
3. Browse `/site/...` as Andrii Builuk with live bookmarks/progress
