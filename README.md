# Skills Forge

Collection of specialized agent skills and subagents.

## Batch Install

Install all skills at once:

```bash
find . -maxdepth 2 -name "SKILL.md" -exec gemini skill install {} \;
```

## Subagents Usage

Each skill acts as a specialized subagent. Call via `invoke_agent` in the CLI.

| Agent Name | Description | Invocation |
|------------|-------------|------------|
| `selina` | Adversarial reviewer | `invoke_agent(agent_name="selina", prompt="...")` |
| `redteam` | Security auditor | `invoke_agent(agent_name="redteam", prompt="...")` |
| `lfm` | Failure memory | `invoke_agent(agent_name="lfm", prompt="...")` |
| `rust-forge` | Rust specialist | `invoke_agent(agent_name="rust-forge", prompt="...")` |
| `ui-forge` | UI/UX specialist | `invoke_agent(agent_name="ui-forge", prompt="...")` |

Refer to `AGENTS.md` for detailed rules and `SKILL.md` within each directory for specific instructions.
