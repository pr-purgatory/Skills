# Skills Forge

Collection of specialized agent skills and subagents for the autonomous engineer.

**Status:** 🟢 100% MVP, Logic, and GAP tasks complete. Expansion phase 2 + Gap Closure active.

## 🆕 Recent Updates
- **Meta-Orchestration:** Added `forge-master` to coordinate complex multi-agent workflows.
- **Root Workspace:** Centralized `Cargo.toml` and `AGENTS.md` registry.
- **20+ Skills Scaffolded:** Including new Gap-Closers like `smoke-tester`, `schema-audit`, `noise-filter`, and `bridge-builder`.
- **Skill Hardening:** Canonicalized LFM hashing, CVSS-to-SARIF mapping for RedTeam, and Tone Drift Guard for Selina.

## 🚀 Batch Install

Install all skills for your preferred tool:

### Antigravity
1. **Install Skills**:
```bash
find . -maxdepth 2 -name "SKILL.md" -exec dirname {} \; | while read dir; do
    cp -R "$dir" ~/.gemini/antigravity/skills/
done
```


### Gemini CLI
```bash
find . -maxdepth 2 -name "SKILL.md" -exec dirname {} \; | xargs -n 1 gemini skill install --consent
```

### Claude Code
```bash
find . -maxdepth 2 -name "SKILL.md" -exec dirname {} \; | while read dir; do                                           
    claude skill install "$dir"                                                                                          
done   
```

### Aider / Continue / Cursor
Add the absolute path of the desired `SKILL.md` to your configuration file or project-specific `.claudecode.md` / `ROO_CLINE_CUSTOM_MODES.md`.


---

## 🤖 Subagents Registry (Alphabetical)

| Agent Name | Description | Rules File |
|------------|-------------|------------|
| `babel-smith` | i18n and localization specialist | `babel-smith/AGENT.md` |
| `bridge-builder` | Legacy compatibility specialist | `bridge-builder/AGENT.md` |
| `context-janitor` | Token usage & context specialist | `context-janitor/AGENT.md` |
| `deploy-forge` | IaC/CI-CD Locksmith | `deploy-forge/AGENT.md` |
| `dependency-janitor` | Cross-project dependency manager | `dependency-janitor/AGENT.md` |
| `doc-forge` | Documentation sync specialist | `doc-forge/AGENT.md` |
| `forge-master` | Meta-orchestrator for multi-agent coordination | `forge-master/AGENT.md` |
| `lfm` | Failure memory manager | `lfm/AGENT.md` |
| `noise-filter` | Telemetry signal specialist | `noise-filter/AGENT.md` |
| `perf-profiler` | Performance bottleneck specialist | `perf-profiler/AGENT.md` |
| `redteam` | Security and risk auditor | `redteam/AGENT.md` |
| `refactor-forge` | Technical debt & legacy cleaner | `refactor-forge/AGENT.md` |
| `revert-forge` | Safe rollback specialist | `revert-forge/AGENT.md` |
| `rust-forge`| Rust development orchestrator | `rust-forge/AGENT.md` |
| `sandbox-forge` | Isolated environment specialist | `sandbox-forge/AGENT.md` |
| `schema-audit` | Database integrity auditor | `schema-audit/AGENT.md` |
| `schema-smith` | Database vault-breaker | `schema-smith/AGENT.md` |
| `selina` | Adversarial code/plan reviewer (Catwoman) | `selina/AGENT.md` |
| `smoke-tester` | Post-deploy verification specialist | `smoke-tester/AGENT.md` |
| `success-forge` | Successful pattern reuse specialist | `success-forge/AGENT.md` |
| `telemetry-eye` | OTel & monitoring watchman | `telemetry-eye/AGENT.md` |
| `test-sentry` | Coverage and regression auditor | `test-sentry/AGENT.md` |
| `ui-forge` | Multi-platform UI orchestrator | `ui-forge/AGENT.md` |
| `vibe-check` | Persona-based style auditor | `vibe-check/AGENT.md` |

---

## 🏗️ Complex Workflows

### Multi-Agent Tandem (Single Prompt)
You can orchestrate multiple specialists to handle a full feature lifecycle in one go:

**Prompt:** 
> "I need to implement a new authenticated route in the Rust backend.
> 1. Use `forge-master` to coordinate `rust-forge` (scaffold) and `test-sentry` (coverage).
> 2. Invoke `redteam` to audit the auth logic for privilege escalation.
> 3. Use `selina` to roast the implementation for edge-case failures.
> 4. Finally, have `doc-forge` update the API spec."


---

## 💡 Practical Examples

### Security Hardening
**User:** "/redteam verbose review the new payment gateway integration."
**Result:** RedTeam assigns CVSS scores, identifies a race condition in balance checks, and provides a PoC `curl` command to prove the double-spend.

### Cross-Platform UI Scaffolding
**User:** "Use `ui-forge` to build a file picker for both iOS and Windows."
**Result:** `ui-forge` delegates to `apple-smith` (SwiftUI) and `windows-smith` (WinUI 3) to ensure native look and feel without abstraction leaks.

### Performance Debugging
**User:** "The new iterator is slow. `perf-profiler` investigate."
**Result:** Sub-agent identifies O(N²) complexity, suggests a `HashMap` cache, and projects a 40% speedup.

### Safe Refactoring
**User:** "Refactor the auth module, then `vibe-check` it."
**Result:** Ensures the new code matches the team's "concise and idiomatic" style rather than just being technically correct.

---

Refer to `AGENTS.md` for detailed rules and `SKILL.md` within each directory for specific technical instructions.
