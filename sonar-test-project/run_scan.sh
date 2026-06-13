#!/bin/sh
if [ -z "$1" ]; then
  echo "Usage: ./run_scan.sh <SONAR_TOKEN>"
  exit 1
fi
TOKEN=$1
docker run --rm -v "$(pwd):/usr/src" -w /usr/src sonarsource/sonar-scanner-cli \
  "-Dsonar.host.url=http://host.docker.internal:9000" \
  "-Dsonar.token=${TOKEN}" \
  "-Dsonar.projectKey=PROD-Sonar"
