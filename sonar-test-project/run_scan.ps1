param([string]$Token)

if (-not $Token) {
    Write-Host "Usage: .\run_scan.ps1 -Token <YOUR_SONAR_TOKEN>"
    exit 1
}

$proj = $PWD.Path

# run tests and generate coverage.xml using a Python container
docker run --rm -v "${proj}:/usr/src" -w /usr/src python:3.11 bash -c "pip install pytest coverage && coverage run -m pytest && coverage xml -i"

docker run --rm -v "${proj}:/usr/src" -w /usr/src sonarsource/sonar-scanner-cli "-Dsonar.host.url=http://host.docker.internal:9000" "-Dsonar.token=$Token" "-Dsonar.projectKey=PROD-Sonar" "-Dsonar.coverageReportPaths=coverage.xml"
