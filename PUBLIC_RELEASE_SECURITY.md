# Public Release Security Checklist

Prefer a fresh Git history for the public v2 release.

Before publishing:

- [ ] Review every tracked file.
- [ ] Run `python scripts/verify_repository.py`.
- [ ] Run `node --check docs/assets/javascripts/app.js`.
- [ ] Run `python -m compileall -q scripts`.
- [ ] Run `gitleaks git .` or `trufflehog git file://.` against the complete Git history.
- [ ] Run `trivy fs --scanners vuln,secret,misconfig .`.
- [ ] Confirm no `.env`, credentials, private keys, tokens, private customer/project data, or internal-only infrastructure details are tracked.
- [ ] Enable GitHub secret scanning and push protection where available.
- [ ] Protect the default branch with a Ruleset.
- [ ] Require repository-quality CI before merge.
- [ ] Block force pushes and default-branch deletion.
- [ ] Keep GitHub Actions permissions minimal and Actions pinned to full commit SHAs.

## Fresh-history release

```bash
git init -b master
git add .
git commit -m "feat: launch Cursor Project Master v2"

bash scripts/security_release_check.sh
```

Only after the checks pass should the public repository be pushed.

## Browser privacy

The guided site stores project information in `sessionStorage` by default.

Persistent `localStorage` is used only when the user explicitly selects **Remember this project on this device**.

When copying prompts into another AI service, that service's data-handling terms apply. Use only a service appropriate for the project's confidentiality requirements.
