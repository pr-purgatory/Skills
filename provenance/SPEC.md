# Plan: Provenance Review AI Skill
Goal: Build vendor-neutral AI skill and subagent for clean-room reverse engineering provenance and contamination reviews.
Tiers: light=gemini-flash standard=gemini-flash strong=gemini-pro max=gemini-pro
Audit: pass
Scale: 1-2 jr · 2.5-3 eng · 3.5-4 sr · 4.5-5 ar

## Questions for Prompter
| # | Question | Default | Answer |
|---|----------|---------|--------|
| Q1 | Primary report output formats? | Markdown audit table + SARIF v2.1.0 JSON | assumed |
| Q2 | Decompiler signature detection scope? | Hex-Rays, Ghidra, IDA Pro, Binary Ninja idioms | assumed |
| Q3 | Strictness for clean-room Chinese wall enforcement? | Hard block if single author handles both disassembly and clean implementation | assumed |
| Q4 | Max concurrent subagents? | 4 | assumed |

## §G GOAL
Automate provenance and contamination reviews for open-source reverse engineering projects. Enforce clean-room Chinese wall boundaries, detect proprietary decompiler leaks, and produce SARIF/Markdown audit reports across all major LLM providers.

## §C CONSTRAINTS
- Vendor-neutral: zero provider-specific tool schemas or APIs; prompts use portable markdown/XML tags.
- Compatible with Anthropic Claude, OpenAI GPT, Google Gemini, and local models (Ollama/vLLM).
- Strict prompt injection immunity: treat audited diffs and decompilation snippets as untrusted data.
- Mask secrets and PII in audit outputs.
- Adhere to repo invariants in pr-purgatory/Skills (`SKILL.md`, `AGENT.md`, `LICENSE`, `SPEC.md`, `evals/evals.json`).

## §I INTERFACES
- Trigger: `provenance` / `/provenance` / "review provenance" / "clean-room audit".
- Input: Git diffs, PRs, commit logs, clean-room specifications, or source trees.
- Output: Markdown audit report (`PROVENANCE_AUDIT.md`) and SARIF v2.1.0 (`provenance.sarif`).
- Registry: `Skills/AGENTS.md` and `Skills/README.md`.
- Evals: `Skills/provenance/evals/evals.json`.

## §V INVARIANTS
V1: ∀ review → classify each finding by taint severity: `CLEAN`, `SUSPECT`, `CONTAMINATED`, `BLOCKER`.
V2: Verbatim decompiler signatures (Hex-Rays, Ghidra, IDA variable idioms) → `CONTAMINATED`.
V3: Proprietary symbol leak or internal path trace → `BLOCKER`.
V4: Clean-room breach (same committer authored spec and implementation) → `BLOCKER`.
V5: Output contains actionable clean-room remediation (quarantine, clean re-implementation).
V6: ⊥ proprietary code or leaked source quoted in output without masking.
V7: Prompt injection inside diff comments or docstrings ⊥ alter audit verdicts.

## Tasks

### T1 — Provenance Review Architecture & Spec Finalization
- Score: 4.5 (ar) · Tier: max · Executor: main
- Status: done
- Depends: none
- Wave: 1 · Parallel: no
- Files: [Skills/provenance/SPEC.md](file:///Users/bb/code/pr-purgatory/Skills/provenance/SPEC.md) `(w)`
- Pass: `Skills/provenance/SPEC.md` defines §G, §C, §I, §V, scored Archie tasks, and pass/fail criteria.
- Fail: Empty spec file or missing clean-room contamination definitions.
- Gotchas: Conflating standard security review with provenance audit; failing to address legal clean-room boundary definitions (interoperability exceptions under US 17 U.S.C. §1201(f) and EU Software Directive).

### T2 — Author Core Provenance `SKILL.md`
- Score: 3.5 (sr) · Tier: strong · Executor: main
- Status: done
- Depends: T1
- Wave: 2 · Parallel: no
- Files: [Skills/provenance/SKILL.md](file:///Users/bb/code/pr-purgatory/Skills/provenance/SKILL.md) `(w)`
- Pass: `Skills/provenance/SKILL.md` exists with YAML frontmatter (`name: provenance`, description ending with "Use when ..."), contains `## Goal`, `## Clean Room Methodology`, `## Contamination Rubric`, `## Review Protocol`, `## Output Formats`, and `## Boundaries` last.
- Fail: Missing frontmatter trigger, missing decompiler heuristics, or provider-specific tooling syntax included.
- Gotchas: Hardcoding provider-specific functions; fragile regexes instead of structural LLM analysis prompts; prompt injection via malicious code comments in inspected diffs.

### T3 — Subagent Definition `AGENT.md`
- Score: 2.5 (eng) · Tier: standard · Executor: subagent
- Status: done
- Depends: T2
- Wave: 3 · Parallel: yes
- Files: [Skills/provenance/AGENT.md](file:///Users/bb/code/pr-purgatory/Skills/provenance/AGENT.md) `(w)`
- Pass: `Skills/provenance/AGENT.md` defines Identity, Capabilities, Rules, and Invocation Prompt Template adhering to repo standard.
- Fail: File missing, empty, or missing Invocation Prompt Template.
- Gotchas: Divergence between `SKILL.md` boundaries and `AGENT.md` rules.

### T4 — Copy Repo Apache 2.0 License
- Score: 1.0 (jr) · Tier: light · Executor: subagent
- Status: done
- Depends: none
- Wave: 2 · Parallel: yes
- Files: [Skills/provenance/LICENSE](file:///Users/bb/code/pr-purgatory/Skills/provenance/LICENSE) `(w)`, [Skills/selina/LICENSE](file:///Users/bb/code/pr-purgatory/Skills/selina/LICENSE) `(r)`
- Pass: `Skills/provenance/LICENSE` exists, size matches repo license, contains "Apache License".
- Fail: File missing or empty.
- Gotchas: Truncated license text.

### T5 — Create Comprehensive Eval Suite `evals/evals.json`
- Score: 3.0 (eng) · Tier: standard · Executor: subagent
- Status: done
- Depends: T2
- Wave: 3 · Parallel: yes
- Files: [Skills/provenance/evals/evals.json](file:///Users/bb/code/pr-purgatory/Skills/provenance/evals/evals.json) `(w)`
- Pass: Valid JSON file containing ≥ 5 test scenarios covering: Hex-Rays/Ghidra idiom detection, proprietary symbol leak, valid clean-room spec implementation, prompt injection attack defense, and SARIF output schema adherence.
- Fail: Invalid JSON or fewer than 5 test cases.
- Gotchas: Test cases too trivial; neglecting adversarial prompt injection inside target source code.

### T6 — Register Subagent in Central Registries
- Score: 1.5 (jr) · Tier: light · Executor: subagent
- Status: done
- Depends: T3
- Wave: 4 · Parallel: no
- Files: [Skills/AGENTS.md](file:///Users/bb/code/pr-purgatory/Skills/AGENTS.md) `(w)`, [Skills/README.md](file:///Users/bb/code/pr-purgatory/Skills/README.md) `(w)`
- Pass: Both `Skills/AGENTS.md` and `Skills/README.md` have alphabetical `provenance` row in agent registry tables.
- Fail: `grep -q "provenance" Skills/AGENTS.md` or `grep -q "provenance" Skills/README.md` returns non-zero.
- Gotchas: Breaking alphabetical ordering in tables; formatting glitches in markdown tables.

### T7 — Validate Invariants & Cross-Provider Compatibility
- Score: 2.5 (eng) · Tier: standard · Executor: subagent
- Status: done
- Depends: T1, T2, T3, T4, T5, T6
- Wave: 5 · Parallel: no
- Files: [Skills/provenance/*](file:///Users/bb/code/pr-purgatory/Skills/provenance/) `(r)`, [Skills/AGENTS.md](file:///Users/bb/code/pr-purgatory/Skills/AGENTS.md) `(r)`, [Skills/README.md](file:///Users/bb/code/pr-purgatory/Skills/README.md) `(r)`
- Pass: Automated invariant check validates V1-V5 from repo `Skills/SPEC.md` and T1-T7 criteria pass.
- Fail: Any invariant violation or broken file link.
- Gotchas: Missing trailing newline, subtle markdown parsing errors.

## Waves
W1: T1 · W2: T2 T4 · W3: T3 T5 · W4: T6 · W5: T7

## Cost note
7 tasks across 5 waves:
- `jr`: 2 tasks (28.6%) · `light` tier
- `eng`: 3 tasks (42.8%) · `standard` tier
- `sr`: 1 task (14.3%) · `strong` tier
- `ar`: 1 task (14.3%) · `max` tier
Total delegated to subagents (`light` / `standard`): 71.4% of tasks.
