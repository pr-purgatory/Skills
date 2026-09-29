# SPEC
## §G GOAL
Roll back failed implementation to known-good git state without losing unrelated work.

## §C CONSTRAINTS
- git only.
- Commands via argv, ⊥ `sh -c` with interpolated refs.
- ≤ 1 rollback attempt per target ref per session.

## §I INTERFACES
- `SKILL.md`: safe execution flow.
- Invocation: "revert / roll back / undo [change]".
- Output: restored state + `lfm` entry for reason.

## §V INVARIANTS
V1: ∀ rollback → dirty tree stashed (`git stash push -u`) first.
V2: ∀ target ref → `git rev-parse --verify` passes before use.
V3: Ref containing shell metachar (`;&|$` backtick) → rejected.
V4: History-discarding op (`reset --hard`, force checkout) → user confirm first.
V5: ∀ rollback → reason logged via `lfm`.

## §T TASKS
id|status|task|cites
001|x|Init `SKILL.md`, `AGENT.md`|this
002|x|Mandate stash before rollback|V1
003|x|Escape/validate branch & ref args|V2,V3
004|x|Cap rollback attempts at 1|§C
005|x|Replace deprecated `git stash save` → `git stash push -u -m`|V1
006|x|Add `## Boundaries`; require confirm for `reset --hard`|V4
007|.|Prefer `git revert` (history-preserving) over `reset --hard` in flow; document when reset allowed|V4
008|.|Define rollback-attempt tracking location (how "per session" is enforced)|§C
009|.|Add evals: dirty tree → stash; ref `main;rm -rf ~` → rejected; second attempt → refused|V1,V3

## §B BUGS
id|date|cause|fix
