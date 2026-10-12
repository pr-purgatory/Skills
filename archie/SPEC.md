# SPEC
## §G GOAL
Cut token cost: plan once at high capability, execute mechanical work on cheap models.

## §C CONSTRAINTS
- Vendor-neutral: tiers, ⊥ model names in skill logic.
- Score scale 1-5, 0.5 steps.
- Subagents only for score ≤ 3.

## §I INTERFACES
- `SKILL.md`: scale, tier resolution, process, plan format.
- Invocation: "archie / plan this / break this down / score these tasks".
- Output: `archie-plan.md` (header, Questions for Prompter, tasks, cost note).
- `evals/evals.json`: behavior checks.

## §V INVARIANTS
V1: ∀ task → score, level, tier, status, depends, pass, fail, gotchas.
V2: 1-2 → jr; 2.5-3 → eng; 3.5-4 → sr; 4.5-5 → ar.
V3: Subagent executor ⇒ score ≤ 3.
V4: Plan drafted on `strong`, audited on `max` before final.
V5: Plan has `## Questions for Prompter` with default per question.
V6: ⊥ vendor/model name outside the `Tiers:` header.
V7: Failed task escalates once, second failure → `blocked`.
V8: Subagent prompt = task, files, criteria, gotchas only.
V9: ∀ task → wave = 1 + max(dep waves); same-wave tasks share no written file or mutable state.
V10: `sr`/`ar` tasks `Parallel: no`; concurrent subagents ≤ prompter limit (default 4).

## §T TASKS
id|status|task|cites
001|x|Write `SKILL.md`, `AGENT.md`|this
002|x|Define scale, tier resolution, plan format|V1,V2,V6
003|x|Add evals|V2,V3,V4,V5,V7
004|x|Register in `AGENTS.md` and README|SPEC V5
005|x|Wave-based parallel execution of light/standard tasks|V9,V10

## §B BUGS
id|date|cause|fix
