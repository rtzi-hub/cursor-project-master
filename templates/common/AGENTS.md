# Agent Engineering Instructions

## Before editing
1. Read REQUIREMENTS.md, ARCHITECTURE.md, ACCEPTANCE_CRITERIA.md, and cpm.project.json when present.
2. Search for existing functionality before creating new abstractions.
3. Identify affected callers, data, authorization, tests, and integrations.
4. Minimize blast radius.

## During implementation
- Implement only approved scope.
- Preserve architecture/public contracts unless the accepted plan changes them.
- Add/update tests with changed behavior.
- Do not weaken valid tests.
- Never hardcode secrets.
- Preserve authorization/data boundaries.

## Stop and report
Stop if architecture, schema, public contract, security boundary, destructive infrastructure, or production credentials become unexpectedly required.

## Git authority
Do not commit, push, merge, deploy production, destroy infrastructure, rotate credentials, or run production migrations unless explicitly authorized.
