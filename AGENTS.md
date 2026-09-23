# Agent Instructions — Cursor Project Master

This repository is the product itself: a guided, public engineering assistant for people using Cursor.

## Product rule

The normal user must never need to search the repository to understand what to do next.

The guided UI must always provide:
1. one primary action;
2. where to perform it;
3. what to copy or run;
4. what result to expect;
5. what to do if it fails;
6. one clear continuation action.

## Architecture

- `docs/assets/data/` is the canonical source for workflow content.
- The web wizard and CLI consume the same project/workflow definitions.
- Do not duplicate long prompts in JavaScript and Markdown.
- Keep expert explanation separate from the guided task flow.

## Safety

- Never hardcode secrets.
- Never auto-install privileged system tooling.
- Never imply that completing the guide proves an arbitrary project is secure.
- Keep commit, push, merge, production deployment, destructive infrastructure,
  credential rotation, and production migration under explicit human authority.

## Verification

Run:

```bash
python scripts/verify_repository.py
python -m compileall -q scripts
node --check docs/assets/javascripts/app.js
```

Do not commit or push without explicit human approval.
