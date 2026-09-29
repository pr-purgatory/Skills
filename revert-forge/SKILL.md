---
name: revert-forge
description: >
  Safe git rollback of a failed or rejected implementation. Stashes uncommitted work,
  validates refs, blocks shell injection, caps retries at one.
  Use when asked to revert, roll back, or undo a failed change.
---

# Revert Forge

## Goal
Restore the working directory or git branch safely to a previous clean state when a feature implementation fails, is rejected, or causes severe regressions. Prevent data loss of unrelated uncommitted work and defend against shell injection.

---

## Safety Requirements

### 1. Mandatory Git Stash (Prevent Data Loss)
Before performing any reset, checkout, or revert operation:
- You MUST save any uncommitted changes in the working directory or staging area.
- Command: `git stash push -u -m "revert-forge auto-stash before rollback"`
- If `git stash` fails or indicates there is nothing to stash, proceed only after confirming the working tree status.

### 2. Argument Validation & Escaping (CWE-88)
To prevent command or option injection via malformed branch/commit names:
- Never pass refs through a shell string (`sh -c`, backticks, `eval`). Use argv (e.g. `Command::new("git").arg("revert").arg(sha)`); from a shell tool, single-quote the ref.
- Reject any ref that starts with `-` or contains whitespace or shell metacharacters (`;`, `&`, `|`, `$`, `` ` ``, `<`, `>`).
- Resolve every target to a commit SHA first and use the SHA from then on:
  `git rev-parse --verify --end-of-options '<ref>^{commit}'`
  Non-zero exit → stop and report the ref as invalid.

### 3. Loop Prevention (Attempt Tracking)
Attempts are tracked on disk so the limit survives context compaction and restarts:
- File: `$(git rev-parse --git-dir)/revert-forge-attempts` — inside `.git`, so never committed.
- Line format: `<target-sha> <ISO-8601 UTC timestamp>`.
- Before rollback: if the resolved SHA has an entry from the last **12 hours**, refuse and tell the user a rollback of this target was already attempted. Proceed only if the user explicitly overrides in the current turn.
- After rollback (success or failure): append the entry.

---

## Choosing the Rollback Method

| Situation | Method | History |
|-----------|--------|---------|
| Bad commit(s) already pushed or on a shared branch | `git revert --no-edit <sha>` (range: `git revert --no-edit <old>..<new>`) | Preserved — **default** |
| Merge commit | `git revert --no-edit -m 1 <merge-sha>` | Preserved |
| Unpushed local commits only, user wants them gone | `git reset --hard <good-sha>` | Discarded — **user confirm required** |
| Return to another branch | `git switch <branch>` | Unchanged |

Unpushed check: `git branch -r --contains <sha>` prints nothing → commit is local only. Even then, prefer `git revert` unless the user asks to drop history.

---

## Safe Execution Flow

1. `git status --porcelain`. Abort if a merge/rebase/cherry-pick is in progress (`git rev-parse -q --verify MERGE_HEAD` / `REBASE_HEAD` / `CHERRY_PICK_HEAD`).
2. Validate and resolve the target to a SHA (§2).
3. Check the attempt log (§3); refuse if a recent attempt exists.
4. If the tree is dirty: `git stash push -u -m "revert-forge auto-stash before rollback"`. Report the stash ref (`stash@{0}`) to the user.
5. Pick the method from the table above. `reset --hard` → ask the user and wait for a yes.
6. Execute. If `git revert` hits conflicts: `git revert --abort`, report the conflicting files, stop. ⊥ auto-resolve.
7. Append the attempt entry (§3).
8. Verify: `git status --porcelain` is clean and `git log --oneline -3` shows the expected state; run the project's test command if one exists.
9. Log the reason via `lfm`. Remind the user their work is in the stash (`git stash pop` to restore).

---

## Boundaries

- ⊥ reset/checkout/revert before uncommitted work is stashed.
- Default to `git revert`; `git reset --hard` or any history-discarding op → confirm with user first.
- ⊥ pass unvalidated ref names to a shell; argv only.
- ≤ 1 rollback attempt per target SHA per 12h, tracked in `.git/revert-forge-attempts`.
- ∀ revert → log reason via `lfm`.
