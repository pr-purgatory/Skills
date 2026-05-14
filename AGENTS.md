# AGENTS

This registry defines the available subagents derived from the local skills. Use `invoke_agent` with the specified names and rules.

| Agent Name | Description | Rules File |
|------------|-------------|------------|
| `selina` | Adversarial code/plan reviewer (Catwoman) | `selina/AGENT.md` |
| `redteam` | Security and risk auditor | `redteam/AGENT.md` |
| `lfm` | Failure memory manager | `lfm/AGENT.md` |
| `rust-forge`| Rust development orchestrator | `rust-forge/AGENT.md` |
| `ui-forge` | Multi-platform UI orchestrator | `ui-forge/AGENT.md` |
| `perf-profiler` | Performance bottleneck specialist | `perf-profiler/AGENT.md` |
| `context-janitor` | Token usage & context specialist | `context-janitor/AGENT.md` |
| `doc-forge` | Documentation sync specialist | `doc-forge/AGENT.md` |
| `success-forge` | Successful pattern reuse specialist | `success-forge/AGENT.md` |
| `vibe-check` | Persona-based style auditor | `vibe-check/AGENT.md` |
| `test-sentry` | Coverage and regression auditor | `test-sentry/AGENT.md` |
| `dependency-janitor` | Cross-project dependency manager | `dependency-janitor/AGENT.md` |
| `revert-forge` | Safe rollback specialist | `revert-forge/AGENT.md` |
| `sandbox-forge` | Isolated environment specialist | `sandbox-forge/AGENT.md` |

## Usage
To utilize a subagent, refer to its specific `AGENT.md` for identity, rules, and invocation templates. Ensure all `invoke_agent` calls respect the defined boundaries and personas.
