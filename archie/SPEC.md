# SPEC
## §G GOAL
Cut token cost: plan once at high capability, execute mechanical work on cheap models, and keep plans cheap to read (status first, finished work on demand).

## §C CONSTRAINTS
- Vendor-neutral: tiers, ⊥ model names in skill logic.
- Score scale 1-5, 0.5 steps.
- Subagents only for score ≤ 3.

## §I INTERFACES
- `SKILL.md`: scale, tier resolution, process, plan layout, completing work.
- Invocation: "archie / plan this / break this down / score these tasks".
- Output per plan: `archie/<plan-slug>/` with `STATUS.md` (status only), `archie-plan.md` (open task specs), `done/` (finished tasks, logs), `ref/` (data). Never the workspace root.
- Workspace files: `archie/INDEX.md` (one row per plan), `archie/ROUTING.md` (tier key and status words), `archie/README.md` (read order).
- `evals/evals.json`: behavior checks.

## §V INVARIANTS
V1: ∀ task → score, level, tier, depends, pass, fail, gotchas in its spec; status in its `STATUS.md` row.
V2: 1-2 → jr; 2.5-3 → eng; 3.5-4 → sr; 4.5-5 → ar.
V3: Subagent executor ⇒ score ≤ 3.
V4: Plan drafted on `strong`, audited on `max` before final.
V5: Plan has `## Questions for Prompter` with default per question.
V6: ⊥ vendor/model name outside `archie/ROUTING.md` and per-plan tier overrides.
V7: Failed task escalates once, second failure → `blocked`.
V8: Subagent prompt = task, files, criteria, gotchas only.
V9: ∀ task → wave = 1 + max(dep waves); same-wave tasks share no written file or mutable state.
V10: `sr`/`ar` tasks `Parallel: no`; concurrent subagents ≤ prompter limit (default 4).
V11: Plan path = `archie/<plan-slug>/archie-plan.md`; plan metadata lives in that folder; ⊥ plan or plan files in workspace root.
V12: Status only in `STATUS.md` + `INDEX.md`; ⊥ `Status:` line in task specs; `STATUS.md` ≤ 4 KB.
V13: Done task → block moved to `done/wave-N.md` with Result line; stub left in `archie-plan.md`.
V14: Status edits committed on the default branch; plan bodies travel with the work branch.
V15: Read order INDEX → STATUS → open specs → done/ on demand; ⊥ loading done/ by default.

## §T TASKS
id|status|task|cites
001|x|Write `SKILL.md`, `AGENT.md`|this
002|x|Define scale, tier resolution, plan format|V1,V2,V6
003|x|Add evals|V2,V3,V4,V5,V7
004|x|Register in `AGENTS.md` and README|SPEC V5
005|x|Wave-based parallel execution of light/standard tasks|V9,V10
006|x|One folder per plan under `archie/`|V11
007|x|STATUS.md/INDEX.md/ROUTING.md, done/ archive, read order, status on default branch|V6,V12,V13,V14,V15

## §B BUGS
id|date|cause|fix
