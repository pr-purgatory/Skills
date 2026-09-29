# LinkedIn Scraping Failures — Session Notes

## Problem
LinkedIn profiles are aggressively protected against automated access. Multiple approaches fail:

| Approach | Result |
|----------|--------|
| Firecrawl `scrape` with `proxy: stealth` | `document_antibot` — blocked after retries |
| Firecrawl `scrape` with `proxy: enhanced` | Same anti-bot block |
| Direct `curl` with browser UA | Returns 404 error page (not profile) |
| `delegate_task` with browser toolset | Firecrawl MCP server temporarily unreachable; even when up, LinkedIn requires login |

## What Works Instead

1. **Search for the person's name + known affiliations** — often reveals the *correct* LinkedIn URL via search result snippets or other sites that embed it.
2. **Check ExpertFile, university faculty pages, corporate bios** — these often display the LinkedIn URL explicitly.
3. **Use `linkedin.com/pub/dir/firstname/lastname`** — directory pages sometimes list profiles (but also block scrapers).
4. **Ask the user for the saved page content** — if they have access, copy-paste is the only reliable path.

## Case Study: Middle-Initial Mismatch
- Provided URL: `https://www.linkedin.com/in/{firstname-x-lastname}/` → **404**
- Discovered URL for the likely intended person (a university faculty member): `https://www.linkedin.com/in/{firstname-y-lastname-id}/` — found via ExpertFile profile and search corroboration.
- Key clue: The middle initial in the provided URL may have been a typo or a different person entirely; the likely intended person uses a different middle initial.

## Recommendation
When a user provides a LinkedIn URL that fails:
1. Report the failure immediately.
2. Search for the person's name + job title/affiliation to find alternative sources.
3. Check if a *different* LinkedIn URL exists for the likely intended person.
4. Ask the user to copy-paste the profile text or save the page as Markdown.
