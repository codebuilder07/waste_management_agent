# Waste Management ADK Agent
There's a second read.me file inside the folder for me detail project structure.
Lightweight FastAPI agent that integrates with ADK, a local rule agent, and a memory service.

## Features
- Exposes REST endpoints to send chat messages to ADK, store memory, and query local rules.
- Configurable via environment variables.
- Run with Uvicorn for development.

## Requirements
- Python 3.8+
- Recommended: create and use a virtual environment
- Key Python packages: FastAPI, Uvicorn, pydantic (see requirements.txt if present)

## Environment variables
Set these before running:
- ADK_API_KEY - API key for ADK client (required by ADKClient)
- LOCAL_RULE_AGENT_URL - URL for local rule agent (default: http://localhost:8000)
- MEMORY_SERVICE_URL - URL for memory service (default: http://localhost:8001)

Example (PowerShell):
```powershell
$env:ADK_API_KEY = "your_adk_api_key"
$env:LOCAL_RULE_AGENT_URL = "http://localhost:8000"
$env:MEMORY_SERVICE_URL = "http://localhost:8001"
```

## Setup (Windows PowerShell)
```powershell
cd "C:\Users\91944\Downloads\hackathon-adk\waste-management-adk-agent"

# create & activate venv
python -m venv .venv
.\.venv\Scripts\Activate

# install deps (if provided) or core deps
if (Test-Path .\requirements.txt) { pip install -r .\requirements.txt } else { pip install fastapi uvicorn pydantic }
```

## Run
Recommended (development, auto-reload):
```powershell
uvicorn src.main_agent:app --host 0.0.0.0 --port 8002 --reload
```

Or run directly (uses uvicorn in __main__):
```powershell
python .\src\main_agent.py
```

The server will listen on http://0.0.0.0:8002

## API Endpoints
- POST /adk/chat  
  Body: { "user_id": "string", "message": "string" }  
  Forwards the message to ADKClient.

- POST /memory/store  
  Body: JSON object  
  Stores memory via MemoryClient.

- POST /waste-management/rules  
  Body: JSON object  
  Queries local rule agent via RuleAgentClient.

## Troubleshooting
- Error "ValueError: 'not' is not a valid parameter name":
  - Common causes:
    - A local file is shadowing a dependency (e.g., pydantic.py, fastapi.py, typing.py). Search and rename/remove such files.
    - Incompatible pydantic / fastapi versions (pydantic v2 vs FastAPI expecting v1).
  - Quick checks:
    ```powershell
    # find potential shadowing files
    Get-ChildItem -Recurse -Include pydantic.py,fastapi.py,typing.py -ErrorAction SilentlyContinue | Select FullName

    python -V
    pip show fastapi pydantic
    ```
  - Fix (if version mismatch): pin compatible versions:
    ```powershell
    pip install "pydantic==1.10.12" "fastapi==0.95.2"
    ```

- If clients (rule agent, memory service) are not running, the endpoints will fail. Ensure the services are reachable at the URLs set in env vars.

## Push to GitHub (quick)
```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/waste-management-adk-agent.git
git push -u origin main
```
Or use `gh repo create`:
```powershell
gh auth login
gh repo create waste-management-adk-agent --public --source=. --remote=origin --push
```

## Notes
- Do not commit secrets (.env). Add them to .gitignore.
- If you change package versions, recreate the virtual environment.

