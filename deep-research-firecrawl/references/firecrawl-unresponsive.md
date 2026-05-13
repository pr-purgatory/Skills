# Firecrawl Unresponsive — Troubleshooting Guide

**Session**: May 11, 2025 — News research task
**Problem**: `/v1/scrape` endpoint hangs/times out on large or heavily-rendered pages (news aggregators especially). Two consecutive attempts timed out after ~60-100 seconds each.

## Symptoms

- `requests.post()` call to `/v1/scrape` blocks indefinitely
- No HTTP response, no error — just hangs until execution timeout kicks in
- Affects pages with heavy JS, lots of ads, or large DOM sizes
- News aggregator pages (AP, BBC, CNN homepages) are particularly problematic

## Quick Diagnosis

```bash
# Is Firecrawl even responding?
curl -s http://localhost:3002

# Test scrape with small timeout (15s) on a known-good page
curl -s http://localhost:3002/v1/scrape -H "Content-Type: application/json" -d '{
  "url": "https://example.com",
  "formats": ["markdown"],
  "timeout": 15000
}'
```

## Fix Attempts (Ordered)

1. **Restart containers** — often resolves Playwright service stuck states:
   ```bash
   cd /Volumes/System\ Downloads/appdata/firecrawl/
   docker compose restart
   ```

2. **Check service health**:
   ```bash
   docker compose ps
   # Should show api, playwright-service, redis, rabbitmq, nuq-postgres all "up"
   ```

3. **Restart just the Playwright service** (most common failure point):
   ```bash
   docker compose restart firecrawl-playwright-service-1
   ```

4. **Check logs** for clues:
   ```bash
   docker compose logs playwright-service | tail -50
   docker compose logs api | tail -50
   ```

5. **Full restart** (worst case):
   ```bash
   cd /Volumes/System\ Downloads/appdata/firecrawl/
   docker compose down
   docker compose up -d
   ```

## Fallback Strategy (When Firecrawl Is Unresponsive)

When Firecrawl's scrape endpoint is timing out, use these alternatives in order:

1. **Firecrawl Search Only** — `/v1/search` was still responding during this session, returning results with title/url/description. Can sometimes get enough info without scraping.

2. **Browser Subagent** — `delegate_task` with `browser` toolset can navigate sites directly, scroll, and read headlines. Slower but reliable.

3. **Manual Briefing** — If both fail, inform the user that Firecrawl is unresponsive and offer alternative sources (user may check themselves).

## Example: Firecrawl Unresponsive During Research

```python
# Step 1: Try search (fast, doesn't require full page load)
results = requests.post(f"{FIRECRAWL_URL}/v1/search", json={"query": "top news", "limit": 10})

# Step 2: If search works but scrape times out, don't retry scrape
# Instead, use the search results' descriptions as summary info

# Step 3: If ALL Firecrawl endpoints timeout, fall back to browser subagent
delegate_task(
    goal="Browse these news sites and extract today's top 10 headlines: apnews.com, bbc.com, reuters.com",
    toolsets=["browser"],
    context="Return headline, one-sentence summary, and URL for each story."
)
```

## Key Takeaway

Firecrawl search works even when scrape is unresponsive. If `/v1/scrape` hangs:
- Do NOT retry (it will likely hang again on the same page)
- Fall back to search-only or browser subagent
- Restart containers if the issue seems systemic (all pages failing, not just specific ones)