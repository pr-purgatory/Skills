---
name: sandbox-forge
description: >
  Run untrusted or experimental code in a locked-down Docker container: no network,
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
   - Auto-kill containers after TTL expires using a background timeout or wrapper daemon.
   - Label every sandbox container (`--label sandbox-forge=1`) and prune only those (`docker container prune -f --filter "label=sandbox-forge=1" --filter "until=5m"`) on startup or shutdown of any sandboxed task. ⊥ unscoped prune — it deletes the user's unrelated stopped containers.

---

## Invocation & Script Generation

When generating sandbox runs:
1. Write the target test/untrusted script to a temporary file inside the workspace.
2. Formulate the docker run command:
   ```bash
   docker run --rm \
     --label sandbox-forge=1 \
     --network none \
     --cap-drop=ALL \
     --security-opt no-new-privileges \
     --read-only \
     --tmpfs /tmp:rw,noexec,nosuid,size=64m \
     --pids-limit 128 \
     -m 512m \
     --cpus="1.0" \
     -v "$(pwd)/sandbox_temp:/app:ro" \
     -w /app \
     python:3.11-slim \
     python test_script.py
   ```
3. Check the exit code and stderr. Return structured feedback.
4. Clean up any generated temporary script files immediately after execution completes.

---

## Boundaries

- ⊥ `--privileged`, ⊥ host root or `~/.ssh`/`/etc` mounts.
- Network off by default; enable only on explicit user approval.
- ⊥ persist data outside sandbox without user approval.
- ∀ container → TTL + cleanup, even on failure.
