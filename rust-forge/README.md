# Rust Forge

Multi-agent Rust programming assistance: debug, scaffold, and test.

## Overview
Rust Forge is a specialized skill for the Rust/Cargo ecosystem. It utilizes specialized sub-agents to handle different development lifecycle tasks, from debugging build failures to scaffolding new modules and generating comprehensive tests.

## Sub-Agents
- **rust-debugger**: Resolves compilation errors and test failures.
- **rust-architect**: Designs module structures and scaffolds code.
- **rust-tester**: Generates unit/integration and property-based tests.

## Integration
Integrated with `@edm` for event-driven orchestration (e.g., auto-triggering on build failures).
