# Self-Hosted Firecrawl Limitations & Workarounds

## What's NOT Available in Self-Hosted

| Feature | Cloud | Self-Hosted | Workaround |
|---------|-------|-------------|------------|
| `/agent` endpoint | ✅ | ❌ Not supported | Use `delegate_task` with browser toolset |
| `/interact` endpoint | ✅ | ❌ Not supported | Use `delegate_task` with browser toolset |
| `actions` (click, scroll, form submit) | ✅ | ❌ Requires Fire Engine | Use `delegate_task` with browser toolset |
| Fire Engine (anti-bot, IP rotation) | ✅ | ❌ Cloud-only | Configure proxy in `.env` |
| `/extract` with AI schema | ✅ | ⚠️ Requires OpenAI key | Set `OPENAI_API_KEY` in `.env` |

## JavaScript Rendering Status

### ✅ Working
- Playwright service renders JS pages
- `waitFor` parameter works (tested up to 15s)
- Basic JavaScript sites load correctly

### ❌ Not Working
- **Interactive elements**: Forms, buttons, AJAX-loaded content
- **Dynamic search results**: Results that load after form submission
- **Infinite scroll**: Content loaded on scroll

## The Hybrid Pattern (Browser + Firecrawl)

For sites requiring interaction:

```python
# Phase 1: Browser subagent navigates and extracts URLs
result = delegate_task(
    goal="Navigate [SITE], perform [ACTION], extract direct URLs",
    toolsets=["browser", "web"]
)

# Phase 2: Firecrawl scrapes the direct URLs
for url in result.urls:
    resp = requests.post("http://localhost:3002/v1/scrape", json={
        "url": url,
        "formats": ["markdown"],
        "waitFor": 5000
    })
    # Process content...
```

## Configuration for AI Features

Add to `.env` for `/extract` support:
```bash
OPENAI_API_KEY=sk-...
MODEL_NAME=gpt-4o-mini
MODEL_EMBEDDING_NAME=text-embedding-3-small
```

Restart required after `.env` changes:
```bash
cd /path/to/firecrawl && docker-compose down && docker-compose up -d
```

## Verified Test Results

- `quotes.toscrape.com/js/` - ✅ JS renders correctly
- `texas.arrests.org` search results - ❌ Requires form submission (use hybrid)
- `recentlybooked.com` - ❌ Requires form submission (use hybrid)
- Direct record pages (e.g., `/Arrests/{Name}_{record_id}/`) - ✅ Scrapes correctly
