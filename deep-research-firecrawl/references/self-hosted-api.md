# Firecrawl Self-Hosted API Reference

Session-discovered details about the self-hosted Firecrawl instance.

## Endpoint Availability

| Endpoint | Status | Notes |
|----------|--------|-------|
| `POST /v1/search` | ✅ Working | Web search with results |
| `POST /v1/scrape` | ✅ Working | Page extraction to markdown |
| `POST /v1/crawl` | ✅ Working | Multi-page crawling |
| `POST /v1/map` | ✅ Working | URL discovery |
| `POST /v1/extract` | ⚠️ Partial | Returns 500 without OpenAI key configured |
| `POST /v1/agent` | ❌ Not available | Cloud-only feature |

## Container Architecture

```
firecrawl-api-1          - Main API (port 3002)
firecrawl-redis-1        - Job queuing
firecrawl-playwright-service-1 - Browser automation
firecrawl-rabbitmq-1     - Message queue
firecrawl-nuq-postgres-1 - Database
```

## Enabling AI Features

Add to `.env`:
```
OPENAI_API_KEY=sk-...
MODEL_NAME=gpt-4o-mini
MODEL_EMBEDDING_NAME=text-embedding-3-small
```

Restart: `docker-compose down && docker-compose up -d`

## Dynamic Content Pitfall

Many modern sites (arrest records, mugshots, social media) load content via JavaScript after initial page load. The `scrape` endpoint captures initial HTML only.

**Mitigation:**
- Use `{"waitFor": 3000}` parameter to wait for JS execution
- Scrape specific record URLs found in search results rather than main pages
- For search-required sites, may need cloud `/agent` or manual navigation

## Tested Working Pattern

```python
import requests

FIRECRAWL_URL = "http://localhost:3002"

# Search
resp = requests.post(f"{FIRECRAWL_URL}/v1/search", json={
    "query": "search terms",
    "limit": 10
})

# Scrape with JS wait
resp = requests.post(f"{FIRECRAWL_URL}/v1/scrape", json={
    "url": "https://example.com",
    "formats": ["markdown"],
    "onlyMainContent": True,
    "waitFor": 3000
})
```
