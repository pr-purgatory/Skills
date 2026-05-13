# Self-Hosted Firecrawl API Behavior (Live Testing Results)

Documented from actual testing with the self-hosted instance at `http://localhost:3002`

## Tested Endpoints

### ✅ Working Endpoints

| Endpoint | Status | Notes |
|----------|--------|-------|
| `GET /` | 200 | Returns `{"message":"Firecrawl API"}` |
| `POST /v1/search` | 200 | Web search with Google |
| `POST /v1/scrape` | 200 | Page scraping with Playwright JS rendering |
| `POST /v1/crawl` | 200 | Multi-page crawling |
| `POST /v1/map` | 200 | URL discovery |

### ❌ Non-Working Endpoints

| Endpoint | Status | Error |
|----------|--------|-------|
| `POST /v1/agent` | 404 | Not available in self-hosted |
| `POST /v1/interact` | 404 | Not available in self-hosted |
| `POST /v1/extract` | 500 | Requires OpenAI key (returns "Failed to parse URL from /responses") |

### ⚠️ Partially Working

| Feature | Status | Notes |
|---------|--------|-------|
| `actions` in scrape | 400 | Returns `SCRAPE_ACTIONS_NOT_SUPPORTED` - requires Fire Engine |
| `interact` parameter | 400 | Returns `BAD_REQUEST` - unrecognized key |

## JavaScript Rendering

**Confirmed working:**
- Playwright service renders JavaScript automatically
- `waitFor` parameter works (tested up to 15000ms)
- Dynamic content loads correctly

**Example:**
```python
requests.post("http://localhost:3002/v1/scrape", json={
    "url": "https://quotes.toscrape.com/js/",
    "formats": ["markdown"],
    "waitFor": 5000
})
# Returns rendered content with quotes loaded via JavaScript
```

## What Doesn't Work (And Why)

### Form Submission / Interaction in Firecrawl
Sites that require:
- Form submission (POST forms)
- Button clicks to load content
- Scrolling to load more results
- Any user interaction

**Reason:** Self-hosted Firecrawl lacks the `/agent` and `/interact` endpoints, and the `actions` parameter requires Fire Engine (cloud-only).

**Solution:** Use `delegate_task` with `browser` toolset to handle interaction. The subagent CAN do all of these things:
- Fill and submit forms
- Click buttons
- Scroll pages
- Navigate between pages
- Extract URLs from dynamic content

Then pass discovered URLs to Firecrawl for content extraction.

## Working Configuration

### docker-compose.yaml Services
- `api` - Main API server (port 3002)
- `playwright-service` - Browser automation for JS rendering
- `redis` - Job queuing
- `rabbitmq` - Message broker
- `nuq-postgres` - Database

### Required .env
```bash
PORT=3002
HOST=0.0.0.0
USE_DB_AUTHENTICATION=false
```

### Optional .env (for AI features)
```bash
OPENAI_API_KEY=sk-...
MODEL_NAME=gpt-4o-mini
MODEL_EMBEDDING_NAME=text-embedding-3-small
```

## Hybrid Pattern for Interactive Sites

Since self-hosted can't interact with forms/buttons, use this pattern:

```python
# Step 1: Browser subagent handles interaction
delegate_task(
    goal="Navigate to texas.arrests.org, search for '{name}', get record URL",
    toolsets=["browser", "web"]
)
# Returns: https://texas.arrests.org/Arrests/{Name}_{record_id}/

# Step 2: Firecrawl scrapes the static record page
requests.post("http://localhost:3002/v1/scrape", json={
    "url": "https://texas.arrests.org/Arrests/{Name}_{record_id}/",
    "formats": ["markdown"],
    "waitFor": 3000
})
```

This pattern successfully extracted:
- Mugshot URLs
- Arrest date
- Charges
- Personal details

## Key Takeaway

Self-hosted Firecrawl is excellent for **scraping** (especially JS-rendered pages) but cannot **interact** with pages. Pair it with Hermes' `delegate_task` + `browser` toolset for full research capabilities.
