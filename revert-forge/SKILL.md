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
To prevent command or shell injection via malformed branch/commit names:
- Avoid passing raw untrusted strings to shell execution (`sh -c`).
- Use argument vectors directly when running commands (e.g. `Command::new("git").arg("checkout").arg(branch_name)`).
- Sanitize and reject any arguments containing shell metacharacters (e.g. `;`, `&`, `|`, `$`, `` ` ``).
- Validate git targets using `git rev-parse --verify <ref>` before executing the revert.

### 3. Loop Prevention
- Maintain a strict state tracking of rollback attempts.
- Limit rollbacks of the same target ref/commit to a maximum of **1 attempt** per session to avoid recursive revert-fail loops.

---

## Safe Execution Flow

1. Check current git status: `git status --porcelain`.
2. If working directory is dirty, execute `git stash`.
3. Verify target commit/ref exists: `git rev-parse --verify <target_ref>`.
4. Perform the checkout or revert:
   - For a specific branch: `git checkout <branch_name>`
   - To undo a specific commit: `git revert --no-edit <commit_hash>`
   - To hard reset: `git reset --hard <target_ref>`
5. Validate working directory matches the desired state.

---

## Boundaries

- ⊥ reset/checkout/revert before uncommitted work is stashed.
- `git reset --hard` or any history-discarding op → confirm with user first.
- ⊥ pass unvalidated ref names to a shell; argv only.
- ≤ 1 rollback attempt per target ref per session.
- ∀ revert → log reason via `lfm`.
