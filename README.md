# fizzbuzz

github.com/opslane/opslane POC app

# Prerequisites 
 
- Python3 
- uv (https://docs.astral.sh/uv/) 
 
# Install 
 
Install the python3 libraries. 
 
``` 
uv sync 
``` 
 
Install opslane 
 
``` 
mkdir -p .claude/skills tmp
git clone https://github.com/opslane/opslane.git tmp
cp -a tmp/skills/* .claude/skills/
``` 
 
Install Playwright 
 
``` 
claude mcp add playwright -- npx @playwright/mcp@latest --storage-state .verify/auth.json --isolated 
``` 
 
Install Chrome 
 
``` 
npx playwright install chrome 
``` 
 
# Run the Server 
 
``` 
uv run flask run 
``` 
 
This fizzbuzz page will be available at http://127.0.0.1:5000/. 
 
 
# Use the Opslane verify skills 
 
from https://github.com/opslane/opslane/README.md 
 
``` 
# One-time setup — auto-detects dev server, indexes app 
/verify-setup 
 
# Run verification against a spec; spec.md is at repo root
/verify @spec.md
``` 
 
You can also use the '/verify' with headless claude. 
Assumes `/verify-setup` and the server is running in another terminal. 
 
``` 
claude -p "the server is already running\n/verify @spec.md" 
``` 

# Troubleshooting

`Dev server not running at http://localhost:5000`

Edit the `.verify/config.json` and set baseUrl to `127.0.0.1:5000`.
