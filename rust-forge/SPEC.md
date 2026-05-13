# SPEC
## §G GOAL
Multi-agent Rust programming assistance: debug, scaffold, & test.

## §C CONSTRAINTS
- Rust/Cargo ecosystem only.
- Strict idiomatic enforcement (Clippy-aligned).
- Sub-agent delegation ! mutative collision.
- Compatible with `@edm` event triggers.

## §I INTERFACES
- `rust-forge`: Primary trigger.
- Sub-agents: `rust-debugger`, `rust-architect`, `rust-tester`.
- Triggers: `CodeChange`, `TaskFailed`, `SessionStart`.

## §V INVARIANTS
V1: ∀ sub-agent invocation → pass relevant `Cargo.toml` context.
V2: ⊥ non-idiomatic `unsafe` code unless explicitly requested.
V3: ∀ build failure → trigger `rust-debugger`.
V4: ∀ new module → trigger `rust-architect` for scaffolding.

## §T TASKS
id|status|task|cites
001|x|Init `SPEC.md` & `SKILL.md`|this
002|x|Define `rust-debugger` sub-agent prompt|review
003|x|Define `rust-architect` sub-agent prompt|review
004|x|Define `rust-tester` sub-agent prompt|review
005|x|Register `rust-forge` rules in `edm.ron`|review
006|x|Validate EDM → Rust-Forge routing|review

## §B BUGS
id|date|cause|fix
