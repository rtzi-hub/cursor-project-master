@echo off
setlocal

echo == Cursor Project Master: public release security check ==

echo.
echo 1/5 Repository verification
python scripts\verify_repository.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo 2/5 JavaScript syntax
node --check docs\assets\javascripts\app.js
if errorlevel 1 exit /b %errorlevel%

echo.
echo 3/5 Python syntax
python -m compileall -q scripts
if errorlevel 1 exit /b %errorlevel%

echo.
echo 4/5 Full Git-history secret scan
where gitleaks >nul 2>nul
if %errorlevel%==0 (
    gitleaks git .
    if errorlevel 1 exit /b %errorlevel%
    goto :trivy
)

where trufflehog >nul 2>nul
if %errorlevel%==0 (
    trufflehog git file://. --results=verified,unknown --fail
    if errorlevel 1 exit /b %errorlevel%
    goto :trivy
)

echo ERROR: Install Gitleaks or TruffleHog before public release.
exit /b 3

:trivy
echo.
echo 5/5 Working-tree security scan
where trivy >nul 2>nul
if %errorlevel%==0 (
    trivy fs --scanners vuln,secret,misconfig .
    if errorlevel 1 exit /b %errorlevel%
) else (
    echo WARNING: Trivy is not installed. Run it before public release.
)

echo.
echo Security release checks completed.
exit /b 0
