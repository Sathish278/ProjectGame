Simple Sonar test project

Files:
- main.py
- utils.py
- sonar-project.properties

Quick run (PowerShell):

```powershell
pip install pysonar
cd sonar-test-project
pysonar --sonar-host-url=http://localhost:9000 \
  --sonar-token=YOUR_TOKEN_HERE \
  --sonar-project-key=PROD-Sonar
```

Replace `YOUR_TOKEN_HERE` with your Sonar token.

Recommended Docker run (PowerShell):

```powershell
.\run_scan.ps1 -Token YOUR_TOKEN_HERE
```

Or on Linux/macOS:

```bash
./run_scan.sh YOUR_TOKEN_HERE
```

Notes:
- `bad_practices.py` contains deliberate security issues (use of `eval`, `os.system`).
- `utils.py` contains a mutable-default-arg bug to trigger a code smell.
- `main.py` and `utils.py` include duplicated logic to illustrate duplication warnings.
After fixes: some issues were refactored to reduce security hotspots and code smells.
