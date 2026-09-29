# SPEC
## §G GOAL
Execute untrusted code in isolated, resource-capped, short-lived Docker containers.

## §C CONSTRAINTS
- Podman or Docker required (template auto-selects podman when present; override with `RT=`).
- Defaults: `--network none`, `--cap-drop=ALL`, `--read-only`, tmpfs `/tmp` noexec, `-m 512m`, `--cpus=1.0`.
- Max runtime 60s.

## §I INTERFACES
- `SKILL.md`: policy + `docker run` template.
- Workspace dir `sandbox_temp/` mounted `:ro` at `/app`.
- Output: exit code, timeout/OOM flag, stdout/stderr summary.
- `evals/evals.json` + `evals/files/`: behavior checks (need Docker).

## §V INVARIANTS
V1: ⊥ `--privileged`; ∀ run → `--cap-drop=ALL`.
V2: Network off unless user approves in current turn.
V3: ⊥ mount `/`, `/etc`, `~/.ssh`, or home root.
V4: ∀ container → killed at TTL (in-container `timeout` + host watchdog) and removed after exit.
V5: Temp scripts deleted after run, incl. failure path.

## §T TASKS
id|status|task|cites
001|x|Init `SKILL.md`, `AGENT.md`|this
002|x|Strict Docker security policy|V1,V2,V3
003|x|Resource limits + TTL pruning|V4
004|x|Add `## Boundaries`|
005|x|Make TTL enforceable: named container + `docker stop` after 60s (killing client alone leaves container running)|V4
006|x|Add `--read-only` + `--tmpfs` + `--security-opt no-new-privileges` + `--pids-limit` to template (policy lists them; example omits)|V1
007|x|Scope `docker container prune` to sandbox-labeled containers (`--filter label=sandbox-forge`) — unscoped prune deletes user's other stopped containers|V4
008|x|Add evals: network call → fails; write outside /tmp → fails; infinite loop → killed ≤ 60s|V2,V4

## §B BUGS
id|date|cause|fix
