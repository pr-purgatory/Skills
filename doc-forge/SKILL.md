---
name: doc-forge
description: >
  Specialist in synchronizing documentation with code state.
  Contains markdown generation templates, SSRF protections, and loop/recursion guards.
---

## Goal
Automate the synchronization of code changes with corresponding documentation (e.g. `README.md`, `CHANGELOG.md`, `SPEC.md`) without causing recursive execution loops, SSRF, or markdown injection.

---

## Safety Requirements

### 1. Loop & Recursion Prevention
- The document generator MUST ignore changes made to documentation files (`*.md`) when watching for events (e.g. code modifications). This prevents the generator from triggering a new documentation update event when it writes a markdown file, avoiding infinite event loops.
- Exclude all `.md` files in the workspace file-watcher configuration.

### 2. SSRF Protection (CWE-918 Mitigation)
- When auditing external links within documentation:
  - Do NOT query or fetch arbitrary URLs.
  - Restrict domain resolution/HTTP requests to pre-approved documentation domains (e.g., `github.com`, `crates.io`, `npmjs.com`, `docs.rs`).
  - Block all local or private addresses (e.g. `localhost`, `127.0.0.1`, `10.0.0.0/8`, `192.168.0.0/16`).
  - Request audit with localhost URL → Verify blocked.

### 3. Markdown Sanitization (CWE-1156 Mitigation)
- Sanitize external input strings (such as package names, author strings, or git commit messages) before injecting them into markdown templates.
- Escape HTML entities and markdown control characters (`#`, `*`, `[`, `]`, `` ` ``) to prevent context hijacking or script execution in markdown renderers.

---

## Markdown Generation Templates

### 1. API Documentation Template
```markdown
# API Reference: <Module/Component Name>

## Overview
<Brief description of module capabilities and usage.>

## Interfaces & Symbols
<List of exports, structs, or functions with signatures.>
```

### 2. Changelog Template
```markdown
# Changelog

## [Version] - YYYY-MM-DD
### Added
- <New features>
### Changed
- <Changes in existing functionality>
### Fixed
- <Bug fixes>
```
