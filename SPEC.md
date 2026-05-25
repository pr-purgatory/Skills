# SPEC
## §G GOAL
Central repo for skills by pr-purgatory team.

## §C CONSTRAINTS
- ∀ skill ! separate dir.
- ∀ skill ! `SKILL.md`.
- No secrets in repo.
- Use `cavekit` for SDD.

## §I INTERFACES
- `SKILL.md`: Skill definition & instructions.
- `README.md`: Human docs.

## §V INVARIANTS
V1: ∀ skill → `SKILL.md` exists.
V2: ∀ skill → `LICENSE` exists.

## §T TASKS
id|status|task|cites
001|x|Init `SPEC.md`|this
002|x|Audit existing skills for V1/V2|
003|x|Standardize skill layout|
004|x|[MVP] Ensure failure modes have specific fixes|review
005|x|[MVP] Implement 1-10 severity scale for RedTeam|review
006|x|[MVP] Implement Einstein Mode warnings in LFM|review
007|x|[MVP] Split Rust Forge sub-prompts (debug/scaffold/test)|review
008|x|[MVP] Isolate platform-native logic in UI Forge|review
010|x|[MVP] Adopt AGENT.md layout for all skills|review
011|x|[MVP] Unified discovery via AGENTS.md|review
012|x|[MVP] Mask secrets and PII in outputs|review
013|x|[MVP] LFM atomic writes (locking/tmp-rename)|review
014|x|[MVP] Selina JSON output support (--json)|review
015|x|[MVP] Map RedTeam to SARIF format|review
016|x|[MVP] Enforce Zod schema on subagent outputs|review
017|x|[MVP] Skip low-signal targets (boredom filter)|review
018|x|[MVP] PoC templates for security findings|review
020|x|[GAP] UI Forge screenshot-audit subagent|review
021|x|[GAP] Cross-project dependency-janitor|review
022|x|[GAP] Log/reuse wins via Success Forge|review
023|x|[GAP] AGENT.md for perf-profiler/context-janitor|review
024|x|[GAP] Create dedicated Doc Forge agent|review
025|x|[GAP] Test Sentry subagent for code changes|review
026|x|[GAP] Persona-based style auditor (Vibe Check)|review
027|x|[GAP] RedTeam binary blob auditing|review
028|x|[GAP] Sandbox Forge for isolated test runs|review
029|x|[GAP] REPL for Rust Forge debugger|review
030|x|[GAP] UI design-to-code comparison subagent|review
032|x|[GAP] Revert Forge for failed implementations|review
033|x|[GAP] Subagent for caveman-stats visualization|review
035|x|[LOGIC] Canonicalize strings for LFM hashing|review
036|x|[LOGIC] Map CVSS severity to SARIF levels|review
037|x|[LOGIC] Auto-detect OS/Framework for UI|review
038|x|[LOGIC] Raw text fallback for Zod failures|review
039|x|[LOGIC] Global PII regex standard|review
040|x|[LOGIC] Minimal Cargo.toml context for Rust subagents|review
041|x|[LOGIC] Deterministic error code lookup table|review
042|x|[LOGIC] --force-audit flag for RedTeam|review
043|x|[LOGIC] 50k char limit enforcement in Selina|review
045|x|[LOGIC] LFM trim check on every 10th write|review
046|x|[LOGIC] Integrate Axe/a11y tools into UI Forge|review
047|x|[LOGIC] Define 'Cost of Attack' scoring scale|review
048|x|Tone Drift Guard (Character audit turns)|review

## §B BUGS
id|date|cause|fix
