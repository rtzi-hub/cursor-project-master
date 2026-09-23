#!/usr/bin/env bash
set -euo pipefail

python scripts/verify_repository.py
node --check docs/assets/javascripts/app.js
python -m compileall -q scripts

echo "== Full Git-history secret scan =="
if command -v gitleaks >/dev/null 2>&1; then
  gitleaks git .
elif command -v trufflehog >/dev/null 2>&1; then
  trufflehog git file://. --results=verified,unknown --fail
else
  echo "ERROR: install Gitleaks or TruffleHog before public release."
  exit 3
fi

echo "== Working-tree security scan =="
if command -v trivy >/dev/null 2>&1; then
  trivy fs --scanners vuln,secret,misconfig .
else
  echo "WARNING: Trivy is not installed. Run it before public release."
fi
