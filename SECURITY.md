# Security

Do not include real secrets, credentials, private keys, customer data, or confidential project information in public issues.

For security-sensitive defects in this toolkit, prefer GitHub private security reporting if enabled.

## Security design

- `cpm.project.json` is treated as untrusted input by the scaffold command.
- Scaffold paths are constrained to the manifest's project root.
- The website stores project information in browser session storage by default.
- Persistent browser storage is opt-in.
- GitHub Actions use minimal permissions and full-SHA-pinned Actions.
- Checkout credentials are not persisted after checkout.

This project provides engineering guardrails and a production-readiness workflow. It does not certify generated applications as secure.
