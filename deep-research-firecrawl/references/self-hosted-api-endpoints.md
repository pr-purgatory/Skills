# Self-Hosted Firecrawl API Endpoints

## Discovered Endpoint Patterns

Tested on the self-hosted instance at `http://localhost:3002`.

### Available Endpoints (Working)

| Endpoint | Method | Status | Notes |
|----------|--------|--------|-------|
| `/` | GET | 200 | Returns `{"message":"Firecrawl API"}` |
| `/v1/scrape` | POST | 200 | Works with `{"url": "...", "formats": ["markdown"]}` |
| `/v1/search` | POST | 200 | Returns search results with title, url, description |
| `/v1/crawl` | POST | 200 | Returns job ID for async crawling |
| `/v1/map` | POST | 200 | Returns list of links on a page |

### Unavailable Endpoints (Require AI Model Config)

| Endpoint | Status | Why Unavailable |
|----------|--------|-----------------|
| `/v1/agent` | 404 | Requires `OPENAI_API_KEY` or `OLLAMA_BASE_URL` in docker-compose |
| `/v1/extract` | 500 | Requires AI model for schema generation |

### Key Finding: No API Key Required for Local Use

Self-hosted instances do NOT require authentication headers. The API is open on localhost.

### Docker-Compose Requirements for Full Features

To enable `/agent` and `/extract`:
```yaml
environment:
  OPENAI_API_KEY: ${OPENAI_API_KEY}  # or
  OLLAMA_BASE_URL: ${OLLAMA_BASE_URL}  # for local LLM
```

### Search Endpoint Behavior

- Returns `{"success": true, "data": [...]}`
- Each result has: `title`, `url`, `description`
- `limit` parameter controls result count
- No `scrape_options` needed for basic search

### Scrape Endpoint Behavior

- Returns `{"success": true, "data": {"markdown": "...", "metadata": {...}}}`
- `onlyMainContent: true` reduces noise
- `formats: ["markdown"]` is the standard format
- Proxy is automatically used (shows `proxyUsed: "basic"` in metadata)
