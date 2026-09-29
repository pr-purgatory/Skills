# SPEC
## §G GOAL
Multi-platform UI app assistance: Swift (Apple), C#/.NET (Windows), Rust (Linux).

## §C CONSTRAINTS
- Platform-specific idioms ! followed.
- ⊥ cross-platform abstraction leak (keep platform logic distinct).
- Support for SwiftUI, WPF/WinUI, and Tauri/Iced/Slint.

## §I INTERFACES
- `ui-forge`: Primary skill trigger.
- Sub-agents: `apple-smith`, `windows-smith`, `linux-smith`.

## §V INVARIANTS
V1: ∀ platform task → delegate to specific sub-agent.
V2: ⊥ non-native UI patterns unless requested.
V3: ∀ build failure → trigger specific debugger sub-agent.
V4: ∀ new UI component → verify accessibility (a11y) standards.

## §T TASKS
id|status|task|cites
001|x|Init `SPEC.md` & `SKILL.md`|this
002|x|Define `apple-smith` sub-agent prompt|review
003|x|Define `windows-smith` sub-agent prompt|review
004|x|Define `linux-smith` sub-agent prompt|review

## §B BUGS
id|date|cause|fix
