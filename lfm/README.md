# lfm — Learn From Mistakes

Persistent failure memory for AI agent sessions. Logs failed approaches with
structured context to disk on each trigger, consults the log before significant
actions, and survives context compaction. Works across Claude, Gemini, Codex,
Cursor, Copilot, Windsurf, Aider, and Continue.

---

## How it works

When the agent tries something that fails — and you correct it — LFM logs the
approach, why it failed, and what worked instead to a plain markdown file on
disk. In `std` and `einstein` modes, the agent reads that file before taking
significant actions and silently adjusts to avoid repeating logged failures.

Because findings are written to disk on each trigger (not stored in context),
they survive context compaction and carry forward to future sessions
automatically.

---

## Installation

### Claude Code

Copy `SKILL.md` to `~/.claude/lfm/`:

```sh
mkdir -p ~/.claude/lfm
cp SKILL.md ~/.claude/lfm/SKILL.md
```

Then wire it into Claude Code by adding this line to your `CLAUDE.md`
(global: `~/.claude/CLAUDE.md`, or per-project: `<repo>/CLAUDE.md`):

```
@/Users/<username>/.claude/lfm/SKILL.md
```

Use the absolute path — `~` does not expand in Claude Code `@`-imports.
Without this line, Claude Code will not load the skill and `/lfm` will not work.

### Gemini CLI

Copy `SKILL.md` to `~/.gemini/skills/lfm/` (Gemini's standard skills directory)
and create the log directory separately:

```sh
mkdir -p ~/.gemini/skills/lfm
cp SKILL.md ~/.gemini/skills/lfm/SKILL.md
mkdir -p ~/.gemini/lfm
```

The log writes to `~/.gemini/lfm/lfm-log.md`, outside the skills directory.

### Codex CLI / Aider / Continue

Copy to `~/.<agent>/lfm/`:

```sh
# Codex
mkdir -p ~/.codex/lfm && cp SKILL.md ~/.codex/lfm/SKILL.md

# Aider
mkdir -p ~/.aider/lfm && cp SKILL.md ~/.aider/lfm/SKILL.md

# Continue
mkdir -p ~/.continue/lfm && cp SKILL.md ~/.continue/lfm/SKILL.md
```

### Cursor / GitHub Copilot (IDE-embedded)

Copy to `~/.<agent>/lfm/` if the agent has home directory access:

```sh
mkdir -p ~/.cursor/lfm && cp SKILL.md ~/.cursor/lfm/SKILL.md
mkdir -p ~/.copilot/lfm && cp SKILL.md ~/.copilot/lfm/SKILL.md
```

If the agent cannot write outside the workspace, LFM degrades gracefully —
it logs to `./lfm-log.md` in the workspace root and warns once:

```
[LFM] No home dir access — logging to ./lfm-log.md instead.
```

### Install all at once

```sh
for agent in claude codex cursor copilot windsurf aider continue; do
  mkdir -p ~/.$agent/lfm && cp SKILL.md ~/.$agent/lfm/SKILL.md
done
mkdir -p ~/.gemini/skills/lfm && cp SKILL.md ~/.gemini/skills/lfm/SKILL.md
mkdir -p ~/.gemini/lfm
```

Then add the Claude Code wiring to `~/.claude/CLAUDE.md`:

```
@/Users/<username>/.claude/lfm/SKILL.md
```

---

## Log file locations

| Agent | Log Path |
|-------|----------|
| Claude Code | `~/.claude/lfm/lfm-log.md` |
| Gemini CLI | `~/.gemini/lfm/lfm-log.md` |
| OpenAI Codex | `~/.codex/lfm/lfm-log.md` |
| Cursor | `~/.cursor/lfm/lfm-log.md` |
| GitHub Copilot | `~/.copilot/lfm/lfm-log.md` |
| Windsurf | `~/.windsurf/lfm/lfm-log.md` |
| Aider | `~/.aider/lfm/lfm-log.md` |
| Continue | `~/.continue/lfm/lfm-log.md` |

The log is plain markdown and append-only. Any agent can read any other
agent's log for cross-agent reference.

---

## Usage

### Activate

```
/lfm
```

Activates in default `std` mode. Stays active for the rest of the session.

```
/lfm einstein
```

Activates in `einstein` mode — surfaces past failures explicitly before
proceeding and requires confirmation before retrying a logged approach.

### Check status

```
/lfm
```

When already active with no arguments:

```
[LFM] Active — mode: std. 3 entries in log. /lfm jr|std|einstein to switch.
```

### Switch modes

```
/lfm jr        # log only, no consultation
/lfm std       # log + silent consultation (default)
/lfm einstein  # log + explicit consultation + confirmation gate
```

### Manually log a failure

```
/lfm log
```

`log` is a reserved subcommand — it triggers an immediate manual log of the
last failed approach. It does not switch modes. Say `"log that failure"` works
too.

### Deactivate

```
stop lfm
lfm off
```

Stops logging and consulting. Does not delete the log.

---

## Modes

| Mode | What the agent does |
|------|---------------------|
| `jr` | Logs failures on trigger only. No pre-action consultation. |
| `std` | Logs on trigger. Reads the log before significant actions and silently adjusts when a past failure matches. Speaks up only if the adjustment meaningfully changes the plan. |
| `einstein` | Logs on trigger. Reads the log before significant actions. If a match is found, surfaces it explicitly and waits for confirmation before proceeding. |

---

## What triggers a log entry

LFM logs automatically when:

- You correct the agent — "no", "wrong", "revert", "undo", "that's not right"
- A shell command exits non-zero and you immediately provide a different approach
- You explicitly invoke `/lfm log`
- A multi-step approach is abandoned mid-task at your direction

LFM does **not** log preference changes, direction pivots unrelated to a
failure, or routine permission denials.

---

## Log format

Plain markdown, append-only. Each entry:

```markdown
## 2026-05-01 short-title
- approach: what was tried (specific — function, command, pattern)
- context: task, file, or condition it was tried in
- why-failed: specific reason — error message, constraint, wrong assumption
- outcome: what worked instead, or "unresolved"
```

Example entry:

```markdown
## 2026-05-01 batch-findstr-whole-log
- approach: findstr "(0% loss)" against full log file to detect packet loss
- context: net-diag.bat summary analysis section
- why-failed: earlier sections matched the pattern, masking real gateway loss
- outcome: wrote ping output to temp file, searched temp file only
```

---

## Updating

Re-run the install script to sync all agents when `SKILL.md` changes:

```sh
for agent in claude codex cursor copilot windsurf aider continue; do
  cp SKILL.md ~/.$agent/lfm/SKILL.md
done
cp SKILL.md ~/.gemini/skills/lfm/SKILL.md
```

Log files are never touched by the install script — existing findings are safe.

---

## Log maintenance

The log is append-only but unbounded growth degrades consultation quality.
Recommended convention:

- Keep the active log under **100 entries**
- Archive entries older than 90 days to `lfm-log.archive.md` in the same directory
- Trigger archival with `/lfm trim` — the agent moves old entries and confirms:
  `[LFM] Archived N entries to lfm-log.archive.md. Active log: M entries.`

The archive file is never consulted automatically — it exists for human
reference only.

---

## Files

```
Skills/lfm/
  SKILL.md       — skill definition (source of truth)
  README.md      — this file

Installed (created by install step):
  ~/.claude/lfm/SKILL.md
  ~/.gemini/skills/lfm/SKILL.md
  ~/.<agent>/lfm/SKILL.md    (others)

Log data (created on first trigger):
  ~/.<agent>/lfm/lfm-log.md
```
