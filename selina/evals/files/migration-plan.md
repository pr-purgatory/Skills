# Database Migration Plan: Monolith to Microservices

## Overview
We're splitting our 5-year-old monolith into microservices. Target: done by end of Q2.
Team size: 4 engineers, 1 PM.

## Phases

### Phase 1: Strangler Fig (Weeks 1-4)
- Route new traffic to new services via nginx
- Old monolith handles fallback
- Start with User Service (least dependencies)

### Phase 2: Data Migration (Weeks 5-8)
- Dual-write to both old DB and new per-service DBs
- Run in parallel, compare results
- Cut over when confident

### Phase 3: Deprecation (Weeks 9-12)
- Remove old monolith endpoints one by one
- Monitor error rates
- Done when traffic = 0 on old paths

## Tech Stack
- New services: Node.js + Postgres
- Old monolith: Rails + MySQL
- Message queue: Redis pub/sub (using existing Redis instance)
- Service discovery: hardcoded URLs in env vars for now, "we'll do proper service mesh later"

## Risks Noted
- Some tables shared across domains (we'll figure it out)
- No rollback plan documented yet
- Team has never done this before
