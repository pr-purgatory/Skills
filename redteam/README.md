# RedTeam Skill

A cross-platform security and risk assessment skill for AI agents.

## Overview
Automates a "red team" methodology to identify security vulnerabilities, architectural flaws, and logic gaps in any codebase.

## Methodology
The skill investigates the codebase through multiple lenses:
- **Premortem Analysis**: Predicts failure modes 6 months out.
- **Security Audit**: Identifies auth bypass and privilege escalation paths.
- **Architecture Stress**: Finds bottlenecks under 100x load.
- **Supply Chain Check**: Audits third-party dependencies.
- **Abuse Scenarios**: Identifies potential for spam, DDoS, or scraping.

## Installation

### Gemini CLI
1. Download `redteam.skill`.
2. Install via CLI:
   ```bash
   gemini skills install redteam.skill --scope user
   ```
3. Reload skills:
   ```bash
   /skills reload
   ```

### Claude (Projects/Artifacts)
1. Open your Claude Project.
2. Upload the `SKILL.md` and `references/criteria.md` files to the Project Knowledge.
3. Add the following to your Project Instructions:
   > "When I say '/redteam', follow the instructions in SKILL.md to perform a security audit and save findings to RedTeamFindings.md."

### Custom GPTs (OpenAI)
1. Create a new GPT.
2. Upload `SKILL.md` and `references/criteria.md` to the "Knowledge" section.
3. In "Instructions", paste:
   > "You are a Red Team Security Expert. Follow the methodology in SKILL.md and criteria.md. When triggered by '/redteam', analyze the provided code and generate RedTeamFindings.md."

## Usage
- `/redteam`: Standard audit with concise bullet points.
- `/redteam verbose`: Detailed audit including exploit steps and resolution plans.

## Output Format
Findings are saved to `RedTeamFindings.md` at the workspace root:
- `* [Module] [Vulnerability] - [Description]`
- (Verbose) `  - Finding/Exploit/Resolution`
