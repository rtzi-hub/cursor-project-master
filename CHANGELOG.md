# Changelog

## 2.0.2 — 2026-09-23

### Windows compatibility

- Explicit UTF-8 reads/writes throughout the Python CLI and repository verifier.
- Fix Windows `charmap` failures when reading project metadata containing Unicode/emoji.
- Add native Windows CMD public-release checker.
- Add native PowerShell public-release checker.
- WSL/Bash is no longer required for Windows release verification.
- Document Windows-specific release commands.

## 2.0.1 — 2026-09-23

### Security hardening

- Reject absolute, drive-qualified, network, and path-traversal scaffold paths.
- Store guided project information in session storage by default.
- Make persistent browser storage explicit opt-in.
- Warn users not to enter secrets and to use an AI service appropriate for project confidentiality.
- Disable persisted Git credentials after Actions checkout.
- Add full-history secret-scan and public-release security guidance.
- Expand verification with credential-pattern and workflow-pinning checks.

## 2.0.0 — 2026-09-23
- Rebuilt around five memorable milestones.
- One-action-per-screen guided UX.
- Beginner / Guided / Expert guidance.
- Architecture Workshop before project-specific AGENTS.md for new projects.
- Evidence-first existing-project workflow.
- Canonical workflow/project/prompt data to prevent drift.
- Added `cpm.project.json`, repository-aware Doctor, and manifest-driven scaffold.
- Existing-project change artifacts are isolated under `.project-master/`.
- Public content contains only generic examples.


