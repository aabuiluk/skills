# Findings

Phone video is Android Chrome on **production** `*.pythonanywhere.com`, course **`python_ai_step` pair 12** (immersive FileViewer, notebook on, stacked `ЗАПУСК` cells).

Checked live 2026-09-08:

- `presentation.html?download=1` — no injected `lh-mobile-code-scroll-js`
- API-served HTML — old chrome, no uncap / passthrough
- `pair-notebook.js` — still `Math.min(480, 45vh)` cap, no `bindMobileCodeScroll`

Local journal / `python_ai_materials` copies do not update that URL. Deploy `presentation_chrome.py`, rebuilt `backend/static`, and `python_ai_step/**/pair-notebook.js` with `--force`, then hard-refresh the phone.
