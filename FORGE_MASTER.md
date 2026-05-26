# FORGE MASTER

Coordination status log.

## State
- Goal: MVP task list for all TBD skills (including context-janitor, test-sentry).
- Status: Completed.
- Subagent Reviews:
  - selina: Done.
  - redteam: Done.

---

## Consolidated MVP Tasks

### doc-forge
- Impl markdown gen templates in `SKILL.md`.
- Prev loop → filter doc path in event watcher config.
- Mitigate SSRF (CWE-918) → restrict domains/IPs queried.
- Mitigate injection (CWE-1156) → sanitize inputs.
- Test: audit local host link → blocked.

### perf-profiler
- Restrict commands (hyperfine only) in `SKILL.md`.
- Prev CPU burn → run profile manually, not on event.
- Prev RCE (CWE-78) → run inside sandbox.
- Test: cmd injection payload → blocked.

### vibe-check
- Reference `STYLE.md` in `SKILL.md` to avoid drift.
- Save tokens → trigger check on PR hooks only.
- Prev hijack (CWE-1156) → XML wrap file contents.
- Test: comment payload `// ignore rules` → ignored.

### sandbox-forge
- Deny host root mount in `SKILL.md`.
- Prev container leak → autokill TTL / prune containers in JobManager (CWE-400).
- Prev escape (CWE-250) → drop privileges, disable network.
- Test: script breakout → blocked.

### revert-forge
- Prev lost code → force `git stash` before reset.
- Prev revert loop → max 1 revert attempt.
- Prev cmd injection (CWE-88) → escape git args.
- Test: branch name payload `; command` → rejected.

### dependency-janitor
- Prev hijack (CWE-353) → verify lockfile hashes.
- Prev startup delay → run scans async.
- Limit registries → block private pkg leaks.
- Test: update with hash mismatch → aborted.

### success-forge
- Impl token parser / `caveman-stats` in `SKILL.md`.
- Prev log bloat → prune log when size >50KB.
- Prev loop hijack (CWE-1156) → sanitize success logs.
- Test: log payload → sanitized.

### context-janitor
- Impl compaction & pruning in `SKILL.md`.
- Prev data loss → backup to app data dir before flush.
- Prev trigger hijack → sign events + check source config.
- Mitigate DoS (CWE-400) → prune log/history to fit token budget.
- Test: trigger event with large payload → compacts safely.

### test-sentry
- Impl test suite mapper & validation schema in `SKILL.md`.
- Prev loops → track commit/change hashes to block recursive audits.
- Mitigate bypass (CWE-358) → enforce test coverage & diff gates.
- Test: add untested file → flags missing tests & halts.

### supply-chain-stub (dependency confusion)
- Mitigate hijacking (CWE-829) → set `publish = false` or `"private": true` in skill configurations.
