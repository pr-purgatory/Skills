# AGENTS

This registry defines the available subagents derived from the local skills. Use `invoke_agent` with the specified names and rules.

| Agent Name | Description | Rules File |
|------------|-------------|------------|
| `selina` | Adversarial code/plan reviewer (Catwoman) | `selina/AGENT.md` |
| `redteam` | Security and risk auditor | `redteam/AGENT.md` |
| `lfm` | Failure memory manager | `lfm/AGENT.md` |
| `rust-forge`| Rust development orchestrator | `rust-forge/AGENT.md` |
| `ui-forge` | Multi-platform UI orchestrator | `ui-forge/AGENT.md` |
| `edm` | Event-driven skill manager | `edm/AGENT.md` |

## Usage
To utilize a subagent, refer to its specific `AGENT.md` for identity, rules, and invocation templates. Ensure all `invoke_agent` calls respect the defined boundaries and personas.
