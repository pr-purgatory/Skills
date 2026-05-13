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
009|.|[MVP] Map EDM failures to auto-repair skills|review
010|x|[MVP] Adopt AGENT.md layout for all skills|review
011|x|[MVP] Unified discovery via AGENTS.md|review
012|x|[MVP] Mask secrets and PII in outputs|review
013|x|[MVP] LFM atomic writes (locking/tmp-rename)|review
014|x|[MVP] Selina JSON output support (--json)|review
015|x|[MVP] Map RedTeam to SARIF format|review
016|x|[MVP] Enforce Zod schema on subagent outputs|review
017|x|[MVP] Skip low-signal targets (boredom filter)|review
018|x|[MVP] PoC templates for security findings|review
019|.|[GAP] Define Agent-to-Agent IPC protocol|review
020|.|[GAP] UI Forge screenshot-audit subagent|review
021|.|[GAP] Cross-project dependency-janitor|review
022|.|[GAP] Log/reuse wins via Success Forge|review
023|.|[GAP] AGENT.md for perf-profiler/context-janitor|review
024|.|[GAP] Create dedicated Doc Forge agent|review
025|.|[GAP] Test Sentry subagent for code changes|review
026|.|[GAP] Persona-based style auditor (Vibe Check)|review
027|.|[GAP] RedTeam binary blob auditing|review
028|.|[GAP] Sandbox Forge for isolated test runs|review
029|.|[GAP] REPL for Rust Forge debugger|review
030|.|[GAP] UI design-to-code comparison subagent|review
031|.|[GAP] Weight-based tie-break for EDM rules|review
032|.|[GAP] Revert Forge for failed implementations|review
033|.|[GAP] Subagent for caveman-stats visualization|review
034|.|[LOGIC] Hard depth limit (5) for EDM triggers|review
035|.|[LOGIC] Canonicalize strings for LFM hashing|review
036|.|[LOGIC] Map CVSS severity to SARIF levels|review
037|.|[LOGIC] Auto-detect OS/Framework for UI|review
038|.|[LOGIC] Raw text fallback for Zod failures|review
039|.|[LOGIC] Global PII regex standard|review
040|.|[LOGIC] Minimal Cargo.toml context for Rust subagents|review
041|.|[LOGIC] Deterministic error code lookup table|review
042|.|[LOGIC] --force-audit flag for RedTeam|review
043|.|[LOGIC] 50k char limit enforcement in Selina|review
044|.|[LOGIC] Priority tie-break via creation date|review
045|.|[LOGIC] LFM trim check on every 10th write|review
046|.|[LOGIC] Integrate Axe/a11y tools into UI Forge|review
047|.|[LOGIC] Define 'Cost of Attack' scoring scale|review
048|.|[LOGIC] Tone Drift Guard (Character audit turns)|review

## §B BUGS
id|date|cause|fix
