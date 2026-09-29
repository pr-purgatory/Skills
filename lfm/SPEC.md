# SPEC
## §G GOAL
Persistent failure memory across agent sessions.

## §C CONSTRAINTS
- Append-only markdown log.
- Disk-based persistence (no context-only drift).
- Cross-agent compatible (Standard Markdown).
- Zero dependencies for core logic.

## §I INTERFACES
- `LFM_LOG`: `~/.<agent>/lfm/lfm-log.md`
- `/lfm jr|std|einstein`: Mode switch.
- `/lfm log`: Manual trigger.

## §V INVARIANTS
V1: ∀ deterministic failure → log entry created.
V2: ∀ significant action → consult `LFM_LOG` first.
V3: ⊥ sensitive data (keys/PII) in log.

## §T TASKS
id|status|task|cites
001|x|Init `SKILL.md`|this
002|x|Implement credential scrubbing (Shell/PII)|review
003|x|Implement file locking & atomic writes|review
004|x|Add `einstein` mode pivot confirmation|review
005|x|Implement 90-day archival & 10MB limit|review
006|x|Use Frontmatter for structured metadata|review
007|x|Implement regex error pattern matching|review
008|x|Add deduplication via approach hashing|review
009|x|Implement sliding window for log reads|review
010|x|Add `revert` command to purge entries|review
011|x|Capture OS/Arch/Tool params in context|review
012|x|Implement chmod 600 & path sanitization|review
013|x|Add optional AES encryption & HMAC signing|review
014|x|Add `search-archive` command|review
015|x|Implement fallback agent name resolution|review

## §R REVIEW
😼 LFM — You're building a memory of every mistake you've ever made, but you've left the diary unlocked on the park bench.

### MVPS (Most Valuable Points)
1. **Einstein Mode** — *Fix: Maintain strict user confirmation for all pivots.*
2. **Deterministic Classification** — *Fix: Use regex for error pattern matching to improve recall.*
3. **Cross-Agent Reads** — *Fix: Standardize JSON schema for easier multi-agent ingestion.*
4. **Append-only log** — *Fix: Implement file locking during writes to prevent corruption.*
5. **Deduplication check** — *Fix: Hash 'approach' strings for faster O(1) lookup.*
6. **Persistence via disk** — *Fix: Use atomic rename for writes to avoid zero-byte files.*
7. **Agent Name Resolution** — *Fix: Fallback to `$(whoami)` if environment ID is missing.*
8. **Automated Trimming** — *Fix: Move archive logic to a background worker to avoid blocking.*
9. **Negation Trigger** — *Fix: Use a semantic distance check for "no/wrong/stop" variants.*
10. **Plain Markdown Format** — *Fix: Use Frontmatter for structured metadata within the MD.*

### GAPS (Gaps)
1. **Context Window Saturation** — *Fix: Implement a sliding window for consultation reads.*
2. **Ambiguous Failures** — *Fix: Force choice between deterministic/transient on manual log.*
3. **Log Poisoning** — *Fix: Add a 'revert' command to purge bad LFM entries.*
4. **Tool-Specific Nuance** — *Fix: Capture tool parameters, not just the tool name.*
5. **Performance Lag** — *Fix: Cache the last 50 entries in memory for instant consult.*
6. **Sync Conflict** — *Fix: Add a monotonic counter to entries for conflict resolution.*
7. **Search Inefficiency** — *Fix: Pre-index entries by 'approach' type.*
8. **Missing 'Success' Log** — *Fix: Optionally log what actually worked for positive reinforcement.*
9. **Environment Sensitivity** — *Fix: Capture OS/Arch in context to avoid cross-platform bad advice.*
10. **Archive Visibility** — *Fix: Add a 'search-archive' command for manual recovery.*

### SECURITY CONCERNS
1. **Credential Leaking** — *Fix: Scrub all shell commands for API keys before logging.*
2. **PII in Context** — *Fix: Redact anything matching email/phone patterns in 'context' field.*
3. **World-Readable Logs** — *Fix: chmod 600 the log directory on creation.*
4. **Path Traversal** — *Fix: Sanitize AGENT_NAME to prevent `../../` in log path.*
5. **Prompt Injection** — *Fix: Treat log content as untrusted data during consultation.*
6. **Local Privilege Escalation** — *Fix: Never execute commands directly from the log outcome.*
7. **Dependency Hijack** — *Fix: Lock down the `lfm` directory permissions.*
8. **Unencrypted Storage** — *Fix: Offer optional AES encryption for the log file.*
9. **Log Forgery** — *Fix: HMAC-sign entries to prevent unauthorized manual edits.*
10. **Resource Exhaustion** — *Fix: Set a hard 10MB limit on the active log file.*

Worst case: An attacker poisons your mistake log to make you "learn" to disable security checks. 🐱
