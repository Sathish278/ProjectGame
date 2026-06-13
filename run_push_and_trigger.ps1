# Stages, commits, and pushes sonar-test-project and workflow to origin/main
# Run this from Windows PowerShell: right-click and "Run with PowerShell" or
# open PowerShell and run: .\run_push_and_trigger.ps1

try {
    Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)
} catch {
    Write-Host "Could not determine script location; please run this script from the repo root." -ForegroundColor Yellow
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "git is not installed or not on PATH. Install Git and retry."
    exit 1
}

Write-Host "Repository path: $(Get-Location)"

# Check ignored
$ignored = git check-ignore -v sonar-test-project 2>$null
if ($ignored) {
    Write-Host "sonar-test-project is ignored by .gitignore:" -ForegroundColor Yellow
    Write-Host $ignored
    Write-Host "Remove it from .gitignore if you want to push it." -ForegroundColor Yellow
    exit 1
} else {
    Write-Host "sonar-test-project is not ignored. Proceeding..."
}

# Stage files
git add sonar-test-project .github/workflows/sonar-scan.yml

# Commit
$commitOutput = git commit -m "ci: add sonar-test-project and Sonar scan workflow" 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Committed changes:" -ForegroundColor Green
    Write-Host $commitOutput
} else {
    if ($commitOutput -match "nothing to commit") {
        Write-Host "No changes to commit." -ForegroundColor Yellow
    } else {
        Write-Host "Commit output:" -ForegroundColor Yellow
        Write-Host $commitOutput
    }
}

# Push
Write-Host "Pushing to origin/main..."
$pushOutput = git push origin main 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Push succeeded." -ForegroundColor Green
    Write-Host $pushOutput
    Write-Host "The GitHub Action should start shortly. Check Actions in your repo." -ForegroundColor Cyan
    exit 0
} else {
    Write-Host "Push failed:" -ForegroundColor Red
    Write-Host $pushOutput
    Write-Host "If this is an auth error, ensure your credentials are set for origin." -ForegroundColor Yellow
    exit 1
}
