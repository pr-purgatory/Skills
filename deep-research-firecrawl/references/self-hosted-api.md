# Self-Hosted Firecrawl API Reference

Tested against the self-hosted instance at `http://localhost:3002`. No auth header required on localhost.

## Endpoint Availability

| Endpoint | Status | Notes |
|----------|--------|-------|
| `GET /` | ✅ 200 | Returns `{"message":"Firecrawl API"}` — use as health check |
| `POST /v1/search` | ✅ 200 | `{"success": true, "data": [{title, url, description}]}`; `limit` sets count |
| `POST /v1/scrape` | ✅ 200 | `{"success": true, "data": {"markdown", "metadata"}}`; Playwright renders JS |
| `POST /v1/crawl` | ✅ 200 | Returns async job ID |
| `POST /v1/map` | ✅ 200 | Returns links on a site |
| `POST /v1/extract` | ⚠️ 500 | Needs an LLM configured (see below); error mentions `/responses` |
| `POST /v1/agent` | ❌ 404 | Cloud-only |
| `POST /v1/interact` | ❌ 404 | Cloud-only |
| `actions` param on scrape | ❌ 400 | `SCRAPE_ACTIONS_NOT_SUPPORTED` — needs Fire Engine (cloud-only) |
| Fire Engine (anti-bot, IP rotation) | ❌ | Cloud-only; configure a proxy in `.env` instead |

## Scrape Options That Matter

- `formats: ["markdown"]` — standard.
- `onlyMainContent: true` — strips nav/footer noise.
- `waitFor: 3000–5000` — lets JS render; tested working up to 15000 ms.
- Metadata shows `proxyUsed: "basic"`.

```python
import requests

FIRECRAWL_URL = "http://localhost:3002"

resp = requests.post(f"{FIRECRAWL_URL}/v1/search", json={"query": "search terms", "limit": 10}, timeout=30)

resp = requests.post(f"{FIRECRAWL_URL}/v1/scrape", json={
    "url": "https://quotes.toscrape.com/js/",
    "formats": ["markdown"],
    "onlyMainContent": True,
    "waitFor": 5000,
}, timeout=30)
```

## What Rendering Can and Can't Do

Works: static JS pages, content that appears after load (`waitFor`).

Doesn't work: form submission, button clicks, AJAX loaded after interaction, infinite scroll, search results that appear only after a form post.

### Hybrid Pattern (Browser + Firecrawl)

1. Hand navigation to whatever browser-capable tool or subagent your agent has: "Navigate `{site}`, perform `{action}`, return only direct URLs of the result pages."
2. Scrape those direct URLs with `/v1/scrape`.
3. Synthesize.

```python
urls = run_browser_subagent(
    task="Navigate {site}, perform {action}, return direct result-page URLs only"
)  # placeholder for your agent's browser tool
for url in urls:
    requests.post(f"{FIRECRAWL_URL}/v1/scrape", json={"url": url, "formats": ["markdown"], "waitFor": 5000}, timeout=30)
```

Verified: `quotes.toscrape.com/js/` renders; form-driven record search sites need the hybrid pattern; their direct record pages scrape fine.

## Deployment

Docker Compose services: `api` (port 3002), `playwright-service`, `redis`, `rabbitmq`, `nuq-postgres`.

Required `.env`:
```bash
PORT=3002
HOST=0.0.0.0
USE_DB_AUTHENTICATION=false
```

Optional, to enable `/v1/extract` (and `/v1/agent` where supported) — use an OpenAI key or a local model:
```bash
OPENAI_API_KEY=...            # or
OLLAMA_BASE_URL=http://host:11434
MODEL_NAME=gpt-4o-mini
MODEL_EMBEDDING_NAME=text-embedding-3-small
```

Restart after `.env` changes, from the Firecrawl compose directory:
```bash
docker compose down && docker compose up -d
```
