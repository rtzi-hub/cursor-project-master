$ErrorActionPreference = "Stop"

Write-Host "== Cursor Project Master: public release security check =="

Write-Host "`n1/5 Repository verification"
python scripts\verify_repository.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "`n2/5 JavaScript syntax"
node --check docs\assets\javascripts\app.js
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "`n3/5 Python syntax"
python -m compileall -q scripts
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "`n4/5 Full Git-history secret scan"
$gitleaks = Get-Command gitleaks -ErrorAction SilentlyContinue
$trufflehog = Get-Command trufflehog -ErrorAction SilentlyContinue

if ($gitleaks) {
    gitleaks git .
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
elseif ($trufflehog) {
    trufflehog git file://. --results=verified,unknown --fail
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
else {
    Write-Host "ERROR: Install Gitleaks or TruffleHog before public release." -ForegroundColor Red
    exit 3
}

Write-Host "`n5/5 Working-tree security scan"
$trivy = Get-Command trivy -ErrorAction SilentlyContinue
if ($trivy) {
    trivy fs --scanners vuln,secret,misconfig .
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
else {
    Write-Host "WARNING: Trivy is not installed. Run it before public release." -ForegroundColor Yellow
}

Write-Host "`nSecurity release checks completed." -ForegroundColor Green
