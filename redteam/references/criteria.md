# RedTeam Audit Lenses

Apply every lens unless the audit is targeted; for targeted audits apply all lenses to the target and its direct dependents/callers. Each finding must cite a file/config location, map to a CWE where one exists, and carry a fix (SKILL.md Workflow step 5–6).

Default lens set = 1–16. Skip a lens only when it cannot apply (e.g., no network surface) and say so in the report.

---

## 1. Premortem
It is 12 months from now and this system failed badly. Why?
- Single points of failure: one DB, one worker, one key, one maintainer.
- Assumptions that silently expire: certs, tokens, API versions, free tiers, date math.
- Growth limits: unbounded tables, queues, logs, caches.

## 2. Authentication & Session
- Every entry point (HTTP route, RPC, CLI, queue consumer, webhook) → identity check before handler. (CWE-306)
- Session/token: expiry, rotation, revocation, storage (⊥ localStorage for long-lived tokens), signature algorithm pinned (⊥ `alg: none`). (CWE-287, CWE-347)
- Password/secret comparison constant-time. (CWE-208)
- Webhooks: signature verified with raw body, replay window enforced.

## 3. Authorization
- Object-level checks on every read/write by ID (IDOR). (CWE-639)
- Role/tenant checks server-side, not UI-only. (CWE-602)
- Privilege escalation paths: self-assignable roles, mass assignment of `role`/`is_admin`. (CWE-915)
- Admin/debug endpoints reachable in production.

## 4. Input Handling & Injection
- SQL/NoSQL built by string concat. (CWE-89, CWE-943)
- Shell: `sh -c`, `exec`, `system`, `subprocess(shell=True)` with interpolated input. (CWE-78, CWE-88)
- Path: user input joined to filesystem paths without canonicalize + prefix check; symlink follow on write. (CWE-22, CWE-59)
- Templates/HTML: unescaped output, `dangerouslySetInnerHTML`, `v-html`, markdown → HTML without sanitizer. (CWE-79)
- Deserialization of untrusted data (pickle, YAML `load`, Java/PHP native). (CWE-502)
- SSRF: server fetches user-supplied URLs without allowlist or private-IP block (incl. redirects, DNS rebinding). (CWE-918)
- Regex on untrusted input with catastrophic backtracking. (CWE-1333)

## 5. LLM / Agent Surface
- Untrusted content (files, web pages, tool output, issues, emails) reaching a model prompt that can call tools. (CWE-1427)
- Tool permissions: can the agent write files, run shell, send messages, or spend money without human confirmation?
- Model output parsed as code/commands/SQL without validation.
- Secrets or other users' data in prompts, logs, or memory files.

## 6. Secrets & Configuration
- Hardcoded keys/tokens/passwords in source, tests, fixtures, CI YAML, Dockerfiles, git history. (CWE-798)
- `.env.example` vs code: every env var read in code documented; no real values in example. Drift = finding.
- Config loaded from untrusted locations (CWD, repo checkout) that can change behavior. (CWE-426)
- Debug flags, verbose errors, permissive CORS (`*` with credentials) defaulting on. (CWE-942)

## 7. Insecure Defaults & Transport
- Missing security headers on HTTP responses: CSP, HSTS, `X-Content-Type-Options`, frame protections, cookie `Secure`/`HttpOnly`/`SameSite`. (CWE-693, CWE-1004)
- TLS verification disabled (`verify=False`, `rejectUnauthorized: false`, `InsecureSkipVerify`). (CWE-295)
- Default credentials, open admin panels, services bound to `0.0.0.0` unnecessarily.

## 8. Cryptography
- Homegrown crypto, ECB mode, static IVs/nonces, MD5/SHA1 for integrity or passwords. (CWE-327, CWE-329)
- Password hashing ≠ bcrypt/scrypt/argon2 with adequate cost. (CWE-916)
- `Math.random` / non-CSPRNG for tokens, IDs, resets. (CWE-338)

## 9. Privacy / GDPR
- PII inventory: what is collected, where stored, who can read it, how long kept.
- PII in logs, analytics, error trackers, URLs/query strings. (CWE-532, CWE-598)
- Deletion/export path exists and actually removes data from backups/replicas within stated window.
- Data sent to third parties (SDKs, LLM APIs) without disclosure.

## 10. Supply Chain
- Run the ecosystem audit: `npm audit`, `pnpm audit`, `cargo audit`, `pip-audit`, `govulncheck`, `bundle audit`.
- Lockfile present and enforced in CI (`--frozen-lockfile`, `--locked`, `npm ci`). (CWE-353)
- Dependency confusion: private package names resolvable on public registries; scoped registry config. (CWE-829)
- Install scripts (`postinstall`, `build.rs`) from unvetted packages; unpinned GitHub Actions (`@main` vs SHA). (CWE-494)
- Transitive risk: abandoned or single-maintainer deps on critical paths.

## 11. Concurrency & State
- Check-then-act races on balances, inventory, quotas, unique constraints. (CWE-367)
- Missing idempotency keys on payment/side-effecting endpoints; retries double-apply.
- Shared mutable state across requests/tenants; cache keys missing tenant/user.

## 12. Architecture Stress
Define thresholds explicitly (default: 10× current peak QPS, 100 concurrent writers on one row/key, dependency latency 5s, dependency down).
- What saturates first: DB connections, thread pool, memory, rate-limited upstream?
- Timeouts and circuit breakers on every outbound call; retry storms.
- Unbounded fan-out, pagination absent, N+1 queries.
- Stress analysis is reasoning + existing benchmarks only; ⊥ live load against shared/prod systems (SKILL Boundaries).

## 13. Abuse Scenarios
For each feature, how would a spammer, scraper, fraudster, or angry ex-user weaponize it? Give **Cost of Attack** (Low: mins / Moderate: hours / High: days / Extreme: weeks+).
- Rate limits on signup, login, password reset, invite, message send, file upload, expensive search. (CWE-307, CWE-770)
- Enumeration via differing responses (user exists / doesn't). (CWE-204)
- Free-tier or trial abuse; outbound email/SMS as spam relay; open redirects. (CWE-601)
- Uploads: type/size limits, stored where, served from which origin. (CWE-434)

## 14. Error Handling & Failure Modes
- Fail-open on auth/permission/validation errors. (CWE-636)
- Stack traces, SQL, internal hostnames in client-facing errors. (CWE-209)
- Swallowed exceptions hiding data loss; partial writes without rollback.

## 15. Binary & Blob Assets
- `strings` + entropy scan on committed binaries, archives, images, notebooks, `.pyc`, `.jar`.
- High-entropy strings → possible embedded keys; unexpected executables in asset dirs.
- Large vendored blobs with unknown provenance.

## 16. Orphaned & Dead Code
- Unused routes/handlers still registered and reachable, especially with weaker or legacy auth.
- Feature flags permanently on/off with dead branches containing old vulnerable logic.
- Deprecated API versions still served.

---

## Report Hygiene (applies to every lens)
- ⊥ paste source snippets; cite `path:line` instead.
- ⊥ include server version strings, internal IPs, or secret values; mask as `sk-...xyz`.
- Log suspected-but-unconfirmed issues under **False Negatives / Needs Verification** rather than dropping them.
