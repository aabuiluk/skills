# roadmap.sh offline business-logic contracts

- **id:** 2026-09-09_roadmap-sh-offline-business
- **saved:** 2026-09-09T01:12:00+03:00
- **source:** live https://roadmap.sh under auth + local SPA JS under data_site/assets
- **how_obtained:** investigate | high-token
- **cost_note:** Playwright live/local smoke; reverse-engineered mutation shapes from SPA chunks + live probes
- **why_keep:** exact method/body/response shapes needed to keep offline /site interactive without roadmap.sh

## Key live contracts

| Endpoint | Method | Body | Response |
|----------|--------|------|----------|
| /api/v1-mark-favorite | PATCH | {resourceType, resourceId} | {status:ok} |
| /api/v1-update-weekly-subscriptions | PATCH | {weeklySubscriptions:[…]} | {status:ok} |
| /api/v1-update-resource-progress | POST | {topicId, resourceType, resourceId, progress} | {done,learning,skipped,personalized} |
| /api/v1-clear-resource-progress | POST | {resourceType, resourceId} | {status:ok} |
| /api/v1-save-personalization/:id | POST | {personalized:{information,topicIds}} | {success:true} |
| /api/v1-clear-roadmap-personalization/:id | POST | {} | {success:true} |
| /api/v1-start-project/:slug | POST | {} | {startedAt} |
| /api/v1-stop-project/:slug | POST | {} | {status:ok} |
| /api/v1-submit-project/:slug | POST | {solutionUrl, languages} | status object |
| /api/v1-lesson-pack-progress/:slug | POST | {lessonId} or {projectId} | full progress |
| /api/v1-update-newsletter-subscription/:id | POST | {subscribed:bool} | {isSubscribed, weeklySubscriptions} |

## Local pitfall

`ssr_has_usable_content` was stripping SPA from /projects etc., leaving `.striped-loader` forever. Keep SPA for interactive routes.
