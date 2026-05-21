# AGENTS

This registry defines the available subagents derived from the local skills. Use `invoke_agent` with the specified names and rules.

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

## Usage
To utilize a subagent, refer to its specific `AGENT.md` for identity, rules, and invocation templates. Ensure all `invoke_agent` calls respect the defined boundaries and personas.
