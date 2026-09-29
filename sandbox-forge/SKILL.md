---
name: sandbox-forge
description: >
  Run untrusted or experimental code in a locked-down Podman or Docker container: no network,
  no capabilities, read-only root, CPU/memory caps, 60s TTL, auto-prune.
  Use when asked to sandbox, isolate, or safely execute code or reproduce a bug.
---

# Sandbox Forge

## Goal
Scaffold and run untrusted code inside highly restricted Docker containers or virtual sandboxes. Ensure complete isolation of the host from any malicious command execution, network access, or resource exhaustion.

---

## Sandbox Security Policies (CWE-250)

Every sandboxed container MUST follow these strict security constraints:

1. **Privileged Mode Disabled**: Never run Docker with `--privileged`. Drop all capabilities (`--cap-drop=ALL`).
2. **Network Disabled**: By default, isolate from the network (`--network none`). Only enable if explicitly requested and approved by the user.
3. **Read-Only Root File System**: Mount the container root file system as read-only (`--read-only`), except for designated temporary write volumes (e.g. `/tmp` using tmpfs: `--tmpfs /tmp:rw,noexec,nosuid,size=64m`).
4. **Host mounts restricted**: Never mount the host root directory (`/` or `C:\`) or sensitive configuration directories (`/etc`, `~/.ssh`). Only mount the narrowest workspace directories needed, explicitly using read-only flags (`:ro`) if execution does not require writing.

---

## Resource Limits & Pruning (CWE-400)

1. **CPU/Memory Limits**:
   - Limit CPU shares (`--cpus="1.0"` or `--cpu-shares=1024`).
   - Limit memory (`-m 512m` or `--memory-swap 512m`).
2. **JobManager Container TTL & Auto-Pruning**:
   - Every spawned container must have a defined TTL (Time-To-Live). Default maximum execution time is **60 seconds**.
   - Enforce TTL with in-container `timeout -s KILL 60` plus a host watchdog `kill` (see template). ⊥ rely on killing the `run` client.
   - Label every sandbox container (`--label sandbox-forge=1`) and prune only those (`$RT container prune -f --filter "label=sandbox-forge=1" --filter "until=5m"`) on startup or shutdown of any sandboxed task. ⊥ unscoped prune — it deletes the user's unrelated stopped containers.

---

## Invocation & Script Generation

When generating sandbox runs:
1. Pick a unique name, then write the untrusted script to `sandbox_temp/$SCRIPT`. Never reuse a filename across runs: podman on macOS caches a deleted path as missing for a few seconds, so a re-created `test_script.py` is invisible to the next container.
2. Run it with the template below. It enforces the 60s TTL twice: `timeout` inside the container, and a host-side watchdog that kills the container if the inner timeout is missing or bypassed. Killing only the `run` client is NOT enough — the container keeps running — so the template runs detached, names the container, and always removes it.
   ```bash
   RT=${RT:-$(command -v podman >/dev/null 2>&1 && echo podman || echo docker)}
   NAME="sandbox-forge-$(date +%s)-$$"
   SCRIPT="$NAME.py"            # write the untrusted code to sandbox_temp/$SCRIPT
   trap '$RT rm -f "$NAME" >/dev/null 2>&1' EXIT

   $RT run -d --name "$NAME" \
     --label sandbox-forge=1 \
     --network none \
     --cap-drop=ALL \
     --security-opt no-new-privileges \
     --read-only \
     --tmpfs /tmp:rw,noexec,nosuid,size=64m \
     --pids-limit 128 \
     -m 512m --memory-swap 512m \
     --cpus="1.0" \
     -v "$(pwd)/sandbox_temp:/app:ro" \
     -w /app \
     python:3.11-slim \
     timeout -s KILL 60 python "$SCRIPT" >/dev/null

   ( sleep 65; $RT kill "$NAME" ) >/dev/null 2>&1 &   # host watchdog
   WATCHDOG=$!
   EXIT_CODE=$($RT wait "$NAME")
   pkill -P "$WATCHDOG" 2>/dev/null; kill "$WATCHDOG" 2>/dev/null   # kill the sleep too, or callers block 65s
   OUTPUT=$($RT logs "$NAME" 2>&1 | tail -c 20000)
   ```
3. Interpret `EXIT_CODE`: `0` success; `137` killed (TTL or OOM — check `$RT inspect -f '{{.State.OOMKilled}}' "$NAME"` before the trap removes it); anything else = script failure. Return exit code, OOM/timeout flag, and `OUTPUT` as structured feedback.
4. Delete the script immediately after execution, including on failure: `rm -f -- "sandbox_temp/${SCRIPT:?}"` (`:?` aborts if the variable is empty).

---

## Boundaries

- ⊥ `--privileged`, ⊥ host root or `~/.ssh`/`/etc` mounts.
- Network off by default; enable only on explicit user approval.
- ⊥ persist data outside sandbox without user approval.
- ∀ container → TTL + cleanup, even on failure.
