# Cursor Project Master

> A guided production-engineering workflow for building a new project or safely changing an existing codebase with Cursor.

## The promise

**You should never need to wonder what to do next.**

```text
💡 Discover → 🗺️ Design → 🛠️ Build → ✅ Prove → 🚀 Launch
```

The guide tells you exactly:

- which app to open;
- which Cursor mode to use;
- what prompt to copy;
- what result/files should appear;
- what command to run;
- how to verify success;
- when to continue.

## Main journeys

### New project

```text
Describe idea
→ Architecture workshop in AI chat
→ Approve architecture
→ Prepare local machine
→ Generate/refine AGENTS.md + Cursor rules
→ Build roadmap
→ Scaffold approved structure
→ Implement phase-by-phase
→ Verify
→ Secure
→ Launch
```

### Existing project

```text
Describe intended change
→ Protect baseline
→ Read-only repository discovery
→ Generate/refine AGENTS.md from repository evidence
→ Blast-radius plan
→ Human approval
→ Minimal implementation
→ Regression verification
→ Security
→ Launch
```

## CLI

```bash
python scripts/project_master.py doctor --repo /path/to/project
python scripts/project_master.py init --type web-app --name my-project --target ../my-project
python scripts/project_master.py scaffold --manifest ../my-project/cpm.project.json
python scripts/project_master.py inspect --repo ../my-project
```

## Principles

- one thing per screen;
- beginner-friendly language;
- expert detail only when requested;
- architecture conversation before project-specific AGENTS.md for new projects;
- evidence-first discovery for existing projects;
- deterministic checks around AI work;
- human authority for high-impact operations;
- one canonical source of workflow/prompt truth.

## License

MIT.


## Public-release security

Before making the repository public, follow [`PUBLIC_RELEASE_SECURITY.md`](PUBLIC_RELEASE_SECURITY.md).

The scaffold CLI rejects unsafe manifest paths. The guided site keeps project details in session storage by default; persistent browser storage is explicit opt-in.


## Windows

The toolkit does not require WSL.

From Windows CMD:

```bat
python scripts\verify_repository.py
scripts\security_release_check.cmd
```

From PowerShell:

```powershell
python scripts\verify_repository.py
powershell -ExecutionPolicy Bypass -File scripts\security_release_check.ps1
```

All Python file I/O in the toolkit explicitly uses UTF-8 so project-type emoji and other Unicode content work on Windows.
