# Skills Forge

Collection of specialized agent skills and subagents for the autonomous engineer.

**Status:** 🟢 100% MVP, Logic, and GAP tasks complete. Expansion phase 2 + Gap Closure active.

## 🆕 Recent Updates
- **Registry:** Central `AGENTS.md` subagent registry.
- **Skill Pruning:** Removed 17 generic/unimplemented scaffold skills; remaining skills each carry concrete, non-obvious procedure.
- **Skill Hardening:** Canonicalized LFM hashing, CVSS-to-SARIF mapping for RedTeam, and Tone Drift Guard for Selina.

## 🚀 Batch Install

Install all skills for your preferred tool:

### Antigravity
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
| `lfm` | Failure memory manager | `lfm/AGENT.md` |
| `redteam` | Security and risk auditor | `redteam/AGENT.md` |
| `revert-forge` | Safe rollback specialist | `revert-forge/AGENT.md` |
| `rust-forge`| Rust development orchestrator | `rust-forge/AGENT.md` |
| `sandbox-forge` | Isolated environment specialist | `sandbox-forge/AGENT.md` |
| `selina` | Adversarial code/plan reviewer (Catwoman) | `selina/AGENT.md` |
| `ui-forge` | Multi-platform UI orchestrator | `ui-forge/AGENT.md` |

---

## 🏗️ Complex Workflows

### Multi-Agent Tandem (Single Prompt)
You can orchestrate multiple specialists to handle a full feature lifecycle in one go:

**Prompt:** 
> "I need to implement a new authenticated route in the Rust backend.
> 1. Use `rust-forge` to scaffold the route and its tests.
> 2. Invoke `redteam` to audit the auth logic for privilege escalation.
> 3. Use `selina` to roast the implementation for edge-case failures."

---

## 💡 Practical Examples

### Security Hardening
**User:** "/redteam verbose review the new payment gateway integration."
**Result:** RedTeam assigns CVSS scores, identifies a race condition in balance checks, and provides a PoC `curl` command to prove the double-spend.

### Cross-Platform UI Scaffolding
**User:** "Use `ui-forge` to build a file picker for both iOS and Windows."
**Result:** `ui-forge` delegates to `apple-smith` (SwiftUI) and `windows-smith` (WinUI 3) to ensure native look and feel without abstraction leaks.

---

Refer to `AGENTS.md` for detailed rules and `SKILL.md` within each directory for specific technical instructions.
